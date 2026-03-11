from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_youtube_song_search(driver):

    driver.get("https://www.youtube.com/")

    # Search box
    search = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.NAME,"search_query"))
    )

    search.send_keys("Banjara Song")
    search.submit()

    # Click first video
    video = WebDriverWait(driver,15).until(
        EC.element_to_be_clickable((By.XPATH,"(//a[@id='video-title'])[1]"))
    )

    video.click()

    # Verify video player loads
    player = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.CLASS_NAME,"video-stream"))
    )

    assert player.is_displayed()