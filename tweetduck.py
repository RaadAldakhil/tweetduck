import tweepy
import logging
from config import create_api
import time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()
    
    # Generate duck fortune
    stream = os.popen('fortune -n 120 | cowsay -f duck')
    output = stream.read()
    # Create a tweet
    api.update_status(output.append(" \n-Made with Tweepy"))

if __name__ == "__main__":
    main()

