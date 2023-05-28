import tweepy

consumer_key = 'MWZCZ2N3aWZTVnlYYzR4WFYyRHI6MTpjaQ'
consumer_secret = '1V9jxiqtdJ5vRk5N6MwG5IsByXaRZNvLbo5go0n6nAQ8phItCk'
access_token = '1575797952291176448-XW7AJpqNEfV6P1wqD16ydUiS2XqjWR'
access_token_secret = 'Xf4odnESsFpVW0S3W5DQWzgHvxohr0x0Yg0lymQPJvfPM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = 'moaly7yaei'

user = api.get_user(screen_name=username)
user_id = user.id_str

tweets = api.user_timeline(user_id=user_id, count=200)

tweets.sort(key=lambda x: x.favorite_count, reverse=True)

most_liked_tweet = tweets[0]

print(f"Most liked tweet by {username}:\n\n{most_liked_tweet.text}\n\nLikes: {most_liked_tweet.favorite_count}")