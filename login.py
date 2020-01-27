from BotTwitter import BotTwitter

if __name__=='__main__':
    username="shanonsamora3@gmail.com"
    password="lokiju12"
    hashtags = ["drstone", "dr stone"]

    bot = BotTwitter(username, password)
    bot.login()
    bot.like_tweet_follow(hashtags)