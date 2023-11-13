from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_console_language_panel_success():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/login')
    wait = WebDriverWait(driver, 10)
    try:
        # Login
        email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        email.send_keys('test@test.com')
        password.send_keys('tester')
        login_button.click()

        # Wait for the next page to load after login
        WebDriverWait(driver, 10).until(EC.url_to_be('http://localhost:3000/'))
        assert driver.current_url == 'http://localhost:3000/', "Login failed"

        # Find and click the 'Two Sum' element
        two_sum_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='title-div' and text()='Two Sum']")))
        two_sum_element.click()

        # Wait for redirection to /problem
        WebDriverWait(driver, 10).until(EC.url_to_be('http://localhost:3000/problem'))
        assert driver.current_url == 'http://localhost:3000/problem', "Navigation to /problem failed"

        # Find and select language
        select_language_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Select Language']")))
        select_language_element.click()

        # Select Python3
        python3_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-']/div[3]/ul/li[13]")))
        python3_element.click()

        language_element = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div/div")))
        assert language_element.text == 'Python3', "Language doesn't match 'Python3'"

    finally:
        driver.quit()

def test_console_theme_panel_success():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/login')
    wait = WebDriverWait(driver, 10)
    try:
        # Login
        email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        email.send_keys('test@test.com')
        password.send_keys('tester')
        login_button.click()

        # Wait for the next page to load after login
        WebDriverWait(driver, 10).until(EC.url_to_be('http://localhost:3000/'))
        assert driver.current_url == 'http://localhost:3000/', "Login failed"

        # Find and click the 'Two Sum' element
        two_sum_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='title-div' and text()='Two Sum']")))
        two_sum_element.click()

        # Wait for redirection to /problem
        WebDriverWait(driver, 10).until(EC.url_to_be('http://localhost:3000/problem'))
        assert driver.current_url == 'http://localhost:3000/problem', "Navigation to /problem failed"

        # Find and select language
        select_theme_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Select Theme']")))
        select_theme_element.click()

        # Select Twilight
        twilight_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-']/div[3]/ul/li[42]")))
        twilight_element.click()

        theme_element = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div")))
        assert theme_element.text == 'Twilight', "Theme doesn't match 'Twilight'"

    finally:
        driver.quit()

def test_console_run_button_success():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/login')
    wait = WebDriverWait(driver, 10)
    try:
        # Login
        email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        email.send_keys('test@test.com')
        password.send_keys('tester')
        login_button.click()

        # Wait for the next page to load after login
        WebDriverWait(driver, 10).until(EC.url_to_be('http://localhost:3000/'))
        assert driver.current_url == 'http://localhost:3000/', "Login failed"

        # Find and click the 'Two Sum' element
        two_sum_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='title-div' and text()='Two Sum']")))
        two_sum_element.click()

        # Wait for redirection to /problem
        WebDriverWait(driver, 10).until(EC.url_to_be('http://localhost:3000/problem'))
        assert driver.current_url == 'http://localhost:3000/problem', "Navigation to /problem failed"

        # Add delay
        import time
        time.sleep(5)

        # Find and select Run Button
        run_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Run']")))
        #run_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[5]/button[2]")))
        run_button_element.click()

        snackbar = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='MuiAlert-message css-1pxa9xg-MuiAlert-message']")))
        assert snackbar.text == 'Code Submitted', "Running of code failed"
    
    finally:
        driver.quit()
        
def test_console_submit_button_success():
    pass
