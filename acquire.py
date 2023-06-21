from requests import get
from bs4 import BeautifulSoup
import os

'''
urls = ['https://codeup.com/featured/apida-heritage-month/','https://codeup.com/featured/women-in-tech-panelist-spotlight/','https://codeup.com/featured/women-in-tech-rachel-robbins-mayhill/','https://codeup.com/codeup-news/women-in-tech-panelist-spotlight-sarah-mellor/','https://codeup.com/events/women-in-tech-madeleine/']
'''

def get_articles_texts(urls):
    '''
    this fnction scrapes the given Codeup urls for the title and content and returns them as a dictionary
    urls should be described as above 
    '''
    articles = []

    for url in urls:
        headers = {'User-Agent': 'Codeup Data Science'}
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('article')
        # setting what to grab from post
        for post in posts:
            title = post.find('h1').text.strip()
            content = post.find('div', class_='entry-content').text.strip()
            #returning dictionary
            article = {
                'title': title,
                'content': content
            }

            articles.append(article)

    return articles

******************** Inshorts *************************
def get_news_articles():
    '''
    this function scrapes the inshorts websight for the title content and catagory of the articles in the perscribed areas
    '''
    #defining what to get
    base_url = "https://inshorts.com/en/read/"
    topics = {
        'business': 'business',
        'sports': 'sports',
        'technology': 'technology',
        'entertainment': 'entertainment'
    }
    articles = []
    #creating loop
    for category, topic_url in topics.items():
        url = base_url + topic_url
        response = get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        news_cards = soup.find_all(class_='news-card')
        # waht to get from each news card
        for card in news_cards:
            title = card.find('span', itemprop='headline').text.strip()
            content = card.find('div', itemprop='articleBody').text.strip()
            # retuning dictionary
            article = {
                'title': title,
                'content': content,
                'category': category
            }

            articles.append(article)
    return articles