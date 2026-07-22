from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    # пользователь 1
    driver.add_cookie({
        "name": "SESSION",
        "value": "Y2ZkYzgzODgtMTQ4Mi00Y2QyLWE3MWUtZjU4OWY4NGY1YTc1",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/a89163594160")
    wait.until(EC.url_contains("a89163594160"))
    url_user1 = driver.current_url

    driver.delete_all_cookies()
    driver.refresh()
    # пользователь 2
    driver.add_cookie({
        "name": "SESSION",
        "value": "MjBhZjdlZTktNjRlMi00NmIyLTlhY2ItNzliZjI5YzU1YzE2",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/alias")
    wait.until(EC.url_contains("alias"))

    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()
