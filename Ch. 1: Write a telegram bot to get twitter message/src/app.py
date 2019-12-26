from configparser import ConfigParser
from functools import partial
from telegram.ext import CommandHandler
from utils import telegram as telegram_utils
from utils import twitter as twitter_utils
import logging

# set config of logger
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
                    level=logging.INFO)

if __name__ == "__main__":
    # Get config (i.e. token of telegram bot) from config.ini
    config = ConfigParser()
    config.read("config.ini")

    # Initialize Twitter API client
    twitter_api = twitter_utils.init_twitter_api(
        consumer_key        = config["twitter"]["CONSUMER_KEY"],
        consumer_secret     = config["twitter"]["CONSUMER_SECRET"],
        access_token        = config["twitter"]["ACCESS_TOKEN"],
        access_token_secret = config["twitter"]["ACCESS_TOKEN_SECRET"]
    )

    # Initialize partial function if they required specific inputs
    getTwitter = partial(telegram_utils.GetTweetsFunc, twitter_api=twitter_api)

    # create handler
    get_handler = CommandHandler("get", getTwitter, pass_args=True)

    # Create a list of handlers to pass as an argument to init_telegram_api
    handlers = []
    handlers.append(get_handler)
    
    # Initialize Telegram Bot
    telegram_client = telegram_utils.init_telegram_api(
        token    = config["telegram"]["Token"], 
        handlers = handlers
    )

    # Start Telegram Bot
    telegram_client.start_polling()
