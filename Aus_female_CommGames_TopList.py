# program for scraping the WA site for results
# Commonwealth event rank data
# only returns AUS athletes in top 100 in each event limited to 3 per country


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import sys

#options for events
# put this in a list to read item in list so bot operated through items automatically
event100 = str("100-meters")
event200 = str("200-meters")
event400 = str("400-meters")
event800 = str("800-meters")
event1500 = str("1500-meters")
eventSC = str("3000-metres-steeplechase")
event5K = str("5000-meters")
event10K = str("10000-meters")
event100H = str("100-metres-hurdles")
event400H = str("400-metres-hurdles")
eventLJ = str("long-jump")
eventTJ = str("triple-jump")
eventHJ = str("high-jump")
eventPV = str("pole-vault")
eventDT = str("discus-throw")
eventSP = str("shot-put")
eventJT = str("javelin-throw")
eventHT = str("hammer-throw")
eventX7 = str("heptathlon")
event20kw = str("10000-metres-race-walk")
eventMAR = str("marathon")
# make list from variables [event100, event200, event400, event800, event1500, eventSC, event5K, event10K, event100H, event400H, eventLJ, eventTJ, eventHJ, eventPV, eventDT, eventHT, eventJT, eventSP, eventX7, event20kw, eventMAR
event_list = [event100, event200, event400, event800, event1500, eventSC, event5K, event10K, event100H, event400H, eventLJ, eventTJ, eventHJ, eventPV, eventDT, eventHT, eventJT, eventSP, eventX7, event20kw, eventMAR]


while True:
    for item in event_list:
        event = item
        # group the events using IFs in categories for the URLs
        if event == "100-meters" or event == "200-meters" or event == "400-meters":
            event_group = "sprints"
        elif event == "800-meters" or event == "1500-meters" or event == "5000-meters" or event == "10000-meters" or event == "3000-metres-steeplechase":
            event_group = "middle-long"
        elif event == "100-metres-hurdles" or event == "400-metres-hurdles":
            event_group = "hurdles"
        elif event == "marathon":
            event_group = "road-running"
        elif event == "long-jump" or event == "high-jump" or event == "triple-jump" or event == "pole-vault":
            event_group = "jumps"
        elif event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw":
            event_group = "throws"
        elif event == "heptathlon":
            event_group = "combined-events"
        elif event == "10000-metres-race-walk":
            event_group = "race-walks"


        sys.stdout = open('/Users/newmac/Desktop/Programs and Code/AUS_female' + '_' + event + '_CommsRank_Toplists' + '.txt', 'wt')
        #print("Athlete Name", ":", "DOB", ":", "Event List", ":", "Event Score", ":", "Event Rank in Australia", ":", "Perf_1", ":", "Perf_2", ":", "Perf_3", ":", "Perf_4", ":", "Perf_5", ":", "Dt_1", ":", "Dt_2", ":", "Dt_3", ":", "Dt_4", ":", "Dt_5")
        #bot for clicking cookie button and opening row1
        PATH = Service("/Applications/chromedriver")
        driver = webdriver.Chrome(service=PATH)
        driver.get("https://www.worldathletics.org/records/toplists/" + event_group + "/" + event + "/outdoor/women/senior/2022?regionType=country-group&region=commonwealth%20games&page=1&bestResultsOnly=true")  # EVENT URL LIMITED TO 4 PER COUNTRY
        time.sleep(0.5)
        cookie_button = driver.find_element(By.XPATH, '/html/body/div[7]/div')
        cookie_button.click()

        # now retrieve only AUS athlete data
        counter = 1
        str(counter)
        while counter < 101:
            try:
                athlete_tab = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']')  # tr1 needs to increase each run
                nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text
            except:
                break
            if nat_check == "AUS":
                try:
                    clicked_row = athlete_tab.click()
                    time.sleep(1.75)
                    grab_rank = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[1]').text
                    grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[2]').text
                    grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[3]').text
                    grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text
                    print(grab_name, ":", event, ":", grab_DOB, ":", grab_score, ":", grab_rank)
                    counter = counter + 1
                except NoSuchElementException:
                    break

                try:
                    time.sleep(0.5)
                    exit_button = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[1]/button')
                    exit_button.click()
                    time.sleep(1)
                    # if 'break' is here then it exits the search once an aussie is found
                except NoSuchElementException or ElementNotInteractableException:
                    time.sleep(1.5)
                    exit_button = driver.find_element(By.XPATH, '//*[@id="media"]/div[2]/div/div[1]/button')
                    time.sleep(0.5)
                    exit_button.click()

            else:
                counter = counter + 1
                #print("not AUS")

    break
