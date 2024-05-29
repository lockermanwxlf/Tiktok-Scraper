from modules.profiles import Profiles
from modules.driver import Driver
from providers.mega import MegaProvider
import asyncio
import time
import re

async def main():
    driver = await Driver.get_instance()
    provider = MegaProvider("/MEGAsync/TikTok")
    while True:
        profiles = Profiles(False)
        for username, directory, recovery_id in profiles:
            result = await driver.get_profile(username)
            post_links = await result.get_post_links()
            pattern = re.compile(rf"https://www.tiktok.com/@{username}/(.*)/(\d*)")
            posts_info = [re.match(pattern, link).groups() for link in post_links]
            posts_ids = [p[1] for p in posts_info]
            
            # Filter for posts that should be downloaded
            posts_ids = provider.filter_list(directory, posts_ids)
            posts_info = [p for p in posts_info if p[1] in posts_ids]
            
            # Download posts
            
            time.sleep(5)
        time.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())