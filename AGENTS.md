# AGENTS.md

## Overview
Collection of small web-crawling projects (Scrapy + Selenium) for learning and data analysis.

## Layout
- `imdbx/` — Scrapy project crawling IMDb best movies (`imdb/spiders/best_movies.py`, SQLite pipeline).
- `livecoinx/` — Scrapy + Selenium spiders for livecoin (`coin.py`, `coin_selenium.py`).
- `tinydealx/` — Scrapy project for TinyDeal special offers.
- `worldometers/` — Scrapy spider for population data (`countries.py`, `runner.py`).
- `CrawlFacebook/` — Selenium script + notebook for Facebook pages (bundled Windows chromedriver).

## Commands
- Run a spider: `cd <project> && scrapy crawl <spider_name> -o out.json`
- Spider names: `best_movies`, `coin`, `special_offers`, `countries`.

## Rules
- Never commit cookies, session files, passwords or tokens (`*cookies*.txt` and `.env` are gitignored).
- Respect each site's terms of service and robots.txt; crawl politely.
- Do not commit `__pycache__/` or generated databases.
- `CrawlFacebook/CrawlDataFacebook.py` has hard-coded local MySQL settings; use environment variables for any change.
