import sys
from time import sleep
import pytest
import uc
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
    driver.get('https://www.skyscanner.co.il/')
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
# def test_flight_no_city2 (driver):
#     sleep(5)
#     city1 = driver.find_element(By.XPATH, "//input[@id ='originInput-input']")
#     city1.clear()
#     city1.send_keys('Ben Gurion Intl (TLV)')
#     sleep(2)
#     first_option.click()
#     sleep(1)
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
#     assert city2.text == '', "Search  have failed ."
#     sleep(3)

def test_sorting_flights(driver):
    sleep(3)
    city1 = driver.find_element(By.XPATH, "//input[@id = 'originInput-input']")
    city1.clear()
    city1.send_keys('Ben Gurion Intl (TLV)')
    sleep(2)

    first_option = driver.find_element(By.XPATH, "//span[text()='Ben Gurion Intl (TLV)']")
    first_option.click()
    sleep(1)

    city2 = driver.find_element(By.XPATH, "//input[@id = 'destinationInput-input']")
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

    date2 = driver.find_element(By.XPATH, "//span[text() = 'Add date']")
    date2.click()
    sleep(2)
    t_date = driver.find_elements(By.XPATH, "//button[@class = 'CustomCalendar_day__MzVhY']")
    t_date[20].click()
    sleep(2)
    btn_date_apply = driver.find_element(By.XPATH, "//button[text() = 'Apply']")
    btn_date_apply.click()
    sleep(2)
    travellers = driver.find_element(By.XPATH, "//span[text() = 'Travelers and cabin class']")
    travellers.click()
    sleep(2)
    adult = driver.find_element(By.XPATH, "//input[@id = 'adult-nudger']")
    adult.clear()
    adult.send_keys('2')
    sleep(2)
    plus_child = driver.find_element(By.XPATH, "//button[@title = 'More Children']")
    plus_child.click()
    sleep(1)
    age1 = driver.find_element(By.XPATH, "//select[@id = 'children-age-dropdown-0']")
    select = Select(age1)
    #     #  Option 2: Select by value
    select.select_by_value("12")
    sleep(2)
    btn_apply = driver.find_element(By.XPATH, "//button[text() = 'Apply']")
    btn_apply.click()
    sleep(2)
    search = driver.find_element(By.XPATH, "//button[@data-testid = 'desktop-cta']")
    search.click()
    sleep(10)

    sort1 = driver.find_element(By.XPATH, "//select[@id = 'secondarySort']")
    select = Select(sort1)
    select.select_by_value("CHEAPEST")
    sleep(2)

    prices = driver.find_elements(By.XPATH, "//span[@class = 'BpkText_bpk-text__MjhhY BpkText_bpk-text--lg__MjFkN']")

    print(len(prices))

    max_num = 0
    min_num = 0

    for i in range(len(prices)):

        if i < len(prices) -1:
            assert int((prices[i].text)[1:]), 'test sorting failed'
    print('Test Pass')
    sleep(2)
#=================================================Add commentMore actions
def test_saved_flights(driver):
    sleep(15)
    login = driver.find_element(By.XPATH,"//span[text() ='Log in']")
    login.click()
    sleep(2)
    cont_w_email = driver.find_element(By.XPATH,"//button[@class = 'BpkButton_bpk-button__OTE4Z BpkButton_bpk-button--large__NTAyN BpkButton_bpk-button--secondary__ZmJjM EmailLoginButton_email-login-button__Nzc5Y']")
    cont_w_email.click()
    sleep(2)
    email_input = driver.find_element(By.XPATH,"//input[@id = 'email']")
    email = generate_email()
    email_input.send_keys(email)
    sleep(4)
    btn_next = driver.find_element(By.XPATH,"//button[@aria-label = 'verify button']")
    btn_next.click()
    sleep(7)
    btn_later = driver.find_element(By.XPATH,"//button[text() = 'Maybe later']")
    btn_later.click()
    sleep(3)
    city1 = driver.find_element(By.XPATH,"//input[@id = 'originInput-input']")
    city1.clear()
    city1.send_keys('Ben Gurion Intl (TLV)')
    sleep(2)
def test_sorting_flights(driver):
    first_option.click()
    sleep(1)

    city2 = driver.find_element(By.XPATH,"//input[@id = 'destinationInput-input']")
    city2.clear()
    city2.send_keys('Berlin Brandenburg (BER)')
    sleep(2)
def test_sorting_flights(driver):
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




    btn_save = driver.find_element(By.XPATH,"//button[@aria-label = 'Save flight, option 1 from Ben Gurion Intl to Berlin Brandenburg']")
    btn_save.click()
    sleep(5)

    btn_manage = driver.find_element(By.XPATH,"//p[text() = 'Manage alert']")
    sleep(2)
    btn_manage.click()
    sleep(2)

    saved_flight = driver.find_element(By.XPATH,"//span[@class = 'BpkText_bpk-text__ZjI3M BpkText_bpk-text--heading-4__MDlkY']")

    sleep(2)
    assert saved_flight.text == 'Tel Aviv to Berlin', "Flight not saved!"
    sleep(2)
#=========================================================================Add commentMore actions

# Hotel Search with valid details
def test_01(driver):
    sleep(20)
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
    btn_search = driver.find_element(By.CLASS_NAME,'BpkButton_bpk-button__ZGRmN.BpkButton_bpk-button--large__ZmE2M.bpk-button--submit.ExpandableLayout_ExpandableLayout__cta__OWY1Z')
    btn_search.click()
    sleep(10)
    results = driver.find_elements(By.XPATH,"//div[@class='HotelCardsListChunk_HotelCardsListChunk__card__O2gi3 HotelCardsListChunk_HotelCardsListChunk__card--newLayout__DTkR9 HotelCardsListChunk_Animation__zkf0j']")
    assert len(results) > 0, "No hotel results were found."
# //////////////////////////////////////////////////////////////////////////////
# Hotel Search functionality with Invalid destination or hotel name
def test_02(driver):
    sleep(15)
    Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
    Hotel_tab.click()
    destination = driver.find_element(By.ID, 'destination-autosuggest')
    destination.send_keys('invaliddestination')
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
    Room_Adult= driver.find_element(By.XPATH,"//input[@id='guests-rooms']")
    Room_Adult.click()
    sleep(3)
    Adults = driver.find_element(By.XPATH,"//input[@id='adults']")
    Adults.clear()
    Adults.send_keys('4')
    sleep(3)
    Rooms= driver.find_element(By.XPATH,"//input[@id='rooms']")
    Rooms.clear()
    Rooms.send_keys('2')
    sleep(3)
    BTN_Done = driver.find_element(By.XPATH,"//span[text()='Done']")
    BTN_Done.click()
    sleep(2)
    btn_search = driver.find_element(By.CLASS_NAME,'BpkButton_bpk-button__ZGRmN.BpkButton_bpk-button--large__ZmE2M.bpk-button--submit.ExpandableLayout_ExpandableLayout__cta__OWY1Z')
    btn_search.click()
    sleep(5)
    error_message= driver.find_element(By.XPATH,"//span[@class='BpkText_bpk-text__ZjI3M BpkText_bpk-text--body-default__ODg2M SearchControls__destinationErr--message']")
    assert error_message.is_displayed(),'Error message not shown for invalid destination'
# //////////////////////////////////////////////////////////////////////////////
# Hotel Search functionality with Empty destination or hotel name
def test_03(driver):
     sleep(15)
     Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
     Hotel_tab.click()
     # sleep(30)
     destination = driver.find_element(By.ID, 'destination-autosuggest')
     destination.send_keys('')
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
        # Rooms= driver.find_element(By.XPATH,"//input[@id='guests-rooms']")
        # Rooms.click()
        # sleep(3)
     btn_search = driver.find_element(By.CLASS_NAME,
                                         'BpkButton_bpk-button__ZGRmN.BpkButton_bpk-button--large__ZmE2M.bpk-button--submit.ExpandableLayout_ExpandableLayout__cta__OWY1Z')
     btn_search.click()
     sleep(5)
     error_message = driver.find_element(By.XPATH,
                                            "//span[@class='BpkText_bpk-text__ZjI3M BpkText_bpk-text--body-default__ODg2M SearchControls__destinationErr--message']")
     assert error_message.is_displayed(), 'Error message not shown for invalid destination'
     # //////////////////////////////////////////////////////////////////////////////
# Save Hotel to Favourite/Wishlist (user is Logged In)
def test_04(driver):
     # sleep(15)
     sleep(2)
     Login = driver.find_element(By.CLASS_NAME, "LoginButton_loginText__N2E5Y")
     Login.click()
     sleep(1.5)
     Login_email = driver.find_element(By.CLASS_NAME,
                                          "BpkText_bpk-text__MjhhY.BpkText_bpk-text--label-1__OGE0O.EmailLoginButton_email-login-button__text__MTg4O")
     Login_email.click()
     sleep(1.5)
     Email = driver.find_element(By.CLASS_NAME, "BpkInput_bpk-input__MDBkO.BpkInput_bpk-input--large__YTUyN")
     Email.send_keys(generate_email())
     sleep(1.5)
     submit_btn = driver.find_element(By.CLASS_NAME,
                                         'BpkButton_bpk-button__OTE4Z.BpkButton_bpk-button--large__NTAyN.BpkButton_bpk-button--featured__NTk3N.ProgressionButton_progression-button__NjNhM')
     submit_btn.click()
     sleep(3)
     later = driver.find_element(By.XPATH, "//button[text()='Maybe later']")
     later.click()
     sleep(1.5)
     Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
     Hotel_tab.click()
     destination = driver.find_element(By.ID, 'destination-autosuggest')
     destination.send_keys('Paris')
     sleep(1.5)
     Check_in = driver.find_element(By.XPATH, "//input[@id='checkin']")
     Check_in.click()
     sleep(1.5)
     checkin = driver.find_element(By.XPATH, "//span[text() = '26']")
     checkin.click()
     sleep(1.5)
     Check_out = driver.find_element(By.XPATH, "//input[@id ='checkout']")
     Check_out.click()
     sleep(1.5)
     checkout = driver.find_element(By.XPATH, "//span[text() = '30']")
     checkout.click()
     sleep(1.5)
    # Rooms= driver.find_element(By.XPATH,"//input[@id='guests-rooms']")
        # Rooms.click()
        # sleep(3)
     btn_search = driver.find_element(By.CLASS_NAME, 'BpkButton_bpk-button__ZGRmN.BpkButton_bpk-button--large__ZmE2M.bpk-button--submit.ExpandableLayout_ExpandableLayout__cta__OWY1Z')
     btn_search.click()
     sleep(5)
     saved_item = driver.find_element(By.XPATH,"//button[@class='BpkSaveButton_bpk-save-button__vYPc- bpk-save-button__default']")
     saved_item.click()
     sleep(1.5)
     btn_view = driver.find_element(By.XPATH,"//button[@class='BpkButton_bpk-button__J0Ljq BpkButton_bpk-button--link-on-dark__asVWZ']")
     btn_view.click()
     sleep(5)
     Header = driver.find_element(By.XPATH, "//h3[text()='Added today']")
     assert Header.is_displayed(), " Not Saved,Hotel not found in wishlist "
        # //////////////////////////////////////////////////////////////////////////////
    # Save Hotel to Favourite/Wishlist (user is not Logged In)
def test_05(driver):
    sleep(15)
    Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
    Hotel_tab.click()
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
    # Rooms= driver.find_element(By.XPATH,"//input[@id='guests-rooms']")
    # Rooms.click()
    # sleep(3)
    btn_search = driver.find_element(By.CLASS_NAME,'BpkButton_bpk-button__ZGRmN.BpkButton_bpk-button--large__ZmE2M.bpk-button--submit.ExpandableLayout_ExpandableLayout__cta__OWY1Z')
    btn_search.click()
    sleep(5)
    saved_item = driver.find_element(By.XPATH,"//button[@class='BpkSaveButton_bpk-save-button__vYPc- bpk-save-button__default']")
    saved_item.click()
    sleep(3)
    Header = driver.find_element(By.XPATH, "//h2[@class='BpkText_bpk-text__MQ3jy BpkText_bpk-text--heading-2__TOA0c LoginIntro_login-intro__title__J0IOr']")
    assert Header.is_displayed(), "Logged in "
        # //////////////////////////////////////////////////////////////////////////////
# Filter Hotels by Popular Filters
def test_06(driver):
    sleep(15)
    Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
    Hotel_tab.click()
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
    # Room_Adult= driver.find_element(By.XPATH,"//input[@id='guests-rooms']")
    # Room_Adult.click()
    # sleep(3)
    # Adults = driver.find_element(By.XPATH,"//input[@id='adults']")
    # Adults.clear()
    # Adults.send_keys('4')
    # sleep(3)
    # Rooms= driver.find_element(By.XPATH,"//input[@id='rooms']")
    # Rooms.clear()
    # Rooms.send_keys('2')
    # sleep(3)
    # BTN_Done = driver.find_element(By.XPATH,"//span[text()='Done']")
    # BTN_Done.click()
    # sleep(2)
    free_cancellation = driver.find_element(By.XPATH, "//input[@name='CancellationPolicy_freeCancellation']")
    free_cancellation.click()
    sleep(2)
    stars_4 = driver.find_element(By.XPATH, "//input[@name='Filters_Stars_label_stars4']")
    stars_4.click()
    sleep(3)
    stars_3 = driver.find_element(By.XPATH, "//input[@name='Filters_Stars_label_stars3']")
    stars_3.click()
    sleep(3)
    btn_search = driver.find_element(By.XPATH,
                                     "//button[@class='BpkButton_bpk-button__ZGRmN BpkButton_bpk-button--large__ZmE2M bpk-button--submit ExpandableLayout_ExpandableLayout__cta__OWY1Z']")
    btn_search.click()
    sleep(5)
    filter_1 = driver.find_element(By.XPATH,"//button[@class='BpkSelectableChip_bpk-chip__L0AHU BpkSelectableChip_bpk-chip--default__IQOfo BpkSelectableChip_bpk-chip--default-selected__MTTKn BpkSelectableChip_bpk-chip--default-dismissible__bLSP3 BpkSelectableChip_bpk-chip--default-dismissible__bLSP3 SelectedFiltersTags_SelectedFiltersTags__item__pGFee']")
    # filter_2= driver.find_element(By.XPATH,"//button[@class='BpkSelectableChip_bpk-chip__bucgu BpkSelectableChip_bpk-chip--default__JiSai BpkSelectableChip_bpk-chip--default-selected__GCKDV BpkSelectableChip_bpk-chip--default-dismissible__YQ924 BpkSelectableChip_bpk-chip--default-dismissible__YQ924 SelectedFiltersTags_SelectedFiltersTags__item__pGFee']")
    # filter_3= driver.find_element(By.XPATH,"//button[@class='BpkSelectableChip_bpk-chip__bucgu BpkSelectableChip_bpk-chip--default__JiSai BpkSelectableChip_bpk-chip--default-selected__GCKDV BpkSelectableChip_bpk-chip--default-dismissible__YQ924 BpkSelectableChip_bpk-chip--default-dismissible__YQ924 SelectedFiltersTags_SelectedFiltersTags__item__pGFee']")
    assert filter_1.is_displayed(), 'Popular Filter Not selected'
    sleep(2)
    # //////////////////////////////////////////////////////////////////////////////
# Verify “Clear” hotel Filters button Functionality.
def test_07(driver):
    sleep(15)
    Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
    Hotel_tab.click()
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
    btn_search = driver.find_element(By.XPATH,"//button[@class='BpkButton_bpk-button__ZGRmN BpkButton_bpk-button--large__ZmE2M bpk-button--submit ExpandableLayout_ExpandableLayout__cta__OWY1Z']")
    btn_search.click()
    sleep(7)
    btn_filter = driver.find_element(By.XPATH,"//button[@class='BpkButton_bpk-button__J0Ljq BpkButton_bpk-button--large__jPpKI BpkButton_bpk-button--featured__joUSS']")
    btn_filter.click()
    sleep(2)
    free_cancellation = driver.find_element(By.XPATH, "//input[@id='free_cancellation']")
    free_cancellation.click()
    sleep(2)
    Price_Range = driver.find_element(By.XPATH, "//input[@id='PR_BK_0']")
    Price_Range.click()
    sleep(2)
    Review = driver.find_element(By.XPATH, "//input[@id='4']")
    Review.click()
    sleep(2)
    show_result = driver.find_element(By.XPATH,"//button[@class='BpkButton_bpk-button__J0Ljq bpk-button--primary ResultButton_ResultButton__8ZxqF']")
    show_result.click()
    sleep(2)
    btn_filter = driver.find_element(By.XPATH,"//button[@class='BpkButton_bpk-button__J0Ljq BpkButton_bpk-button--large__jPpKI BpkButton_bpk-button--featured__joUSS']")
    btn_filter.click()
    sleep(2)
    btn_clear = driver.find_element(By.XPATH,"//button[@class='BpkButton_bpk-button__J0Ljq BpkButton_bpk-button--link__CXGRg DesktopFilters_Filters__filtersClear__EoPPi']")
    btn_clear.click()
    sleep(3)
    assert not free_cancellation.is_selected(), 'not cleared'
    # //////////////////////////////////////////////////////////////////////////////
# Verify the Date Range Selection
def test_08(driver):
    sleep(30)
    Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
    Hotel_tab.click()
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
    # Room_Adult= driver.find_element(By.XPATH,"//input[@id='guests-rooms']")
    # Room_Adult.click()
    # sleep(3)
    # Adults = driver.find_element(By.XPATH,"//input[@id='adults']")
    # Adults.clear()
    # Adults.send_keys('4')
    # sleep(3)
    # Rooms= driver.find_element(By.XPATH,"//input[@id='rooms']")
    # Rooms.clear()
    # Rooms.send_keys('2')
    # sleep(3)
    # BTN_Done = driver.find_element(By.XPATH,"//span[text()='Done']")
    # BTN_Done.click()
    # sleep(2)
    checkindate = Check_in.get_attribute('value').split('/')[0]
    # print(checkindate)
    checkoutdate = Check_out.get_attribute('value').split('/')[0]
    # print(checkoutdate)
    assert checkindate < checkoutdate, 'invalid date range'

    # Verify hotel details page
# //////////////////////////////////////////////////////////////////////////////
def test_09(driver):
    sleep(15)
    Hotel_tab = driver.find_element(By.XPATH, "//span[text()='Hotels']")
    Hotel_tab.click()
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
    btn_search = driver.find_element(By.XPATH,"//button[@class='BpkButton_bpk-button__ZGRmN BpkButton_bpk-button--large__ZmE2M bpk-button--submit ExpandableLayout_ExpandableLayout__cta__OWY1Z']")
    btn_search.click()
    sleep(7)
    Cards = driver.find_elements(By.XPATH, "//div[@class='CardLayout_CardLayout__primary__4WU9W CardLayout_CardLayout__primary--horizontal__jbbi2']")
    assert len(Cards) > 0, 'hotel details page does not display '

    # //////////////////////////////////////////////////////////////////////////////
    # Changing the currency according to the city/region(bug)
def test_10(driver):
    sleep(30)
    Regional_Setting = driver.find_element(By.XPATH, "//button[@class='GlobalHeader_buttonDark__ZDU3Z']")
    Regional_Setting.click()
    sleep(3)
    Country = driver.find_element(By.XPATH, "//select[@id='culture-selector-market']")
    Country.click()
    Turkey = driver.find_element(By.XPATH, "//option[text()='Türkiye']")
    Turkey.click()
    sleep(3)
    Country.click()
    Currency = driver.find_element(By.XPATH, "//option[text()='TRY - TL']")
    assert Currency.text == 'TRY - TL', 'it does not work right '
    sleep(3)
    Country.click()
    U_S = driver.find_element(By.XPATH,"//option[text()='Israel']")
    U_S.click()
    US_Currency = driver.find_element(By.XPATH,"//select[@class='BpkSelect_bpk-select__YmY5M']").get_attribute('value')
    assert US_Currency == 'ILS - ₪' , 'it does not work right'
    print('it is already a bug !!!')
    sleep(3)
    Country.click()
    sleep(3)
    BTN_Save = driver.find_element(By.XPATH, "//button[@id='culture-selector-save']")
    BTN_Save.click()
    sleep(3)
    #///////////////////////////////////////////////////////////////////////////////////////
    ### First Test: Car rental search with valid dates and locations
def test_1(driver):
# sleep(40)
    Car_tab = driver.find_element(By.XPATH, "//span[text()='Car rental']")
    Car_tab.click()
    sleep(3)
    DestInput = driver.find_element(By.ID, 'carhire-search-controls-location-pick-up')
    DestInput.send_keys('Ben Gurion Intl (TLV)')
    sleep(4)

    PickupDate = driver.find_element(By.XPATH, "//span[text()='Pickup date']")
    PickupDate.click()
    SelectPickupDate = driver.find_elements(By.XPATH,
                                            "//button[@class ='BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectPickupDate[2].click()
    sleep(3)

    PickupTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-pick-up']"))
    PickupTime.select_by_index(2)
    sleep(3)

    DropoffDate = driver.find_element(By.XPATH, "//span[text() = 'Drop-off date']")
    DropoffDate.click()
    sleep(3)
    SelectDropoffDate = driver.find_elements(By.XPATH,
                                             "//button[@class = 'BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectDropoffDate[7].click()
    sleep(3)

    DropoffTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-drop-off']"))
    DropoffTime.select_by_index(7)
    sleep(3)

    SearchButton = driver.find_element(By.ID, 'carhire-search-controls-search-button')
    SearchButton.click()
    sleep(3)
    assert len(driver.find_elements(By.CSS_SELECTOR,
                                    "[data-testid='inventory-card-clickable-button']")) > 0, "No cars were found on the page."

### ------------------------------------------------------------------------------------------------------------###
### ------------------------------------------------------------------------------------------------------------###
## Second Test: Car rental with same pick-up and drop-off date and time
def test_2(driver):
    # sleep(40)
    Car_tab = driver.find_element(By.XPATH, "//span[text()='Car rental']")
    Car_tab.click()
    sleep(3)
    DestInput = driver.find_element(By.ID, 'carhire-search-controls-location-pick-up')
    DestInput.send_keys('Ben Gurion Intl (TLV)')
    sleep(4)

    PickupDate = driver.find_element(By.XPATH, "//span[text()='Pickup date']")
    PickupDate.click()
    SelectPickupDate = driver.find_elements(By.XPATH,
                                            "//button[@class ='BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectPickupDate[3].click()
    sleep(3)

    PickupTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-pick-up']"))
    PickupTime.select_by_index(7)
    sleep(3)

    DropoffDate = driver.find_element(By.XPATH, "//span[text() = 'Drop-off date']")
    DropoffDate.click()
    sleep(3)
    SelectDropoffDate = driver.find_elements(By.XPATH,
                                             "//button[@class = 'BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectDropoffDate[3].click()
    sleep(3)

    DropoffTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-drop-off']"))
    DropoffTime.select_by_index(7)
    sleep(5)

    SearchButton = driver.find_element(By.ID, 'carhire-search-controls-search-button')
    SearchButton.click()
    sleep(3)

    # # assert len(driver.find_elements(By.CSS_SELECTOR, "[data-testid='inventory-card-clickable-button']")) == 0, "Some cars were unexpectedly found on the page."
    error_boxes = driver.find_elements(By.ID, "carhire-search-controls-errors")

    assert error_boxes, "Error element not found, no error displayed"
    error_text = error_boxes[0].text.strip()
    assert error_text != "", "Error box found but empty, expected an error message"

### ------------------------------------------------------------------------------------------------------------###

## Test Three: Car rental with the same pick-up and drop-off location
def test_3(driver):
    # sleep(50)
    Car_tab = driver.find_element(By.XPATH, "//span[text()='Car rental']")
    Car_tab.click()

    #  sleep(20)

    DiffLocCheck = driver.find_element(By.XPATH, "//input[@id='carhire-search-controls-different-drop-off']")
    DiffLocCheck.click()

    DestInput = driver.find_element(By.ID, 'carhire-search-controls-location-drop-off')
    DestInput.send_keys('Ben Gurion Intl (TLV)')
    sleep(4)

    DropoffInput = driver.find_element(By.ID, 'carhire-search-controls-location-pick-up')
    DropoffInput.send_keys('Ben Gurion Intl (TLV)')
    sleep(4)

    PickupDate = driver.find_element(By.XPATH, "//span[text()='Pickup date']")
    PickupDate.click()
    SelectPickupDate = driver.find_elements(By.XPATH,
                                            "//button[@class ='BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectPickupDate[2].click()
    sleep(3)

    PickupTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-pick-up']"))
    PickupTime.select_by_index(5)
    sleep(3)

    DropoffDate = driver.find_element(By.XPATH, "//span[text() = 'Drop-off date']")
    DropoffDate.click()
    sleep(3)
    SelectDropoffDate = driver.find_elements(By.XPATH,
                                             "//button[@class = 'BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectDropoffDate[4].click()
    sleep(3)

    DropoffTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-drop-off']"))
    DropoffTime.select_by_index(7)
    sleep(5)

    SearchButton = driver.find_element(By.ID, 'carhire-search-controls-search-button')
    SearchButton.click()
    sleep(3)

    error_boxes = driver.find_elements(By.ID, "carhire-search-controls-errors")

    assert error_boxes, "Error element not found, no error displayed"
    error_text = error_boxes[0].text.strip()
    assert error_text != "", "Error box found but empty, expected an error message"

### ------------------------------------------------------------------------------------------------------------###

##Fourth Test: Car rental with no available cars for the selected locations

def test_4(driver):
    #  sleep(30)
    Car_tab = driver.find_element(By.XPATH, "//span[text()='Car rental']")
    Car_tab.click()

    #  sleep(20)

    DiffLocCheck = driver.find_element(By.XPATH, "//input[@id='carhire-search-controls-different-drop-off']")
    DiffLocCheck.click()

    DestInput = driver.find_element(By.ID, 'carhire-search-controls-location-drop-off')
    DestInput.send_keys('Ben Gurion Intl (TLV)')
    sleep(4)

    DropoffInput = driver.find_element(By.ID, 'carhire-search-controls-location-pick-up')
    DropoffInput.send_keys('Hong Kong Intl (HKG)')
    sleep(4)

    PickupDate = driver.find_element(By.XPATH, "//span[text()='Pickup date']")
    PickupDate.click()
    SelectPickupDate = driver.find_elements(By.XPATH,
                                            "//button[@class ='BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectPickupDate[2].click()
    sleep(3)

    PickupTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-pick-up']"))
    PickupTime.select_by_index(5)
    sleep(3)

    DropoffDate = driver.find_element(By.XPATH, "//span[text() = 'Drop-off date']")
    DropoffDate.click()
    sleep(3)
    SelectDropoffDate = driver.find_elements(By.XPATH,
                                             "//button[@class = 'BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectDropoffDate[4].click()
    sleep(3)

    DropoffTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-drop-off']"))
    DropoffTime.select_by_index(7)
    sleep(5)

    SearchButton = driver.find_element(By.ID, 'carhire-search-controls-search-button')
    SearchButton.click()
    sleep(3)

    assert len(driver.find_elements(By.CSS_SELECTOR,
                                    "[data-testid='inventory-card-clickable-button']")) == 0, "Some cars were unexpectedly found on the page."

### ------------------------------------------------------------------------------------------------------------###

##Test five: Car rental with filter applied
def test_5(driver):
    #  sleep(30)
    Car_tab = driver.find_element(By.XPATH, "//span[text()='Car rental']")
    Car_tab.click()

    # sleep(20)

    # DiffLocCheck = driver.find_element(By.XPATH, "//input[@id='carhire-search-controls-different-drop-off']")
    # DiffLocCheck.click()

    DestInput = driver.find_element(By.ID, 'carhire-search-controls-location-pick-up')
    DestInput.send_keys('Palma - Majorca (PMI)')
    sleep(4)

    # DropoffInput = driver.find_element(By.ID, 'carhire-search-controls-location-drop-off')
    # DropoffInput.send_keys('Hong Kong Intl (HKG)')
    # sleep(4)

    PickupDate = driver.find_element(By.XPATH, "//span[text()='Pickup date']")
    PickupDate.click()
    SelectPickupDate = driver.find_elements(By.XPATH,
                                            "//button[@class ='BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectPickupDate[2].click()
    sleep(3)

    PickupTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-pick-up']"))
    PickupTime.select_by_index(5)
    sleep(3)

    DropoffDate = driver.find_element(By.XPATH, "//span[text() = 'Drop-off date']")
    DropoffDate.click()
    sleep(3)
    SelectDropoffDate = driver.find_elements(By.XPATH,
                                             "//button[@class = 'BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectDropoffDate[4].click()
    sleep(3)

    DropoffTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-drop-off']"))
    DropoffTime.select_by_index(7)
    sleep(5)

    SearchButton = driver.find_element(By.ID, 'carhire-search-controls-search-button')
    SearchButton.click()
    sleep(3)

    # SeatsFilterB = driver.find_element(By.XPATH,'//h3[text()="Seats"]')
    # SeatsFilterB.click()
    # sleep(10)
    #
    SeatsFilter = driver.find_element(By.XPATH, "//button[@title='4-5']")
    SeatsFilter.click()
    sleep(1)

    ManualTransFilter = driver.find_element(By.XPATH, '//input[@id="filter-option-manual"]')
    ManualTransFilter.click()
    sleep(1)

    AcFilter = driver.find_element(By.XPATH, '//input[@id="filter-option-ac"]')
    AcFilter.click()
    sleep(5)

    car_cards = driver.find_elements(By.CLASS_NAME, 'CarCard')

    for card in car_cards:
        labels = card.find_elements(By.CLASS_NAME, 'bpk-icon-label__text')
        label_texts = [label.text.lower() for label in labels]

        # Seats
        numbers = [int(t) for t in label_texts if t.isdigit()]
        assert any(4 <= n <= 5 for n in numbers), f"Seats issue: {numbers}"

        # Transmission
        assert any("automatic" in t for t in label_texts), "Missing automatic"

        # AC
        assert any("ac" in t for t in label_texts), "Missing AC"

### ------------------------------------------------------------------------------------------------------------###

##Test Six: Car rental with invalid date input
def test_6(driver):
    # sleep(30)
    Car_tab = driver.find_element(By.XPATH, "//span[text()='Car rental']")
    Car_tab.click()

    # sleep(20)

    # DiffLocCheck = driver.find_element(By.XPATH, "//input[@id='carhire-search-controls-different-drop-off']")
    # DiffLocCheck.click()

    DestInput = driver.find_element(By.ID, 'carhire-search-controls-location-pick-up')
    DestInput.send_keys('Palma - Majorca (PMI)')
    sleep(4)

    # DropoffInput = driver.find_element(By.ID, 'carhire-search-controls-location-drop-off')
    # DropoffInput.send_keys('Hong Kong Intl (HKG)')
    # sleep(4)

    PickupDate = driver.find_element(By.XPATH, "//span[text()='Pickup date']")
    PickupDate.click()
    SelectPickupDate = driver.find_elements(By.XPATH,
                                            "//button[@class ='BpkCalendarDate_bpk-calendar-date__N2RjO']")
    print("Number of dates found:", len(SelectPickupDate))

    SelectPickupDate[3].click()

    sleep(3)

    PickupTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-pick-up']"))
    PickupTime.select_by_index(5)
    sleep(3)

    DropoffDate = driver.find_element(By.XPATH, "//span[text() = 'Drop-off date']")
    DropoffDate.click()
    sleep(3)
    SelectDropoffDate = driver.find_elements(By.XPATH,
                                             "//button[@class = 'BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectDropoffDate[1].click()
    sleep(3)

    DropoffTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-drop-off']"))
    DropoffTime.select_by_index(7)
    sleep(5)

    SearchButton = driver.find_element(By.ID, 'carhire-search-controls-search-button')
    SearchButton.click()
    sleep(3)
    assert len(driver.find_elements(By.CSS_SELECTOR,
                                    "[data-testid='inventory-card-clickable-button']")) > 0, "No cars were found on the page."

### ------------------------------------------------------------------------------------------------------------###

##Test Seven: Car rental with empty pick-up location
def test_7(driver):
    sleep(30)
    Car_tab = driver.find_element(By.XPATH, "//span[text()='Car rental']")
    Car_tab.click()

    # sleep(20)

    # DiffLocCheck = driver.find_element(By.XPATH, "//input[@id='carhire-search-controls-different-drop-off']")
    # DiffLocCheck.click()

    DestInput = driver.find_element(By.ID, 'carhire-search-controls-location-pick-up')
    DestInput.send_keys('')
    sleep(4)

    # DropoffInput = driver.find_element(By.ID, 'carhire-search-controls-location-drop-off')
    # DropoffInput.send_keys('Hong Kong Intl (HKG)')
    # sleep(4)

    PickupDate = driver.find_element(By.XPATH, "//span[text()='Pickup date']")
    PickupDate.click()
    SelectPickupDate = driver.find_elements(By.XPATH,
                                            "//button[@class ='BpkCalendarDate_bpk-calendar-date__N2RjO']")
    print("Number of dates found:", len(SelectPickupDate))

    SelectPickupDate[2].click()

    sleep(3)

    PickupTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-pick-up']"))
    PickupTime.select_by_index(5)
    sleep(3)

    DropoffDate = driver.find_element(By.XPATH, "//span[text() = 'Drop-off date']")
    DropoffDate.click()
    sleep(3)
    SelectDropoffDate = driver.find_elements(By.XPATH,
                                             "//button[@class = 'BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectDropoffDate[3].click()
    sleep(3)

    DropoffTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-drop-off']"))
    DropoffTime.select_by_index(7)
    sleep(5)

    SearchButton = driver.find_element(By.ID, 'carhire-search-controls-search-button')
    SearchButton.click()
    sleep(3)

### ------------------------------------------------------------------------------------------------------------###

##Test eight: Add a rental car to favourites
def test_8(driver):
    # sleep(30)
    LoginButton = driver.find_element(By.XPATH, "//span[@class='LoginButton_loginText__N2E5Y']")
    LoginButton.click()
    sleep(3)

    EmailLogIn = driver.find_element(By.XPATH,
                                     "//span[@class='BpkText_bpk-text__MjhhY BpkText_bpk-text--label-1__OGE0O EmailLoginButton_email-login-button__text__MTg4O']")
    EmailLogIn.click()
    sleep(3)
    EmailInput = driver.find_element(By.XPATH,
                                     "//input[@class='BpkInput_bpk-input__MDBkO BpkInput_bpk-input--large__YTUyN']")
    EmailInput.send_keys(
        'rraagghhaadddd@gmail.com')  ## each time we test we should change the email to a never used email

    NextButton = driver.find_element(By.XPATH,
                                     "//button[@class='BpkButton_bpk-button__OTE4Z BpkButton_bpk-button--large__NTAyN BpkButton_bpk-button--featured__NTk3N ProgressionButton_progression-button__NjNhM']")
    NextButton.click()
    sleep(3)

    MaybeLaterButton = driver.find_element(By.XPATH, "//button[text()='Maybe later']")
    MaybeLaterButton.click()
    sleep(3)

    Car_tab = driver.find_element(By.XPATH, "//span[text()='Car rental']")
    Car_tab.click()

    # sleep(20)

    # DiffLocCheck = driver.find_element(By.XPATH, "//input[@id='carhire-search-controls-different-drop-off']")
    # DiffLocCheck.click()

    DestInput = driver.find_element(By.ID, 'carhire-search-controls-location-pick-up')
    DestInput.send_keys('Palma - Majorca (PMI)')
    sleep(4)

    # DropoffInput = driver.find_element(By.ID, 'carhire-search-controls-location-drop-off')
    # DropoffInput.send_keys('Hong Kong Intl (HKG)')
    # sleep(4)

    PickupDate = driver.find_element(By.XPATH, "//span[text()='Pickup date']")
    PickupDate.click()
    SelectPickupDate = driver.find_elements(By.XPATH,
                                            "//button[@class ='BpkCalendarDate_bpk-calendar-date__N2RjO']")
    ##  print("Number of dates found:", len(SelectPickupDate))

    SelectPickupDate[2].click()

    sleep(3)

    PickupTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-pick-up']"))
    PickupTime.select_by_index(5)
    sleep(3)

    DropoffDate = driver.find_element(By.XPATH, "//span[text() = 'Drop-off date']")
    DropoffDate.click()
    sleep(3)
    SelectDropoffDate = driver.find_elements(By.XPATH,
                                             "//button[@class = 'BpkCalendarDate_bpk-calendar-date__N2RjO']")
    SelectDropoffDate[3].click()
    sleep(3)

    DropoffTime = Select(driver.find_element(By.XPATH, "//select[@id ='carhire-search-controls-time-drop-off']"))
    DropoffTime.select_by_index(7)
    sleep(5)

    SearchButton = driver.find_element(By.ID, 'carhire-search-controls-search-button')
    SearchButton.click()
    sleep(3)

    Fav = driver.find_element(By.XPATH,
                              "//button[@class='BpkSaveButton_bpk-save-button__ZGY0M bpk-save-button__default']")
    Fav.click()
    sleep(3)

    wishlist = driver.find_element(By.XPATH,
                                   "//a[@class='BpkButton_bpk-button__ZGRmN BpkButton_bpk-button--link-on-dark__MmI0Z SecondaryNav_SecondaryNav__heartIcon__YjFhZ']")
    wishlist.click()
    sleep(7)
    saved_cars = driver.find_elements(By.CSS_SELECTOR, '[data-testid="CAR_HIRE_DEAL_GROUP_V1"]')
    assert len(saved_cars) > 0, "No rental cars were found in the wishlist"

# *******************************************************************************************




    # -Login via email Testing (first time/ new email)
def test_1(driver):
    sleep(20)
    login_btn = driver.find_element(By.XPATH, "//span[@class='LoginButton_loginText__N2E5Y']")
    login_btn.click()
    sleep(1)

    email_btn = driver.find_element(By.XPATH, "//span[text()='Continue with email']")
    email_btn.click()
    sleep(3)

    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('nnnoorr2250@gmail.com')

    next_btn = driver.find_element(By.XPATH, "//div[@class='js-progressionButton']")
    next_btn.click()
    sleep(3)

    notf_btn = driver.find_element(By.XPATH, "//button[text()='Maybe later']")
    notf_btn.click()
    sleep(3)

    # -Login via facebook Testing (valid user)
 def test_2(driver):
    login_btn = driver.find_element(By.XPATH, "//span[@class='LoginButton_loginText__N2E5Y']")
    login_btn.click()
    sleep(15)
    facebook_btn = driver.find_element(By.XPATH, "//span[text()='Facebook']")
    # facebook_btn.click();
    sleep(5)
    driver.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=1961295020753592&kid_directed_site=0&app_id=1961295020753592&signed_next=1&next=https%3A%2F')
    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('qaautomation275@gmail.com')
    sleep(3)
    password = driver.find_element(By.ID, 'pass')
    password.send_keys('Qa123456*')
    sleep(3)
    login_btn = driver.find_element(By.ID, 'loginbutton')
    login_btn.click()
    sleep(3)
    driver.get('https://www.skyscanner.co.il')
    sleep(10)

    # -Logout Testing
def test_3(driver):
    sleep(5)

    login_btn = driver.find_element(By.XPATH, "//span[text() ='Log in']")
    login_btn.click()
    sleep(2)

    email_btn = driver.find_element(By.XPATH,
                                    "//button[@class = 'BpkButton_bpk-button__OTE4Z BpkButton_bpk-button--large__NTAyN BpkButton_bpk-button--secondary__ZmJjM EmailLoginButton_email-login-button__Nzc5Y']")
    email_btn.click()
    sleep(2)

    email_input = driver.find_element(By.XPATH, "//input[@id = 'email']")
    email = generate_email()
    email_input.send_keys(email)
    sleep(4)

    next_btn = driver.find_element(By.XPATH, "//button[@aria-label = 'verify button']")
    next_btn.click()
    sleep(5)

    notf_btn = driver.find_element(By.XPATH, "//button[text() = 'Maybe later']")
    notf_btn.click()
    sleep(3)
    login_img = driver.find_element(By.XPATH, "//img[@data-testid='ProfilePicture']")
    login_img.click()
    sleep(5)

    logout_btn = driver.find_element(By.XPATH, "//div[text()='Log out']")
    logout_btn.click()
    sleep(5)

    login_btn = driver.find_element(By.XPATH, "//span[@class='LoginButton_loginText__N2E5Y']")
    assert login_btn.is_displayed() == True, 'Error: Login button is not displayed'
    sleep(5)
    # *********************************************************************************
    # Privecy Policy link
def test_4(driver):
    login_btn = driver.find_element(By.XPATH, "//span[@class='LoginButton_loginText__N2E5Y']")
    login_btn.click()
    sleep(15)

    pp_link = driver.find_element(By.XPATH, "//a[text()='Privacy Policy']")
    pp_link.click()
    sleep(3)
    # *********************************************************************************
    # check box (remember me)
def test_5(driver):
    login_btn = driver.find_element(By.XPATH, "//span[@class='LoginButton_loginText__N2E5Y']")
    login_btn.click()
    sleep(15)

    checkBox = driver.find_element(By.XPATH,"//input[@name='remember-me']")
    checkBox.click()
    sleep(6)
    #**********************************************************************************
