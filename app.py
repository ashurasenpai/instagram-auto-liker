import requests
import json
import zlib
import time
from random import *


class instagram_auto_liker:

    cookie = None
    __csrftoken = None
    __HASHTAG_PAGE_URL = 'https://www.instagram.com/explore/tags/'
    __HASHTAG_PAGE_HEADERS = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6,ro;q=0.4,ru;q=0.2',
        'accept': '*/*',
        'referer': None,
        'authority': 'www.instagram.com',
        'cookie': None
    }
    __LIKE_URL = 'https://www.instagram.com/web/likes/'
    __LIKE_HEADERS = {
        'cookie': None,
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6,ro;q=0.4,ru;q=0.2',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': None,
        'x-instagram-ajax': '1',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': None,
        'authority': 'www.instagram.com',
        'content-length': '0'
    }

    def __init__(self):
        print('started')

    def __is_valid_cookie(self, cookie):
        return cookie.find('csrftoken=') > 0 and cookie.find('ds_user_id=') > 0

    def __get_csrftoken(self):
        token_start = self.cookie.find('csrftoken=') + 10
        return self.cookie[token_start:token_start + 32]

    def __get_posts(self, hashtag):
        self.__HASHTAG_PAGE_HEADERS['referer'] = 'https://www.instagram.com/explore/tags/' + hashtag + '/'
        url = self.__HASHTAG_PAGE_URL + hashtag + '/?__a=1'
        headers = self.__HASHTAG_PAGE_HEADERS
        res = requests.get(url, headers=headers)
        jsonData = json.loads(res.text)
        return jsonData['tag']['media']['nodes']

    def __like(self, hashtag, delay):
        posts = self.__get_posts(hashtag)
        # Always like the first post
        post_code = posts[0]['code']
        post_id = posts[0]['id']
        self.__LIKE_HEADERS['referer'] = 'https://www.instagram.com/p/' + \
            post_code + '/'
        self.__LIKE_HEADERS['x-csrftoken'] = self.__get_csrftoken()
        url = self.__LIKE_URL + post_id + '/like/'
        headers = self.__LIKE_HEADERS
        requests.post(url, headers=headers)
        print('Liked:', self.__LIKE_HEADERS['referer'])
        print('Next in', delay, 'seconds')
        time.sleep(delay)

    def start(self, hashtag, amount=50, min_delay=1, max_delay=60):
        print('Starting...')
        try:
            for i in range(0, amount - 1):
                print('(', i + 1, '/', amount, ')')
                self.__like(hashtag, randint(min_delay, max_delay))
            print('Complete.')
        except Exception as e:
            print('Error connecting to Instagram', e)

    def set_cookie(self, cookie):
        if self.__is_valid_cookie(cookie):
            self.cookie = cookie
            self.__HASHTAG_PAGE_HEADERS['cookie'] = self.cookie
            self.__LIKE_HEADERS['cookie'] = self.cookie
            print('Cookie set successfully.')
        else:
            print('Invalid cookie.')


if __name__ == '__main__':
    app = instagram_auto_liker()
    while app.cookie is None:
        cookie = input('IG cookie: ')
        app.set_cookie(cookie)
    hashtag = input('Hashtag #')
    amount = input('Amount of likes: ')
    min_delay = input('Minimum delay(s): ')
    max_delay = input('Maximum delay(s): ')
    app.start(hashtag, int(amount), int(min_delay), int(max_delay))
