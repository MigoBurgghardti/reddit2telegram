#encoding:utf-8

subreddit = 'wholesome+WholesomeComics+wholesomegifs+wholesomepics+wholesomememes+MadeMeSmile+gatesopencomeonin'
t_channel = '@r_wholesome'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
