from requests_html import HTMLSession   
from bs4 import BeautifulSoup as bs
  
youtuber="vegetta777" #Escribe el nombre del canal del youtuber

video_url = f"https://www.youtube.com/user/{youtuber}"  
 
session = HTMLSession()  

response = session.get(video_url)  

response.html.render(timeout=20)  

soup = bs(response.html.html, "html.parser")  

id_Canal = soup.find("meta", itemprop="channelId")['content']  
  
print(f"{id_Canal}")  
