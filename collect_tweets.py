import twint as tw
import logging 
keyword = 'verified_0_prepre'
logging.basicConfig(filename= f'./{keyword}_logs.txt', level= logging.INFO)

tags = ['#NFTs', '#NFT', '#nftart', '#nftcollector', '#NFTCommunity',  '#Metaverse, #NFTs', '#Web3, #NFTs', '#NFTCollection', '#NFTGame',
'#NFTdrop', '#NFTartists', '#NFTProject', '#NFTMarketplace', '#NFTdrops', '#NFTGiveaway', '#NFTmint'] # '#nfts', '#nft', 

# tags = ['#Web3, #NFTs']

c = tw.Config()
c.Since = ('2020-10-01')
c.Until = ('2021-02-28')
c.Min_likes = 0
c.Lowercase = True
c.Show_hashtags = False
c.Email = False
c.Phone = False
c.Hide_output= True
c.Store_csv = True
c.Verified = True
# c.Limit = 20
# c.Location = False
# c.Lang = 'en'



def csv_num_records(filename, tag):
    '''
    Get the number of tweets scraped

    Input:
        filename: str: Path to the .csv file in which tweets are output

    Output:  
        num_records: str: Count of records in .csv file

    '''
    try:
        
        with open(filename, 'r') as f:
            num_records =sum(1 for line in f)
            return num_records
    except:
        print(f'0 tweets collected for {tag}')
        return 0

def scrape_tweets(tags, config_var=c):
    '''
    Scrape tweets based on tag(s) provided using twint

    Input:
        tags: list of strings: Array of all tags 
        for which tweets are to be scraped
        config_var: object: Twint object with predefined, fixed parameters
    '''

    total_tweets = 0

    for tag in tags:
        scroll_id_path = f'./data/{keyword}/scroll_ids/{tag}_scroll_id.txt' 
        csv_path = f'./data/{keyword}/tweets/{tag}.csv' 

        config_var.Search = tag
        config_var.Resume = scroll_id_path
        config_var.Output = csv_path

        tw.run.Search(config_var)

        tweet_count = csv_num_records(csv_path, tag)
        total_tweets += tweet_count
        out = str(tweet_count)+' tweets collected for '+tag
        logging.info(out)
        print(out)
    return total_tweets

total_tweets = scrape_tweets(tags)
logging.info(f'{total_tweets} tweets collected in total')
print(f'{total_tweets} tweets collected in total')



