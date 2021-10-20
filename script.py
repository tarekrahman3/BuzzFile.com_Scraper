import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from random import randint as rand
import os
import random
loc = ['Mountain', 'Ranch', 'Cub', 'Snow', 'Vice', 'Empire', 'Precedent', 'Dogg', 'Cobain', 'Expo 67',  'The 6', 'Granville', 'Vansterdam', 'Seine', 'Castle', 'Canal',  'Fjord', 'Alphorn', 'Crumpets', 'Custard', 'Ataturk', 'Victoria',]

urls=pd.read_csv('import.csv').links.tolist()

options = uc.ChromeOptions()
options.user_data_dir = "chrome_profile"
driver = uc.Chrome(options=options)

d =[]
try:
	for index, url in enumerate(urls):
		driver.get('https://'+url)
		time.sleep(rand(4,6))
		if 'Cloudflare' in driver.page_source:
			driver.delete_all_cookies()
	        time.sleep(2)
	        os.system(f"windscribe connect {loc[random.randrange(len(loc))]}")
	        time.sleep(5)
	        driver.get(url)
		try:
			businessname = driver.find_element_by_xpath('//span[@itemprop="name"]').text
		except:
			businessname = None
		try:
			name= driver.find_element_by_xpath('//span[@itemprop="employee"]').text
		except:
			name= None
		try:
			title = driver.find_element_by_xpath('//span[@itemprop="contactType"]').text
		except:
			title = None
		try:
			phone = driver.find_element_by_xpath('//span[@itemprop="telephone"]').text
		except:
			phone = None
		try:
			website = driver.find_element_by_xpath('//span[@itemprop="url"]').text
		except:
			website = None
		try:
			streetAddress= driver.find_element_by_xpath('//span[@itemprop="streetAddress"]').text
		except:
			streetAddress= None
		try:
			addressLocality= driver.find_element_by_xpath('//span[@itemprop="addressLocality"]').text
		except:
			addressLocality= None
		try:
			addressRegion= driver.find_element_by_xpath('//span[@itemprop="addressRegion"]').text
		except:
			addressRegion= None
		try:
			postalCode= driver.find_element_by_xpath('//span[@itemprop="postalCode"]').text
		except:
			postalCode= None
		data = {
		'url':url,
		'businessname':businessname
		'name':name,
		'title':title,
		'phone':phone,
		'website':website,
		'streetAddress':streetAddress,
		'addressLocality':addressLocality,
		'addressRegion':addressRegion,
		'postalCode':postalCode
		}
		print(f"{index} | {data['businessname']}")
		d.append(data)

except Exception as e:
    print(e)

finally:
	os.system('windscribe disconnect')
	pd.DataFrame(d).to_csv('export.csv')