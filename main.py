import time
import os
import selenium
from selenium.webdriver.common.by import By
driver = selenium.webdriver.Chrome(executable_path=r"C:\Users\anilt\PycharmProjects\python  API TEST\venv\chromedriver.exe")

#
# from selenium.webdriver.common.by import By
#
# driver = selenium.webdriver.Chrome()

driver.maximize_window()
driver.get("http://uat.devopsmcfinance.com/los")
time.sleep(10)

# User ID

driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div/form/div/input[1]").send_keys("M3084")

# Password

driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/form/div/input[2]').send_keys("M3084")

# click on Login Button

driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div/form/div/button").click()
time.sleep(10)
time.sleep(10)
# driver.save_screenshot("C:\\Users\\anilt\\Desktop\\Python\\Testing .. file  screenshots\\aug.png")
# time.sleep(5)
#
# # click on Leadmanagement
#
#
driver.find_element(By.XPATH, "/html/body/app-root/app-dashbaord/div/div[1]/div/app-side-menu/ul/li[2]/ul/li/a").click()
time.sleep(10)
#
# #For filter button click
#
# driver.find_element(By.CSS_SELECTOR,"#pr_id_18-table > thead > tr > th:nth-child(2) > div > p-columnfilter > div > button").click()
# time.sleep(10)
# #for seletion Done
#
# driver.find_element(By.XPATH,'/html/body/div/div[2]/div/p-columnfilterformelement/p-dropdown/div/span').click()
# time.sleep(10)
# #For Data selected
#
# driver.find_element(By.XPATH,'//*[@id="pr_id_23_list"]/p-dropdownitem[1]/li/span[1]').click()
# time.sleep(10)
# #for apply button
#
#
# driver.find_element(By.XPATH,'/html/body/div/div[4]/button[2]').click()
# time.sleep(10)
#

# for Next  Button



driver.find_element(By.CSS_SELECTOR,"#pr_id_3 > p-paginator > div > button.p-ripple.p-element.p-paginator-next.p-paginator-element.p-link").click()
time.sleep(10)

# for Eye Button

driver.find_element(By.XPATH, '//*[@id="pr_id_3-table"]/tbody/tr[3]/td[1]/button').click()
time.sleep(10)

driver.save_screenshot("C:\\Users\\anilt\Documents\Lightshot\\New folder\\agu.png")
time.sleep(10)


# for co-applicant

driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.grid.ng-star-inserted > div > button:nth-child(2) > span.p-button-label").click()
time.sleep(10)

# For exit button

driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
time.sleep(10)

# --------------------------------------------------

# for Next View Button

driver.find_element(By.CSS_SELECTOR,"#pr_id_3 > p-paginator > div > button.p-ripple.p-element.p-paginator-next.p-paginator-element.p-link").click()
time.sleep(10)

# for Eye Button

driver.find_element(By.XPATH, '//*[@id="pr_id_3-table"]/tbody/tr[3]/td[1]/button').click()
time.sleep(10)

# for co-applicant

driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.grid.ng-star-inserted > div > button:nth-child(2) > span.p-button-label").click()
time.sleep(10)

# For exit button

# driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
# time.sleep(5)


# For exit button

driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
time.sleep(10)









# for Next View Button

driver.find_element(By.CSS_SELECTOR,"#pr_id_3 > p-paginator > div > button.p-ripple.p-element.p-paginator-next.p-paginator-element.p-link").click()
time.sleep(10)



# for Eye Button

# driver.find_element(By.XPATH, '//*[@id="pr_id_3-table"]/tbody/tr[3]/td[1]/button').click()
# time.sleep(10)

# for co-applicant

driver.find_element(By.CSS_SELECTOR,"#pr_id_3-table > tbody > tr:nth-child(4) > td:nth-child(1) > button").click()
time.sleep(5)


# For exit button

# driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
# time.sleep(5)


# For exit button

#driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
#time.sleep(10)












# for Next View Button

# driver.find_element(By.CSS_SELECTOR,"#pr_id_3 > p-paginator > div > button.p-ripple.p-element.p-paginator-next.p-paginator-element.p-link").click()
# time.sleep(10)
#
# # for Eye Button
#
# driver.find_element(By.XPATH, '//*[@id="pr_id_3-table"]/tbody/tr[3]/td[1]/button').click()
# time.sleep(10)
#
# # for co-applicant
#
# driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.grid.ng-star-inserted > div > button:nth-child(2) > span.p-button-label").click()
# time.sleep(10)
#
# # For exit button
#
# # driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
# # time.sleep(5)
#
#
# # For exit button
#
# driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
# time.sleep(10)
#
#
#
#
#
#
#
# # for Next View Button
#
# driver.find_element(By.CSS_SELECTOR,"#pr_id_3 > p-paginator > div > button.p-ripple.p-element.p-paginator-next.p-paginator-element.p-link").click()
# time.sleep(10)
#
# # for Eye Button
#
# driver.find_element(By.XPATH, '//*[@id="pr_id_3-table"]/tbody/tr[3]/td[1]/button').click()
# time.sleep(10)
#
#
# # for co-applicant
#
# driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.grid.ng-star-inserted > div > button:nth-child(2) > span.p-button-label").click()
# time.sleep(10)
#
#
# # For exit button
#
# # driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
# # time.sleep(5)
#
#
# # For exit button
#
# driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > div.layout-main > div > app-lead-management-main > p-dialog > div > div > div.p-dialog-header.ng-tns-c54-7.ng-star-inserted > div.p-dialog-header-icons.ng-tns-c54-7 > button").click()
# time.sleep(10)
#
#
#
#
#
#
#
#
#
#
#
#
#
# # For Log out Button

driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > app-top-header > div > div > div.layout-topbar-right > ul > li > a").click()
time.sleep(10)

# For Log_out

driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashbaord > div > app-top-header > div > div > div.layout-topbar-right > ul > li > ul > li:nth-child(2) > a > h6").click()
time.sleep(10)

print("Test has been Passed")
time.sleep(10)


print(driver.title)



driver.quit()
