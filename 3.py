from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://x.threatbook.cn/domain/360jq.com")
webEle=driver.find_element_by_css_selector("#domain_tab > li:nth-child(3) > a:nth-child(1)")
webEle.click()
webEle2=driver.find_element_css_selector("#permissions_table > tbody:nth-child(2)")
print webEle2.text
#time.sleep(5)
driver.quit()