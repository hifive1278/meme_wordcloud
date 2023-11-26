# Wordcloud of /r/memes
Scraped top 300 trending memes /r/memes during Thanksgiving 2023 and used text-recognition to create a word cloud.

Used the Python Reddit API Wrapper (“praw”) to extract the top 300 posts from the /r/memes subreddit, limiting the scraped content to images. These images were then fed into API Ninja’s text-recognition model, the results of which were assembled into a .csv file containing all identified words contained across the 300 memes. The dataset was cleaned for obvious garbage (i.e. “e%nn;u,ex,nu”) or text unrelated to the meme content itself (i.e. “Made with Mematic”). Finally, a word cloud was assembled containing words which appeared between 3 and 13 times in the dataset.

![bettermemewordcloud](https://github.com/hifive1278/meme_wordcloud/assets/106018830/a8a15521-0a7b-4dfd-9617-47d8ce060a60)

Credit for much of praw scraping code: https://github.com/daspartho/meme-videos
