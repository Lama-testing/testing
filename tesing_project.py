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


# def test_flight(driver):
#     sleep(2)
#     city1 = driver.find_element(By.XPATH,"//input[@id = 'originInput-input']")
#     city1.clear()
#     city1.send_keys('Ben Gurion Intl (TLV)')
#     sleep(2)
#
#     first_option = driver.find_element(By.XPATH, "//span[text()='Ben Gurion Intl (TLV)']")
#     first_option.click()
#     sleep(1)
#
#     city2 = driver.find_element(By.XPATH,"//input[@id = 'destinationInput-input']")
#     city2.clear()
#     city2.send_keys('Berlin Brandenburg (BER)')
#     sleep(2)
#
#     first_opt = driver.find_element(By.XPATH, "//span[text()='Berlin Brandenburg (BER)']")
#     first_opt.click()
#     sleep(1)
#
#     date1 = driver.find_element(By.XPATH, "//span[text() ='Depart']")
#     date1.click()
#     sleep(2)
#
#     s_date = driver.find_elements(By.XPATH, "//button[@class ='CustomCalendar_day__MzVhY']")
#     s_date[1].click()
#     sleep(1)
#
#     date2 = driver.find_element(By.XPATH,"//span[text() = 'Add date']")
#     date2.click()
#     sleep(2)
#     t_date = driver.find_elements(By.XPATH,"//button[@class = 'CustomCalendar_day__MzVhY']")
#     t_date[20].click()
#     sleep(2)
#     btn_date_apply = driver.find_element(By.XPATH,"//button[text() = 'Apply']")
#     btn_date_apply.click()
#     sleep(2)
#     travellers = driver.find_element(By.XPATH,"//span[text() = 'Travelers and cabin class']")
#     travellers.click()
#     sleep(2)
#     adult = driver.find_element(By.XPATH,"//input[@id = 'adult-nudger']")
#     adult.clear()
#     adult.send_keys('2')
#     sleep(2)
#     plus_child = driver.find_element(By.XPATH,"//button[@title = 'More Children']")
#     plus_child.click()
#     sleep(1)
#     age1 = driver.find_element(By.XPATH,"//select[@id = 'children-age-dropdown-0']")
#     select = Select(age1)
#     #     #  Option 2: Select by value
#     select.select_by_value("12")
#     sleep(2)
#     btn_apply  = driver.find_element(By.XPATH,"//button[text() = 'Apply']")
#     btn_apply.click()
#     sleep(2)
#     search = driver.find_element(By.XPATH,"//button[@data-testid = 'desktop-cta']")
#     search.click()
#     sleep(10)
#
#     flight_deals = driver.find_elements(By.XPATH,"//div[@class = 'FlightsResults_dayViewItems__NzJiY']")
#     sleep(2)
#     assert len(flight_deals) > 0, "No flight deals found — search might have failed or no flights are available."
#     sleep(3)

#======================================================
# def test_flight_no_city2 (driver):
#     sleep(5)
#     city1 = driver.find_element(By.XPATH, "//input[@id = 'originInput-input']")
#     city1.clear()
#     city1.send_keys('Ben Gurion Intl (TLV)')
#     sleep(2)
#
#     first_option = driver.find_element(By.XPATH, "//span[text()='Ben Gurion Intl (TLV)']")
#     first_option.click()
#     sleep(1)
#
#     city2 = driver.find_element(By.XPATH, "//input[@id = 'destinationInput-input']")
#     city2.clear()
#     #city2.send_keys('Berlin Brandenburg (BER)')
#     sleep(2)
#
#     # first_opt = driver.find_element(By.XPATH, "//span[text()='Berlin Brandenburg (BER)']")
#     # first_opt.click()
#     # sleep(1)
#
#     date1 = driver.find_element(By.XPATH, "//span[text() ='Depart']")
#     date1.click()
#     sleep(2)
#
#     s_date = driver.find_elements(By.XPATH, "//button[@class ='CustomCalendar_day__MzVhY']")
#     s_date[1].click()
#     sleep(1)
#
#     date2 = driver.find_element(By.XPATH, "//span[text() = 'Add date']")
#     date2.click()
#     sleep(2)
#     t_date = driver.find_elements(By.XPATH, "//button[@class = 'CustomCalendar_day__MzVhY']")
#     t_date[20].click()
#     sleep(2)
#     btn_date_apply = driver.find_element(By.XPATH, "//button[text() = 'Apply']")
#     btn_date_apply.click()
#     sleep(2)
#     travellers = driver.find_element(By.XPATH, "//span[text() = 'Travelers and cabin class']")
#     travellers.click()
#     sleep(2)
#     adult = driver.find_element(By.XPATH, "//input[@id = 'adult-nudger']")
#     adult.clear()
#     adult.send_keys('2')
#     sleep(2)
#     plus_child = driver.find_element(By.XPATH, "//button[@title = 'More Children']")
#     plus_child.click()
#     sleep(1)
#     age1 = driver.find_element(By.XPATH, "//select[@id = 'children-age-dropdown-0']")
#     select = Select(age1)
#     #     #  Option 2: Select by value
#     select.select_by_value("12")
#     sleep(2)
#     btn_apply = driver.find_element(By.XPATH, "//button[text() = 'Apply']")
#     btn_apply.click()
#     sleep(2)
#     search = driver.find_element(By.XPATH, "//button[@data-testid = 'desktop-cta']")
#     search.click()
#     sleep(10)
#
# <<<<<<< HEAD
#     assert city2.text == '', "Search  have failed ."
#     sleep(3)
# =======
#     flight_deals = driver.find_elements(By.XPATH,"//div[@class = 'FlightsResults_dayViewItems__NzJiY']")
#     sleep(2)
#     assert len(flight_deals) > 0, "No flight deals found — search might have failed or no flights are available."
#     sleep(3)
#     # //////////////////////////////////////////////////////////////////////////////
# # Hotel Search with valid details
# def test_1(driver):
#     sleep(15)
#     Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
#     Hotel_tab.click()
#     # sleep(30)
#     destination = driver.find_element(By.ID, 'destination-autosuggest')
#     destination.send_keys('Paris')
#     sleep(3)
#     Check_in = driver.find_element(By.XPATH, "//input[@id='checkin']")
#     Check_in.click()
#     sleep(3)
#     checkin = driver.find_element(By.XPATH, "//span[text() = '20']")
#     checkin.click()
#     sleep(3)
#     Check_out = driver.find_element(By.XPATH, "//input[@id ='checkout']")
#     Check_out.click()
#     sleep(3)
#     checkout = driver.find_element(By.XPATH, "//span[text() = '26']")
#     checkout.click()
#     sleep(3)
#     Room_Adult = driver.find_element(By.XPATH, "//input[@id='guests-rooms']")
#     Room_Adult.click()
#     sleep(3)
#     Adults = driver.find_element(By.XPATH, "//input[@id='adults']")
#     Adults.clear()
#     Adults.send_keys('4')
#     sleep(3)
#     Rooms = driver.find_element(By.XPATH, "//input[@id='rooms']")
#     Rooms.clear()
#     Rooms.send_keys('2')
#     sleep(3)
#     BTN_Done = driver.find_element(By.XPATH, "//span[text()='Done']")
#     BTN_Done.click()
#     sleep(2)
#     btn_search = driver.find_element(By.CLASS_NAME,
#                                      'BpkButton_bpk-button__ZGRmN.BpkButton_bpk-button--large__ZmE2M.bpk-button--submit.ExpandableLayout_ExpandableLayout__cta__OWY1Z')
#     btn_search.click()
#     sleep(10)
#     results = driver.find_elements(By.XPATH,
#                                    "//div[@class='HotelCardsListChunk_HotelCardsListChunk__card__O2gi3 HotelCardsListChunk_HotelCardsListChunk__card--newLayout__DTkR9 HotelCardsListChunk_Animation__zkf0j']")
#     assert len(results) > 0, "No hotel results were found."
# >>>>>>> d90b8b7359e3782660b02aa306c8945da43aeeff
#===================================================================
# def test_sorting_flights(driver):
#
#     sleep(3)
#     city1 = driver.find_element(By.XPATH, "//input[@id = 'originInput-input']")
#     city1.clear()
#     city1.send_keys('Ben Gurion Intl (TLV)')
#     sleep(2)
#
#     first_option = driver.find_element(By.XPATH, "//span[text()='Ben Gurion Intl (TLV)']")
#     first_option.click()
#     sleep(1)
#
#     city2 = driver.find_element(By.XPATH, "//input[@id = 'destinationInput-input']")
#     city2.clear()
#     city2.send_keys('Berlin Brandenburg (BER)')
#     sleep(2)
#
#     first_opt = driver.find_element(By.XPATH, "//span[text()='Berlin Brandenburg (BER)']")
#     first_opt.click()
#     sleep(1)
#
#     date1 = driver.find_element(By.XPATH, "//span[text() ='Depart']")
#     date1.click()
#     sleep(2)
#
#     s_date = driver.find_elements(By.XPATH, "//button[@class ='CustomCalendar_day__MzVhY']")
#     s_date[1].click()
#     sleep(1)
#
#     date2 = driver.find_element(By.XPATH, "//span[text() = 'Add date']")
#     date2.click()
#     sleep(2)
#     t_date = driver.find_elements(By.XPATH, "//button[@class = 'CustomCalendar_day__MzVhY']")
#     t_date[20].click()
#     sleep(2)
#     btn_date_apply = driver.find_element(By.XPATH, "//button[text() = 'Apply']")
#     btn_date_apply.click()
#     sleep(2)
#     travellers = driver.find_element(By.XPATH, "//span[text() = 'Travelers and cabin class']")
#     travellers.click()
#     sleep(2)
#     adult = driver.find_element(By.XPATH, "//input[@id = 'adult-nudger']")
#     adult.clear()
#     adult.send_keys('2')
#     sleep(2)
#     plus_child = driver.find_element(By.XPATH, "//button[@title = 'More Children']")
#     plus_child.click()
#     sleep(1)
#     age1 = driver.find_element(By.XPATH, "//select[@id = 'children-age-dropdown-0']")
#     select = Select(age1)
#     #     #  Option 2: Select by value
#     select.select_by_value("12")
#     sleep(2)
#     btn_apply = driver.find_element(By.XPATH, "//button[text() = 'Apply']")
#     btn_apply.click()
#     sleep(2)
#     search = driver.find_element(By.XPATH, "//button[@data-testid = 'desktop-cta']")
#     search.click()
#     sleep(10)
#
#     sort1 = driver.find_element(By.XPATH, "//select[@id = 'secondarySort']")
#     select = Select(sort1)
#     select.select_by_value("CHEAPEST")
#     sleep(2)
#
#     prices = driver.find_elements(By.XPATH, "//span[@class = 'BpkText_bpk-text__MjhhY BpkText_bpk-text--lg__MjFkN']")
#
#     print(len(prices))
#
#     max_num = 0
#     min_num = 0
#
#     for i in range(len(prices)):
#
#         if i < len(prices) -1:
#             assert int((prices[i].text)[1:]), 'test sorting failed'
#
#     print('Test Pass')
#
#     sleep(2)
#=================================================
# def test_saved_flights(driver):
#     sleep(15)
#
#     login = driver.find_element(By.XPATH,"//span[text() ='Log in']")
#     login.click()
#     sleep(2)
#
#     cont_w_email = driver.find_element(By.XPATH,"//button[@class = 'BpkButton_bpk-button__OTE4Z BpkButton_bpk-button--large__NTAyN BpkButton_bpk-button--secondary__ZmJjM EmailLoginButton_email-login-button__Nzc5Y']")
#     cont_w_email.click()
#     sleep(2)
#
#     email_input = driver.find_element(By.XPATH,"//input[@id = 'email']")
#     email = generate_email()
#     email_input.send_keys(email)
#     sleep(4)
#
#     btn_next = driver.find_element(By.XPATH,"//button[@aria-label = 'verify button']")
#     btn_next.click()
#     sleep(7)
#
#     btn_later = driver.find_element(By.XPATH,"//button[text() = 'Maybe later']")
#     btn_later.click()
#     sleep(3)
#
#
#     city1 = driver.find_element(By.XPATH,"//input[@id = 'originInput-input']")
#     city1.clear()
#     city1.send_keys('Ben Gurion Intl (TLV)')
#     sleep(2)
#
#     first_option = driver.find_element(By.XPATH, "//span[text()='Ben Gurion Intl (TLV)']")
#     first_option.click()
#     sleep(1)
#
#     city2 = driver.find_element(By.XPATH,"//input[@id = 'destinationInput-input']")
#     city2.clear()
#     city2.send_keys('Berlin Brandenburg (BER)')
#     sleep(2)
#
#     first_opt = driver.find_element(By.XPATH, "//span[text()='Berlin Brandenburg (BER)']")
#     first_opt.click()
#     sleep(1)
#
#     date1 = driver.find_element(By.XPATH, "//span[text() ='Depart']")
#     date1.click()
#     sleep(2)
#
#     s_date = driver.find_elements(By.XPATH, "//button[@class ='CustomCalendar_day__MzVhY']")
#     s_date[1].click()
#     sleep(1)
#
#     date2 = driver.find_element(By.XPATH,"//span[text() = 'Add date']")
#     date2.click()
#     sleep(2)
#
#     t_date = driver.find_elements(By.XPATH,"//button[@class = 'CustomCalendar_day__MzVhY']")
#     t_date[20].click()
#     sleep(2)
#     btn_date_apply = driver.find_element(By.XPATH,"//button[text() = 'Apply']")
#     btn_date_apply.click()
#     sleep(2)
#
#     travellers = driver.find_element(By.XPATH,"//span[text() = 'Travelers and cabin class']")
#     travellers.click()
#     sleep(2)
#
#     adult = driver.find_element(By.XPATH,"//input[@id = 'adult-nudger']")
#     adult.clear()
#     adult.send_keys('2')
#     sleep(2)
#
#     plus_child = driver.find_element(By.XPATH,"//button[@title = 'More Children']")
#     plus_child.click()
#     sleep(1)
#
#     age1 = driver.find_element(By.XPATH,"//select[@id = 'children-age-dropdown-0']")
#     select = Select(age1)
#         #     #  Option 2: Select by value
#     select.select_by_value("12")
#     sleep(2)
#
#     btn_apply  = driver.find_element(By.XPATH,"//button[text() = 'Apply']")
#     btn_apply.click()
#     sleep(2)
#
#     search = driver.find_element(By.XPATH,"//button[@data-testid = 'desktop-cta']")
#     search.click()
#     sleep(5)
#
#     btn_save = driver.find_element(By.XPATH,"//button[@aria-label = 'Save flight, option 1 from Ben Gurion Intl to Berlin Brandenburg']")
#     btn_save.click()
#     sleep(5)
#
#     btn_manage = driver.find_element(By.XPATH,"//p[text() = 'Manage alert']")
#     sleep(2)
#     btn_manage.click()
#     sleep(2)
#
#     saved_flight = driver.find_element(By.XPATH,"//span[@class = 'BpkText_bpk-text__ZjI3M BpkText_bpk-text--heading-4__MDlkY']")
#
#     sleep(2)
#     assert saved_flight.text == 'Tel Aviv to Berlin', "Flight not saved!"
#     sleep(2)
#=========================================================================
# def test_same_deptodes(driver):
#     sleep(25)
#
#     city1 = driver.find_element(By.XPATH,"//input[@id = 'originInput-input']")
#     city1.clear()
#     city1.send_keys('Ben Gurion Intl (TLV)')
#     sleep(2)
#
#     first_option = driver.find_element(By.XPATH, "//span[text()='Ben Gurion Intl (TLV)']")
#     first_option.click()
#     sleep(1)
#
#     city2 = driver.find_element(By.XPATH, "//input[@id = 'destinationInput-input']")
#     city2.clear()
#     city2.send_keys('Ben Gurion Intl (TLV)')
#     sleep(2)
#
#     first_option = driver.find_element(By.XPATH, "//span[text()='Ben Gurion Intl (TLV)']")
#     first_option.click()
#     sleep(1)
#
#     date1 = driver.find_element(By.XPATH, "//span[text() ='Depart']")
#     date1.click()
#     sleep(2)
#
#     s_date = driver.find_elements(By.XPATH, "//button[@class ='CustomCalendar_day__MzVhY']")
#     s_date[1].click()
#     sleep(1)
#
#     date2 = driver.find_element(By.XPATH,"//span[text() = 'Add date']")
#     date2.click()
#     sleep(2)
#
#     t_date = driver.find_elements(By.XPATH,"//button[@class = 'CustomCalendar_day__MzVhY']")
#     t_date[7].click()
#     sleep(2)
#
#     btn_date_apply = driver.find_element(By.XPATH,"//button[text() = 'Apply']")
#     btn_date_apply.click()
#     sleep(2)
#
#     travellers = driver.find_element(By.XPATH,"//span[text() = 'Travelers and cabin class']")
#     travellers.click()
#     sleep(2)
#
#     adult = driver.find_element(By.XPATH,"//input[@id = 'adult-nudger']")
#     adult.clear()
#     adult.send_keys('2')
#     sleep(2)
#
#     btn_apply  = driver.find_element(By.XPATH,"//button[text() = 'Apply']")
#     btn_apply.click()
#     sleep(2)
#
#     search = driver.find_element(By.XPATH,"//button[@data-testid = 'desktop-cta']")
#     search.click()
#     sleep(2)
#
#     result_places = driver.find_element(By.XPATH,"//h1[@data-testid = 'CombinedResultsPlaces_title']")
#     full_text = result_places.text
#     sleep(2)
#
#     assert full_text.startswith("Explore everywhere"), "Failed, search did not work as intended!"
#     sleep(2)
#=============================================
def test_currency (driver):
    sleep(5)

    btn_regional = driver.find_element(By.XPATH, "//button[@class ='GlobalHeader_buttonDark__ZDU3Z']")
    btn_regional.click()
    sleep(5)

    currency = driver.find_element(By.ID, 'culture-selector-currency')
    select = Select(currency)
    select.select_by_value('ILS')
    sleep(5)

    btn_save = driver.find_element(By.ID, 'culture-selector-save')
    btn_save.click()
    sleep(2)

    city1 = driver.find_element(By.XPATH, "//input[@id = 'originInput-input']")
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
    sleep(5)

    cur_icon = driver.find_element(By.XPATH,"//span[@class = 'BpkText_bpk-text__MjhhY BpkText_bpk-text--heading-4__Y2FlY']")
    icon = cur_icon.text[0]
    sleep(2)

    assert icon == "₪" , "Failed, Currency did not change after selection!"