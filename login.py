from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import json

# obtain input info 
with open("info.json") as info_file:
    info = json.load(info_file)

username = info['username']
password = info['password']
department = info['department']
class_num = info['class_num']
crn = info['crn']

# login to enterprise
driver = webdriver.Chrome()
driver.get("https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1")
elem = driver.find_element_by_name("USER")
elem.clear()
elem.send_keys(username)

pas = driver.find_element_by_name("PASSWORD")
pas.clear()
pas.send_keys(password)
pas.send_keys(Keys.RETURN)

# navigate to registration & records page
driver.find_element_by_link_text("Registration & Records").click()

# navigate to classic registration
driver.find_element_by_link_text("Classic Registration").click()

# navigate to add/drop classes
driver.find_element_by_link_text("Add/Drop Classes").click()

# accept registration agreement
driver.find_element_by_link_text("I Agree to the Above Statement").click()

# select registration period
driver.find_element_by_css_selector("input[value = 'Submit']").click()

# navigate to class search
driver.find_element_by_css_selector("input[value = 'Class Search']").click()

# select department 
select_dep = Select(driver.find_element_by_css_selector("select[name = 'sel_subj']"))
select_dep.select_by_value(department)
driver.find_element_by_css_selector("input[value = 'Course Search']").click()

# select class
classes = driver.find_elements_by_css_selector("input[value = 'View Sections']")
classes[class_num].click()

# check boxes to register for section
for crn_val in crn:
    val = crn_val + " 120201"
    selector_string = "input[type='checkbox'][value='"+ val + "']"
    try:
        checkbox = driver.find_element_by_css_selector(selector_string)
    except Exception:
        print("Course is either closed or crn value is invalid. Exiting...")
        driver.close()
        exit()
    checkbox.click()
driver.find_element_by_css_selector("input[value = 'Register']").click()
