# Twitter NFT Analysis
**Adarsh Nair**

![image](https://user-images.githubusercontent.com/51357266/160265904-9abf64c4-c185-4ebc-b09a-4a730009d138.png)

## Table of Contents
1) Overview
2) Data Collection and Processing
3) Visualization
4) Sentiment Analysis
5) Closing Remarks
6) References and Acknowledgements

## Overview
  NFTs are a relatively new concept and have been making headlines for the related events happening in the space. This project aims to capture the trend of NFTs by using available data and tries to answer a few questions that helps understand how far NFTs have come. 
  
  This analysis report covers the steps performed for various stages of the analysis and also presents insights including visualizations and understanding sentiment of the masses.

## Data Collection
  The best way to gauge the sentiments and get basic level stats is to use data from social media. Twitter is a powerful platform for people to express their opinions on any given topic. The tweets which include hashtags(`#`) related to NFTs are collected. The tweets are collected with using the Twint package using Python programming language 
  
  For the sake of simplicity, the data collected includes tweets from _[verfied Twitter accounts](https://help.twitter.com/en/managing-your-account/twitter-verified-accounts)_ for the approximately one-and-a-half year period from October 2020 to March 2022. For data collection `full_scrape.py` file can be referred. The [configurations](https://github.com/twintproject/twint/wiki/Configuration) used for the Twint object can be referred from the official documentation (docs). 
  Tweets are collected for individual search queries provided (hashtags). The list of hashtags can be referred to in the `tags.txt` file.
  
## Data Aggregation and Processing
  Once tweets are collected, they are present in different `.csv` files, based on individual hashtag provided as query. The `aggregation.ipynb` notebook concatenates all the individual files to a master `.csv` file. Because a single tweet can contain multiple hashtags, the duplicated tweets in master are deleted. The `aggregation.ipynb` file can be referred for the record aggregation.
  
  Now that the master file of tweets is obtained, different processing techniques were used to transform the data for better insights and visualizations. Refer to the  `process.ipynb` file.
  
## Visualization

## Sentiment Analysis 
  The set of tweets are available, but no sentiment labels are associated with each tweet that gives us a perception of the sentiment. This makes the problem an unsupervised learning problem.   
  
  To obtain a sentiment score, the [vaderSentiment](https://github.com/cjhutto/vaderSentiment) package is used; which uses lists of predefned idioms and phrases to evaluate the sentiment of sentiment based on given context. Besides the keywords/idioms provided with the package, a number of idioms and lexicons were added to the code keeping NFTs in mind to provide more context to the program. The keywords included were heavily derived form Henrique Centieiro's excellent [article]((https://medium.datadriveninvestor.com/79-nft-crypto-words-you-need-to-know-the-crypto-nft-slang-dictionary-adcc39ad846b)) on Medium.  
  
  Again, for simplicity, tweets only in English language were used for understanding sentiment. The `sentiment.ipynb` file can be referred for implementation of the analysis of tweets. 
  
## Closing Remarks


## References and Acknowledgements

### References


### Acknowledgements
  
  
  
  

  

