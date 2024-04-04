# Fake-news-prediction

This repository contains the code for our final project in GDS.

## Using our code

To test the results of our code, follow these steps:

1. Navigate to the "FakeNewsCorpus" dataset and locate the CSV file you want to use.
2. Save the CSV file as "Data/bigdata/big.csv" in the project directory.

Next, run the Jupyter notebook provided in the repository. This notebook contains the necessary preprocessing steps and model training code, so to see the results of our models you would simply have to run the entire Jupyter notebook file.

## Exploring the data

In the "dataexploration" folder, you'll find Python scripts that we used to explore and visualize the dataset. To run these scripts, navigate to the "dataexploration" folder in your terminal or command prompt and execute each script using Python (e.g., `python filename.py`).

### Medianwords.py
This file plots a figure that shows median word count of LIAR dataset and the dataset used to train our models.

### top50.py
this file takes a cleaned CSV file (not stemmed and with stopwords removed) as input and returns the top 50 words with the highest absolute value log ratio of frequency (how many times they occur) in real and fake. It also accounts for the fact that there are more real articles than fake ones and that real articles tend to be longer.
