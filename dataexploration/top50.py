import re
import pandas as pd
from nltk.stem import *
from nltk.corpus import stopwords
import csv
from collections import Counter
import matplotlib.pyplot as plt
import math
import numpy as np


def thingy(counter, opposite, dict):
    for token, freq in counter:
        if opposite[token] == 0:
            dict[token] = freq
        else:
            ratio = freq/opposite[token]
            dict[token] = math.log(ratio, 2) - math.log(1.43, 2) - math.log(1.186, 2) # just gives how much more

            # the one article type mentions token more than other type.
    return dict


def plot(x, y):
    colors = ['blue' if val >= 0 else 'red' for val in y]
    plt.bar(x, y, color=colors)
    ax = plt.gca()
    plt.setp(ax.get_xticklabels(), rotation=60)
    plt.xticks(fontsize=8)
    plt.xlabel("Words")
    plt.ylabel("Log(Ratio)")
    plt.title('Top 50 biggest log(ratio) of tokens\' frequency between article type')
    
    # Add legend
    plt.legend(handles=[plt.Rectangle((0,0),1,1, color='blue', label='appears more in real'), 
                        plt.Rectangle((0,0),1,1, color='red', label='appears more in fake')],
               loc='upper right')
    
    plt.show()


def get_all_words_smarter(stringiterable, mode):
    wordpattern = r'\b[a-z]+\b'
    words = Counter()
    for article in stringiterable:
        all_words = re.findall(wordpattern, str(article))
        words.update(Counter(all_words))
    print("LIST OF WORDS MADE YAY")
    if mode == "return":
        return words
    elif mode == "to_txt":
        with open("../data/ABOWSUNE.txt", "w") as file:
            for word in words:
                file.write(f"{word}\n")


def remove_stop_words(counter_object):
    stop_words = stopwords.words('english')
    for word in list(counter_object):
        if word in stop_words:
            del counter_object[word]
    print("STOP WORDS REMOVED YAY")    

def stemmify_words(counter_object):
    stemmer = SnowballStemmer("english")
    for word in list(counter_object):
        stemmed_word = stemmer.stem(word)
        if not stemmed_word == word:
            count = counter_object[word]
            del counter_object[word]
            counter_object[stemmed_word] += count
        else:
            pass
    print("UNIQUE WORDS STEMMED YAY")


df = pd.read_csv("Data/for_advanced_model/CLEANED_BINARY.csv")
print("cleaned_data er loaded")
fake_articles = df[df["type"] == "fake"]
real_articles = df[df["type"] == "real"]

real = get_all_words_smarter(real_articles["content"],"return")

fake = get_all_words_smarter(fake_articles["content"],"return")

remove_stop_words(real)
stemmify_words(real)

remove_stop_words(fake)
stemmify_words(fake)

common_real = real.most_common(100)
common_fake = fake.most_common(100)


tokens_and_ratios = {}

tokens_and_ratios = thingy(common_real, fake, tokens_and_ratios)

for token, freq in common_fake:
    if real[token] == 0:
        tokens_and_ratios[token] = freq
    else:
        ratio = freq/real[token]
        tokens_and_ratios[token] = math.log( (1 / (ratio * 1.43 * 1.186)), 2) # just gives how much more

# print(tokens_and_ratios["cent"])
tokens = list( tokens_and_ratios.keys() )
ratios = list(tokens_and_ratios.values() )


sorted_pairs = sorted(zip(ratios, tokens), key= lambda x: abs(x[0]), reverse=True)

ratios, tokens = zip(*sorted_pairs)


# Open the file in write mode
# with open("../data/big_difference_words.txt", 'w') as file:
#     # Iterate over each element in the list
#     for token in tokens[3:53]:
#         # Write the element to the file
#         file.write(token + '\n')

# some weird values in the start, should be able to skip those with no problem. 
plot(tokens[2:52], ratios[2:52])
