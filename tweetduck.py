import tweepy
import logging
from config import create_api
import time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()
    output = ""

    while len(output) > 280 or len(output) == 0:
        # Generate duck fortune
        stream = os.popen('fortune -s')
        output = stream.read() + "\ \n  \ \n   \  >()_ \n     (__)__ _\n-Posted by Tweepy"

    # Create a tweet
    api.update_status(output)

if __name__ == "__main__":
    main()

