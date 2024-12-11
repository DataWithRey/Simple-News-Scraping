#News Scraping and Analysis by Rey
import newspaper
import feedparser
import lxml.html.clean

def scrape_news_from_feed(feed_url):    #function
    articles=[]       #Initialize an Empty List, This list will
                    # store the details of each article, such as title,
                    # author, publish date, and content.

    feed =feedparser.parse(feed_url) #function reads the RSS feed and returns a structured object
    for entry in feed.entries: #corresponds to a news item in the RSS feed.
        article = newspaper.Article(entry.link)
        article.download() #Downloads the article content from the link
        article.parse()   #Extracts the article's content, title, author, and publish date

        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text
        })

    return articles


feed_url = 'http://feeds.bbci.co.uk/news/rss.xml'
articles = scrape_news_from_feed(feed_url)

for article in articles:
    print('Title:', article['title'])
    print('Author:', article['author'])
    print('Publish Date:', article['publish_date'])
    print('Content:', article['content'])
    print()