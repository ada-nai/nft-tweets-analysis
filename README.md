# Twitter NFT Analysis
**Adarsh Nair**

![image](https://user-images.githubusercontent.com/51357266/160265904-9abf64c4-c185-4ebc-b09a-4a730009d138.png)

## Table of Contents
0) File Structure of Submission  
1) Overview  
2) Data Collection  
3) Data Aggregation and Processing  
4) Visualization  


## File Structure of Submission
The file structure with description is as follows:
- `notebooks_and_data` [folder]
    - `collect_tweets.py` [python script]
    - `aggregation.ipynb` [notebook]
    - `processing.ipynb` [notebook]
    - `sentiment.ipynb` [notebook]
    - `tags.txt` [text file]
- `nft_env_conda.yml` [yml file for environment replication]
- `nft-tweets-analysis-story` [presentation file]

The file names are referenced below in the document where applicable.

## Overview
  [Non-Fungible Tokens (NFTs)](https://en.wikipedia.org/wiki/Non-fungible_token) are a relatively new concept and have been making headlines for the related events happening in the space. This project aims to capture the trend of NFTs by using available data and tries to answer a few questions that help understand how far NFTs have come. 
  
  This analysis report covers the steps performed for various stages of the analysis and also presents insights including visualizations and understanding sentiment of the masses.

## Data Collection
  The best way to gauge the sentiments and get basic level stats is to use data from social media. Twitter is a powerful platform for people to express their opinions on any given topic. The tweets which include hashtags(`#`) related to NFTs are collected. The tweets are collected using the Twint package using Python programming language 
  
  For the sake of simplicity, the data collected includes tweets from _[verfied Twitter accounts](https://help.twitter.com/en/managing-your-account/twitter-verified-accounts)_ for the approximately 18 month period from October 2020 to March 2022. For data collection `collect_tweets.py` file can be referred. The configurations used for the Twint object can be referred from the [official documentation](https://github.com/twintproject/twint/wiki/Configuration) (docs). 
  Tweets are collected for individual search queries provided (hashtags). The list of hashtags can be referred to in the `tags.txt` file. 
  
  
## Data Aggregation and Processing
  Once tweets are collected, they are present in different `.csv` files, based on individual hashtag provided as query. The `aggregation.ipynb` notebook concatenates all the individual files to a master `.csv` file. Because a single tweet can contain multiple hashtags, the duplicated tweets in master are deleted. The `aggregation.ipynb` file can be referred for the record aggregation.
  
  Now that the master file of tweets is obtained, different processing techniques were used to transform the data for better insights and visualizations. Refer to the  `processing.ipynb` file for the same.  
  
  The transformed dataset is stored and provided as `nft_verified_tweets.csv`
  
  ![image](https://user-images.githubusercontent.com/51357266/160277896-f3828d42-a633-484c-b79c-9d5b42924ad3.png)

  
  
## Visualization
![image](https://user-images.githubusercontent.com/51357266/160276348-169685c0-cf85-40de-a7fe-0e576211d4d9.png)


  The NFT tweets data has been visualized based on multiple parameters. The visualizations are created in Tableau. The plots can be viewed as a [story](https://public.tableau.com/app/profile/adarsh6567/viz/verified-nft-tweets-analysis/NFTTweets) (recommended) and a [dashboard](https://public.tableau.com/app/profile/adarsh6567/viz/nft-tweets-dashboard/NFTTweets_1). A copy of the story is also attached with the extract in PPT format for reference (`nft-tweets-analysis-story.pptx`). 
  
  Based on the data and visuals, the following insights can be mentioned:
  
### Trend of Tweet count (Based on Time)
- The monthly count of tweets clearly shows the trend of NFTs. The number of tweets are slowly, but steadily increasing. Note that the tweet count for March 2022 is only till the 25th. It is highly likely that the count will surpass the previous month's tally. 
- Users tend to tweet at the earlier/later parts of the day. The tweet counts are lowest at 11AM-12PM. The distribution seems like and inverted bell curve.  

Note: The time reference is Indian Standard Time(IST)

### Tweets By Language
- English is the dominant language by which NFT tweets are expressed. 
- Other notable languages include Spanish, French, Japanese, Arabic, German, Portugese
- The language codes can be referred in the [Twitter docs](https://developer.twitter.com/en/docs/twitter-for-websites/supported-languages)

### Users
- Users [@markshaw](https://twitter.com/markshaw),[@kokid951](https://twitter.com/kokid951) and [@darcydonavan](https://twitter.com/darcydonavan) have posted upwards of 1500 tweets so far. That is almost 3 NFT tweets a day!
- While the above users have high tweet counts, user [@poodletoken](https://twitter.com/poodletoken) has amassed a staggering ~900K likes on all their tweets, albeit being a fraction of the users with max tweet counts
- [@darcydonavan](https://twitter.com/darcydonavan)'s tweets are quoted the most, while NFT marketplace [@opensea](https://twitter.com/opensea) have got the most mentions by Twitter users as far as NFTs are concerned

### Other Parameters
- [`#nft`, `#nfts`, `#nftcommunity`] are the most used `hashtags` when users tweet about these digital entities and related platforms, opinions
- In terms of `cashtags`, ArtPrice ($PRC) and ETH ($eth) are widely mentioned, with a number of others talked about, though at a smaller scale
- Besides Twitter, the different `forums` used by NFT enthusiasts include Discord, OpenSea, YouTube, Demeure du Chaos among others

