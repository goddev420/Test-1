import tweepy
import re
import time

class TwitterMonitor:
    def __init__(self, api_key, api_secret, access_token, access_secret):
        self.auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
        self.api = tweepy.API(self.auth)
        self.accounts = []  # List of accounts to monitor

    def monitor_accounts(self, accounts):
        if len(accounts) > 20:
            raise ValueError("Cannot monitor more than 20 accounts.")
        self.accounts = accounts
        class CustomStreamListener(tweepy.Stream):
            def on_status(self, status):
                print(f"New tweet from {status.user.screen_name}: {status.text}")
                token_data = self.extract_token_data(status.text)
                if token_data:
                    print(f"Token data extracted: {token_data}")

            def extract_token_data(self, text):
                # Detect contract addresses, Pump.fun links, or tickers
                contract_address = re.search(r'0x[a-fA-F0-9]{40}', text)
                pump_fun_link = re.search(r'pump\\.fun/[a-zA-Z0-9]+', text)
                ticker = re.search(r'\$[A-Z]{3,6}', text)

                return {
                    "contract_address": contract_address.group() if contract_address else None,
                    "pump_fun_link": pump_fun_link.group() if pump_fun_link else None,
                    "ticker": ticker.group() if ticker else None
                }

        stream = CustomStreamListener(self.auth.consumer_key, self.auth.consumer_secret,
                                      self.auth.access_token, self.auth.access_token_secret)
        while True:
            try:
                stream.filter(follow=[str(account) for account in accounts])
            except tweepy.RateLimitError:
                print("Rate limit reached. Sleeping for 15 minutes...")
                time.sleep(900)  # Sleep for 15 minutes