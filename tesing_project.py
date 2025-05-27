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
    # Setup undetected Chrome driver
    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')

    # You can add more options as needed
    # options.add_argument('--headless')  # Optional, for headless mode

    driver = uc.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://www.skyscanner.co.il')
    sleep(3)
    yield driver
    driver.quit()


def test_flight(driver):
    sleep(20)
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
    # //////////////////////////////////////////////////////////////////////////////
# Hotel Search with valid details
def test_1(driver):
    sleep(15)
    Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
    Hotel_tab.click()
    # sleep(30)
    destination = driver.find_element(By.ID, 'destination-autosuggest')
    destination.send_keys('Paris')
    sleep(3)
    Check_in = driver.find_element(By.XPATH, "//input[@id='checkin']")
    Check_in.click()
    sleep(3)
    checkin = driver.find_element(By.XPATH, "//span[text() = '20']")
    checkin.click()
    sleep(3)
    Check_out = driver.find_element(By.XPATH, "//input[@id ='checkout']")
    Check_out.click()
    sleep(3)
    checkout = driver.find_element(By.XPATH, "//span[text() = '26']")
    checkout.click()
    sleep(3)
    Room_Adult = driver.find_element(By.XPATH, "//input[@id='guests-rooms']")
    Room_Adult.click()
    sleep(3)
    Adults = driver.find_element(By.XPATH, "//input[@id='adults']")
    Adults.clear()
    Adults.send_keys('4')
    sleep(3)
    Rooms = driver.find_element(By.XPATH, "//input[@id='rooms']")
    Rooms.clear()
    Rooms.send_keys('2')
    sleep(3)
    BTN_Done = driver.find_element(By.XPATH, "//span[text()='Done']")
    BTN_Done.click()
    sleep(2)
    btn_search = driver.find_element(By.CLASS_NAME,
                                     'BpkButton_bpk-button__ZGRmN.BpkButton_bpk-button--large__ZmE2M.bpk-button--submit.ExpandableLayout_ExpandableLayout__cta__OWY1Z')
    btn_search.click()
    sleep(10)
    results = driver.find_elements(By.XPATH,
                                   "//div[@class='HotelCardsListChunk_HotelCardsListChunk__card__O2gi3 HotelCardsListChunk_HotelCardsListChunk__card--newLayout__DTkR9 HotelCardsListChunk_Animation__zkf0j']")
    assert len(results) > 0, "No hotel results were found."