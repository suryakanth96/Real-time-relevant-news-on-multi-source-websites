import requests
from bs4 import BeautifulSoup
import time
import sys

#query = input("What would you like to search: ")
query = sys.argv[1]
query = query.replace(" ","+")
#query = "https://www.google.com/search?q=" + query
while True:

    print("********TIMES OF INDIA*********")
    query1 = "https://timesofindia.indiatimes.com/topic/" + query

    r = requests.get(query1)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    for s in soup.find_all('div',attrs={"class":"content"}):
        for s1 in s.find_all('a'):
            str1=s1.find('span').text
            print("https://timesofindia.indiatimes.com"+s1.get('href')+" "+str1.strip())
    
    print("********GOOGLE NEWS*********")
    query3 = "https://news.google.com/news/search/section/q/" + query + "/" + query + "?hl=en&gl=US&ned=us"

    r = requests.get(query3)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    for s in soup.find_all('c-wiz',attrs={"class":"M1Uqc kWyHVd"}):
        for s1 in s.find_all('a'):
            str1=s1.text
            print(s1.get('href')+" "+str1.strip())
    
    print("********NDTV*********")
    query2 = "https://www.ndtv.com/topic/" + query

    r = requests.get(query2)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    for s in soup.find_all('p',attrs={"class":"header fbld"}):
        for s1 in s.find_all('a'):
            str1=s1.find('strong').text
            print(s1.get('href')+" "+str1.strip())

   

    #time.sleep(5)

