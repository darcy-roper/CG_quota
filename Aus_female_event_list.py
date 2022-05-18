# program for scraping the WA site for results
# AUS event rank data
# only returns AUS each event


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys
from webdriver_manager.chrome import ChromeDriverManager


#options for events
# put this in a list to read item in list so bot operated through items automatically
event100 = str("100m")
event200 = str("200m")
event400 = str("400m")
event800 = str("800m")
event1500 = str("1500m")
eventSC = str("3000msc")
event5K = str("5000m")
event10K = str("10000m")
event100H = str("100mh")
event400H = str("400mh")
eventLJ = str("long-jump")
eventTJ = str("triple-jump")
eventHJ = str("high-jump")
eventPV = str("pole-vault")
eventDT = str("discus-throw")
eventSP = str("shot-put")
eventJT = str("javelin-throw")
eventHT = str("hammer-throw")
eventX7 = str("heptathlon")
event20kw = str("race-walking")
eventMAR = str("marathon")
# make list from variables [event100, event200, event400, event800, event1500, eventSC, event5K, event10K, event100H, event400H, eventLJ, eventTJ, eventHJ, eventPV, eventDT, eventHT, eventJT, eventSP, eventX7, event20kw, eventMAR
# we use this comment list above to quickly paste in or over below list to begin running program from an event 
# without rewriting all the events starting from event100 if that event executed correctly
event_list = [eventJT, eventSP, eventX7, event20kw, eventMAR]

while True:
    for item in event_list:
        event = item
        sys.stdout = open('output/AUS_female' + '_' + event + '.txt', 'wt')
        #print("Athlete Name", ":", "DOB", ":", "Event List", ":", "Event Score", ":", "Event Rank in Australia", ":", "Perf_1", ":", "Perf_2", ":", "Perf_3", ":", "Perf_4", ":", "Perf_5", ":", "Dt_1", ":", "Dt_2", ":", "Dt_3", ":", "Dt_4", ":", "Dt_5") # only use this if major errors found
        #bot for clicking cookie button and opening row1
        driver = webdriver.Chrome(ChromeDriverManager().install())  # should install chromedriver if not found
        driver.get("https://www.worldathletics.org/world-rankings/" + event + "/women?regionType=countries&region=aus&page=1&rankDate=")  # URL already filters for AUS ONLY!
        time.sleep(1)
        cookie_button = driver.find_element(By.XPATH, '/html/body/div[7]/div')
        cookie_button.click()

        # now retrieve only AUS athlete data as this is Av. points so only used for Aus Quals checker
        counter = 1
        str(counter)
        while counter < 101:
            try:
                athlete_tab = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']')  # tr1 needs to increase each run
                time.sleep(1)
                clicked_row = athlete_tab.click()
                time.sleep(1.75)
            except NoSuchElementException:
                break
            grab_rank = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[1]').text
            grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[2]').text
            grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[3]').text
            grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text
            try:
                perf_1 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[1]/td[9]').text
            except NoSuchElementException:
                perf_1 = ""
            try:
                perf_2 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[2]/td[9]').text
            except NoSuchElementException:
                perf_2 = ""
            try:
                perf_3 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[3]/td[9]').text
            except NoSuchElementException:
                perf_3 = ""
            try:
                perf_4 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[4]/td[9]').text
            except NoSuchElementException:
                perf_4 = ""
            try:
                perf_5 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[5]/td[9]').text
            except NoSuchElementException:
                perf_5 = ""
            #date grabs
            try:
                dt_1 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]').text
            except NoSuchElementException:
                dt_1 = ""
            try:
                dt_2 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[2]/td[1]').text
            except NoSuchElementException:
                dt_2 = ""
            try:
                dt_3 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[3]/td[1]').text
            except NoSuchElementException:
                dt_3 = ""
            try:
                dt_4 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[4]/td[1]').text
            except NoSuchElementException:
                dt_4 = ""
            try:
                dt_5 = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]').text
            except NoSuchElementException:
                dt_5 = ""

            print(grab_name, ":", event, ":", grab_DOB, ":", grab_score, ":", grab_rank, ":", perf_1, ":", perf_2, ":", perf_3, ":", perf_4, ":", perf_5, ":", dt_1, ":", dt_2, ":", dt_3, ":", dt_4, ":", dt_5)
            counter = counter + 1
            try:
                exit_button = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[1]/button')
            except NoSuchElementException:
                time.sleep(1)
            exit_button.click()
    break
