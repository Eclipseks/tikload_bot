import os
import time
import urllib.request

from aiogram import types
from selenium import webdriver as web
from bs4 import BeautifulSoup as bs

from config import dp, bot, ADMIN_USER

def tik_tok(url, username):
    op=web.ChromeOptions()
    op.add_argument('--headless')
    driver=web.Chrome('./chromedriver', options=op)
    driver.get(url)
    time.sleep(5)
    html=driver.page_source
    soup=bs(html, 'html.parser')
    video=soup.find('video')
    urllib.request.urlretrieve(video['src'], f'{username}.mp4')


@dp.message_handler(content_types='text')
async def tiktok_handler(message: types.Message):
    if message.text[:4] == 'http':
        await bot.delete_message(
            message.chat.id,
            message.message_id
        )
        
        msg = await message.answer(
            '⬇️Загрузка началась, ожидайте.'
        )
        
        tik_tok(
            message.text,
            message.from_user.username
        )
        
        video=types.InputFile(f'./{message.from_user.username}.mp4')
        
        await bot.send_video(
            message.chat.id,
            video,
            caption=f'Ссылка на видео: {message.text}'
        )
        
        os.remove(f'./{message.from_user.username}.mp4')
        
        await bot.delete_message(
            msg.chat.id,
            msg.message_id
        )

