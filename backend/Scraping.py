import os

import snscrape.modules.twitter as sntwitter
import pandas as pd


def get_tweets(query, n, start, end):
    path = os.path.join(__file__, "../..", 'backend', 'tweets')
    posts = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        max = int(n)
        if i >= max:
            break
        posts.append([tweet.id, tweet.date, tweet.retweetCount, tweet.likeCount, tweet.content])
    tweets_df2 = pd.DataFrame(posts, columns=['Tweet Id', 'Datetime', 'retweetCount', 'likeCount', 'Text'])
    tweets_df2.to_csv(path + "/" + query[:10]+".csv", sep=';', index=False)
