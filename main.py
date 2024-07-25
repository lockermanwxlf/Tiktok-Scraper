from modules.profiles import Profiles
from tiktok_driver import TiktokDriver
from tiktok_driver.providers.tiksave import get_download_info, DownloadType
import asyncio
import requests
import time
import json
import os
import re

async def main():
    driver = await TiktokDriver.get_instance()
    pattern = re.compile(r' (\d+)[ .]')
    while True:
        profiles = Profiles()
        for username, directory, recovery_id in profiles:
            
            # Get posts
            result = await driver.get_user(username)
            posts = await result.get_posts()
            
            # Get the post ids of currently existing files in output directory.
            with open('config.json', 'r') as f:
                output_directory = os.path.join(json.load(f)['OUTPUT_DIRECTORY'], directory)
            os.makedirs(output_directory, exist_ok=True)
            existing_files = next(os.walk(output_directory))[2]
            matches = [re.search(pattern, filename) for filename in existing_files]
            matches = [match.group(1) for match in matches if len(match.groups()) > 0]
            
            # Remove posts from download list if they are already downloaded.
            posts = filter(lambda post: post.id not in matches, posts)
            
            # Download posts
            for post in posts:
                download_info = get_download_info(post.url)
                print('Downloading', directory, post.id)
                for i, download in enumerate(download_info, 1):
                    filename = f'{directory} {post.id}{f' {i}' if len(download_info) > 1 else ''}.{'png' if download.type == DownloadType.IMAGE else 'mp4'}'
                    response = requests.get(download.url)
                    response.raise_for_status()
                    content = response.content
                    with open(os.path.join(output_directory, filename), 'wb+') as f:
                        f.write(content)
                    time.sleep(5)
            time.sleep(24)

if __name__ == "__main__":
    asyncio.run(main())