# Twitter NFT Analysis
**Adarsh Nair**

![image](https://user-images.githubusercontent.com/51357266/160265904-9abf64c4-c185-4ebc-b09a-4a730009d138.png)

## Table of Contents
1) Overview
2) Data Collection and ssing
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
  
  Now that the master file of tweets is obtained, different processing techniques were used to transform the data for better insights and visualizations. Refer to the  `processing.ipynb` file.
  
## Visualization
  The NFT tweets data has visualized based on multiple parameters. The visualizations are created in Tableau. The plots can be viewed as a [story](https://public.tableau.com/app/profile/adarsh6567/viz/verified-nft-tweets-analysis/NFTTweets) (recommended) and a [dashboard](https://public.tableau.com/app/profile/adarsh6567/viz/nft-tweets-dashboard/NFTTweets_1). A copy of the story is also attached with the extract in PDF format for reference. 
  
  Based on the data and visuals, the following insights can be mentioned:
  
### Trend of Tweet count (Based on Time)
- The monthly count of tweets clearly shows the trend of NFTs. The number of tweets are slowly, but steadily increasing. Note that the tweet count for MArch 2022 is only till the 25th. It is highly likely that the count will surpass the previous month's tally. 
- Users tend to tweet at the earlier/later parts of the day. The tweet counts are lowest at 11AM-12PM. The distribution seems like and inverted bell curve. Note: The time reference is Indian Standard Time(IST)

### Tweets By Language
- English is the dominant language by which NFT tweets are expressed. 
- Other notable languages include Spanish, French, Japanese, Arabic, German, Portugese
- The language codes can be referred in the [Twitter docs](https://developer.twitter.com/en/docs/twitter-for-websites/supported-languages)

### Users
- Users [@markshaw](https://twitter.com/markshaw),[@kokid951](https://twitter.com/kokid951) and [@darcydonavan](https://twitter.com/darcydonavan) have posted upwards of 1500 tweets so far. That is almost 3 NFT tweets a day!
- While the above users have high tweet counts, user [@poodletoken](https://twitter.com/poodletoken) has amassed a staggering ~900K likes on all their tweets, albeit being a fraction of the users with max tweet counts
- [@darcydonavan](https://twitter.com/darcydonavan)'s tweets are quoted the most, while NFT marketplace [@opensea](https://twitter.com/opensea) have got the most mentions by Twitter users as far as NFTs are concerned

### Other Parameters
- [`#nft`, `#nfts`, `#nftcommunity`] are the most used hashtags when users tweet about these digital entities and related platforms, opinions
- In terms of cashtags, ArtPrice ($PRC) and ETH ($eth) are widely mentioned, with a number of others talked about, though at a smaller scale
- Besides Twitter, the different forums used by NFT enthusiasts include Discord, OpenSea, YouTube, Demeure du Chaos among others

## Sentiment Analysis 
  The set of tweets are available, but no sentiment labels are associated with each tweet that gives us a perception of the sentiment. This makes the problem an unsupervised learning problem.   
  
  To obtain a sentiment score, the [vaderSentiment](https://github.com/cjhutto/vaderSentiment) package is used; which uses lists of predefned idioms and phrases to evaluate the sentiment of sentiment based on given context. Besides the keywords/idioms provided with the package, a number of idioms and lexicons were added to the code keeping NFTs in mind to provide more context to the program. The keywords included were heavily derived form Henrique Centieiro's excellent [article]((https://medium.datadriveninvestor.com/79-nft-crypto-words-you-need-to-know-the-crypto-nft-slang-dictionary-adcc39ad846b)) on Medium.  
  
  Again, for simplicity, tweets only in English language were used for understanding sentiment. The `sentiment.ipynb` file can be referred for implementation of the analysis of tweets. 
  
  The sentiment is evaluated based on the compound score of the tweets. The distribution of compound scores is shown below. 
  
  The sentiment (positive | neutral | negative) is decided based on the below mentioned threshold o compound score (`cs`):
  ```
  cs > 0.3  => positive
  cs < -0.3 => negative
  otherwise => neutral
  ```
  
  The following result is obtained (proportion of sentiment labels of tweets):
  ```
  Sentiment Label distribution: 

  positive    53.74%
  neutral     37.68%
  negative    8.56%
  ```
## Closing Remarks


## References and Acknowledgements

### References


### Acknowledgements
  
  
  
  

  

