from InternetSpeedTweetBot import Bot
PROMISED_UP = 50
PROMISED_DOWN = 10

bot = Bot()
bot.get_internet_speed()
up = bot.get_up()
down = bot.get_down()
if (up < PROMISED_UP) and (down < PROMISED_DOWN):
    bot.tweet_at_provider()
    bot.close_web_driver()
