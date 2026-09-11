#!/usr/bin/env python3

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()

    page1.goto('https://www.ioba.org/members-directory')
    time.sleep(10)

    browser.close()
