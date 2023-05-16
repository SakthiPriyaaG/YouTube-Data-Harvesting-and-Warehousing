## YouTube-Data-Harvesting-and-Warehousing ##
This is my intermediate level Python Project to harvest YouTube data using YouTube Data API and store the data in a MongoDB database as a data lake.After that the data is migrated from the data lake to a SQL database as tables and are displayed in the streamlit application.

## STEPS TO BE FOLLOWED ##

Install the necessary libraries: Make sure you have the required Python libraries installed, such as google-api-python-client, pymysql, pymongo, and streamlit.

Set up YouTube API access: Go to the Google Developers Console and create a new project. Enable the YouTube Data API and obtain API credentials (API key or OAuth client ID).

Retrieve YouTube data: Use the google-api-python-client library to interact with the YouTube Data API. You can fetch data such as video details, channel information, comments, etc. Refer to the YouTube Data API documentation for more details on available endpoints and parameters.

Store data in MySQL: Use the pymysql library to establish a connection with your MySQL database. Create a table to store the YouTube data you want to capture. You can define the table schema based on the specific data you're interested in (e.g., video ID, title, description, view count, etc.). Insert the retrieved data into the MySQL table.

Store data in MongoDB: Use the pymongo library to connect to your MongoDB database. Create a collection to store the YouTube data. You can define the structure of the document based on the data you want to store (similar to the MySQL schema). Insert the retrieved data into the MongoDB collection.

Create a Streamlit application: Use the streamlit library to build a web application that allows you to interact with the harvested YouTube data. You can create a dashboard or a search functionality, for example, to query and display the stored information.

## Thank You ##
## Hope this is useful for you ##
