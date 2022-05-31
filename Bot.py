import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import os
import json
import urllib.request
 



 

id_canal_youtube="UC1s7u4KXpKD1MBCvOVuZCQg" #Obten el id del canal de youtube

url = f"https://www.youtube.com/feeds/videos.xml?channel_id={id_canal_youtube}"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')



titulo_Video = soup.find_all("title")[1].text

link_Video = []
for link in soup.find_all('link'):
    link_Video.append(link.get('href'))

print(f"Link Video: {link_Video[2]}\n\nTitulo del video: {titulo_Video}") 
