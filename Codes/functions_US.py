# Vinted functions

import os
import urllib
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import re
import sys
from datetime import datetime

global dict_order, dict_catalog, dict_size, dict_color, dict_brand, dict_condition
dict_order = dict({'relevance': '&order=relevance','decreasing price' : '&order=price_high_to_low',\
'increasing price' : '&order=price_low_to_high', 'most recent first' : '&order=newest_first'})
dict_catalog = dict({'men':'&catalog[]=5', 'women':'&catalog[]=1904', 'children': '&catalog[]=1193'})
dict_size = dict({'MenXS':'&size_id[]=206', 'MenS':'&size_id[]=207', 'MenM':'&size_id[]=208', 'MenL':'&size_id[]=209',\
'MenXL':'&size_id[]=210', 'MenXXL':'&size_id[]=211', 'MenXXXL':'&size_id[]=212', 'Men4XL':'&size_id[]=308',\
'Men5XL':'&size_id[]=309', 'Men6XL':'&size_id[]=1192', 'Men7XL':'&size_id[]=1193', 'Men8XL':'&size_id[]=1194',\
'Men38':'&size_id[]=776', 'Men39':'&size_id[]=778',\
'Men40':'&size_id[]=780', 'Men41':'&size_id[]=782', 'Men42':'&size_id[]=784',\
'Men42.5':'&size_id[]=785', 'Men43':'&size_id[]=786', 'Men43.5':'&size_id[]=787', 'Men44':'&size_id[]=788',\
'Men44.5':'&size_id[]=789', 'Men45':'&size_id[]=790', 'Men45.5':'&size_id[]=791', 'Men46':'&size_id[]=792',\
'Men47':'&size_id[]=794', 'Men48':'&size_id[]=1190', 'Men49':'&size_id[]=1191',\
'WomenXXXS':'&size_id[]=1226','WomenXXS':'&size_id[]=102',\
'WomenXS':'&size_id[]=2', 'WomenS':'&size_id[]=3', 'WomenM':'&size_id[]=4', 'WomenL':'&size_id[]=5',\
'WomenXL':'&size_id[]=6', 'WomenXXL':'&size_id[]=7', 'WomenXXXL':'&size_id[]=310', 'Women4XL':'&size_id[]=311',\
'Women5XL':'&size_id[]=312', 'Women6XL':'&size_id[]=1227', 'Women7XL':'&size_id[]=1228', 'Women8XL':'&size_id[]=1229',\

'Women35':'&size_id[]=55', 'Women35.5':'&size_id[]=1195',\
'Women36':'&size_id[]=56', 'Women36.5':'&size_id[]=1196', 'Women37':'&size_id[]=57',\
'Women37.5':'&size_id[]=1197', 'Women38':'&size_id[]=58', 'Women38.5':'&size_id[]=1198',\

'Women39':'&size_id[]=59', 'Women39.5':'&size_id[]=1199',\
'Women40':'&size_id[]=60', 'Women40.5':'&size_id[]=1200', 'Women41':'&size_id[]=61',\
'Women41.5':'&size_id[]=1201', 'Women42':'&size_id[]=62', 'Women43':'&size_id[]=62'})
dict_color = dict({'black':'&color_id[]=1', 'white':'&color_id[]=12', 'grey':'&color_id[]=3', \
'cream':'&color_id[]=20', 'beige':'&color_id[]=4', 'apricot':'&color_id[]=21', 'orange':'&color_id[]=11',\
'coral':'&color_id[]=22', 'red':'&color_id[]=7','burgundy':'&color_id[]=23','pink':'&color_id[]=5',\
'rose':'&color_id[]=24', 'purple':'&color_id[]=6', 'lila':'&color_id[]=25', 'light blue':'&color_id[]=26',\
'blue':'&color_id[]=9', 'navy blue':'&color_id[]=27', 'turquoise':'&color_id[]=17', 'mint':'&color_id[]=30',\
'green':'&color_id[]=10','dark green':'&color_id[]=28','khaki':'&color_id[]=16', 'brown':'&color_id[]=2',\
'mustard':'&color_id[]=29', 'yellow':'&color_id[]=8', 'silver':'&color_id[]=13', 'golden':'&color_id[]=14',\
'multicolor':'&color_id[]=15'})
dict_brand = dict({'nike':'&brand_id[]=13', 'adidas': '&brand_id[]=22', 'zara':'&brand_id[]=21', "levi's":'&brand_id[]=76',\
'h&m':'&brand_id[]=10', 'ralph lauren':'&brand_id[]=374', 'mango':'&brand_id[]=12', 'lacoste':'&brand_id[]=3595', \
'calvin klein':'&brand_id[]=28', 'tommy hilfiger': '&brand_id[]=355', 'guess':'&brand_id[]=31', 'michael kors':'&brand_id[]=457', \
'jordan':'&brand_id[]=227', 'puma':'&brand_id[]=526', 'balenciaga':'&brand_id[]=6411', 'vans':'&brand_id[]=116'})
dict_condition = dict({'new with tags':'&status[]=6', 'new without tags': '&status[]=1', 'very good condition': '&status[]=2', \
'good condition':'&status[]=3', 'satisfactory':'&status[]=4'})

#os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\Vinted\\Data")
global driver
options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--ignore-ssl-errors')
#options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
global DRIVER_LOCATION
DRIVER_LOCATION = "C:\\Users\\Sébastien CARARO\\Desktop\\chromedriver1.exe"

driver = webdriver.Chrome(executable_path = DRIVER_LOCATION, chrome_options=options)



#driver.get('https://www.vinted.fr/')
#driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/button[2]').click() # accept cookies



def fi(a):
    try:
        driver.find_element_by_xpath(a).text
    except:
        return False

def ffi(a):
    if fi(a) != False :
        return driver.find_element_by_xpath(a).text

def fi2(a):
    try:
        driver.find_element_by_xpath(a).click()
    except:
        return False

def ffi2(a):
    if fi2(a) != False :
        fi2(a)
        return(True)
    else:
        return(None)

def advance(data, i):
    print(i)
    usr = driver.find_elements_by_xpath('//*[contains(@id, "Catalog-react-component")]')[0]
    usr.find_element_by_xpath('./div/div/div[{}]/div/div/div/div[2]/a'.format(i)).click() # click on result n°i
    new_data = collect_info(driver.current_url)
    print(new_data)
    data = data.append(new_data)
    return(data)

def scrape_research_page(search_url):
    # (a)Initialize variables
    data = pd.DataFrame()
    c = 0
    # (b) Collect data on first result, then on every else result # print(usr.text);print(usr.id)
    for i in range(1,1000):
        if c == 10: # if there are 10 articles in a row we cannot scrape, we consider we finished to scrape the page
            return(data)
        driver.get(search_url)
        try:
            data = advance(data,i)
            c=0
        except:
            print('Unable to scrape item n°{}'.format(i))
            c+=1

    return(data)


def define_criteria_string(order = [], catalog = [], size = [], color = [], brand = [], min_price = 'Na', max_price = 'Na', condition = []):   
    # I - Create criteria string based on these dictionaries
    order_str = ''.join([dict_order[y] for y in order])
    catalog_str = ''.join([dict_catalog[y] for y in catalog])
    size_str = ''.join([dict_size[y] for y in size])
    color_str = ''.join([dict_color[y] for y in color])
    brand_str = ''.join([dict_brand[y] for y in brand])
    condition_str = ''.join([dict_condition[y] for y in condition])

    if min_price != 'Na':
        min_price_str = '&price_from={}'.format(min_price)
    else:
        min_price_str = ''

    if max_price != 'Na':
        max_price_str = '&price_to={}'.format(max_price)
    else:
        max_price_str = ''

    criteria_string = order_str + catalog_str + size_str + color_str + \
        brand_str + min_price_str + max_price_str + condition_str

    return(criteria_string)






def research_and_scrape(query, criteria_string, end_page = 2):
    start_page = 1
    # https://www.vinted.fr/vetements?search_text=nike%20air%20max
    DATA_ALL = pd.DataFrame()
    if start_page == 1 :
        # start first page
        page = 1
        print('We start to scrape page n° {}'.format(page))
        search_url = 'https://www.vinted.com/clothes?search_text=' + query.replace(' ', '%20') + criteria_string
        driver.get(search_url)
        input("You might need to manually accept the cookies (only necessary at page 1).\n Press Enter to continue when it is done (or not displayed on the site)...")
        print('Thanks!')
        DATA_ALL = DATA_ALL.append(scrape_research_page(search_url))
        print('We finished to scrape page n° {}'.format(page))
    
    for page in range(2, end_page + 1):
        print('We start to scrape page n° {}'.format(page))
        search_url = 'https://www.vinted.com/clothes?search_text=' + query.replace(' ', '%20') + criteria_string + '&page={}'.format(page) # 
        DATA_ALL = DATA_ALL.append(scrape_research_page(search_url))
        print('We finished to scrape page n° {}'.format(page))


    if not os.path.exists('./Scraped'):
        os.makedirs('./Scraped')

    DATA_ALL.to_csv("./Scraped/{}_{}_page{}_page{}.csv".format(query.replace(' ', '-'), str(datetime.now()).replace(' ','-').\
        replace(':','-').replace('.','-'), start_page, end_page), sep = ";", index = False)

  

    print('We finished scraping the query {} between page {} and page {}!'.format(query, start_page, end_page))
    return(DATA_ALL) # Everything went good

def collect_info(page_url):
    '''Date of post, Price, Brand, Size, Condition, Color, Location, Views, 
    Interested, category'''
    driver.get(page_url)
    #time.sleep(4)
    # (a) Collect basic info
    data = ffi('/html/body/div[4]/div/section/div/div[2]/main/aside/div[1]')

    # (b) Transform the data into a cleaner form
    clean_data = data.split('\n')

    # (c) Exctract info from the clean form
    try:
        price = clean_data[0][1:]
    except:
        price = 'Na'

    try:
        brand = clean_data[np.where([(y[:5]=='BRAND') for y in clean_data])[0][0]][5:].strip() # obtain brand without any spaces
    except:
        brand = 'Na'

    try:
        colors = clean_data[np.where([(y[:5]=='COLOR') for y in clean_data])[0][0]][5:].strip() 
    except:
        colors = 'Na'

    try:
        size = clean_data[np.where([(y[:4]=='SIZE') for y in clean_data])[0][0]][4:].strip() 
    except:
        size = 'Na'

    try:
        condition = clean_data[np.where([(y[:9]=='CONDITION') for y in clean_data])[0][0]][9:].strip() 
    except:
        condition = 'Na'

    try:
        views = clean_data[np.where([(y[:5]=='VIEWS') for y in clean_data])[0][0]][5:].strip() 
    except:
        views = '0'

    try:
        interested = re.split(' ',clean_data[np.where([(y[:10]=='INTERESTED') for y in clean_data])[0][0]][10:].strip())[0]
    except:
        interested = '0'

    try:
        location = clean_data[np.where([(y[:8]=='LOCATION') for y in clean_data])[0][0]][8:].strip() 
    except:
        location = 'Na'

    try:
        date = driver.find_element_by_xpath('/html/body/div[4]/div/section/div/div[2]/main/aside/div[1]/div[1]/div[2]/div[8]/div[2]/time').get_attribute('title')
    except:
        try:
            date = driver.find_element_by_xpath('/html/body/div[4]/div/section/div/div[2]/main/aside/div[1]/div[1]/div[2]/div[9]/div[2]/time').get_attribute('title')
        except:
            date = 'Na'

    try:
        description = clean_data[np.where([(y[:8]=='UPLOADED') for y in clean_data])[0][0] + 1].strip() 
    except:
        description = 'Na'

    try:
        number = re.split('-',re.split('/', page_url)[-1])[0]
    except:
        number = 'Na'

    try:
        category = re.split('/', page_url)[-2]
    except:
        category = 'Na'

    return(pd.DataFrame({'Description':description,
                        'category': category,
                        'Price': price,
                        'Brand':brand,
                        'Colors': colors,
                        'Size':size,
                        'Condition':condition,
                        'Views':views,
                        'Interested':interested,
                        'Location':location,
                        'Date':date,
			'Current_date' : datetime.now(),
                        'No':number,
                        'url':driver.current_url
                        }, index = [0]))


def interactive_version():
    # I - Ask query and criteria 
    query = input("Which item do you want to research on vinted.com ? \n")

    print('\n Now a few criteria, you can skip any by pressing enter directly \n ')
    order_str = [input("Indicate order of search (1 choice max) among following choices : \n {} \n".format(dict_order.keys()))]
    order_str = [element for item in order_str for element in item.split(',')] 
    catalog_str = [input("Indicate catalog for search (1 choice max) among following choices : \n {} \n".format(dict_catalog.keys()))]
    catalog_str = [element for item in catalog_str for element in item.split(',')] 
    size_str = [input("Indicate size for search (no max choices) among following choices : \n {} \n".format(dict_size.keys()))]
    size_str = [element for item in size_str for element in item.split(',')] 
    color_str = [input("Indicate colors for search (2 choices max) among following choices : \n {} \n".format(dict_color.keys()))]
    color_str = [element for item in color_str for element in item.split(',')] 
    brand_str = [input("Indicate brand for search (no max choices) among following choices : \n {} \n".format(dict_brand.keys()))]
    brand_str = [element for item in brand_str for element in item.split(',')] 
    condition_str = [input("Indicate confitions for search (5 choices max) among following choices : \n {} \n".format(dict_condition.keys()))]
    condition_str = [element for item in condition_str for element in item.split(',')] 

    min_price, max_price = 'Na', 'Na'
    min_price = input("Do you want a minimal price ? ")
    max_price = input("Do you want a maximal price ? ")

    end_page = input('Until which page do you want to collect data? (max = 400)')
    if order_str == ['']:
        order_str = []
    if catalog_str == ['']:
        catalog_str = []
    if size_str == ['']:
        size_str = []
    if color_str == ['']:
        color_str = []
    if brand_str == ['']:
        brand_str = []
    if condition_str == ['']:
        condition_str = []
    
    criteria_string = define_criteria_string(order = order_str, catalog = catalog_str, size = size_str, color = color_str,\
     brand = brand_str, min_price = min_price, max_price = max_price, condition = condition_str)


    #print(criteria_string)
    scraped_data = research_and_scrape(query, criteria_string,  end_page = end_page)
