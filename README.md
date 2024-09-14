# Tiktok-Scraper
Nodriver-based scraper for TikTok

There is a memory leak in this. From my experience it seems running any automated browser in a loop (like selenium) leads to a memory leak, so 
try not to let the program run for more than an hour or you'll have an 8gb task. You can restart it immediately after cancellation 
if you want to.

TikTok has recently upgraded their API and they no longer seem to rate limit (or are more lenient with it). This is probably going to change in the future.

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
For now `RecoveryId` is useless.

4) Run the program. In the command line, you can do:
```bash
python main.py
```

# Issues
If you are reporting an issue with the driver itself (for example, Tiktok likes to change the class names in their DOM often), please report it in the [tiktok_driver repo](https://github.com/lockermanwxlf/Tiktok-Driver) instead.
