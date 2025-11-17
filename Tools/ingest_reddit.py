"""
Sample reddit ingestion script (example).
Requires: set REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET in .env for full OAuth usage.
This stub uses the public reddit endpoints for demonstration only.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')

def fetch_subreddit(subreddit, limit=100):
    # Public read-only endpoint (limited). For production use OAuth.
    url = f'https://www.reddit.com/r/{subreddit}/top.json?limit={limit}'
    headers = {'User-Agent': 'x-lang-ingest/0.1'}
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    data = r.json()
    posts = [p['data']['title'] + '\n' + (p['data'].get('selftext') or '') for p in data['data']['children']]
    return posts

if __name__ == '__main__':
    print(fetch_subreddit('machinelearning', 10))
