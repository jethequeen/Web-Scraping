from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32com.client
import win32print
import os


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://app.print.avery.com/dpo8/app/target;name=US_en;ep=USP/product;profile=YouPrint;product=e4ff815be1e19643ef64f6e2c8b0758d/design;hideDesignCategories=false;source=OpenProject;product=e4ff815be1e19643ef64f6e2c8b0758d/customize;project=f8d600fe47a31f4255bedd82623eac1e/ctx;consumer=Avery/view?customize&')
time.sleep(5)
email = driver.find_element_by_name("signInEmail")
password = driver.find_element_by_id("sign-in-password")

email.send_keys("binobrick@gmail.com")
password.send_keys("zxzxws12")

driver.find_element_by_xpath('//*[@id="sign-in-btn"]').click()
time.sleep(10)

driver.find_element_by_xpath("""//*[@id="tool-panel-import-data-btn"]/div[1]""").click()
time.sleep(2)

driver.find_element_by_xpath("""//*[@id="data-tools-replace-spreadsheet"]""").click()
time.sleep(2)

file = driver.find_element_by_xpath("""//*[@id="import-data-from-pc-button"]""")
file.send_keys("K://Other computers//Ordi Jérémie//Documents//Magasin BrickLink//Scraping//Lettermail.csv")
time.sleep(1)

driver.find_element_by_css_selector("#mail-merge-check-first-row").click()
time.sleep(1)
driver.find_element_by_xpath("""//*[@id="next"]""").click()
time.sleep(1)
action = ActionChains(driver)
action.drag_and_drop(driver.find_element_by_css_selector("""#dpo8-mail-merge-list > div:nth-child(1)"""),
                     driver.find_element_by_css_selector("""#merge-editor-container > div""")).perform()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[6]/button[2]").click()

driver.find_element_by_xpath("""//*[@id="finish"]""").click()
time.sleep(5)

driver.find_element_by_css_selector("#dpo8-footer-next-btn").click()
time.sleep(1)
driver.find_element_by_css_selector("#print-options-control > div.section > div:nth-child(2) > button").click()
time.sleep(1)
driver.find_element_by_css_selector("#cancel-btn").click()
time.sleep(10)
driver.find_element_by_css_selector("#download-pdf-trigger").click()



# -------  Imprimer le fichier ------- #

current_printer = win32print.GetDefaultPrinter()
win32print.SetDefaultPrinter('Brother QL-1110NWB')
driver.get("C://Users//jerem//Downloads//Avery5292ShippingLabels.pdf")
time.sleep(1)
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('{ENTER}')
time.sleep(2)  # Adjust as necessary
shell.SendKeys('^p')
time.sleep(10)  # Adjust as necessary
shell.SendKeys('{ENTER}')  # dismiss the print dialog box
win32print.SetDefaultPrinter(current_printer)
time.sleep(10)
os.remove("C://Users//jerem//Downloads//Avery5292ShippingLabels.pdf")

os.remove("K://Other computers//Ordi Jérémie//Documents//Magasin BrickLink//Scraping//Lettermail.csv")

driver.close()
driver.quit()