"""
    ULTIMATE SCRIPT

    It uses data written in files:
        * follow_followers.txt
        * follow_following.txt
        * like_hashtags.txt
        * like_users.txt
    and do the job. This bot can be run 24/7.
"""

import os
import sys
from instabot import Bot

sys.path.append(os.path.join(sys.path[0], '../../'))

bot = Bot(
            proxy=None,
            max_likes_per_day=500,
            max_unlikes_per_day=0,
            max_follows_per_day=350,
            max_unfollows_per_day=0,
            max_comments_per_day=0,
            max_likes_to_like=100,
            filter_users=True,
            filter_business_accounts=True,
            filter_verified_accounts=True,
            max_followers_to_follow=1000,
            min_followers_to_follow=100,
            max_following_to_follow=7500,
            min_following_to_follow=10,
            max_followers_to_following_ratio=10,
            max_following_to_followers_ratio=2,
            max_following_to_block=2000,
            min_media_count_to_follow=3,
            like_delay=10,
            unlike_delay=10,
            follow_delay=30,
            unfollow_delay=30,
            comment_delay=60,
            whitelist='/whitelist.txt',
            blacklist=False,
            comments_file=False,
            stop_words=['shop', 'store', 'free']
)

bot.login()

# print(bot.whitelist)

hashtags = bot.read_list_from_file('hashtags.txt')
print(hashtags)
print(bot.get_hashtag_users('zon'))

# users_to_follow = [bot.get_hashtag_users('zon') for x in hashtags]
# print(users_to_follow)


print("Current script's schedule:")
follow_followers_list = bot.read_list_from_file("follow_followers.txt")
print("Going to follow followers of:", follow_followers_list)
follow_following_list = bot.read_list_from_file("follow_following.txt")
print("Going to follow following of:", follow_following_list)
like_hashtags_list = bot.read_list_from_file("like_hashtags.txt")
print("Going to like hashtags:", like_hashtags_list)


tasks_list = []
for item in follow_followers_list:
    tasks_list.append((bot.follow_followers, {'user_id': item, 'nfollows': None}))
for item in follow_following_list:
    tasks_list.append((bot.follow_following, {'user_id': item}))
for item in like_hashtags_list:
    tasks_list.append((bot.like_hashtag, {'hashtag': item, 'amount': None}))

# shuffle(tasks_list)
for func, arg in tasks_list:
    func(**arg)
