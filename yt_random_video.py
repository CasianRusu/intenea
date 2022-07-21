import numpy as np
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def youtube_video():
    # Prepare logger
    logging.basicConfig(filename="YtLog.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # Define the options of your webdriver here
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Define webdriver here
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    # Select page to open here
    try:
        driver.get("https://www.youtube.com")
        driver.maximize_window()
        logger.info('Opened YouTube in Chrome and maximized the window\n')
        driver.implicitly_wait(2)
    except:
        logger.error("error\n")

    # WEB PAGE CONTENT HERE
    # Automatically accept Terms of Service for YouTube
    try:
        button = driver.find_element(
            By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/a/tp-yt-paper-button")
        button.click()
        logger.info('Accepted Terms of Service\n')
        driver.implicitly_wait(2)
    except:
        logger.error(
            "Terms of Service didn't appear/ Page loaded too quickly/ other error\n")

    # Automatically select a random video from the first row
    # Refresh page to avoid certain errors
    driver.refresh()
    try:
        video_to_select = np.random.randint(1, 4)
        video = driver.find_element(
            By.XPATH, f"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[{video_to_select}]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a")
        video.click()
        logger.info('Selected a random video\n')
        driver.implicitly_wait(2)
    except:
        logger.error("Page loaded too quickly/ other error\n")

    # Automatically skip adds before recording
    # The program checks up to 4 ads with the variable check_ads
    # First it verifies if it is an unskippable ad then it checks if it is a skippable ad
    check_ads = 0
    while check_ads < 4:
        try:
            check_skip_button = driver.find_element(
                By.ID, 'ad-image:4').value_of_css_property("display")

            while check_skip_button != "none":
                check_skip_button = driver.find_element(
                    By.ID, 'ad-image:4').value_of_css_property("display")

        except:
            logger.warning("no unskippable adds\n")

        try:
            skip_button = driver.find_element(
                By.XPATH, "//button[contains(@class, 'ytp-ad-skip-button ytp-button')]")
            skip_button.click()
            logger.info('Skipped an ad\n')
        except:
            logger.warning("no skippable adds\n")

        check_ads += 1

    # Refresh the page in order for the VideoRecorder script to catch-up with the webpage
    driver.refresh()
    driver.implicitly_wait(1)
    # Automatically put video in fullscreen
    try:
        video_fullscreen_button = driver.find_element(
            By.XPATH, "//button[contains(@class, 'ytp-fullscreen-button ytp-button')]")
        video_fullscreen_button.click()
        logger.info('Video now in fullscreen\n')
        driver.implicitly_wait(3)
    except:
        logger.error("Page loaded too quickly/ other error\n")
