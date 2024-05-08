# Web-Scraper

Web-Scraper is a CLI application that makes it possible to scrape data from a URL.
To scrape data from a website and save it to a CSV file, Python developers often use libraries like requests for making HTTP requests and BeautifulSoup from the bs4 package for parsing HTML content. Additionally, the csv module from Python's standard library is typically used to write data into a CSV file.

### Getting Started 

Clone the repo to your computer. Go to your terminal and navigate to the repo folder. Then type "pip install" then enter. This command installs all the modules you need to run the program.

## Prerequisites & Installing

Since Web-Scraper is a server side python application you need to run that from your terminal. Depend on which OS you are using that can be different. Here is a guide about how to run a node.js app on your computer if you are using windows: http://blog.gvm-it.eu/post/20404719601/getting-started-with-nodejs-on-windows. If you are using mac that would be easier. Just go to your terminal and navigate to the Hangman-CLI folder. Then you need to download and install all the python modules that are used in this application. So type "pip install" then hit enter. That would install the needed modules.

Web scraping, the process of extracting data from websites, has emerged as a powerful technique to gather information from the vast expanse of the internet. In this CLI app, we’ll explore various Python libraries and modules commonly used for web scraping and delve into why Python 3 is the preferred choice for this task.

Essential Packages and Tools for Python Web Scraping
The latest version of Python, offers a rich set of tools and libraries specifically designed for web scraping, making it easier than ever to retrieve data from the web efficiently and effectively.

### 1. Requests Module
- Find the API Documentation here : https://requests.readthedocs.io/en/latest/api/
### 2. BeautifulSoup Library
- Beautiful Soup is a Python library that works with a parser to extract data from HTML and can turn even invalid markup into a parse tree. However, this library is only designed for parsing and cannot request data from web servers in the form of HTML documents/files. For this reason, it's mostly used alongside the Python Requests Library. Note that Beautiful Soup makes it easy to query and navigate the HTML but still requires a parser. The following example demonstrates the use of the html.parser module, which is part of the Python Standard Library. 
### 3. Selenium
### 4. Lxml 
### 5. Urllib Module
### 6. PyautoGUI
### 7. Schedule
### 8. Pandas 
||Requests|Beautiful Soup|lxml|Selenium|
|:--- |:--- |:--- |:---|:---|
|Purpose|Simplify making HTTP requests|Parsing|Parsing|Simplify making HTTP requests|
|Ease-of-use|High|High|Medium|Medium|
|Speed|Fast|Fast|Very Fast|Slow|
|Learning Curve|Very easy (beginner-friendly)|Very easy (beginner-friendly)|Easy|Easy|
|Documentation|Excellent|Excellent|Good|Good|
|JavaScript Support|None|None|None|Yes|
|CPU and Memory Usage|Low|Low|Low|High|
|Size of Web Scraping Project Supported|Large and small|Large and small|Large and small|Small|


 
### Running and test

At the start you see a command that asks if you want to start a new game. Type "yes" and hit enter to start the game. If you type "no" and then u hit enter you would exit the game. This process happens at the end of each round though. Whether you win or lose. After submitting yes, you will be asked to guess a letter, if you guess a letter that exist in the randomly picked word from an animation movie array, it would show up on the screen. Otherwise you would see underscores indicating the unguessed letters. You would have 15 chances to guess the whole word by guessing each letters.

## Deployment

This application is not deployed on the web. To run this locally you need to go to your terminal and run the program from there. For more information about how to do that, read the app description, Prerequisites & Installing and Running and test section on this file. 

## Built With

* [Python](https://python.org)