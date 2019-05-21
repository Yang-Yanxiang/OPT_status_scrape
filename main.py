from bs4 import BeautifulSoup
import csv
import requests
import time

#Case Was Received
#Card Was Delivered To Me By The Post Office
#New Card Is Being Produced
#Card Was Mailed To Me
#Card Was Picked Up By The United States Postal Service
candidates = set(['Case Was Received', 'Card Was Delivered To Me By The Post Office', 'New Card Is Being Produced', 'Card Was Mailed To Me', 'Card Was Picked Up By The United States Postal Service'])
my_case_num = 1990232789
url_prefix = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=YSC'
count_total = 0
count_valid = 0
for i in range(my_case_num - 2000, my_case_num + 2000):
    url = url_prefix + str(i)
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    temp = bs.find(class_='col-lg-12 appointment-sec center')
    content = temp.find('p').get_text()
    status = temp.find('h1').get_text()
    if 'I-765' in content:
        count_total += 1
        if status in candidates:
            count_valid += 1
    time.sleep(1)
print(count_total)
print(count_valid)
print(count_valid / count_total * 100)

