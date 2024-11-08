import requests
import pandas as pd

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "P9HVZT8Q80Y9ORHR"
NEWS_KEY = "729f32ee673b494198c9a315a58158ee"

funct = "TIME_SERIES_DAILY"
FIVE = 0.5
TEN = 0.10

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
url = STOCK_ENDPOINT + "?function=" + funct + "&symbol=" + STOCK + "&apikey=" + STOCK_KEY
response = requests.get(url)
data = response.json()

#this code convert data dict to a pandas data frame
df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient='index')

# this convert the index to the date value
df.index = pd.to_datetime(df.index)
# Sorting by the date index, most recent first
df.sort_index(ascending=False, inplace=True)  

# this extract the closing prices for yesterday and the day before yesterday
yesterday_close = df.loc[df.index[0], "4. close"]
day_before_yesterday_close = df.loc[df.index[1], "4. close"]

# this Compare the closing prices
print(f"Yesterday's closing price ({df.index[0].date()}): {yesterday_close}")
print(f"Day before yesterday's closing price ({df.index[1].date()}): {day_before_yesterday_close}")
ayer = float(yesterday_close)
antes_ayer = float(day_before_yesterday_close)
diff = abs(ayer - antes_ayer)

diff_per = (diff / ayer) * 100 

print(diff_per)

if diff_per > 5.00:
    print("Get NEWS")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

news_url = NEWS_ENDPOINT + "?q=" + COMPANY_NAME + "&apiKey=" + NEWS_KEY

news_response = requests.get(news_url)
news_data = news_response.json()

df_news = pd.DataFrame(news_data)
slice_data = df_news[:3]
title = slice_data["articles"][0]["title"]
print(title)
print(slice_data)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

