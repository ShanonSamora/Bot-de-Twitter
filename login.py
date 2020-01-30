from BotTwitter import BotTwitter

if __name__=='__main__':
    username=" " #Entre las comillas necesitas poner el email de la cuenta que vas a usar.
    password=" " #Acá necesitas poner la contraseña.
    hashtags = [" ", " "] #Acá necesitas poner los hashtags que quieras que el bot likee y siga a los autores de dichos tweets.

    bot = BotTwitter(username, password)
    bot.login()
    bot.like_tweet_follow(hashtags)
