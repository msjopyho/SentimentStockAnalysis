'''beautiful soup - scrape
pandas nltk for sentiment analysis
matplotlib for visualization'''

# # accumulate headlines
# # sentiment analysis on headlines on finviz
# # parse title and timestamp
#
# # need request module and beautiful soup
#
# from urllib.request import urlopen, Request
# from bs4 import BeautifulSoup
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import pandas as pd
# import matplotlib.pyplot as plt
#
#url = 'https://finviz.com/quote.ashx?t='  # raw url
# # come up with list of tickers
#ticker = ['AMZN', 'APPL', 'FB', 'AMD']
#
# news_tables = {}
#
# for ticker in ticker:
#     url = finviz_url + ticker  # append ticker to url
#     req = Request(url=url, headers={'user-agent': 'my-app'})
#     response = urlopen(req)
#
#     html = BeautifulSoup(response, "html.parser") #needed to specify 'x.parser' not just 'html'
#     news_table = html.find(id='news-table')
#     news_table[ticker] = news_tables #storing in dictionary
#
#     break
#
# '''Manipulating Fiz Data'''
# #extract data to use sentiment analysis on
# parsed_data = []
#
# for ticker, news_table in news_tables.items():
#
#     for row in news_table.findAll('tr'):
#
#         title = row.a.text
#         date_data = row.td.text.split(' ')
#
#         if len(date_data) == 1:
#             time = date_data[0] #timestamp = row.td.text
#         else:
#             date = date_data[0]
#             time = date_data[1]
#
#         parsed_data.append([ticker, date, time, title])
#
# df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])
# """apply sentiment analysis"""
#
# vader = SentimentIntensityAnalyzer()
#
# f = lambda title: vader.polarity_scores(title)['compound']
# df['compound'] = df['title'].apply(f)
# df['date'] = pd.to_datetime(df.date).dt.date
#
# plt.figure(figsize=(10,8))
# mean_df = df.groupby(['ticker', 'date']).mean().unstack()
# mean_df = mean_df.xs('compound', axis="columns")
# mean_df.plot(kind='bar')
# plt.show()

import requests
import pandas as pd
headers = {
    'user-agent': 'my-app'
}


def main(url):
    with requests.Session() as req:
        req.headers.update(headers)
        allin = []
        for t in ['AMZN', 'GS']:
            params = {
                't': t
            }
            r = req.get(url, params=params)
            df = pd.read_html(r.content, attrs={'id': 'news-table'})[0]
            allin.append(df)
        df = pd.concat(allin, ignore_index=True)
        #df[['date', 'time']] = df[0].astype(str).str.split(' ', expand=True)
        print(df.head)
        # df.to_csv('data.csv', index=False)

        # parsed_data = []
        #
        # for index, row in df.iterrows():
        #
        #     title = df[1]
        #     date_data = df[0].str.split(' ')
        #
        #     if len(date_data) == 1:
        #         time = date_data[0] #timestamp = row.td.text
        #     else:
        #         date = date_data[0]
        #         time = date_data[1]
        #
        #     parsed_data.append([t, date, time, title])
        # print(parsed_data)

main('https://finviz.com/quote.ashx')
