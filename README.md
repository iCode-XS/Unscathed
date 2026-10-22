



# Unscathed

This project was created because of my previous repository: multi-source-project

Normally, when you click to the next page button on a site, what happens in the browser URL bar:

Before clicking next page, URL: website.com/page1

After clicking next page, URL: website.com/page2

This wasn't happening with one of the websites I m extracting in my previous project, causing my previous tool(beautifulSoup4) to only extract data from Page 1

I couldn't go beyond to the rest of the pages with the extraction.

So, In this project, I used Playwright - the browser automation tool to solve the extraction problem, which I couldn't do it before with beautifulsoup.

### Target Website

You can access the link to the website - [Click here](https://www.ioba.org/members-directory)

### Demo

https://github.com/user-attachments/assets/47bfb201-58d6-47f3-b02b-4d56c96ead27

I created a CSV file of the postgreSQL database storing the data, you can check the file with link down below:

[Preview](https://www.dropbox.com/scl/fi/v96h67mlsocvhka1gm6ij/bookstores_export.csv?rlkey=52klvo7ej2uysq83fsnkek542&st=qc80dycm&e=1&dl=0) | [Download File](https://www.dropbox.com/scl/fi/v96h67mlsocvhka1gm6ij/bookstores_export.csv?rlkey=52klvo7ej2uysq83fsnkek542&st=qc80dycm&e=1&dl=1)

### Tech Stack

> python: the language i am using

> playwright: the browser automation tool I am using to extract the data from the website

> postgreSQL: for storing the data

> loguru: for logging the state of the entire extraction just in case something unexpected happened
