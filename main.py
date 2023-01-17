import requests
import pandas as pd
headers = {
    'user-agent': 'my-app'
}


# def main(url):
#     with requests.Session() as req:
#         req.headers.update(headers)
#         allin = []
#         for t in ['AMZN', 'GS', 'AAPL']:
#             params = {
#                 't': t
#             }
#             r = req.get(url, params=params)
#             df = pd.read_html(r.content, attrs={'id': 'news-table'})[0]
#             df[2] = t
#             allin.append(df)
#         df = pd.concat(allin, ignore_index=True)
#         #print(df[2])
#         #df.to_csv('data.csv', index=False)

df = pd.read_csv('data.csv', usecols=[0,1,2], names=['date_time', 'title','ticker'])
# drop first row
data = df
#print(data)

date_data = data.iloc[0][0].split(' ')
day = 0 #define to be used in loop
time = 0 #defined to be used in loop
print(day)

parsed_data = []
for i, row in data.iterrows():
    title = data['title'].iloc[i]
    ticker = data['ticker'].iloc[i]
    date_data = data.iloc[i][0].split(' ')
    if len(date_data) == 2:
        day = date_data[0]
        time = date_data[1]
    else:
        time = date_data[0]

    parsed_data.append([day, time, ticker, title])

clean_df = pd.DataFrame(parsed_data, columns=['date', 'time', 'ticker', 'title'])
print(clean_df)

# main('https://finviz.com/quote.ashx')