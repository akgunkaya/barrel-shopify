import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

access_token = os.getenv('SHOPIFY_ACCESS_TOKEN')


url = 'https://barrel-ak.myshopify.com/admin/api/2024-04/blogs.json'

headers = {
    'Content-Type': 'application/json',
    'X-Shopify-Access-Token': access_token,
    'Accept': 'application/json'  
}

data = {
    "blog": {
        "id": 57057603,
        "handle": "news",
        "title": "News",
        "updated_at": "2020-02-17T12:27:55-05:00",
        "commentable": "no",
        "feedburner": None,
        "feedburner_location": None,
        "created_at": "2016-04-12T12:59:17-04:00",
        "template_suffix": None,
        "tags": "",
        "admin_graphql_api_id": "gid://shopify/OnlineStoreBlog/57057603"
    }
}


response = requests.post(url, headers=headers, data=json.dumps(data))  

