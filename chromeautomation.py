from selenium import webdriver
search = input('enter the search word:  ')

web = webdriver.Chrome("C:\DRIVERS\chromedriver.exe")

for i in range(1):
    L = web.get("https://www.google.com/search?q=" + search + "&start" + str(i))