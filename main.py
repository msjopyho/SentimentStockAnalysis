'''beautiful soup - scrape
pandas nltk for sentiment analysis
matplotlib for visualization'''

# accumulate headlines
# sentiment analysis on headlines on finviz
# parse title and timestamp

# need request module and beautiful soup

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
#import nltk --> terminal of pycharm --> "python3"command terminal to download corpus
#nltk.download() --> pop up window to select package (from "all packages" -->vader_lexicon

finviz_url = 'https://finviz.com/quote.ashx?t='  # raw url
# come up with list of tickers
ticker = ['AMZN', 'APPL', 'FB', 'AMD']

news_tables = {}

for ticker in ticker:
    url = finviz_url + ticker  # append ticker to url
    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, "html") #needed to specify 'x.parser' not just 'html'
    news_table = html.find(id='news-table')
    news_table[ticker] = news_tables #storing in dictionary

    break

'''Manipulating Fiz Data'''
#extract data to use sentiment analysis on
parsed_data = []

for ticker, news_table in news_tables.items():

    for row in news_table.findAll('tr'):

        title = row.a.text
        date_data = row.td.text.split(' ')

        if len(date_data) == 1:
            time = date_data[0] #timestamp = row.td.text
        else:
            date = date_data[0]
            time = date_data[1]

        parsed_data.append([ticker, date, time, title])

df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])
"""apply sentiment analysis"""

vader = SentimentIntensityAnalyzer()

f = lambda title: vader.polarity_scores(title)['compound']
df['compound'] = df['title'].apply(f)
df['date'] = pd.to_datetime(df.date).dt.date

plt.figure(figsize=(10,8))
mean_df = df.groupby(['ticker', 'date']).mean().unstack()
mean_df = mean_df.xs('compound', axis="columns")
mean_df.plot(kind='bar')
plt.show()

