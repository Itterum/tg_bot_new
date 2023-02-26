import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as BS

URL = 'https://www.youtube.com/playlist?list=PLFgquLnL59alW3xmYiWRaoz0oM3H17Lth'
options = Options()
options.add_argument('--headless')

arr_video = {
    'content': []
}


def pars_html():
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(10)
    html = driver.page_source

    soup = BS(html, 'html.parser')
    videos = soup.find_all('ytd-playlist-video-renderer')
    return videos


def collect_video():
    videos = pars_html()
    for video in videos:
        video_obj = {}
        a = video.find('a', {'id': 'video-title'})
        if a is None:
            continue
        link = f'https://www.youtube.com{a.get("href")}'
        name = a.get_text()
        video_obj['name'] = name.strip()
        video_obj['url'] = link
        arr_video['content'].append(video_obj)

    with open('data.json', 'w', encoding="utf-8") as file:
        json.dump(arr_video, file, indent=4)
