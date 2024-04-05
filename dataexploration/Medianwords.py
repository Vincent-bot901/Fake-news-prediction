import pandas as pd
import matplotlib.pyplot as plt

def median_word_count(text):
    words = text.split()
    return len(words)

df = pd.read_csv("../Data/otherdata/BIGCLEANED.csv")
df2 = pd.read_csv("../Data/liardata/FinalTest.tsv", usecols=[2], sep='\t', header=None)

# Calculate average word counts
median_word_count1 = df['content'].apply(median_word_count)
median_word_count2 = df2[2].apply(median_word_count)

# Plotting
plt.bar(['Dataset brugt til traning', 'Liar dataset'], [median_word_count1.median(), median_word_count2.median()], color=['skyblue', 'salmon'])
plt.xlabel('Datasets')
plt.ylabel('Amount of Words')
plt.title('Comparison of median word count')
plt.grid(False)
plt.show()
