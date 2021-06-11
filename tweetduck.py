import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()

    # Create a tweet
    api.update_status(os.system('fortune -n 130 | cowsay -f duck'))

if __name__ == "__main__":
    main()

