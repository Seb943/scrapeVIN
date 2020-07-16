#### Scrape Vinted.fr

# Example of research url
import os
#os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\Vinted\\Codes")


from functions import * 

criteria_string = define_criteria_string(order = ['most recent first'], catalog = [], size = [], color = [],\
     brand = ['adidas'], min_price = 'Na', max_price = 'Na', condition = [])
query = 'stan smith'
print(criteria_string)
scraped_data = research_and_scrape(query, criteria_string,  end_page = 400)

