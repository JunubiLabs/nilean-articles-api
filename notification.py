import requests
import random
import news_db

def send_notification(title, body, image_url):
  url = 'https://nilean-notifications.onrender.com'
  data = {
    "topic": "news_titles",
    "title": title,
    "body": body,
    "image": image_url,
  }
  requests.post(url, data=data)

def send_today_news():
  try:
    todays_news = news_db.get_todays_news()
    
    news = random.choice(todays_news)

    print(news)

    news = news.to_dict()
    title = news['title_en']
    body = news['description']
    image_url = news['imageUrl']

    send_notification(title, body, image_url)

  except Exception as e:
    print(e)
    raise Exception(status_code=500, detail=str(e))
  