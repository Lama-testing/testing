import sys
from time import sleep
import pytest
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime

def generate_email(base="test", domain="gmail.com"):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base}+{timestamp}@{domain}"

@pytest.fixture
def driver():

    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')

    driver = uc.Chrome(options=options)
    driver.get('https://www.skyscanner.co.il')
    sleep(3)
    yield driver
    driver.quit()


def test_flight(driver):
    sleep(3)
    city1 = driver.find_element(By.XPATH,"//input[@id = 'originInput-input']")
    city1.clear()
    city1.send_keys('Ben Gurion Intl (TLV)')
    sleep(2)

    first_option = driver.find_element(By.XPATH, "//span[text()='Ben Gurion Intl (TLV)']")
    first_option.click()
    sleep(1)

    city2 = driver.find_element(By.XPATH,"//input[@id = 'destinationInput-input']")
    city2.clear()
    city2.send_keys('Berlin Brandenburg (BER)')
    sleep(2)

    first_opt = driver.find_element(By.XPATH, "//span[text()='Berlin Brandenburg (BER)']")
    first_opt.click()
    sleep(1)

    date1 = driver.find_element(By.XPATH, "//span[text() ='Depart']")
    date1.click()
    sleep(2)

    s_date = driver.find_elements(By.XPATH, "//button[@class ='CustomCalendar_day__MzVhY']")
    s_date[1].click()
    sleep(1)

    date2 = driver.find_element(By.XPATH,"//span[text() = 'Add date']")
    date2.click()
    sleep(2)
    t_date = driver.find_elements(By.XPATH,"//button[@class = 'CustomCalendar_day__MzVhY']")
    t_date[20].click()
    sleep(2)
    btn_date_apply = driver.find_element(By.XPATH,"//button[text() = 'Apply']")
    btn_date_apply.click()
    sleep(2)
    travellers = driver.find_element(By.XPATH,"//span[text() = 'Travelers and cabin class']")
    travellers.click()
    sleep(2)
    adult = driver.find_element(By.XPATH,"//input[@id = 'adult-nudger']")
    adult.clear()
    adult.send_keys('2')
    sleep(2)
    plus_child = driver.find_element(By.XPATH,"//button[@title = 'More Children']")
    plus_child.click()
    sleep(1)
    age1 = driver.find_element(By.XPATH,"//select[@id = 'children-age-dropdown-0']")
    select = Select(age1)
    #     #  Option 2: Select by value
    select.select_by_value("12")
    sleep(2)
    btn_apply  = driver.find_element(By.XPATH,"//button[text() = 'Apply']")
    btn_apply.click()
    sleep(2)
    search = driver.find_element(By.XPATH,"//button[@data-testid = 'desktop-cta']")
    search.click()
    sleep(10)

    flight_deals = driver.find_elements(By.XPATH,"//div[@class = 'FlightsResults_dayViewItems__NzJiY']")
    sleep(2)
    assert len(flight_deals) > 0, "No flight deals found — search might have failed or no flights are available."
    sleep(3)