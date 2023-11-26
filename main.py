import praw
import requests
import os
import pandas as pd
from google.colab import files

# Scrape the memes from /r/memes
def get_images(sub_name='memes', limit=1000):

    login = praw.Reddit(
        client_id='YOUR CLIENT ID',
        client_secret='YOUR CLIENT SECRET',
        user_agent='YOUR USER AGENT',
    )

    os.makedirs('memes') # only run this the first time, comment out otherwise
    
    sub = login.subreddit(sub_name) # creates a subreddit instance

    n=1 # n is used for naming images
    for post in sub.hot(limit=limit):
        url=post.url
        if url.endswith('.jpg'):
            img_data = requests.get(url).content
            with open(f'memes/img{n}.jpg', 'wb') as handler:
                handler.write(img_data) # saving images
                n+=1  
              
get_images()

# Extract text from each meme
df = pd.DataFrame()
word_list = []

for scraped_meme in os.listdir('memes'):
    api_url = 'https://api.api-ninjas.com/v1/imagetotext'
    image_file_descriptor = open('memes/' + scraped_meme, 'rb')
    files = {'image': image_file_descriptor}
    headers = {
        'X-Api-Key': 'YOUR API KEY'
    }
    r = requests.post(api_url, files=files, headers=headers)
    # print(r.json())

    for word in r.json():
      curr_word = word.get('text')
      word_list.append(curr_word)

df = pd.Series(word_list).to_frame()

# Export to .csv and download locally
df.to_csv('trendingmemes.csv')
files.download('trendingmemes.csv')
