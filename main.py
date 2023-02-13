from get_text_data import GetData
import pandas as pd
import os


# url = "https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy/"
# GetData.article_data(url)

cwd = os.getcwd()

url_data = pd.read_csv(f"{cwd}\input.csv")

# Remove column name 'URL_ID'
url_data = url_data.drop(['URL_ID'], axis=1)
# url_data = url_data.reset_index()


for row in url_data.itertuples():

    url = row[1]
    # creates .txt files in input folder
    GetData.article_data(url)
