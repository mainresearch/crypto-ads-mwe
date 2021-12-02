#!/usr/bin/env python3

import sys
import os
import time
from flask import Flask
from flask_restplus import Api

def __init__ ():
    global api_port
    global api_host
    global app
    global api
    global general_ns
    global CryptOhAdz
    global EazyPeazy

    try:
        api_port        = os.environ.get ('API_PORT', 12345)
        api_host        = os.environ.get ('API_HOST', '0.0.0.0')

    except Exception as e:
        print ('Could not load all environment variables')
        print (e)
        sys.exit (1)

    try:
        app = Flask (__name__)
        api = Api(
            app = app,
            version = "1.0",
            title = "Crypto Ads API",
            description = "Proof of Concept API endpoints for crypto based ads")

        general_ns = api.namespace('general', description='General APIs')

    except Exception as e:
        print ('Could not create API service')
        print (e)
        sys.exit (1)

    # For example's sake, we create a fictional Crytpo Currency based Advertisement
    # Service and since this is 2021, we give it an edgy name
    CryptOhAdz=CryptoAdService ()

    # We put all the logic for the sharing of money earned with all users in a
    # class. Again, we give it an edgy name
    EazyPeazy=WebsiteService()

# The below is hard coded for example's sake only. This represents the website.
class CryptUserAccount:
    def __init__ (self, id):
        self.id = id
        self.transactions = []

    def add_transaction (self, timestamp, amount):
        self.transactions.append ({
            'id': len(self.transactions),
            'timestamp': timestamp,
            'amount': amount
        })

    def get_transactions (self):
        return self.transactions

# We create a class here to represent a crypto advertising service. This is
# purely to illustrate to the Freelancer that we want a service to handle the
# transactions for us
class CryptoAdService:
    def __init__ (self):
        self.rewards=[
            {
                'ad_id': 0,
                 'amount': 0.00001
            }
        ]

        # The user account here is the single website (us)
        self.user_accounts = [CryptUserAccount (id=i) for i in range (1)]

    def get_ad_reward (self, ad_id):
        for reward in self.rewards:
            if reward ['ad_id'] == ad_id:
                return reward['amount']

        print ('Ad {} not found'.format(ad_id))
        raise Exception ()

    # NOTE: if the user_id is not found, we exit the prgoram but we don't check
    # to see if the ad_id is valid
    def pay_customer (self, user_id, ad_id):
        for user_account in self.user_accounts:
            if user_account.id == user_id:
                user_account.add_transaction (time.time(), self.get_ad_reward(ad_id=ad_id))
                return True

        # You are searching for a user that does not exist
        print ('User {} not found'.format(user_id))
        raise Exception ()

    # NOTE: if the user_id is not found, we exit the prgoram but we don't check
    # to see if the ad_id is valid
    def get_customer_transactions (self, user_id):
        for user_account in self.user_accounts:
            if user_account.id == user_id:
                return user_account.transactions

        # You are searching for a user that does not exist
        print ('User {} not found'.format(user_id))
        raise Exception ()

    # NOTE: if the user_id is not found, we exit the prgoram but we don't check
    # to see if the ad_id is valid
    def get_customer_transaction (self, user_id, transaction_id):
        for user_account in self.user_accounts:
            if user_account.id == user_id:
                if transaction_id < 0 or transaction_id >= len(user_account.transactions):
                    # You are searching for a transaction that does not exist
                    print ('Transaction {} not found'.format(transaction_id))
                    raise Exception ()

                return user_account.transactions[transaction_id]

        # You are searching for a user that does not exist
        print ('User {} not found'.format(user_id))
        raise Exception ()

    # NOTE: if the user_id is not found, we exit the prgoram but we don't check
    # to see if the ad_id is valid
    def get_last_customer_transaction (self, user_id):
        for user_account in self.user_accounts:
            return self.get_customer_transaction (user_id, len (user_account.transactions)-1)

        # You are searching for a user that does not exist
        print ('User {} not found'.format(user_id))
        raise Exception ()

    # NOTE: if the user_id is not found, we exit the prgoram but we don't check
    # to see if the ad_id is valid
    def get_customer_revenue (self, user_id):
        for user_account in self.user_accounts:
            if user_account.id == user_id:
                revenue = 0.0
                for transaction in user_account.transactions:
                    revenue += transaction['amount']

                return revenue

        # You are searching for a user that does not exist
        print ('User {} not found'.format(user_id))
        raise Exception ()

# The below is hard coded for example's sake only. This represents the users of
# our website. For example, the advertisement company pays us out $100 (or 100
# crypto coins) and we decide when to share it with our customer base (eg. share
# half among all our users)
class UserAccount:
    def __init__ (self, id):
        self.id = id
        self.transactions = []

    def add_transaction (self, timestamp, ad_id, amount):
        self.transactions.append ({
            'id': len(self.transactions),
            'timestamp': timestamp,
            'ad_id': ad_id,
            'amount': amount
        })

    def get_transactions (self):
        return self.transactions

# We create a class here to represent our web service.
class WebsiteService:
    def __init__ (self, CryptOhAdzId=0):
        # For example's sake we will add 10 users and manage them here so the
        # Freelancer does not have to worry about connecting to and maintaining
        # a database. Since this is an example only, we will not worry about
        # registration and authentication
        self.user_accounts = [UserAccount (id=i) for i in range (10)]

        # Technically we should have login credentials for the Crypto
        # Advertisement service, but to keep things simple we will just record
        # the id here
        self.CryptOhAdzId=CryptOhAdzId

        # When this service gets paid out by the CryptoAdService (CryptOhAdz),
        # we will want to give some percentage of that pay out to the
        # appropriate user(s). The house will keep 90% and the customer will get
        # 10%
        self.house_take = 0.9

    # Share a portion of the transaction with the appropriate users. To keep
    # things simple, here we will share only with the user that clicked on the
    # ad (ignore who uploaded the pictures being viewed, etc.)
    #
    # NOTE: if the user_id is not found, we exit the prgoram but we don't check
    # to see if the ad_id is valid
    def pay_customer (self, user_id, ad_id, transaction_amount):
        house_amount = transaction_amount * self.house_take
        customer_amount = transaction_amount - house_amount

        for user_account in self.user_accounts:
            if user_account.id == user_id:
                user_account.add_transaction (timestamp=time.time(), ad_id=ad_id, amount=customer_amount)
                return True

        # You are searching for a user that does not exist
        print ('User {} not found'.format(user_id))
        raise Exception ()

    def get_all_customer_transactions (self):
        transactions=[]
        for user_account in self.user_accounts:
            transactions.append(user_account.transactions)

        return transactions

    # NOTE: if the user_id is not found, we exit the prgoram but we don't check
    # to see if the ad_id is valid
    def get_customer_transactions (self, user_id):
        for user_account in self.user_accounts:
            if user_account.id == user_id:
                return user_account.transactions

        # You are searching for a user that does not exist
        print ('User {} not found'.format(user_id))
        raise Exception ()

