from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os
import time
import sys

# APIの情報

key = '1b056851fb3f9ffbebae54b48574f72e'
secret = 'ab284fce99618cc6'
wait_time = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = './'+animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=animalname,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q,license'
)

photos = result['photos']
# 返り値を保存する
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
