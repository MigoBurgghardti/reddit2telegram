#encoding:utf-8

subreddit = 'meme_battles+meme+dank_meme'
t_channel = '@MemeArea'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
