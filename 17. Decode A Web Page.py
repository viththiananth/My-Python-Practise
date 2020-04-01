#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.


import requests
from bs4 import BeautifulSoup

url='https://www.nytimes.com/'
#These lines make the request to the New York Times homepage. Making a request is simple, according to the documentation you supply a URL and make a GET request.
r=requests.get(url)

#Reading further through the documentation, we discover that r, contains all the information from the request sent to the New York Times homepage. What we actually want is to look at the HTML of the page and analyze it, so we find that r.text returns all the HTML from the returned request.
soup1=BeautifulSoup(r.text,'lxml')

#Following are the way how the story heading looks
#<h2 class="css-1vvhd4r esl82me0">Business Updates: Stock Markets Tumble</h2>
#<h2 class="css-14byr0y esl82me0">Malaria Drug Helps Virus Patients Improve, in Small Study</h2>
#This returns a list of all tags with story-heading as a class. What we need to do is loop through all of them with a for loop and see what format the output is in.
for headings in soup1.find_all("h2"):
    print(headings.name+' '+headings.text.strip())
