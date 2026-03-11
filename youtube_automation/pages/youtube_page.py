from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YouTubePage:

    def __init__(self, driver):
        self.driver = driver

    search_box = (By.NAME, "search_query")
    first_video = (By.XPATH, "(//a[@id='video-title'])[1]")
    player = (By.CLASS_NAME, "video-stream")

    def open_youtube(self):
        self.driver.get("https://www.youtube.com/")

    def search_song(self, song):
        search = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located(self.search_box)
        )
        search.send_keys(song)
        search.submit()

    def click_first_video(self):
        video = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable(self.first_video)
        )
        video.click()

    def verify_video_playing(self):
        player = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located(self.player)
        )
        return player.is_displayed()