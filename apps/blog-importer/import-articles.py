import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

access_token = os.getenv('SHOPIFY_ACCESS_TOKEN')


url = 'https://barrel-ak.myshopify.com/admin/api/2024-04/blogs/87064576152/articles.json'

headers = {
    'Content-Type': 'application/json',
    'X-Shopify-Access-Token': access_token,
    'Accept': 'application/json'  
}

with open('articles-57057603.json', 'r') as file:
    data = json.load(file)

for article in data['articles']:    
    response = requests.post(url, headers=headers, data=json.dumps({"article": article}))
    print(response.text) 

