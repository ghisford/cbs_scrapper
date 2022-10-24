from flask import render_template,Blueprint,redirect,request
from bs4 import BeautifulSoup
from news.models import Article
import requests


views = Blueprint('views',__name__)

url = 'https://www.cbsnews.com/latest/rss/main'
resp = requests.get(url)

data = BeautifulSoup(resp.content,features='xml')
articles = data.find_all('item')
# print(articles)

for article in articles:
    title = article.find('title').text
    link = article.find('link').text
    image = article.find('image').text
    description = article.find('description').text
    stored_article = Article(title= title,link= link,image= image,description= description)
    stored_article.save()


@views.route('/cbs_news')
def print_all_articles():
    all_articles = Article.get_all()
    return render_template('news.html',all_articles= all_articles)
