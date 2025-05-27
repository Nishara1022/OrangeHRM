
from selenium import webdriver
from selenium.webdriver.common.by import By  
import time
from selenium.webdriver.support.ui import Select
# wait for the page to load

# open driver 
driver = webdriver.Firefox()

# open website
driver.get("https://www.orangehrm.com/")

time.sleep(10)



# logo find 
logo = driver.find_element(By.XPATH,"//a[@class='navbar-brand nav-logo']")
print("logo href value is ",logo.get_attribute("href"))
print("Logo clicked and open",logo.get_attribute('href'))
time.sleep(2)
print("")




# Language dropdown find 
language = driver.find_element(By.XPATH,"//select[@name='locale']")
language.click()

# Select option 
option = Select(language)

# find option by <input type="//option[@value='/es']" 
option = driver.find_element(By.XPATH,"//option[@value='/es']")
option.click()
print("Language clicked and open")
time.sleep(2)


# check language button 
Url = driver.current_url
if Url == "https://www.orangehrm.com/es":
    print("Language button is working")
else:
    print("Language button is not working")



# back to the EN language 
print("back to the EN language")

# Language dropdown find by 
language = driver.find_element(By.XPATH,"//select[@name='locale']")
language.click()

# Select option 
option = Select(language)

# find option by <input type="//option[@value='/es']" 
option = driver.find_element(By.XPATH,"//option[@value='/en']")
option.click()
print("Language clicked and open")
time.sleep(2)
print("")





# Header links
print("Header links")
print("")




# Solutions / Header link 1 find by <input type="//a[@class='nav-link-hed'][normalize-space()='Solutions']" 
Header_link_1 = driver.find_element(By.XPATH,"//a[@class='nav-link-hed'][normalize-space()='Solutions']")

# hover on Solutions / Header link 1
action = webdriver.ActionChains(driver)
action.move_to_element(Header_link_1).perform()
print("Solutions / Header link 1 ")
time.sleep(8)



# Why Orange HRM / Header link 2 find by  
Header_link_2 = driver.find_element(By.XPATH,"//a[@class='nav-link-hed'][normalize-space()='Why OrangeHRM']")
# move to Why Orange HRM / Header link 2
action = webdriver.ActionChains(driver)
action.move_to_element(Header_link_2).perform()
print("Why Orange HRM / Header link 2 clicked and open",Header_link_2.get_attribute('innerHTML'))
time.sleep(2)



# Resources / Header link 3 find 
Header_link_3 = driver.find_element(By.XPATH,"//a[@class='nav-link-hed'][normalize-space()='Resources']")
# move to Resources / Header link 3
action = webdriver.ActionChains(driver)
action.move_to_element(Header_link_3).perform()
print("Header link 3 clicked and open",Header_link_3.get_attribute('innerHTML'))
time.sleep(2)



# Company / Header link 4 find by 
Header_link_4 = driver.find_element(By.XPATH,"//a[@class='nav-link-hed'][normalize-space()='Company']")
# move to Company / Header link 4
action = webdriver.ActionChains(driver)
action.move_to_element(Header_link_4).perform()
print("Company / Header link 4 clicked and open",Header_link_4.get_attribute('innerHTML'))
time.sleep(2)



# Pricing / Header link 5 find by 
Header_link_5 = driver.find_element(By.XPATH,"//a[@class='nav-link-hed'][normalize-space()='Pricing']")
# move to Pricing / Header link 5
action = webdriver.ActionChains(driver)
action.move_to_element(Header_link_5).perform()
print("Pricing / Header link 5 clicked and open",Header_link_5.get_attribute('innerHTML'))
time.sleep(2)
print("")




#Book a Demo

# Book a Demo find
Book_a_Demo = driver.find_element(By.XPATH,"//div[contains(@class,'d-flex web-menu-btn')]//li[1]//a[1]")
Book_a_Demo.click()
print("Book a Demo clicked")
print("Book a Demo page open ")
time.sleep(2)



# title find by
title = driver.find_element(By.XPATH,"//h1[normalize-space()='Manage Your People and Operations in One Place']")
print("Book a Demo page title is ",title.get_attribute("innerHTML"))
time.sleep(2)



# name input find by Form_getForm_FullName
name = driver.find_element(By.ID,"Form_getForm_FullName")
name.send_keys("Nishara")
print("Enter name ",name.get_attribute("value"))
time.sleep(2)



# phone input find by Form_getForm_Contact
phone = driver.find_element(By.ID,"Form_getForm_Contact")
phone.send_keys("0777777777")
print("Enter phone  ",phone.get_attribute("value"))
time.sleep(2)



# email Form_getForm_Email find by 
email = driver.find_element(By.ID,"Form_getForm_Email")
email.send_keys("tharushi@me.com")
print("Enter email: ",email.get_attribute("value"))
time.sleep(2)



# CompanyName find by 
CompanyName = driver.find_element(By.ID,"Form_getForm_CompanyName")
CompanyName.send_keys("Nishara")
print("Enter CompanyName: ",CompanyName.get_attribute("value"))
time.sleep(2)




# Country find by Form_getForm_Country
Country = driver.find_element(By.ID,"Form_getForm_Country")
Country.click()

# Select option 
option = Select(Country)

# find option by <input type="//option[@value='United States']" 
option = driver.find_element(By.XPATH,"//option[@value='Australia']")
option.click()

print("Enter Country name: ",Country.get_attribute("value"))
time.sleep(2)



# No of Employees find by Form_getForm_NoOfEmployees
No_of_Employees = driver.find_element(By.ID,"Form_getForm_NoOfEmployees")
No_of_Employees.click()

# Select option 
option = Select(No_of_Employees)

# find option by innerHTML 11 - 50
option = driver.find_element(By.XPATH,"//option[normalize-space()='11 - 50']")
option.click()

print("Enter No of Employees: ",No_of_Employees.get_attribute("value"))
time.sleep(4)



# click_I_m_not_a_Robot = driver.find_element(By.XPATH,"//div[@class='d-flex web-menu-btn']//li[1]//a[1]")
# click_I_m_not_a_Robot.click()
# print(" I'm not a Robot clicked")


# <input type="body" data-field=
Recaptcha = driver.find_element(By.XPATH,"//body")
driver.execute_script("arguments[0].scrollIntoView(true);", Recaptcha)
print("I'm not a Robot icon found ")
time.sleep(10)
driver.execute_script("arguments[0].click();", Recaptcha)
print("I'm not a Robot icon clicked")
time.sleep(10)


# Submit find by Form_getForm_action_submitForm
Submit = driver.find_element(By.ID,"Form_getForm_action_submitForm")
Submit.click()
print("Submit clicked and open")
time.sleep(10)
print("")





# Contact Sales page test 
print("Contact Sales page ")



# Contact Sales button find 
Contact_Sales = driver.find_element(By.XPATH,"//div[@class='d-flex web-menu-btn']//li[2]//a[1]")
Contact_Sales.click()
print("Contact Sales clicked")
print("Contact Sales page open ")
time.sleep(10)


# name input find by Form_getForm_FullName
name = driver.find_element(By.ID,"Form_getForm_FullName")
name.send_keys("Nishara")
print("Enter name: ",name.get_attribute("value"))
time.sleep(2)


# phone input find by Form_getForm_Contact
phone = driver.find_element(By.ID,"Form_getForm_Contact")
phone.send_keys("0777777777")
print("Enter phone: ",phone.get_attribute("value"))
time.sleep(2)


# EMail find by Form_getForm_Email
EMail = driver.find_element(By.ID,"Form_getForm_Email")
EMail.send_keys("tharushi@me.com")
print("Enter Email: ",EMail.get_attribute("value"))
time.sleep(2)



# Country find by  
Country = driver.find_element(By.ID,"Form_getForm_Country")
Country.click()

# Select option 
option = Select(Country)

# find option by  
option = driver.find_element(By.XPATH,"//option[@value='Australia']")
option.click()

print("Enter Country ",Country.get_attribute("value"))
time.sleep(2)



# No of Employees find by Form_getForm_NoOfEmployees
No_of_Employees = driver.find_element(By.ID,"Form_getForm_NoOfEmployees")
No_of_Employees.click()

# Select option 
option = Select(No_of_Employees)

# find option by innerHTML 51 - 200
option = driver.find_element(By.XPATH,"//option[normalize-space()='51 - 200']")
option.click()

print("Enter No of Employees: ",No_of_Employees.get_attribute("value"))
time.sleep(2)



# JobTitle find by Form_getForm_JobTitle
JobTitle = driver.find_element(By.ID,"Form_getForm_JobTitle")
JobTitle.send_keys("QA")
print("Enter JobTitle ",JobTitle.get_attribute("value"))
time.sleep(2)


# Comment find by 
Comment = driver.find_element(By.ID,"Form_getForm_Comment")
Comment.send_keys("Nishara")
print("Enter Comment: ",Comment.get_attribute("value"))
time.sleep(6)
print("")


# # I'm not a Robot button find 
# <input type="html" data-field=
Recaptcha = driver.find_element(By.XPATH,"//body")
driver.execute_script("arguments[0].scrollIntoView(true);", Recaptcha)
print("I'm not a Robot icon found ")
driver.execute_script("arguments[0].click();", Recaptcha)
print("I'm not a Robot icon clicked")
time.sleep(7)
print("")



# Submit find by 
Submit = driver.find_element(By.ID, "Form_getForm_action_submitForm")

# Scroll to the element (optional but helpful if it's off-screen)
driver.execute_script("arguments[0].scrollIntoView(true);", Submit)

# Click using JavaScript
driver.execute_script("arguments[0].click();", Submit)

# Submit Contact Sales 

print("Submit clicked and open / Contact Sales button clicked")
time.sleep(6)
print("")
print("")




# Home Page 
print("Home Page")
# logo find by 
logo = driver.find_element(By.XPATH,"//a[@class='navbar-brand nav-logo']")
logo.click()



# page title
Home = driver.find_element(By.XPATH,"//h1[1]")
print("Home page title: ",Home.get_attribute('innerHTML'))
time.sleep(2)
print("")


# homepage-slider-bottom']" 
slider = driver.find_element(By.XPATH,"//div[@class='homepage-slider-bottom']")
driver.execute_script("arguments[0].scrollIntoView(true);", slider)
print("home page image slider: ",slider.get_attribute('alt'))
time.sleep(2)


# description
text = driver.find_element(By.XPATH,"//p[contains(text(),'At OrangeHRM, AI isn’t just technology—it’s a comm')]")
driver.execute_script("arguments[0].scrollIntoView(true);", text)
print("home page description: ",text.get_attribute('innerHTML'))
time.sleep(2)
print("")




# free trial function
print("free trial button in home page")


# 30 days free trial find 
Free_trial = driver.find_element(By.ID,"Form_submitForm_EmailHomePage")
time.sleep(3)
driver.execute_script("arguments[0].scrollIntoView(true);", Free_trial)
Free_trial.send_keys("tharushi@gmail.com")
print("Free trial email Entered: ",Free_trial.get_attribute("value"))
time.sleep(10)


# Reuest butto Form_submitForm_action_request
Reuest = driver.find_element(By.ID,"Form_submitForm_action_request")
# scroll to the element (optional but helpful if it's off-screen)
driver.execute_script("arguments[0].scrollIntoView(true);", Reuest)
driver.execute_script("arguments[0].click();", Reuest)
print("Reuest button clicked")
print("open ",Reuest.get_attribute('value'))
time.sleep(10)
print("")



# Free trial page 
print("Free trial page")


# title 
title = driver.find_element(By.XPATH,"//h1[contains(text(),'Revolutionize Your Human Resource Management Exper')]")
title_text = title.text
print("Free trial page title: ",title_text)
time.sleep(2)


# user name 
name = driver.find_element(By.ID,"Form_getForm_subdomain")
name.send_keys("Nishara")
print("Enter user name: ",name.get_attribute("value"))
time.sleep(2)


# full name 
full_name = driver.find_element(By.ID,"Form_getForm_Name")
full_name.send_keys("Nishara")
print("Enter full name: ",full_name.get_attribute("value"))
time.sleep(2)


# email
email = driver.find_element(By.ID,"Form_getForm_Email")
# clear the existing value
email.clear()
email.send_keys("tharushiQA@megmail.com")
print("Enter email: ",email.get_attribute("value"))
time.sleep(2)


# phone
phone = driver.find_element(By.ID,"Form_getForm_Contact")
phone.send_keys("0777777777")
print("Enter phone: ",phone.get_attribute("value"))
time.sleep(2)



# Country 
country = driver.find_element(By.ID,"Form_getForm_Country")
country.click()

# Select option 
option = Select(country)

# find option by innerHTML Sri Lanka
option = driver.find_element(By.XPATH,"//option[normalize-space()='Sri Lanka']")
option.click()
print("Enter country: ",country.get_attribute("value"))
time.sleep(2)



# I'm not a Robot
Recaptcha = driver.find_element(By.XPATH,"//body")
driver.execute_script("arguments[0].scrollIntoView(true);", Recaptcha)
print("I'm not a Robot icon found ")
driver.execute_script("arguments[0].click();", Recaptcha)
print("I'm not a Robot icon clicked")
time.sleep(7)
print("")


# submit
Submit = driver.find_element(By.ID,"Form_getForm_action_submitForm")
driver.execute_script("arguments[0].click();", Submit)
Submit.click()
print("Submit clicked and open",Submit.get_attribute('innerHTML'))
time.sleep(10)
print("")




# Home Page test other elements
# logo find by  
logo = driver.find_element(By.XPATH,"//a[@class='navbar-brand nav-logo']")
logo.click()
print("back to home page")
time.sleep(7)


# HR for All find 
HR = driver.find_element(By.XPATH,"//h3[normalize-space()='HR for All']")
print("HR for All text: ",HR.get_attribute('innerHTML'))
driver.execute_script("arguments[0].scrollIntoView(true);", HR)
time.sleep(2)
print("")



# YouTube video
print("YouTube video Test in home page")


iframe = driver.find_element(By.CSS_SELECTOR, "div.homepage-hrforall-video iframe")
driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
time.sleep(5)

# Switch to the iframe
driver.switch_to.frame(iframe)
print("Switched to iframe.")
time.sleep(10)

# Wait for the YouTube video to load
print("YouTube video loaded.")

# Play button find 
play_button = driver.find_element(By.CSS_SELECTOR, "button.ytp-large-play-button")
play_button.click()
print("YouTube button clicked. ")
print("video is playing")
time.sleep(10)


# Switch back to main content if needed
driver.switch_to.default_content()
print("Switched back to main content.")
print("")




# HR for All find 
HR = driver.find_element(By.XPATH,"//h3[normalize-space()='HR for All']")
print("HR for All text: ",HR.get_attribute('innerHTML'))
driver.execute_script("arguments[0].scrollIntoView(true);", HR)
time.sleep(2)





# people Management Section
print("people Management Section")


# People Management find 
People = driver.find_element(By.XPATH,"//h2[normalize-space()='People Management']")
print("People Management text: ",People.get_attribute('innerHTML'))
driver.execute_script("arguments[0].scrollIntoView(true);", People)
time.sleep(10)


# Learn More find by 
Learn_More = driver.find_element(By.XPATH,"//a[@href='/en/solutions/people-management/hr-administration']//div[@class='link-text']//h6[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn_More)
Learn_More.click()
time.sleep(10)
print("Learn More button clicked")
print("open HR Administration page after clicking People Management learn more button")
print("")
print("")




# HR Administration page test 
print("HR Administration page test")


# NR title 
HR = driver.find_element(By.XPATH,"//h1[normalize-space()='HR Administration']")
driver.execute_script("arguments[0].scrollIntoView(true);", HR)
print("HR Administration text:" ,HR.get_attribute('innerHTML'))
time.sleep(5)


# 'Book a Free Demo']" 
Book = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Book)
print("Book a Free Demo button: ",Book.get_attribute('innerHTML'))  
Book.click()
time.sleep(5)


# back to HR Administration page
driver.back()


# Enhanced Security with MFA 
Enhanced = driver.find_element(By.XPATH,"//h2[normalize-space()='Enhanced Security with MFA']")
driver.execute_script("arguments[0].scrollIntoView(true);", Enhanced)
print("Enhanced Security with MFA text: ",Enhanced.get_attribute('innerHTML'))
time.sleep(5)


# Enhanced Security with MFA']" 
MFA = driver.find_element(By.XPATH,"//h2[normalize-space()='Enhanced Security with MFA']")
driver.execute_script("arguments[0].scrollIntoView(true);", MFA)
print("MFA image: ",MFA.get_attribute('alt'))
time.sleep(5)
print("")


# Audit Trail
Audit = driver.find_element(By.XPATH,"//h2[normalize-space()='Audit Trail']")
driver.execute_script("arguments[0].scrollIntoView(true);", Audit)
print("Audit Trail text: ",Audit.get_attribute('innerHTML'))
time.sleep(5)


# (@alt,'Audit Trail')]" 
Audit = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Audit Trail')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Audit)
print("Audit Trail image: ",Audit.get_attribute('alt'))
time.sleep(5)
print("")


# Asset Tracking
Asset = driver.find_element(By.XPATH,"//h2[normalize-space()='Asset Tracking']")
driver.execute_script("arguments[0].scrollIntoView(true);", Asset)
print("Asset Tracking image: ",Asset.get_attribute('innerHTML'))
time.sleep(5)

# Asset Tracking
Asset = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Asset Tracking')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Asset)
print("Asset Tracking image: ",Asset.get_attribute('alt'))
time.sleep(5)
print("")



# News & HR Policy Publisher
News = driver.find_element(By.XPATH,"//h2[normalize-space()='News & HR Policy Publisher']")
driver.execute_script("arguments[0].scrollIntoView(true);", News)
print("News & HR Policy Publisher: ",News.get_attribute('innerHTML'))
time.sleep(5)


# 'News & HR Policy Publisher')]" 
News = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'News & HR Policy Publisher')]")
driver.execute_script("arguments[0].scrollIntoView(true);", News)
print("News & HR Policy Publisher image: ",News.get_attribute('alt'))
time.sleep(5)
print("")



# Notifications
Notifications = driver.find_element(By.XPATH,"//h2[normalize-space()='Notifications']")
driver.execute_script("arguments[0].scrollIntoView(true);", Notifications)
print("Notifications text: ",Notifications.get_attribute('innerHTML'))
time.sleep(5)


# 'Notifications')]" 
Notifications = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Notifications')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Notifications)
print("Notifications image: ",Notifications.get_attribute('alt'))
time.sleep(5)
print("")



# Custom User Roles
Custom = driver.find_element(By.XPATH,"//h2[normalize-space()='Custom User Roles']")
driver.execute_script("arguments[0].scrollIntoView(true);", Custom)
print("Custom User Roles text: ",Custom.get_attribute('innerHTML'))
time.sleep(5)


# 'User Roles')]" 
Custom = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'User Roles')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Custom)
print("Custom User Roles image: ",Custom.get_attribute('alt'))
time.sleep(5)
print("")



# Check out what else you can do with People Management
Check = driver.find_element(By.XPATH,"//h4[contains(text(),'Check out what else you can do with People Management')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Check)
print("Check out what else you can do with People Management text: /n ",Check.get_attribute('innerHTML'))
time.sleep(5)
print("")


# EmplyeeManagement
Employee = driver.find_element(By.XPATH,"//h4[normalize-space()='Employee Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
print("Employee Management text: ",Employee.get_attribute('innerHTML'))
time.sleep(6)


# 'Learn More')]" 
Employee = driver.find_element(By.XPATH,"//a[@href='/en/solutions/people-management/employee-management']//div[@class='link-text']//p[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
driver.execute_script("arguments[0].click();", Employee)
time.sleep(5)
print("")




# Employee Management Page
print("Employee Management page test")


# Employee Management']" 
Employee = driver.find_element(By.XPATH,"//h1[normalize-space()='Employee Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
print("Employee Management title: ",Employee.get_attribute('innerHTML'))
time.sleep(10)


# Book a Free Demo']" 
Demo = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
print("Get a Demo button clicked: ",Demo.get_attribute('innerHTML'))
time.sleep(5)


driver.get("https://www.orangehrm.com/en/solutions/people-management/employee-management")


# Demo button 2
Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
driver.execute_script("arguments[0].click();", Demo)
print("Demo button 2 clicked: ",Demo.get_attribute('value'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/people-management/employee-management")


# Dashboard']" 
Dashboard = driver.find_element(By.XPATH,"//h2[normalize-space()='Dashboard']")
driver.execute_script("arguments[0].scrollIntoView(true);", Dashboard)
print("Dashboard text: ",Dashboard.get_attribute('innerHTML'))
time.sleep(5)


# Dashboard')]" 
Dashboard = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Dashboard')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Dashboard)
print("Dashboard image: ",Dashboard.get_attribute('alt'))
time.sleep(5)
print("")



# Employee Database & Profiles']" 
Database = driver.find_element(By.XPATH,"//h2[normalize-space()='Employee Database & Profiles']")
driver.execute_script("arguments[0].scrollIntoView(true);", Database)
print("Employee Database & Profiles text: ",Database.get_attribute('innerHTML'))
time.sleep(5)


# Employee Databse and Profile')]" 
Database = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Employee Databse and Profile')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Database)
print("Employee Database & Profiles image: ",Database.get_attribute('alt'))
time.sleep(5)
print("")



# Streamline Staff Scheduling with Work Schedules']" 
Schedule = driver.find_element(By.XPATH,"//h2[normalize-space()='Streamline Staff Scheduling with Work Schedules']")
driver.execute_script("arguments[0].scrollIntoView(true);", Schedule)
print("Streamline Staff Scheduling with Work Schedules text: ",Schedule.get_attribute('innerHTML'))
time.sleep(5)


# Streamline Staff Scheduling with Work Schedules')]" 
Schedule = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Streamline Staff Scheduling with Work Schedules')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Schedule)
print("Streamline Staff Scheduling with Work Schedules image: ",Schedule.get_attribute('alt'))
time.sleep(5)
print("")



# Disciplinary Tracking
Disciplinary = driver.find_element(By.XPATH,"//h2[normalize-space()='Disciplinary Tracking']")
driver.execute_script("arguments[0].scrollIntoView(true);", Disciplinary)
print("Disciplinary Tracking text: ",Disciplinary.get_attribute('innerHTML'))
time.sleep(5)


# Disciplinary Tracking
Disciplinary = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Disciplinary Tracking')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Disciplinary)
print("Disciplinary Tracking image: ",Disciplinary.get_attribute('alt'))
time.sleep(5)
print("")



# Organization Chart']" 
Org = driver.find_element(By.XPATH,"//h2[normalize-space()='Organization Chart']")
driver.execute_script("arguments[0].scrollIntoView(true);", Org)
print("Organization Chart text: ",Org.get_attribute('innerHTML'))
time.sleep(5)


# Org Chart')]" 
Org = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Org Chart')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Org)    
print("Org Chart image: ",Org.get_attribute('alt'))
time.sleep(5)
print("")



# Corporate Directory']" 
Directory = driver.find_element(By.XPATH,"//h2[normalize-space()='Corporate Directory']")
driver.execute_script("arguments[0].scrollIntoView(true);", Directory)
print("Corporate Directory text: ",Directory.get_attribute('innerHTML'))
time.sleep(5)


# Corporate Directory')]" 
Directory = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Corporate Directory')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Directory)
print("Corporate Directory image: ",Directory.get_attribute('alt'))
time.sleep(5)
print("")



# Reporting & Analytics test 
print("Reporting & Analytics test")


# Reporting 
Reporting = driver.find_element(By.XPATH,"//h4[normalize-space()='Reporting and Analytics']")
driver.execute_script("arguments[0].scrollIntoView(true);", Reporting)
print("Reporting and Analytics text: ",Reporting.get_attribute('innerHTML'))
time.sleep(5)


# Reporting button
Reporting = driver.find_element(By.XPATH,"//a[@href='/en/solutions/people-management/reporting-and-analytics']//div[@class='link-icon']//img")
driver.execute_script("arguments[0].scrollIntoView(true);", Reporting)
driver.execute_script("arguments[0].click();", Reporting)
time.sleep(6)
print("")
print("")   



# Reporting page test
print("Reporting page test")



# reporting and analytics
Report = driver.find_element(By.XPATH,"//h1[normalize-space()='Reporting and Analytics']")
driver.execute_script("arguments[0].scrollIntoView(true);", Report)
print("Reporting and Analytics title: ",Report.get_attribute('innerHTML'))
time.sleep(5)
print("")


# Demo 
Demo = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
Demo.click()
time.sleep(5)


driver.get("https://www.orangehrm.com/en/solutions/people-management/reporting-and-analytics")


# platform-page-description text-center']" 
desc = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", desc)
print("Reporting and Analytics description: ",desc.get_attribute('innerHTML'))
time.sleep(5)
print("")


# Demo button 2
# <input type="//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']" 
Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
Demo.click()
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/people-management/reporting-and-analytics")


# Custom Reports']" 
Custom = driver.find_element(By.XPATH,"//h2[normalize-space()='Custom Reports']")
driver.execute_script("arguments[0].scrollIntoView(true);", Custom)
print("Custom Reports text: ",Custom.get_attribute('innerHTML'))
time.sleep(5)


# Custom Reports')]" 
Custom = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Custom Reports')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Custom)
print("Custom Reports image: ",Custom.get_attribute('alt'))
time.sleep(5)
print("")


# Graphical Reports
Graph = driver.find_element(By.XPATH,"//h2[normalize-space()='Graphical Reports']")
driver.execute_script("arguments[0].scrollIntoView(true);", Graph)
print("Graphical Reports text: ",Graph.get_attribute('innerHTML'))
time.sleep(5)



# Graphical Reports
Graph = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Graphical Reports')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Graph)
print("Graphical Reports image: ",Graph.get_attribute('alt'))
time.sleep(5)
print("")



# Extraction of Reports
Extract = driver.find_element(By.XPATH,"//h2[normalize-space()='Extraction of Reports']")
driver.execute_script("arguments[0].scrollIntoView(true);", Extract)
print("Extraction of Reports text: ",Extract.get_attribute('innerHTML'))
time.sleep(5)


Extract = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Extraction of Reports')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Extract)
print("Extraction of Reports image: ",Extract.get_attribute('alt'))
time.sleep(5)
print("")


# Snapshot Reporting 
Snapshot = driver.find_element(By.XPATH,"//h2[normalize-space()='Snapshot Reporting']")
driver.execute_script("arguments[0].scrollIntoView(true);", Snapshot)
print("Snapshot Reporting text: ",Snapshot.get_attribute('innerHTML'))
time.sleep(5)


Snapshot = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Snapshot Reporting')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Snapshot)
print("Snapshot Reporting image: ",Snapshot.get_attribute('alt'))
time.sleep(5)
print("")



# Streamline Your Reporting with Scheduled Reports
Scheduled = driver.find_element(By.XPATH,"//h2[normalize-space()='Streamline Your Reporting with Scheduled Reports']")
driver.execute_script("arguments[0].scrollIntoView(true);", Scheduled)
print("Streamline Your Reporting with Scheduled Reports text: ",Scheduled.get_attribute('innerHTML'))
time.sleep(5)


Scheduled = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Streamline Your Reporting with Scheduled Reports')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Scheduled)
print("Streamline Your Reporting with Scheduled Reports image: ",Scheduled.get_attribute('alt'))
time.sleep(5)
print("")


# Check out what else you can do with People Managem')]" 
Check = driver.find_element(By.XPATH,"//h4[contains(text(),'Check out what else you can do with People Management')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Check)
print("Check out what else you can do with People Management text: ",Check.get_attribute('innerHTML'))
time.sleep(5)
print("")



# Employee Management
print("Employee Management text: ")


# Employee Management 
Employee = driver.find_element(By.XPATH,"//h4[normalize-space()='Employee Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
print("Employee Management text: ",Employee.get_attribute('innerHTML'))
time.sleep(5)


Employee = driver.find_element(By.XPATH,"//a[@href='/en/solutions/people-management/employee-management']//div[@class='link-text']//p[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
driver.execute_script("arguments[0].click();", Employee)
print("Employee Management page open")
time.sleep(5)
print("")
print("")




# Employee Management Page
print("Employee Management page test")


# Employee Management page title 
Employee = driver.find_element(By.XPATH,"//h1[normalize-space()='Employee Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
print("Employee Management page title: ",Employee.get_attribute('innerHTML'))
time.sleep(5)
print("")


Demo = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
print("Get a Demo button clicked: ",Demo.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/people-management/employee-management")


# description
desc = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", desc)
print("Employee Management description: ",desc.get_attribute('innerHTML'))
time.sleep(5)
print("")


# demo 2
Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
Demo.click()
time.sleep(5)
print("")

driver.get("https://www.orangehrm.com/en/solutions/people-management/employee-management")



Dashboard = driver.find_element(By.XPATH,"//h2[normalize-space()='Dashboard']")
driver.execute_script("arguments[0].scrollIntoView(true);", Dashboard)
print("Dashboard text: ",Dashboard.get_attribute('innerHTML'))
time.sleep(5)


Dashboard = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Dashboard')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Dashboard)
print("Dashboard image: ",Dashboard.get_attribute('alt'))
time.sleep(5)
print("")



Database = driver.find_element(By.XPATH,"//h2[normalize-space()='Employee Database & Profiles']")
driver.execute_script("arguments[0].scrollIntoView(true);", Database)
print("Employee Database & Profiles text: ",Database.get_attribute('innerHTML'))
time.sleep(5)


Database = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Employee Databse and Profile')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Database)
print("Employee Database & Profiles image: ",Database.get_attribute('alt'))
time.sleep(5)
print("")



Schedule = driver.find_element(By.XPATH,"//h2[normalize-space()='Streamline Staff Scheduling with Work Schedules']")
driver.execute_script("arguments[0].scrollIntoView(true);", Schedule)
print("Streamline Staff Scheduling with Work Schedules text: ",Schedule.get_attribute('innerHTML'))
time.sleep(5)


Schedule = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Streamline Staff Scheduling with Work Schedules')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Schedule)
print("Streamline Staff Scheduling with Work Schedules image: ",Schedule.get_attribute('alt'))
time.sleep(5)
print("")


Disciplinary = driver.find_element(By.XPATH,"//h2[normalize-space()='Disciplinary Tracking']")
driver.execute_script("arguments[0].scrollIntoView(true);", Disciplinary)
print("Disciplinary Tracking text: ",Disciplinary.get_attribute('innerHTML'))
time.sleep(5)


Disciplinary = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Disciplinary Tracking')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Disciplinary)
print("Disciplinary Tracking image: ",Disciplinary.get_attribute('alt'))
time.sleep(5)
print("")



Org = driver.find_element(By.XPATH,"//h2[normalize-space()='Organization Chart']")
driver.execute_script("arguments[0].scrollIntoView(true);", Org)
print("Organization Chart text: ",Org.get_attribute('innerHTML'))
time.sleep(5)


Org = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Org Chart')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Org)
print("Organization Chart image: ",Org.get_attribute('alt'))
time.sleep(5)
print("")



Directory = driver.find_element(By.XPATH,"//h2[normalize-space()='Corporate Directory']")
driver.execute_script("arguments[0].scrollIntoView(true);", Directory)
print("Corporate Directory text: ",Directory.get_attribute('innerHTML'))
time.sleep(5)


Directory = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Corporate Directory')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Directory)
print("Corporate Directory image: ",Directory.get_attribute('alt'))
time.sleep(5)
print("")



Document = driver.find_element(By.XPATH,"//h2[normalize-space()='Document Templates']")
driver.execute_script("arguments[0].scrollIntoView(true);", Document)
print("Document Templates text: ",Document.get_attribute('innerHTML'))
time.sleep(5)


Document = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Document Templates')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Document)
print("Document Templates image: ",Document.get_attribute('alt'))
time.sleep(5)
print("")



Buzz = driver.find_element(By.XPATH,"//h2[normalize-space()='Orange Buzz']")
driver.execute_script("arguments[0].scrollIntoView(true);", Buzz)
print("Orange Buzz text: ",Buzz.get_attribute('innerHTML'))
time.sleep(5)


Buzz = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Orange Buzz')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Buzz)
print("Orange Buzz image: ",Buzz.get_attribute('alt'))
time.sleep(5)
print("")



# Build your custom HR experience
Build = driver.find_element(By.XPATH,"//h3[normalize-space()='Build your custom HR experience.']")
driver.execute_script("arguments[0].scrollIntoView(true);", Build)
print("Build your custom HR experience text: ",Build.get_attribute('innerHTML'))
time.sleep(5)


# Build your custom HR experience Image
Build = driver.find_element(By.XPATH,"//img[@alt='artwork']")
driver.execute_script("arguments[0].scrollIntoView(true);", Build)
print("Build your custom HR experience image name: ",Build.get_attribute('alt'))
time.sleep(5)
print("")



# 30 Free Trial
Free = driver.find_element(By.XPATH,"//a[normalize-space()='30-Day Free Trial']")
driver.execute_script("arguments[0].scrollIntoView(true);", Free)
driver.execute_script("arguments[0].click();", Free)
print("30-Day Free Trial text: ",Free.get_attribute('innerHTML')) 
print("open free trial page")
time.sleep(5)
print("")



logo = driver.find_element(By.XPATH,"//img[@alt='OrangeHRM Logo']")
driver.execute_script("arguments[0].scrollIntoView(true);", logo)
driver.execute_script("arguments[0].click();", logo)
time.sleep(5)
print("")



# People management icons test
print("People management icons test")


HR = driver.find_element(By.XPATH,"//img[@alt='hr administration']")
driver.execute_script("arguments[0].scrollIntoView(true);", HR)
driver.execute_script("arguments[0].click();", HR)
print("hr administration image clicked: ",HR.get_attribute('alt'))
time.sleep(5)

driver.back()
print("clicked back")
time.sleep(5)



# HR Administration logo test
HR = driver.find_element(By.XPATH,"//p[normalize-space()='HR Administration']")
driver.execute_script("arguments[0].scrollIntoView(true);", HR)
driver.execute_script("arguments[0].click();", HR)
print("HR Administration logo text clicked: ",HR.get_attribute('innerHTML'))
time.sleep(5)

driver.back()
print("clicked back")
time.sleep(5)
print("")



# Employee managment logo test
Employee = driver.find_element(By.XPATH,"//img[@alt='Employee managment']")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
driver.execute_script("arguments[0].click();", Employee)
print("Employee managment logo image clicked: ",Employee.get_attribute('alt'))
time.sleep(5)

driver.back()
print("clicked back")
time.sleep(5)


Employee = driver.find_element(By.XPATH,"//p[normalize-space()='Employee Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
driver.execute_script("arguments[0].click();", Employee)
print("Employee Management logo text clicked: ",Employee.get_attribute('innerHTML'))
time.sleep(5)

driver.back()
print("clicked back")
time.sleep(5)
print("")   



# Reporting logo test
Reporting = driver.find_element(By.XPATH,"//img[@alt='Reporting']")
driver.execute_script("arguments[0].scrollIntoView(true);", Reporting)
driver.execute_script("arguments[0].click();", Reporting)
print("Reporting logo image clicked: ",Reporting.get_attribute('alt'))
time.sleep(5)

driver.back()
print("clicked back")
time.sleep(5)


Reporting = driver.find_element(By.XPATH,"//p[normalize-space()='Reporting']")
driver.execute_script("arguments[0].scrollIntoView(true);", Reporting)
driver.execute_script("arguments[0].click();", Reporting)
print("Reporting logo text clicked: ",Reporting.get_attribute('innerHTML'))
time.sleep(5)

driver.back()
print("clicked back")
time.sleep(5)
print("")



# mobile app logo test
Mobile = driver.find_element(By.XPATH,"//img[@alt='Mobile App logo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Mobile)
driver.execute_script("arguments[0].click();", Mobile)
print("Mobile App logo image clicked: ",Mobile.get_attribute('alt'))
time.sleep(10)



logo = driver.find_element(By.XPATH,"//a[@class='navbar-brand nav-logo']")
driver.execute_script("arguments[0].scrollIntoView(true);", logo)
driver.execute_script("arguments[0].click();", logo)
time.sleep(5)


 
Mobile = driver.find_element(By.XPATH,"//p[normalize-space()='Mobile App']")
driver.execute_script("arguments[0].scrollIntoView(true);", Mobile)
driver.execute_script("arguments[0].click();", Mobile)
print("Mobile App logo text clicked: ",Mobile.get_attribute('innerHTML'))
time.sleep(10)
print("")
print("")




# Mobile App page test 
print("Mobile App page open")


Mobile = driver.find_element(By.XPATH,"//h1[normalize-space()='OrangeHRM Mobile App']")
driver.execute_script("arguments[0].scrollIntoView(true);", Mobile)
print("Mobile App title: ",Mobile.get_attribute('innerHTML'))
time.sleep(5)


# <input type="//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']" 
Demo = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
print("Get a Demo button: ",Demo.get_attribute('innerHTML'))
time.sleep(5)


# open mobile page 
driver.get("https://www.orangehrm.com/en/solutions/people-management/orangehrm-mobile-app")



Mobile = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", Mobile)
print("Mobile App description: ",Mobile.get_attribute('innerHTML'))
time.sleep(5)


# Demo 2nd button
Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
print("Get a Demo button: ",Demo.get_attribute('innerHTML'))
time.sleep(5)
print("")


# open mobile page 
driver.get("https://www.orangehrm.com/en/solutions/people-management/orangehrm-mobile-app")



# Mobile App Youtube Video
iframe = driver.find_element(By.XPATH,"//div[@class='row']//div//iframe")
driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
driver.execute_script("arguments[0].click();", iframe)
print("Mobile App Youtube Video clicked: ",iframe.get_attribute('src'))
time.sleep(5)
print("")



# Mobile App google play store
iframe = driver.find_element(By.XPATH,"//a[@href='https://play.google.com/store/apps/details?id=com.orangehrm.enterprise']")
driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
driver.execute_script("arguments[0].click();", iframe)
print("Mobile App google play store clicked: ",iframe.get_attribute('href'))
time.sleep(5)


# back to mobile app page
get = driver.get("https://www.orangehrm.com/en/solutions/people-management/orangehrm-mobile-app")
print("Back to Mobile App page")
print("")



# Mobile app ios
ios = driver.find_element(By.XPATH,"//img[@alt='ios']")
driver.execute_script("arguments[0].scrollIntoView(true);", ios)
driver.execute_script("arguments[0].click();", ios)
print("Mobile app ios image clicked: ",ios.get_attribute('alt'))
time.sleep(5)


# back to mobile app page
get = driver.get("https://www.orangehrm.com/en/solutions/people-management/orangehrm-mobile-app")
print("Back to Mobile App page")
print("")



# Mobile App Dashboard 
Dashboard = driver.find_element(By.XPATH,"//h2[normalize-space()='Dashboard']")
driver.execute_script("arguments[0].scrollIntoView(true);", Dashboard)
print("Dashboard text: ",Dashboard.get_attribute('innerHTML'))
time.sleep(5)


Dashboard = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Dashboard')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Dashboard)
driver.execute_script("arguments[0].click();", Dashboard)
print("Dashboard image clicked: ",Dashboard.get_attribute('alt'))
time.sleep(5)
print("")



# Employee
Employee = driver.find_element(By.XPATH,"//h2[normalize-space()='Employee Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
print("Employee Management text: ",Employee.get_attribute('innerHTML'))
time.sleep(5)


Employee = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Employee Management')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
driver.execute_script("arguments[0].click();", Employee)
print("Employee Management image clicked: ",Employee.get_attribute('alt'))
time.sleep(5)
print("")



# Leave
Leave = driver.find_element(By.XPATH,"//h2[normalize-space()='Leave Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Leave)
print("Leave Management text: ",Leave.get_attribute('innerHTML'))
time.sleep(5)


Employee = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Employee Management')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Employee)
driver.execute_script("arguments[0].click();", Employee)
print("Employee Management image clicked: ",Employee.get_attribute('alt'))
time.sleep(5)
print("")



# Time Tracking
Time = driver.find_element(By.XPATH,"//h2[normalize-space()='Time Tracking']")
driver.execute_script("arguments[0].scrollIntoView(true);", Time)
print("Time Tracking text: ",Time.get_attribute('innerHTML'))
time.sleep(5)


Time = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Time Tracking')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Time)
driver.execute_script("arguments[0].click();", Time)
print("Time Tracking image clicked: ",Time.get_attribute('alt'))
time.sleep(5)
print("")



# Performance
Performance = driver.find_element(By.XPATH,"//h2[normalize-space()='Performance']")
driver.execute_script("arguments[0].scrollIntoView(true);", Performance)
print("Performance text: ",Performance.get_attribute('innerHTML'))
time.sleep(5)


Performance = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Performance Management')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Performance)
driver.execute_script("arguments[0].click();", Performance)
print("Performance Management image clicked: ",Performance.get_attribute('alt'))
print("")



# Enhanced Security
Enhanced = driver.find_element(By.XPATH,"//h2[normalize-space()='Enhanced Security']")
driver.execute_script("arguments[0].scrollIntoView(true);", Enhanced)
print("Enhanced Security text: ",Enhanced.get_attribute('innerHTML'))
time.sleep(5)


Password = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Password Reset')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Password)
driver.execute_script("arguments[0].click();", Password)
print("Password Reset image clicked: ",Password.get_attribute('alt'))
time.sleep(5)
print("")


# Go back to home page
get = driver.get("https://www.orangehrm.com/en")
print("Go back to home page")
time.sleep(5)
print("")




# Culture Managemnent Section
print("Culture Managemnent Section")


# Culture Text
Culture = driver.find_element(By.XPATH,"//h2[normalize-space()='Culture']")
driver.execute_script("arguments[0].scrollIntoView(true);", Culture)
print("Culture text: ",Culture.get_attribute('innerHTML'))
time.sleep(5)


# Learn More
Learn = driver.find_element(By.XPATH,"//a[@href='/en/solutions/culture/performance-management']//div[@class='link-text']//h6[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More text: ",Learn.get_attribute('innerHTML'))
time.sleep(5)


# go back 
driver.back()


# Culture Learn more icon
Learn = driver.find_element(By.XPATH,"//a[@href='/en/solutions/culture/performance-management']//div[@class='link-icon']")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More icon clicked: ",Learn.get_attribute('innerHTML'))
print("Performance Management page opened after clicking culture learn more icon")
time.sleep(5)
print("")
print("")



# Performance Management page test
print("Performance Management page test")


# Performance Management title
Performance = driver.find_element(By.XPATH,"//h1[normalize-space()='Performance Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Performance)
print("Performance Management title: ",Performance.get_attribute('innerHTML'))
time.sleep(5)


# Performance Management description
Performance = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", Performance)
print("Performance Management description: ",Performance.get_attribute('innerHTML'))
time.sleep(5)


# Book a Free Demo
Book = driver.find_element(By.XPATH,"//div[contains(@class,'platform-main-description')]//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Book)
driver.execute_script("arguments[0].click();", Book)
print("Book a Free Demo text: ",Book.get_attribute('innerHTML'))
time.sleep(5)


# go back
driver.back()


# 360° Employee Reviews
text360 = driver.find_element(By.XPATH,"//h2[normalize-space()='360° Employee Reviews']")
driver.execute_script("arguments[0].scrollIntoView(true);", text360)
print("360° Employee Reviews text: ",text360.get_attribute('innerHTML'))
time.sleep(5)


text360 = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'360 Employee Reviews')]")
driver.execute_script("arguments[0].scrollIntoView(true);", text360)
driver.execute_script("arguments[0].click();", text360)
print("360° Employee Reviews image clicked: ",text360.get_attribute('alt'))
time.sleep(5)


text360 = driver.find_element(By.XPATH,"//p[contains(text(),'Whether you are setting up Performance Reviews year')]")
driver.execute_script("arguments[0].scrollIntoView(true);", text360)
print("Whether you are setting up Performance Reviews year text: ",text360.get_attribute('innerHTML'))
time.sleep(5)


# check Whether you are setting text 
text = text360.text
if "Whether you are setting up Performance Reviews year" in text:
    print("✔ Correct text found: Whether you are setting up Performance Reviews year text Correct")
else:
    print("✖ Wrong text not found")
time.sleep(5)
print("")



Goal = driver.find_element(By.XPATH,"//h2[normalize-space()='Goal Tracking']")
driver.execute_script("arguments[0].scrollIntoView(true);", Goal)
print("Goal Tracking text: ",Goal.get_attribute('innerHTML'))
time.sleep(5)


Goal = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Goal Tracking')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Goal)
driver.execute_script("arguments[0].click();", Goal)
print("Goal Tracking image clicked: ",Goal.get_attribute('alt'))
time.sleep(5)
print("")



Custom = driver.find_element(By.XPATH,"//h2[normalize-space()='Custom Review Questions']")
driver.execute_script("arguments[0].scrollIntoView(true);", Custom)
print("Custom Review Questions text: ",Custom.get_attribute('innerHTML'))
time.sleep(5)


Custom = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Custom Review Questions')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Custom)
driver.execute_script("arguments[0].click();", Custom)
print("Custom Review Questions image clicked: ",Custom.get_attribute('alt'))
time.sleep(5)
print("")



Performance = driver.find_element(By.XPATH,"//h2[normalize-space()='Electronic Performance Sign-off']")
driver.execute_script("arguments[0].scrollIntoView(true);", Performance)
print("Electronic Performance Sign-off text: ",Performance.get_attribute('innerHTML'))
time.sleep(5)


Performance = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Electronic Performance Sign off')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Performance)
driver.execute_script("arguments[0].click();", Performance)
print("Electronic Performance Sign-off image clicked: ",Performance.get_attribute('alt'))
time.sleep(5)
print("")
print("")




# Career Developemet section
print("Career Developemet")


Career = driver.find_element(By.XPATH,"//img[@alt='Career Developemet']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
print("Career Developemet image name: ",Career.get_attribute('alt'))
time.sleep(5)


Career = driver.find_element(By.XPATH,"//h4[normalize-space()='Career Development']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
print("Career Development text: ",Career.get_attribute('innerHTML'))
time.sleep(5)



# Learn More
Learn = driver.find_element(By.XPATH,"//a[contains(@href,'/en/solutions/culture/career-development')]//div[contains(@class,'link-text')]//p[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More text: ",Learn.get_attribute('innerHTML'))
time.sleep(5)


# go back
driver.back()
time.sleep(5)


# Learn more icon
Learn = driver.find_element(By.XPATH,"//a[contains(@href,'/en/solutions/culture/career-development')]//div[contains(@class,'link-icon')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More icon clicked: ")
print("Career Development page opened after clicking learn more icon")
time.sleep(5)
print("")
print("")




# Career Development page test
print("Career Development page open")



Career = driver.find_element(By.XPATH,"//h1[normalize-space()='Career Development']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
print("Career Development text: ",Career.get_attribute('innerHTML'))
time.sleep(5)


Career = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
Career_description = Career.get_attribute('innerHTML')
time.sleep(5)
print("")


# check decription
if Career_description == "Employees want to feel empowered by their employer. If an employee feels like their manager and the HR team are investing into their future, the employee’s loyalty will grow. Stop losing your top talent to other companies because your employees don’t see a career path developing.":
    print("✔ Correct description found")
else:
    print("✖ Wrong description not found")
time.sleep(5)
print("")


# 9 Box Matrix
Career = driver.find_element(By.XPATH,"//h2[normalize-space()='9 Box Matrix']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
print("9 Box Matrix text: ",Career.get_attribute('innerHTML'))
time.sleep(5)


Career = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'9 Box Matrix')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
driver.execute_script("arguments[0].click();", Career)
print("9 Box Matrix image clicked: ",Career.get_attribute('alt'))
time.sleep(5)
print("")



# Individual Development Plan
Career = driver.find_element(By.XPATH,"//h2[normalize-space()='Individual Development Plan (IDP)']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
print("Individual Development Plan (IDP) text: ",Career.get_attribute('innerHTML'))
time.sleep(5)


Career = driver.find_element(By.XPATH,"//div[@role='button']//img[@alt='Individual Development Plan IDP']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
driver.execute_script("arguments[0].click();", Career)
print("Individual Development Plan (IDP) image clicked: ",Career.get_attribute('alt'))
time.sleep(5)
print("")



# Training LMS Logo 
Training = driver.find_element(By.XPATH,"//img[@alt='Traning']")
driver.execute_script("arguments[0].scrollIntoView(true);", Training)
print("Traning LMS logo image: ",Training.get_attribute('alt'))
time.sleep(5)


Training = driver.find_element(By.XPATH,"//h4[normalize-space()='Training (LMS)']")
driver.execute_script("arguments[0].scrollIntoView(true);", Training)
print("Training (LMS) logo text: ",Training.get_attribute('innerHTML'))
print("")


# Training (LMS) learn more
Learn = driver.find_element(By.XPATH,"//a[@href='/en/solutions/culture/training']//div[@class='link-text']//p[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More text: ",Learn.get_attribute('innerHTML'))
time.sleep(5)


driver.back()


Learn = driver.find_element(By.XPATH,"//a[@href='/en/solutions/culture/training']//div[@class='link-icon']//img")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More icon clicked: ")
print("Training (LMS) page opened after clicking learn more icon")
time.sleep(5)
print("")
print("")




# Training (LMS) page test
print("Training (LMS) page test")


# Training (LMS) title
Training = driver.find_element(By.XPATH,"//h1[normalize-space()='Training']")
driver.execute_script("arguments[0].scrollIntoView(true);", Training)
print("Training (LMS) title: ",Training.get_attribute('innerHTML'))
time.sleep(5)


# Demo 
Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
driver.execute_script("arguments[0].click();", Demo)
print("Book a Free Demo text: ",Demo.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/culture/training")


Training = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", Training)
Training_description = Training.get_attribute('innerHTML')
time.sleep(5)
print("")

if Training_description == "Welcome to the OrangeHRM Online Training (OTM) module, a comprehensive solution designed to streamline your employee training efforts. With OTM, your organization can create and manage individual or group courses, providing your employees with access to valuable training materials from anywhere, at any time.":
    print("Training (LMS) description: ",Training_description)
else:
    print("Training (LMS) description not found")
time.sleep(5)
print("")


# Flexible Course Creation and Delivery
Training = driver.find_element(By.XPATH,"//h2[normalize-space()='Flexible Course Creation and Delivery']")
driver.execute_script("arguments[0].scrollIntoView(true);", Training)
print("Flexible Course Creation and Delivery text: ",Training.get_attribute('innerHTML'))
time.sleep(5)


Flexible = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Flexible Course Creation and Delivery.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Flexible)
driver.execute_script("arguments[0].click();", Flexible)
print("Flexible Course Creation and Delivery image clicked: ",Flexible.get_attribute('alt'))
time.sleep(4)
print("")



# Anytime, Anywhere Access
Anytime = driver.find_element(By.XPATH,"//h2[normalize-space()='Anytime, Anywhere Access']")
driver.execute_script("arguments[0].scrollIntoView(true);", Anytime)
print("Anytime, Anywhere Access text: ",Anytime.get_attribute('innerHTML'))
time.sleep(5)


Anytime = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Anytime Anywhere Access.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Anytime)
driver.execute_script("arguments[0].click();", Anytime)
print("Anytime, Anywhere Access image clicked: ",Anytime.get_attribute('alt'))
time.sleep(4)
print("")



Course = driver.find_element(By.XPATH,"//h2[normalize-space()='Course Completion Reminders']")
driver.execute_script("arguments[0].scrollIntoView(true);", Course)
print("Course Completion Reminders text: ",Course.get_attribute('innerHTML'))
time.sleep(5)


Course = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Course Completion Reminders.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Course)
driver.execute_script("arguments[0].click();", Course)
print("Course Completion Reminders image clicked: ",Course.get_attribute('alt'))
time.sleep(4)
print("")



Certificates = driver.find_element(By.XPATH,"//h2[normalize-space()='E-Certificates for Course Completion']")
driver.execute_script("arguments[0].scrollIntoView(true);", Certificates)
print("E-Certificates for Course Completion text: ",Certificates.get_attribute('innerHTML'))
time.sleep(5)


Certificates = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'E Certificates for Course Completion.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Certificates)
driver.execute_script("arguments[0].click();", Certificates)
print("E-Certificates for Course Completion image clicked: ",Certificates.get_attribute('alt'))
time.sleep(4)
print("")



# Course Coordinators
Course = driver.find_element(By.XPATH,"//h2[normalize-space()='Centralize Course Management, Simplify Delivery']")
driver.execute_script("arguments[0].scrollIntoView(true);", Course)
print("Centralize Course Management, Simplify Delivery text: ",Course.get_attribute('innerHTML'))
time.sleep(5)


Course = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Course Coordinators')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Course)
driver.execute_script("arguments[0].click();", Course)
print("Course Coordinators image clicked: ",Course.get_attribute('alt'))
time.sleep(4)
print("")



Centralize = driver.find_element(By.XPATH,"//h2[normalize-space()='Centralize Course Management, Simplify Delivery']")
driver.execute_script("arguments[0].scrollIntoView(true);", Centralize)
print("Centralize Course Management, Simplify Delivery text: ",Centralize.get_attribute('innerHTML'))
time.sleep(5)


Centralize = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Course Coordinators')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Centralize)
driver.execute_script("arguments[0].click();", Centralize)
print("Course Coordinators image clicked: ",Centralize.get_attribute('alt'))
time.sleep(4)
print("")
print("")


# Go back to home page
get = driver.get("https://www.orangehrm.com/en")
time.sleep(10)




# Home page Culture icons
print("Home page Culture icons test")
print("")


# performance
Performance = driver.find_element(By.XPATH,"//img[@alt='performance 1']")
driver.execute_script("arguments[0].scrollIntoView(true);", Performance)
print("performance icon image: ",Performance.get_attribute('alt'))
time.sleep(5)

get = driver.get("https://www.orangehrm.com/en")


Performance = driver.find_element(By.XPATH,"//p[normalize-space()='Performance']")
driver.execute_script("arguments[0].scrollIntoView(true);", Performance)
print("Performance icon text clicked: ",Performance.get_attribute('innerHTML'))
time.sleep(5)

get = driver.get("https://www.orangehrm.com/en")


Career = driver.find_element(By.XPATH,"//img[@alt='Career Developemet']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
print("Career Developemet icon clicked: ",Career.get_attribute('alt'))
time.sleep(5)

get = driver.get("https://www.orangehrm.com/en")


Career = driver.find_element(By.XPATH,"//p[normalize-space()='Career Development']")
driver.execute_script("arguments[0].scrollIntoView(true);", Career)
print("Career Development icon text clicked: ",Career.get_attribute('innerHTML'))
time.sleep(5)

get = driver.get("https://www.orangehrm.com/en")



Training = driver.find_element(By.XPATH,"//img[@alt='Traning']")
driver.execute_script("arguments[0].scrollIntoView(true);", Training)
print("Traning icon text clicked: ",Training.get_attribute('alt'))
time.sleep(5)

get = driver.get("https://www.orangehrm.com/en")


Training = driver.find_element(By.XPATH,"//img[@alt='Traning']")
driver.execute_script("arguments[0].scrollIntoView(true);", Training)
print("Traning icon text clicked: ",Training.get_attribute('alt'))
time.sleep(5)

get = driver.get("https://www.orangehrm.com/en")
print("")




# Talent Management Section
print("Talent Management Section test")
print("")


Talent = driver.find_element(By.XPATH,"//h2[normalize-space()='Talent Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Talent)
print("Talent Management text: ",Talent.get_attribute('innerHTML'))
time.sleep(5)


Talent = driver.find_element(By.XPATH,"//p[contains(text(),'s royal jewels, then the recruiting team is the gu')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Talent)
print("Talent Management text: ",Talent.get_attribute('innerHTML'))
time.sleep(5)


Talent = driver.find_element(By.XPATH,"//img[@alt='Talent Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Talent)
print("Talent Management image clicked: ",Talent.get_attribute('alt'))
time.sleep(5)



Learn = driver.find_element(By.XPATH,"//a[@href='/en/solutions/talent-management/recruitment']//div[@class='link-text']//h6[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More text: ",Learn.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com")


Learn = driver.find_element(By.XPATH,"//a[@href='/en/solutions/talent-management/recruitment']//div[@class='link-icon']")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More icon: ",Learn.get_attribute('innerHTML'))
print("Recruitment page opened after clicking learn more icon")
time.sleep(5)
print("")
print("")




# Requirements page
print("Requirements page test")


Recruitment = driver.find_element(By.XPATH,"//h1[normalize-space()='Recruitment (ATS)']")
driver.execute_script("arguments[0].scrollIntoView(true);", Recruitment)
print("Recruitment (ATS) title: ",Recruitment.get_attribute('innerHTML'))
time.sleep(5)


Book = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Book)
driver.execute_script("arguments[0].click();", Book)
print("Book a Free Demo button clicked: ",Book.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/talent-management/recruitment")


desc = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", desc)
print("Recruitment (ATS) description: ",desc.get_attribute('innerHTML'))
time.sleep(5)
print("")


demo2 = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", demo2)
driver.execute_script("arguments[0].click();", demo2)
print("Book a Free Demo 2nd button clicked: ",demo2.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/talent-management/recruitment")


Job = driver.find_element(By.XPATH,"//h2[normalize-space()='Job Posting']")
driver.execute_script("arguments[0].scrollIntoView(true);", Job)
print("Job Posting text: ",Job.get_attribute('innerHTML'))
time.sleep(5)


Job = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Job Posting')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Job)
print("Job Posting icon: ",Job.get_attribute('alt'))
time.sleep(5)
print("")


# integration
Job = driver.find_element(By.XPATH,"//h2[normalize-space()='Integrate System with Company Website']")
driver.execute_script("arguments[0].scrollIntoView(true);", Job)
print("Integrate System with Company Website text: ",Job.get_attribute('innerHTML'))
time.sleep(5)


Job = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Integrate System with Company Website')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Job)
print("Integrate System with Company Website icon: ",Job.get_attribute('alt'))
time.sleep(5)
print("")


# Signatures
Sign = driver.find_element(By.XPATH,"//h2[normalize-space()='Signatures Made Simple']")
driver.execute_script("arguments[0].scrollIntoView(true);", Sign)
print("Signatures Made Simple text: ",Sign.get_attribute('innerHTML'))
time.sleep(5)


Sign = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Newsletter Esignature')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Sign)
print("Newsletter Esignature icon: ",Sign.get_attribute('alt'))
time.sleep(5)
print("")


# Customization
Custom = driver.find_element(By.XPATH,"//h2[normalize-space()='Customizable Application Forms & Questions']")
driver.execute_script("arguments[0].scrollIntoView(true);", Custom)
print("Customizable Application Forms & Questions text: ",Custom.get_attribute('innerHTML'))
time.sleep(5)


Custom = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Questions')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Custom)
driver.execute_script("arguments[0].click();", Custom)
print("Customization image clicked: ",Custom.get_attribute('alt'))
time.sleep(5)
print("")



# Interview
Inter = driver.find_element(By.XPATH,"//h2[normalize-space()='Interview Assistant Automation']")
driver.execute_script("arguments[0].scrollIntoView(true);", Inter)
print("Interview Assistant Automation text: ",Inter.get_attribute('innerHTML'))
time.sleep(5)


Inter = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Interactions')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Inter)
driver.execute_script("arguments[0].click();", Inter)
print("Interview image clicked: ",Inter.get_attribute('alt'))
time.sleep(5)




Check = driver.find_element(By.XPATH,"//h4[contains(text(),'Check out what else you can do with Talent Management')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Check)
print("Check out what else you can do with Talent Management text: ",Check.get_attribute('innerHTML'))
time.sleep(5)
print("")



# Onboarding
On = driver.find_element(By.XPATH,"//img[@alt='onboarding']")
driver.execute_script("arguments[0].scrollIntoView(true);", On)
print("Onboarding icon name: ",On.get_attribute('alt'))
time.sleep(5)


On = driver.find_element(By.XPATH,"//h4[normalize-space()='Onboarding']")
driver.execute_script("arguments[0].scrollIntoView(true);", On)
print("Onboarding text: ",On.get_attribute('innerHTML'))
time.sleep(5)
print("")



Learn = driver.find_element(By.XPATH,"//p[normalize-space()='Learn More']")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
driver.execute_script("arguments[0].click();", Learn)
print("Learn More text clicked: ",Learn.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/talent-management/recruitment")


Arrow = driver.find_element(By.XPATH,"//img[@src='/public/_resources/themes/orangehrm/dist/images/arrow.svg']")
driver.execute_script("arguments[0].scrollIntoView(true);", Arrow)
driver.execute_script("arguments[0].click();", Arrow)
print(" Learn More arrow clicked: ",Arrow.get_attribute('src'))
print("Employee Management page open again")
time.sleep(5)

driver.get("https://www.orangehrm.com")
print("Go back to home page")
time.sleep(5)
print("")




# talent management icons in home page
print("talent management icons in home page test")


Rec = driver.find_element(By.XPATH,"//img[@alt='Recruitment']")
driver.execute_script("arguments[0].scrollIntoView(true);", Rec)
print("Recruitment icon name: ",Rec.get_attribute('alt'))
time.sleep(5)

driver.get("https://www.orangehrm.com")


Rec = driver.find_element(By.XPATH,"//p[normalize-space()='Recruitment (ATS)']")
driver.execute_script("arguments[0].scrollIntoView(true);", Rec)
print("Recruitment (ATS) text: ",Rec.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com")


On = driver.find_element(By.XPATH,"//img[@alt='onboarding']")
driver.execute_script("arguments[0].scrollIntoView(true);", On)
print("Onboarding icon name: ",On.get_attribute('alt'))
time.sleep(5)

driver.get("https://www.orangehrm.com")


On = driver.find_element(By.XPATH,"//p[normalize-space()='Onboarding']")
driver.execute_script("arguments[0].scrollIntoView(true);", On)
print("Onboarding text: ",On.get_attribute('innerHTML'))
time.sleep(5)
print("")
print("")   




# Onboarding page
print("Onboarding page test")


On = driver.find_element(By.XPATH,"//h1[normalize-space()='Onboarding']")
driver.execute_script("arguments[0].scrollIntoView(true);", On)
print("Onboarding text: ",On.get_attribute('innerHTML'))
time.sleep(5)


Demo = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
print("Get a Demo button clicked: ",Demo.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/talent-management/onboarding")


desc = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", desc)
print("Description text: ",desc.get_attribute('innerHTML'))
time.sleep(5)


Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
print("Get a Demo button clicked: ",Demo.get_attribute('innerHTML'))
time.sleep(5)


Pre = driver.find_element(By.XPATH,"//h2[normalize-space()='Preboarding Made Simple']")
driver.execute_script("arguments[0].scrollIntoView(true);", Pre)
print("Preboarding Made Simple text: ",Pre.get_attribute('innerHTML'))
time.sleep(5)


Pre = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Consent Form')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Pre)
print("Consent Form icon name: ",Pre.get_attribute('alt'))
time.sleep(5)



Stream = driver.find_element(By.XPATH,"//h2[contains(text(),'Streamline Onboarding and Offboarding with Templates')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Stream)
print("Streamline Onboarding and Offboarding with Templates text: ",Stream.get_attribute('innerHTML'))
time.sleep(5)


Stream = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Streamline Onboarding and Offboarding with Templates.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Stream)
print("Streamline Onboarding and Offboarding with Templates image: ",Stream.get_attribute('alt'))
time.sleep(5)



Manage = driver.find_element(By.XPATH,"//h2[normalize-space()='Manage Any Type of Task with Ease']")
driver.execute_script("arguments[0].scrollIntoView(true);", Manage)
print("Manage Any Type of Task with Ease text: ",Manage.get_attribute('innerHTML'))
time.sleep(5)


Manage = driver.find_element(By.XPATH,"//h2[normalize-space()='Manage Any Type of Task with Ease']")
driver.execute_script("arguments[0].scrollIntoView(true);", Manage)
print("Manage Any Type of Task with Ease text: ",Manage.get_attribute('innerHTML'))
time.sleep(5)



Monitor = driver.find_element(By.XPATH,"//h2[normalize-space()='Monitor Progress at a Glance']")
driver.execute_script("arguments[0].scrollIntoView(true);", Monitor)
print("Monitor Progress at a Glance text: ",Monitor.get_attribute('innerHTML'))
time.sleep(5)


Monitor = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Monitor Progress at a Glance.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Monitor)
print("Monitor Progress at a Glance image: ",Monitor.get_attribute('alt'))
time.sleep(5)



Auto = driver.find_element(By.XPATH,"//h2[normalize-space()='Automate Onboarding and Offboarding Events']")
driver.execute_script("arguments[0].scrollIntoView(true);", Auto)
print("Automate Onboarding and Offboarding Events text: ",Auto.get_attribute('innerHTML'))
time.sleep(5)


Auto = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Automate Onboarding and Offboarding Events.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Auto)
print("Automate Onboarding and Offboarding Events image: ",Auto.get_attribute('alt'))
time.sleep(5)


driver.get("https://www.orangehrm.com/en")
print("")




# Request desk icons in home page
print("Request desk icons in home page test")


Request = driver.find_element(By.XPATH,"//img[@alt='RequestDesk']")
driver.execute_script("arguments[0].scrollIntoView(true);", Request)
print("RequestDesk icon clicked: ",Request.get_attribute('alt'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en")


Request = driver.find_element(By.XPATH,"//p[normalize-space()='Request Desk']")
driver.execute_script("arguments[0].scrollIntoView(true);", Request)
print("Request Desk text clicked: ",Request.get_attribute('innerHTML'))
print("Request desk page open")
time.sleep(5)
print("")
print("")





# Request desk page 
print("Request desk page ")


# Title
title = driver.find_element(By.XPATH,"//h1[normalize-space()='Request Desk']")
driver.execute_script("arguments[0].scrollIntoView(true);", title)
print("Title text: ",title.get_attribute('innerHTML'))
time.sleep(5)


# Demo first
Demo = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
Demo.click()
time.sleep(5)

# open Request desk page
driver.get("https://www.orangehrm.com/en/solutions/value-added-services/request-desk")


descr = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", descr)
print("Description text: ",descr.get_attribute('innerHTML'))
time.sleep(5)


Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
Demo.click()
time.sleep(5)
print("")

driver.get("https://www.orangehrm.com/en/solutions/value-added-services/request-desk")


central = driver.find_element(By.XPATH,"//h2[contains(text(),'Centralized Platform for Request Tracking and Resolution')]")
driver.execute_script("arguments[0].scrollIntoView(true);", central)
print("Centralized Platform for Request Tracking and Resolution text: ",central.get_attribute('innerHTML'))
time.sleep(5)


central = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Centralized Platform for Request Tracking and Resolution.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", central)
print("Centralized Platform for Request Tracking and Resolution image: ",central.get_attribute('alt'))
time.sleep(5)
print("")



Manage = driver.find_element(By.XPATH,"//h2[normalize-space()='Manage Hiring Requisitions and Workflow Automation']")
driver.execute_script("arguments[0].scrollIntoView(true);", Manage)
print("Manage Hiring Requisitions and Workflow Automation text: ",Manage.get_attribute('innerHTML'))
time.sleep(5)


Manage = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Manage Hiring Requisitions and Workflow Automation.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Manage)
print("Manage Hiring Requisitions and Workflow Automation image: ",Manage.get_attribute('alt'))
time.sleep(5)
print("")



Self = driver.find_element(By.XPATH,"//h2[contains(text(),'Self-Resignation Request Management and Workflow Automation')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Self)
print("Self-Resignation Request Management and Workflow Automation text: ",Self.get_attribute('innerHTML'))
time.sleep(5)


Self = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Self Resignation Request Management and Workflow Automation.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Self)
print("Self Resignation Request Management and Workflow Automation image: ",Self.get_attribute('alt'))
time.sleep(5)
print("")



IT = driver.find_element(By.XPATH,"//h2[normalize-space()='IT-related Query Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", IT)
print("IT-related Query Management text: ",IT.get_attribute('innerHTML'))
time.sleep(5)


IT = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'IT related Query Management.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", IT)
print("IT related Query Management image: ",IT.get_attribute('alt'))
time.sleep(5)
print("")



HR = driver.find_element(By.XPATH,"//h2[normalize-space()='HR Department Request Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", HR)
print("HR Department Request Management text: ",HR.get_attribute('innerHTML'))
time.sleep(5)


HR = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'HR Department Request Management.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", HR)
print("HR Department Request Management image: ",HR.get_attribute('alt'))
time.sleep(5)
print("")


Request = driver.find_element(By.XPATH,"//h2[normalize-space()='Request Communication Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Request)
print("Request Communication Management text: ",Request.get_attribute('innerHTML'))
time.sleep(5)


Request = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Request Communication Management.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Request)
print("Request Communication Management image: ",Request.get_attribute('alt'))
time.sleep(5)
print("")



Workflow = driver.find_element(By.XPATH,"//h2[normalize-space()='Workflow Automation for Streamlined Operations']")
driver.execute_script("arguments[0].scrollIntoView(true);", Workflow)
print("Workflow Automation for Streamlined Operations text: ",Workflow.get_attribute('innerHTML'))
time.sleep(5)


Workflow = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Workflow Automation for Streamlined Operations.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Workflow)
print("Workflow Automation for Streamlined Operations image: ",Workflow.get_attribute('alt'))
time.sleep(5)
print("")



Analytics = driver.find_element(By.XPATH,"//h2[normalize-space()='Reporting and Analytics for Continuous Improvement']")
driver.execute_script("arguments[0].scrollIntoView(true);", Analytics)
print("Reporting and Analytics for Continuous Improvement text: ",Analytics.get_attribute('innerHTML'))
time.sleep(5)


Analytics = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Reporting and Analytics for Continuous Improvement.PNG')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Analytics)
print("Reporting and Analytics for Continuous Improvement image: ",Analytics.get_attribute('alt'))
time.sleep(5)
print("")



Simplify = driver.find_element(By.XPATH,"//h2[normalize-space()='Simplify Approvals, Enhance Efficiency']")
driver.execute_script("arguments[0].scrollIntoView(true);", Simplify)
print("Simplify Approvals, Enhance Efficiency text: ",Simplify.get_attribute('innerHTML'))
time.sleep(5)


Simplify = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Request Employee Details Change')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Simplify)
print("Request Employee Details Change image: ",Simplify.get_attribute('alt'))
time.sleep(5)
print("")



Streamlined = driver.find_element(By.XPATH,"//h2[normalize-space()='Streamlined Request Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", Streamlined)
print("Streamlined Request Management text: ",Streamlined.get_attribute('innerHTML'))
time.sleep(5)


Streamlined = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Streamlined Request Management')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Streamlined)
print("Streamlined Request Management image: ",Streamlined.get_attribute('alt'))
time.sleep(5)
print("")


Data = driver.find_element(By.XPATH,"//h2[normalize-space()='Improved Data Analysis']")
driver.execute_script("arguments[0].scrollIntoView(true);", Data)
print("Improved Data Analysis text: ",Data.get_attribute('innerHTML'))
time.sleep(5)



Data = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Improved Data Analysis')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Data)
print("Improved Data Analysis image: ",Data.get_attribute('alt'))
time.sleep(5)
print("")


# back to home page
get = driver.get("https://www.orangehrm.com/en")
print("Go back to home page")
time.sleep(10)
print("")




# Compensation section in home page
print("Compensation section in home page test")


Compensation = driver.find_element(By.XPATH,"//h2[normalize-space()='Compensation']")
driver.execute_script("arguments[0].scrollIntoView(true);", Compensation)
print("Compensation text: ",Compensation.get_attribute('innerHTML'))
time.sleep(5)


Compensation = driver.find_element(By.XPATH,"//p[contains(text(),'Remove the headaches of manually tracking PTO, fig')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Compensation)
print("Remove the headaches of manually tracking PTO, fig text: ",Compensation.get_attribute('innerHTML'))
time.sleep(5)


Compensation = driver.find_element(By.XPATH,"//img[@alt='Compensation']")
driver.execute_script("arguments[0].scrollIntoView(true);", Compensation)
print("Compensation image: ",Compensation.get_attribute('alt'))
time.sleep(5)


# compensation Learn more 
compensation = driver.find_element(By.XPATH,"//a[@href='/en/solutions/compensation/payroll-connector']//div[@class='link-text']//h6[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", compensation)
print("compensation Learn more text: ",compensation.get_attribute('innerHTML'))
time.sleep(5)


driver.get("https://www.orangehrm.com/en")


compensation = driver.find_element(By.XPATH,"//a[@href='/en/solutions/compensation/payroll-connector']//div[@class='link-icon']")
driver.execute_script("arguments[0].scrollIntoView(true);", compensation)
driver.execute_script("arguments[0].click();", compensation)
print("compensation Learn more icon: ",compensation.get_attribute('innerHTML'))
print("Payroll Connector page opened after clicking learn more icon")
time.sleep(5)
print("")
print("")   





# open Payroll Connector page
print("Payroll Connector page ")


Payroll = driver.find_element(By.XPATH,"//h1[normalize-space()='Payroll Connector']")
driver.execute_script("arguments[0].scrollIntoView(true);", Payroll)
print("Payroll Connector title: ",Payroll.get_attribute('innerHTML'))
time.sleep(5)


demo = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", demo)
driver.execute_script("arguments[0].click();", demo)
print("Book a Free Demo button: ",demo.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/compensation/payroll-connector")


desc = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", desc)
print("Payroll Connector description: ",desc.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en/solutions/compensation/payroll-connector")



demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", demo)
driver.execute_script("arguments[0].click();", demo)
print("Book a Free Demo button: ",demo.get_attribute('innerHTML'))
time.sleep(5)
print("")



Definitiv = driver.find_element(By.XPATH,"//h2[normalize-space()='Definitiv']")
driver.execute_script("arguments[0].scrollIntoView(true);", Definitiv)
print("Definitiv text: ",Definitiv.get_attribute('innerHTML'))
time.sleep(5)


Definitiv = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Definitiv')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Definitiv)
print("Definitiv image: ",Definitiv.get_attribute('alt'))
time.sleep(5)
print("")



hSenid = driver.find_element(By.XPATH,"//h2[normalize-space()='hSenid']")
driver.execute_script("arguments[0].scrollIntoView(true);", hSenid)
print("hSenid text: ",hSenid.get_attribute('innerHTML'))
time.sleep(5)


hSenid = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'hSenid')]")
driver.execute_script("arguments[0].scrollIntoView(true);", hSenid)
print("hSenid image: ",hSenid.get_attribute('alt'))
time.sleep(5)
print("")



InterCorp = driver.find_element(By.XPATH,"//h2[normalize-space()='InterCorp Solutions']")
driver.execute_script("arguments[0].scrollIntoView(true);", InterCorp)
print("InterCorp text: ",InterCorp.get_attribute('innerHTML'))
time.sleep(5)


InterCorp = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'InterCorp Solutions')]")
driver.execute_script("arguments[0].scrollIntoView(true);", InterCorp)
print("InterCorp image: ",InterCorp.get_attribute('alt'))
time.sleep(5)
print("")



MC = driver.find_element(By.XPATH,"//h2[normalize-space()='MC Systems']")
driver.execute_script("arguments[0].scrollIntoView(true);", MC)
print("MC text: ",MC.get_attribute('innerHTML'))
time.sleep(5)


MC = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'MC Systems')]")
driver.execute_script("arguments[0].scrollIntoView(true);", MC)
print("MC image: ",MC.get_attribute('alt'))
time.sleep(5)
print("")   



Nitso = driver.find_element(By.XPATH,"//h2[normalize-space()='Nitso']")
driver.execute_script("arguments[0].scrollIntoView(true);", Nitso)
print("Nitso text: ",Nitso.get_attribute('innerHTML'))
time.sleep(5)


Nitso = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Nitso')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Nitso)
print("Nitso image: ",Nitso.get_attribute('alt'))
time.sleep(5)
print("")



PayPros = driver.find_element(By.XPATH,"//h2[normalize-space()='PayPros']")
driver.execute_script("arguments[0].scrollIntoView(true);", PayPros)
print("PayPros text: ",PayPros.get_attribute('innerHTML'))
time.sleep(5)


PayPros = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'PayPros')]")
driver.execute_script("arguments[0].scrollIntoView(true);", PayPros)
print("PayPros image: ",PayPros.get_attribute('alt'))
time.sleep(5)
print("")



PTO = driver.find_element(By.XPATH,"//img[@alt='PTO leave mangement']")
driver.execute_script("arguments[0].scrollIntoView(true);", PTO)
print("PTO image name: ",PTO.get_attribute('alt'))
time.sleep(5)


PTO = driver.find_element(By.XPATH,"//h4[normalize-space()='PTO / Leave Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", PTO)
print("PTO text: ",PTO.get_attribute('innerHTML'))
time.sleep(5)



Learn = driver.find_element(By.XPATH,"//a[contains(@href,'/en/solutions/compensation/pto-leave-management')]//div[contains(@class,'link-text')]//p[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
print("Learn More text: ",Learn.get_attribute('innerHTML'))
time.sleep(5)


driver.get("https://www.orangehrm.com/en")


Learn = driver.find_element(By.XPATH,"//a[contains(@href,'/en/solutions/compensation/pto-leave-management')]//div[contains(@class,'link-icon')]//img")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
print("Learn More image: ",Learn.get_attribute('alt'))
time.sleep(5)
print("")





# open PTO leave mangement page
print("PTO leave mangement page open")



PTO = driver.find_element(By.XPATH,"//h1[normalize-space()='PTO / Leave Management']")
driver.execute_script("arguments[0].scrollIntoView(true);", PTO)
print("PTO text: ",PTO.get_attribute('innerHTML'))
time.sleep(5)


Book = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Book)
print("Book a Free Demo text: ",Book.get_attribute('innerHTML'))
time.sleep(5)


PTO = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", PTO)
print("PTO description: ",PTO.get_attribute('innerHTML'))
time.sleep(5)


Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
print("Demo text: ",Demo.get_attribute('innerHTML'))
time.sleep(5)


# Request
Request = driver.find_element(By.XPATH,"//h2[normalize-space()='Request / Approve Leave']")
driver.execute_script("arguments[0].scrollIntoView(true);", Request)
print("Request text: ",Request.get_attribute('innerHTML'))
time.sleep(5)


Request = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Request Apply Leave')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Request)
print("Request image: ",Request.get_attribute('alt'))
time.sleep(5)


# PTO
calendar = driver.find_element(By.XPATH,"//h2[normalize-space()='PTO Calendar']")
driver.execute_script("arguments[0].scrollIntoView(true);", calendar)
print("PTO text: ",calendar.get_attribute('innerHTML'))
time.sleep(5)


calendar = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'PTO Calendar')]")
driver.execute_script("arguments[0].scrollIntoView(true);", calendar)
print("PTO image: ",calendar.get_attribute('alt'))
time.sleep(5)


# Advanced Leave
Leave = driver.find_element(By.XPATH,"//h2[normalize-space()='Advanced Leave Configuration']")
driver.execute_script("arguments[0].scrollIntoView(true);", Leave)
print("Leave text: ",Leave.get_attribute('innerHTML'))
time.sleep(5)


Leave = driver.find_element(By.XPATH,"//h2[normalize-space()='Automated PTO Accrual']")
driver.execute_script("arguments[0].scrollIntoView(true);", Leave)
print("Leave text: ",Leave.get_attribute('innerHTML'))
time.sleep(5)


Leave = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Automated PTO Accrual')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Leave)
print("Leave image: ",Leave.get_attribute('alt'))
time.sleep(5)


# Time Tracking
Time = driver.find_element(By.XPATH,"//img[@alt='Time Tracking']")
driver.execute_script("arguments[0].scrollIntoView(true);", Time)
print("Time image name: ",Time.get_attribute('alt'))
time.sleep(5)


Time = driver.find_element(By.XPATH,"//h4[normalize-space()='Time Tracking']")
driver.execute_script("arguments[0].scrollIntoView(true);", Time)
print("Time text clicked open: ",Time.get_attribute('innerHTML'))
time.sleep(5)


Learn = driver.find_element(By.XPATH,"//a[contains(@href,'/en/solutions/compensation/time-tracking')]//div[contains(@class,'link-text')]//p[contains(text(),'Learn More')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
print("Learn More text clicked open: ",Learn.get_attribute('innerHTML'))
time.sleep(5)

driver.get("https://www.orangehrm.com/en")


Learn = driver.find_element(By.XPATH,"//a[contains(@href,'/en/solutions/compensation/time-tracking')]//div[contains(@class,'link-icon')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Learn)
print("Learn More image clicked open: ",Learn.get_attribute('innerHTML'))
time.sleep(5)
print("")
print("")





# open Time Tracking page
print("Time Tracking page open")


Time = driver.find_element(By.XPATH,"//h1[normalize-space()='Time Tracking']")
driver.execute_script("arguments[0].scrollIntoView(true);", Time)
print("Time title: ",Time.get_attribute('innerHTML'))
time.sleep(5)


Time = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']")
driver.execute_script("arguments[0].scrollIntoView(true);", Time)
print("Time page image: ",Time.get_attribute('innerHTML'))
time.sleep(5)


Demo = driver.find_element(By.XPATH,"//div[@class='platform-slider-content']//button[@class='btn btn-ohrm']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
print("Time page button: ",Demo.get_attribute('innerHTML'))
time.sleep(5)


Time = driver.find_element(By.XPATH,"//p[@class='platform-page-description text-center']")
driver.execute_script("arguments[0].scrollIntoView(true);", Time)
print("Time page description: ",Time.get_attribute('innerHTML'))
time.sleep(5)



Demo = driver.find_element(By.XPATH,"//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
driver.execute_script("arguments[0].scrollIntoView(true);", Demo)
driver.execute_script("arguments[0].click();", Demo)
print("Book a Free Demo button: ",Demo.get_attribute('innerHTML'))
time.sleep(5)


# Clock-In / Clock-Out
clock = driver.find_element(By.XPATH,"//h2[normalize-space()='Clock-In / Clock-Out']")
driver.execute_script("arguments[0].scrollIntoView(true);", clock)
print("Clock-In / Clock-Out text: ",clock.get_attribute('innerHTML'))
time.sleep(5)


clock = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Clock In Clock Out')]")
driver.execute_script("arguments[0].scrollIntoView(true);", clock)
print("Clock-In / Clock-Out image: ",clock.get_attribute('alt'))
time.sleep(5)


# pay
pay = driver.find_element(By.XPATH,"//h2[normalize-space()='Pay Policies and Overtime']")
driver.execute_script("arguments[0].scrollIntoView(true);", pay)
print("Pay Policies and Overtime text: ",pay.get_attribute('innerHTML'))
time.sleep(5)



pay = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Pay Policies and Overtime')]")
driver.execute_script("arguments[0].scrollIntoView(true);", pay)
print("Pay Policies and Overtime image: ",pay.get_attribute('alt'))
time.sleep(5)


# timesheet
timesheet = driver.find_element(By.XPATH,"//h2[normalize-space()='Timesheets']")
driver.execute_script("arguments[0].scrollIntoView(true);", timesheet)
print("Timesheets text: ",timesheet.get_attribute('innerHTML'))
time.sleep(5)


timesheet = driver.find_element(By.XPATH,"//div[contains(@role,'button')]//img[contains(@alt,'Timesheets')]")
driver.execute_script("arguments[0].scrollIntoView(true);", timesheet)
print("Timesheets image: ",timesheet.get_attribute('alt'))
time.sleep(5)


# Go back to home page
get = driver.get("https://www.orangehrm.com/en")
print("Go back to home page")
time.sleep(10)
print("")




# Build your custom HR experience Section
print("Build your custom HR experience Section test")


# Build your custom HR experience
Build = driver.find_element(By.XPATH,"//h3[normalize-space()='Build your custom HR experience.']")
driver.execute_script("arguments[0].scrollIntoView(true);", Build)
print("Build your custom HR experience text: ",Build.get_attribute('innerHTML'))
time.sleep(5)


# Leave request
leave = driver.find_element(By.XPATH,"//img[@alt='leave']")
driver.execute_script("arguments[0].scrollIntoView(true);", leave)
print("leave image name: ",leave.get_attribute('alt'))
time.sleep(5)


number = driver.find_element(By.XPATH,"//h2[normalize-space()='10M+']")
driver.execute_script("arguments[0].scrollIntoView(true);", number)
print("10M+ text: ",number.get_attribute('innerHTML'))
time.sleep(5)



# Active users
Users = driver.find_element(By.XPATH,"//img[@alt='Active users']")
driver.execute_script("arguments[0].scrollIntoView(true);", Users)
print("Active users image: ",Users.get_attribute('alt'))
time.sleep(5)


earth = driver.find_element(By.XPATH,"//img[@alt='earth']")
driver.execute_script("arguments[0].scrollIntoView(true);", earth)
print("earth image: ",earth.get_attribute('alt'))
time.sleep(5)


users = driver.find_element(By.XPATH,"//img[@alt='Active users v2']")
driver.execute_script("arguments[0].scrollIntoView(true);", users)
print("Active users v2 image: ",users.get_attribute('alt'))
time.sleep(5)





