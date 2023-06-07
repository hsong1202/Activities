import requests
from dotenv import load_dotenv
import pandas as pd
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(dir(response))


