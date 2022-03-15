import twint as tw

# '#nfts', '#nft', '#nftart', '#nftcommunity', '#nftcollector', '#NFTs', '#NFT', '#NFTCommunity', '#NFTcommunity', '#nftgiveaway', '#NFTGiveaway', '#metaverse', '#web3', '#NFTCollection', '#NFTGame', '#NFTdrop',' #NFTartists', '#NFTProject', '#NFTMarketplace', '#NFTdrops' 


c = tw.Config()
c.Search = '#nfts'#, '#nft', '#nftart' , '#nftcommunity', '#nftcollector', '#NFTs', '#NFT', '#NFTCommunity', '#NFTcommunity', '#nftgiveaway', '#NFTGiveaway', '#metaverse', '#web3', '#NFTCollection', '#NFTGame', '#NFTdrop',' #NFTartists', '#NFTProject', '#NFTMarketplace', '#NFTdrops' 
c.Limit = 4000
c.Until = ('2022-03-01')
c.Since = ('2021-09-01')
# c.Lang = 'en'
c.Store_csv = True
c.Output = './tweets.csv'
# c.Location = True
c.Min_likes = 0
# c.Verified = True
c.Lowercase = True
c.Show_hashtags = False
c.Email = False
c.Phone = False
c.HideOutput= True
c.Verified = True
c.Resume = './scroll_id.txt'

tw.run.Search(c)