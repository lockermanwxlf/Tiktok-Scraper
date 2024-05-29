from nodriver import Tab, start, Browser
from asyncio import TimeoutError
import random
import time
import re

random.seed(time.time())

class TiktokErrors:
    class ProfilePrivate(RuntimeError):
        def __init__(self, *args: object) -> None:
            super.__init__("This account is private")
            
    class ProfileNonexistent(RuntimeError):
        def __init__(self, *args: object) -> None:
            super.__init__("Couldn't find this account")

class DriverResult:
    def __init__(self, tab: Tab, username: str) -> None:
        self.__tab = tab
        self.__username = username
        self.__pattern = re.compile(rf"https://www.tiktok.com/@{self.__username}/.*/(\d*)")

    async def get_post_links(self):
        try:
            a_elements = await self.__tab.select_all(f'[href^="https://www.tiktok.com/@{self.__username}/"]', timeout=3)
            hrefs = [str(element.attrs['href']) for element in a_elements]
            return hrefs
        except TimeoutError:
            return []
        
    async def get_post_ids(self):
        groups = [re.match(self.__pattern, link).groups() for link in await self.get_post_links()]
        return [group[0] for group in groups if group and len(group) > 0]
    
    async def raise_for_error(self, strict=True):
        '`strict`: If true, will only raise if the displayed error is in `TiktokErrors`. Otherwise it will raise on any displayed error.'
        try:
            error = await self.__tab.select("p[class*=emuynwa1]", timeout=3)
        except TimeoutError:
            return
        
        match error.text:
            case "This account is private":
                raise TiktokErrors.ProfilePrivate()
            case "Couldn't find this account":
                raise TiktokErrors.ProfileNonexistent()
                

class Driver:
    async def get_instance():
        browser = await start()
        return Driver(browser)
        
    def __init__(self, browser: Browser) -> None:
        self.__browser = browser
        
    async def get_profile(self, username: str):
        tab = await self.__browser.get(f"https://tiktok.com/@{username}")
        await self.__sign_in_as_guest(tab)
        await self.__something_went_wrong(tab)
        
        return DriverResult(tab, username)
    
    async def __sign_in_as_guest(self, tab: Tab):
        while True:
            try:
                buttons = await tab.select_all('div[class*=css-1cp64nz-DivTextContainer]', timeout=5)
                await buttons[-1].click()
            except TimeoutError:
                break
    
    async def __something_went_wrong(self, tab: Tab):
        while True:
            try:
                button = await tab.select('button[class*=emuynwa3]', timeout=3)
                print("Refreshing 'something went wrong' button.")
                time.sleep(random.random()/2)
                await button.click()
            except TimeoutError:
                break