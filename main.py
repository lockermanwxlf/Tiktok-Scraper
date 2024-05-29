from modules.profiles import Profiles
from modules.driver import Driver
from providers.mega import MegaProvider
import asyncio
import time
import re

async def main():
    driver = await Driver.get_instance()
    provider = MegaProvider("")
    while True:
        profiles = Profiles()
        for username, directory, recovery_id in profiles:
            result = await driver.get_profile(username)
            post_links = await result.get_post_links()
            pattern = re.compile(rf"https://www.tiktok.com/@{username}/(.*)/(\d*)")
            posts_info = [re.match(pattern, link).groups() for link in post_links]
            filenames = [f"{directory} {post_id}.{"mp4" if post_type == "video" else "jpg"}" for (post_type, post_id) in posts_info]
            
            print(filenames)
            
            # Filter for posts that should be downloaded
            
            # Download posts
            
            time.sleep(5)
        time.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())