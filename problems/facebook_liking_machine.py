from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--disable-notifications")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.facebook.com")

try:
    # wait for the "Allow All Cookies" button and click it if it appears
    allow_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]"))
    )

    # scroll to the button (optional) and click it
    driver.execute_script("arguments[0].scrollIntoView();", allow_cookies_button)
    allow_cookies_button.click()
    print("Clicked on 'Allow All Cookies' button.")

except Exception as e:
    print("No 'Allow All Cookies' button found or an error occurred:", e)

# login
try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    password_input = driver.find_element(By.NAME, "pass")

    email_input.send_keys("radu01binhn@yahoo.com")  # Replace with your email
    password_input.send_keys("Sp3ciala7")          # Replace with your password

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    print("Logged in successfully.")

except Exception as e:
    print("Error during login:", e)

# Handle the alert
try:
    alert = driver.switch_to.alert
    alert.dismiss()  # Close the alert
    print("Alert dismissed.")
except Exception as e:
    print(f"No alert found or error occurred: {e}")

# handle notification with xpath
try:
    # Wait for the "accept notification pop up" button and click it if it appears
    notification_popup = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]"))
    )

    # Scroll to the button and click it
    driver.execute_script("arguments[0].scrollIntoView();", notification_popup)
    notification_popup.click()
    print("Clicked on 'Allow All notifications' button.")
except Exception as e:
    print("did not click on 'Allow All notifications' button:", e)

# go to search
try:
    search_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/label/input"))
    )
    time.sleep(2)
    # scroll to the button and click it
    driver.execute_script("arguments[0].scrollIntoView();", search_button)
    search_button.click()
    print("Clicked on 'search' button.")
    search_button.send_keys("iulian-vasile")
    search_button.click()
    # press enter for displaying search results
    # search_button.send_keys(Keys.RETURN)
    driver.implicitly_wait(2)
    print("wrote desired text successfully.")
except Exception as e:
    print("Error during searching:", e)

#select first result
try:
    result_selection = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/ul/li[1]/a/div[1]/div[2]/div/div[1]/span/span/span[2]"))
    )

    result_selection.click()
    print("Clicked on first result")
except Exception as e:
    print("did not click on first result:", e)

# #select pictures
# try:
#     pictures_selection = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[4]/div[1]/span"))
#
#     )
#     time.sleep(2)
#     # profile_picture = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[1]/div/a/div/svg/g/image")
#     pictures_selection.click()
#     print("Clicked on profile picture")
# except Exception as e:
#     print("did not click on profile picture:", e)

#select profile picture
try:
    # driver.execute_script("window.scrollBy(0, 1000);")
    # profile_picture_selection = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[1]/div/div[2]/div[2]/span/div/span/span"))
    #
    # )
    # driver.execute_script("arguments[0].scrollIntoView();", profile_picture_selection)
    time.sleep(5)
    driver.find_element(By.xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[3]/div/div[1]/div/div[2]/a/div/img")).click();

    profile_picture_css = '#\:r1kt\: > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6 > div > div.x1qjc9v5.x1q0q8m5.x1qhh985.xu3j5b3.xcfux6l.x26u7qi.xm0m39n.x13fuv20.x972fbf.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xs83m0k.x1qughib.xat24cr.x11i5rnm.x1mh8g0r.xdj266r.x2lwn1j.xeuugli.x84yb8i.x1v2h3a6.xr9oo41.x1p5oq8j.x1n2onr6.x1ja2u2z > a > div > img'
    profile_picture = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, profile_picture_css))
    )
    profile_picture.click()
    time.sleep(2)
    # profile_picture = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[1]/div/a/div/svg/g/image")
    # profile_picture_selection.click()
    print("Clicked on profile picture")
except Exception as e:
    print("did not click on profile picture:", e)

#click on like on profile picture
try:
    profile_picture_like = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[1]/div[1]"))
    )

    profile_picture_like.click()
    print("Clicked on profile picture")
except Exception as e:
    print("did not like profile picture:", e)
time.sleep(5)  # Wait for 5 seconds (optional)

# Close the browser
#driver.quit()
