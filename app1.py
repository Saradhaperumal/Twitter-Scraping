import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import json

st.set_page_config(page_title='TWITTER SCRAPER')

st.subheader("""
Let's scrape some Tweets... :
""")

# customize form


def scrapetwitter(search_term,start_date,end_date,limit):
# Created a list to append all tweet attributes(data)
    attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search_term} since:{start_date} until:{end_date}').get_items()):
        if i > limit:
            break
        attributes_container.append(
        [tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,
         tweet.lang, tweet.sourceLabel, tweet.likeCount])

# Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(attributes_container,
                         columns=["Date Created", "ID", "URL", "Content", "User", "Replycount", "Retweetcount",
                                  "Language", "Source", "Likecount"])
    return tweets_df


##### TWITTER SCRAPING USING STREAMLIT

search_term = st.text_input('What do you want to search for?')
start_date = st.date_input('Start date', )
end_date = st.date_input('End date',)
limit = st.slider('How many tweets do you want to get?', 0, 500, step=20)
submit_button = st.button(label='Search')


if submit_button:

    tweets_df=scrapetwitter(search_term,start_date,end_date,limit)
    st.dataframe(tweets_df)
    csv1=tweets_df.to_csv()


    json_string = tweets_df.to_json()
    #st.json(json_string, expanded=True)


    col1, col2 = st.columns([1, 1])

    with col1:
        st.download_button(
            "Download CSV ",
            tweets_df.to_csv(),
            file_name='Output_df.csv',
            mime='text/csv')
    with col2:
        st.download_button(
            label="Download JSON",
            file_name="Output.json",
            mime="application/json",
            data=json_string)


##### STORING DATA FRAME TO MONGODB COLLECTION

import pymongo
from pymongo import MongoClient

client=MongoClient('mongodb+srv://saradha:guvi2023@cluster0.vhhfunm.mongodb.net/?retryWrites=true&w=majority')
test_database=scrapetwitter(search_term,start_date,end_date,limit)
test_database.reset_index(inplace=True)
db=client.test_database

collection=db.test_collection

data_dict=test_database.to_dict("records")
#data_dict
#collection.insert_one(data_dict)





