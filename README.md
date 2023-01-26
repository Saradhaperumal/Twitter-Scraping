Twitter Scraping Using Streamlit and Snscrape
Project Title	Twitter Scraping
Skills take away From This Project	Python scripting, Data Collection, MongoDB, Streamlit
Domain	Social Media

Problem Statement:
Today, data is scattered everywhere in the world. Especially in social media, there may be a big quantity of data on Facebook, Instagram, Youtube, Twitter, etc. This consists of pictures and films on YouTube and Instagram as compared to Facebook and Twitter. To get the real facts on Twitter, you want to scrape the data from Twitter. You Need to Scrape the data like (date, id, url, tweet content, user, reply count, retweet count, language, source, like count etc) from twitter.

Approach: 	
•	By using the “snscrape” Library, Scrape the twitter data from Twitter Reference
•	Create a dataframe with date, id, url, tweet content, user,reply count, retweet count, language, source, like count.
•	Store each collection of data into a document into Mongodb along with the hashtag or key word we use to  Scrape from twitter. eg:({“LIC corporation+current Timestamp”: [{1000  Scraped data from past 100 days }]})
•	Create a GUI using streamlit that should contain the feature to enter the keyword or Hashtag to be searched, select the date range and limit the tweet count need to be scraped. After scraping, the data needs to be displayed in the page and need a button to upload the data into Database and download the data into csv and json format.


Step 1:
Install the packages pandas, streamlit, pymongo, snscrape and pycharm version 2020.3 before executing the project;
Now, Run the program app1.py in pycharm using streamlit command.
 ![image](https://user-images.githubusercontent.com/116868444/214867547-4b391129-b88b-4c17-8078-6cd82ec86979.png)



Step2: You will get link that opens in browser
 ![image](https://user-images.githubusercontent.com/116868444/214867954-44f97b73-2a4a-47df-8c28-204c04f6e0f9.png)


Step 3: The Screen appears like this
 ![image](https://user-images.githubusercontent.com/116868444/214867992-44fff5b9-242a-4ca8-8079-ecb3e997d354.png)

Step 4: Give the input details
 ![image](https://user-images.githubusercontent.com/116868444/214868041-bd8aa9ed-c9cc-468c-8af1-df3d95f0f263.png)

Step 5:
The dataframe appears as below
 
 ![image](https://user-images.githubusercontent.com/116868444/214868120-d091c82f-84a9-494f-8b8b-86d3e624fac5.png)


Step 6:
Now you can download the file either in csv or in json format, the csv file is as below
 ![image](https://user-images.githubusercontent.com/116868444/214868168-5f859c4b-cebc-40d8-92f5-c8e56325a76e.png)	![image](https://user-images.githubusercontent.com/116868444/214868246-38aadee3-770a-4373-82aa-92977ae7bfdb.png)

Step 7:
The json file is as below
 ![image](https://user-images.githubusercontent.com/116868444/214868278-375dae51-ebcf-4a85-bde4-cdee4497fd2b.png)


Step 8:
The same dataframe gets updated in Cloud .(MongoDB Atlas)
![Uploading image.png…]()

 

