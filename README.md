# crypto-ads-poc
Proof of concept application for upwork freelancing job requiring an
implementation of Advertisement banners which return revenue in crypto as
opposed to USD

# General concept
We are creating a website where users can upload content and we compensate them.
We need some revenue sharing scheme based on advertisement and we are looking to
freelancers to offer their suggestions through this minimum working example
(MWE).

# Grading Criteria
1. Has to be simple. We are not accountants so we can't contact Chase Manhattan
   bank to set up an account. This is why we want a simple, coder friendly
   solution which crypto provides (we transfer to people's wallets and it is up
   to them to get that crypto onto the modern banking system). Google Ads seems
   like a good solution, but we would need you to explain how we would transfer
   the funds from our account to our user's accounts
2. End to end solution. For example, if you recommend using XYZ Crypto Ad
   Service, do you suggest not only registering an account for us but also
   provide instructions on transfering of those coins to our customers. Also do
   you advise us on the steps involved in getting paid (every 1 cent? every 10
   cents? every 100 dollars?)
3. Providing MWE in Python & Flask. We are using Flask right now because of the
   overhead of using Django. We need someone who is comfortable writing the MWE
   in Python, as well as the minimal coding required in Pure JS.
4. Advising us of the complications. If, for example, we have to register with
   some crypto exchange and that takes 3-6 months, it would be good to tell us.

# Installation
We have made this MWE easy enough such that it will run out of the box on an
Ubuntu machine.

## API Server
The API endpoints have been tested. Simply running `./api/api.sh` should launch
the api on 127.0.0.1. You can then go to https://reqbin.com/ and issue API calls
like so to make sure the service is up. Remember that all calls are POST. You
may need to install a browser plugin to allow you to call 127.0.0.1

127.0.0.1:12345/general/click_ad/0/0
127.0.0.1:12345/general/click_ad/1/0
127.0.0.1:12345/general/click_ad/2/0
127.0.0.1:12345/general/click_ad/3/0
127.0.0.1:12345/general/click_ad/4/0
127.0.0.1:12345/general/click_ad/5/0
127.0.0.1:12345/general/click_ad/6/0
127.0.0.1:12345/general/click_ad/7/0
127.0.0.1:12345/general/click_ad/8/0
127.0.0.1:12345/general/click_ad/9/0

127.0.0.1:12345/general/view_ad/0/0
127.0.0.1:12345/general/view_ad/1/0
127.0.0.1:12345/general/view_ad/2/0
127.0.0.1:12345/general/view_ad/3/0
127.0.0.1:12345/general/view_ad/4/0
127.0.0.1:12345/general/view_ad/5/0
127.0.0.1:12345/general/view_ad/6/0
127.0.0.1:12345/general/view_ad/7/0
127.0.0.1:12345/general/view_ad/8/0
127.0.0.1:12345/general/view_ad/9/0

## HTML
CORS policy will not allow a local copy of a file to make API calls to
127.0.0.1, therefore, launch your browser with web security disabled. In chrome,
you would issue the following command

```
google-chrome --disable-web-security --user-data-dir=~/
```
https://stackoverflow.com/questions/3102819/disable-same-origin-policy-in-chrome

Once opened, go to `/html/index.html`. All links should now work

# HTML Page
The entire MWE, and therefore the HTML page, is designed so as to not need a
database. It is recommended that you always have the developer console open on
your browser to view all output.

When you open the page, you will see a yellow menubar along the top with all the
settings you can tweak, a green "content" area in the middle left with
hypothetical content that has been uploaded, a red "transaction" area to the
middle right with the revenue and transaction information based on user activity
and a purple ad banner at the bottom.

10 users are created and you can simulate logging in with any one of
them using the select DOM object at the top left side. Everytime you change the
user, it simulates a page refresh. To make this obvious, it randomly changes the
content on the page. It also writes some information onto the console. The
purpose of this is to see who gets paid what to better illustrate the revenue
sharing.

To simulate a page refresh you can click the simulate button. This updates the
content area with new thumbnails and makes any API calls, where appropriate (eg.
if "reward on viewing" is checked).

As mentioned above, we are not clear on how revenue will be generated: through
clicking on Ads or through viewing of Ads (or both). Therefore, we have
introduced two checkboxes for tighter control: reward on viewing and reward on
clicking. Modifying these two settings will determine how the website hands out
rewards

# API Service
## api.py
This is the main Flask Python file and it carries out 3 functions
1. Calls settings.__init__ () to initialize the API
2. Imports the /click_ad endpoint
3. Imports the /view_ad endpoint

## settings.py
This file initializes the API but also has many of the classes which simulate
the logic of a crypto based advertisement service. Note that this is purely to
illustrate to the Freelancer what we need in a service. The Freelancer is free
to modify this code in any way they wish (including moving the code out of the
settings.py file and into the actual endpoint files at `/api/endpoint/*.py`)

### CryptoAdService Class
This class represents the hypothentical Crypto Advertisement Service. We ignore
registration and simply assign user ID 0 to our account and we assume whe are
the only user they have. Furthermore, we ignore different advertisement
classes/types and simply assign advertisement id 0 to our ad. We further assume
that the ad returns 0.00001 coins/dollars for every call (whether that call is
on an ad click or view). We then have a few functions

get_ad_reward (): Helper function only

pay_customer (): Presumably when an ad get's clicked on, somehow we get paid.
This is the purpose of this function, to pay us

get_customer_transactions (): Returns all the times the ad was clicked and we
were paid. There are multiple variations of this function, but they are 

### CryptUserAccount Class
Essentially this represents the `user_account` table on the Crypto Advertisement
Service's database. It is a ledger of all of the transactions from our website
and, therefore, the money they have paid out to us

### WebsiteService Class
This class represents our database of users as well as the logic for our revenue
sharing scheme. For simplicity we define 10 users. It is important to note that
we are hard coding these 10 users both here and on the javascript frontend. We
then define a ratio of how much of every dollar goes to us versus how much of it
we give to our users (`house_take`). We then have a few functions to help
facilitate the revenue sharing logic.

pay_customer (): Records a user_id x ad_id x amount triplicate.

get_customer_transactions (): Returns the transactions we gave out to our
customers. There are a few versions of this, but they are all very similar
triplicate.

get_customer_transactions (): Returns the transactions we gave out to our
customers. There are a few versions of this, but they are all very similar

## click_ad.py
This is the implementation of the /click_on_add/ endpoint. Everytime a logged in
user clicks on an ad, they call this endpoint, passing to it their user_id and
the ad_id. To keep the programming simple, we always send 0 for the ad_id.

This function carries out the following actions
1. Instructs the Crypto Advertisement Service to pay us (the website). We don't
   pretend to know how this works out in real life, but here we use
   CryptOhAdz.pay_customer ()
2. We get all the server transactions (website transactions) from the Crypto Ad
   Service. We look at the last, most recent one, to know how much we were paid,
   so we can determine how much of that to share with the user. We also return
   these transactions to the HTML page so it can output it to the browser. In
   practice, we would have individual endpoints for things like `GET
   /server/transactions`, `GET /server/transaction/{transaction_id}`, `GET
   /server/revenue`..., but we are cheating here and just returning everything
   and letting the frontend calculate things like the revenue in Pure JS
3. We then instruct our service (the website) to pay the user
   (EazyPeazy.pay_customer)
4. We retrieve the user_transactions and return that to the frontend for display
   purposes

## view_ad.py
This is the implementation of the /view_add/ endpoint. Everytime a logged in
user views an ad, they call this endpoint, passing to it their user_id and
the ad_id. To keep the programming simple, we always send 0 for the ad_id.

This function works exactly the same as `/click_on_ad`. Technically, the Crypto
Advertising Service should distinguish between the two and return less of an
amount on simply viewing, but due to time constraints we could not implement
this.
