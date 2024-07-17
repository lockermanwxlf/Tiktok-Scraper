# Tiktok-Scraper
Nodriver-based scraper for TikTok

There is a memory leak in this. From my experience it seems running any automated browser in a loop (like selenium) leads to a memory leak, so 
try not to let the program run for more than an hour or you'll have an 8gb task. You can restart it immediately after cancellation 
if you want to.

---

This makes use of my [tiktok_driver](https://github.com/lockermanwxlf/Tiktok-Driver) package, thus Python version >= 3.9 is required.

# Installation

Ensure you have Google Chrome installed. This is required for nodriver.

```bash
git clone https://github.com/lockermanwxlf/Tiktok-Scraper.git
cd Tiktok-Scraper
pip install -r requirements.txt
```

# Usage
1) Set `OUTPUT_DIRECTORY` in [config.json](config.json) if you want to. By default, posts are saved to 'Tiktok-Scraper/output'.

2) Add profiles you want to download posts for in [profiles.csv](profiles.csv). User posts are stored in '`OUTPUT_DIRECTORY`/`Directory`'.

3) Run the program. In the command line, you can do:
```bash
python main.py
```

# Issues
Likely, regardless of how long you wait between profiles and downloads, you are going to get rate limited by TikTok. They will just give you a 403 forbidden when visiting a user's page. You can use a VPN to bypass this.

If you are reporting an issue with the driver itself (for example, Tiktok likes to change the class names in their DOM often), please report it in the [tiktok_driver repo](https://github.com/lockermanwxlf/Tiktok-Driver) instead.
