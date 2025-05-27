from selenium import webdriver
from selenium.webdriver.common.by import By  
import time
# wait for the page to load
from selenium.webdriver.common.action_chains import ActionChains


# open driver 
driver = webdriver.Firefox()

# open website
driver.get("https://www.orangehrm.com/")

# Wait for the page to load
time.sleep(5)


# Hover over "Solutions" to show dropdown
solutions_menu = driver.find_element(By.XPATH, "//a[contains(text(), 'Solutions')]")
ActionChains(driver).move_to_element(solutions_menu).perform()
time.sleep(5)  # Wait for dropdown to appear


# List of sub-headers to check
sub_headers = ["People Management", "Talent Management", "Compensation", "Culture", "Connectors"]
time.sleep(5)

# Check presence of sub-headers
print("\n--- Checking Sub-Headers ---")
for header in sub_headers:
    elements = driver.find_elements(By.XPATH, f"//li[contains(normalize-space(), '{header}')]")
    if elements:
        print(f"✅ Found: {header}")
        # click on the sub-header
        driver.execute_script("arguments[0].click();", elements[0])
        print(f"Sub-header clicked: {header}")
        # go back to previous page
        driver.back()
        print("Back to previous page")
        time.sleep(5)
    else:
        print(f"❌ Not Found: {header}")





# test people managemnt sub menu
print("\n--- Checking People Management Sub-Menu Items ---")


# ActionChains instance
actions = ActionChains(driver)

# Hover over "Solutions"
def hover_over_solutions():
    try:
        solutions_menu = driver.find_element(By.XPATH, "//a[contains(@class,'nav-link-hed')][normalize-space()='Solutions']")
        actions.move_to_element(solutions_menu).perform()
        time.sleep(2)
    except Exception as e:
        print("Error hovering over Solutions:", e)


# Hover over "People Management"
def hover_over_people_management():
    try:
        people_management = driver.find_element(By.XPATH, "//li[contains(., 'People Management')]")
        actions.move_to_element(people_management).perform()
        time.sleep(2)
    except Exception as e:
        print("Error hovering over People Management:", e)

# People Management submenu items
people_sub_items = [
    "HR Administration",
    "Employee Management",
    "Reporting & Analytics",
    "Mobile App"
]

for item in people_sub_items:
    try:
        hover_over_solutions()
        hover_over_people_management()
        time.sleep(2)
        link = driver.find_element(By.LINK_TEXT, item)
        if link:
            print(f"✅ Found: {item}")
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            driver.execute_script("arguments[0].click();", link)
            print(f"🖱️ Clicked: {item}")
            time.sleep(5)
            driver.back()
            time.sleep(5)
        else:
            print(f"❌ Not Found: {item}")
    except Exception as e:
        print(f"❌ Exception for '{item}':", e)




# test talent managemnt sub menu
print("\n--- Checking Talent Management Sub-Menu Items ---")


# ActionChains instance
actions = ActionChains(driver)

# Hover over "Solutions"
def hover_over_solutions():
    try:
        solutions_menu = driver.find_element(By.XPATH, "//a[contains(@class,'nav-link-hed')][normalize-space()='Solutions']")
        actions.move_to_element(solutions_menu).perform()
        time.sleep(2)
    except Exception as e:
        print("Error hovering over Solutions:", e)

# Hover over "Talent Management"
def hover_over_talent_management():
    try:
        talent_management = driver.find_element(By.XPATH, "//li[contains(., 'Talent Management')]")
        actions.move_to_element(talent_management).perform()
        time.sleep(2)
    except Exception as e:
        print("Error hovering over Talent Management:", e)

# Talent Management submenu items
talent_sub_items = [
    "Recruitment (ATS)",
    "Onboarding",
    "Request Desk",
]

print("\n--- Checking Talent Management Sub-Menu Items ---")
for item in talent_sub_items:
    try:
        hover_over_solutions()
        hover_over_talent_management()
        time.sleep(2)
        link = driver.find_element(By.LINK_TEXT, item)
        if link:
            print(f"✅ Found: {item}")
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            driver.execute_script("arguments[0].click();", link)
            print(f"🖱️ Clicked: {item}")
            time.sleep(5)
            driver.back()
            time.sleep(5)
    except Exception as e:
        print(f"❌ Exception for '{item}':", e)