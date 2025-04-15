from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

# Initialize the FastAPI app
app = FastAPI()

# Define the site checking model
class CheckUsername(BaseModel):
    username: str

# Define the sites.json as a global variable (or import if external)
SITES = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Medium": "https://medium.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Dev.to": "https://dev.to/{}",
    "Facebook": "https://www.facebook.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Twitch": "https://www.twitch.tv/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "YouTube": "https://www.youtube.com/c/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "Flickr": "https://www.flickr.com/photos/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "CodePen": "https://codepen.io/{}",
    "Behance": "https://www.behance.net/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Tumblr": "https://{}.tumblr.com/",
    "Quora": "https://www.quora.com/profile/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "MySpace": "https://myspace.com/{}"
}

@app.get("/")
async def read_root():
    return {"message": "Welcome to ShadowHawk OSINT API!"}

@app.post("/check_username/")
async def check_username(data: CheckUsername):
    found_sites = []
    
    for site, url in SITES.items():
        user_url = url.format(data.username)
        response = requests.get(user_url)
        
        if response.status_code != 404:
            found_sites.append({site: user_url})

    if found_sites:
        return {"status": "success", "found_on": found_sites}
    else:
        return {"status": "not found", "message": "Username not found on any platform."}

# Run this app using Uvicorn from terminal:
# uvicorn app:app --reload
