
import requests
import json
api_day="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response=requests.get(api_day)

content=response.content.decode('UTF-8')
# print(content)
# print(type(content))

dic_content=json.loads(content)
# print(dic_content)
image_url=dic_content['url']
print(image_url)

res=requests.get(image_url)
print(res)

with open('file.png','wb') as image:
    image.write(res.content)
image.close()