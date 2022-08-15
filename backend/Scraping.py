import snscrape.modules.twitter as sntwitter
import pandas as pd


class Scraping:

    def get_tweets(self,query,n,start,end):
        posts = []
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i >= n:
                break
            posts.append([tweet.id,tweet.date,tweet.retweetCount, tweet.likeCount, tweet.content])
        tweets_df2 = pd.DataFrame(posts, columns=['Tweet Id','Datetime','retweetCount','likeCount', 'Text'])
        tweets_df2.to_csv('tweets/PKOst.csv', sep=';', index=False)


