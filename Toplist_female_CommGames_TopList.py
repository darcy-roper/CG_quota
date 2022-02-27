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
event_list = [event100, event200, event400, event800, event1500, eventSC, event5K, event10K, event100H, event400H, eventLJ, eventTJ, eventHJ, eventPV, eventDT, eventHT, eventJT, eventSP, eventX7, event20kw, eventMAR]


while True:
    for item in event_list:
        event = item
        # grouping events by numbers for the selection in the dropdown filter list
        if event == "100m":
            event_num = "2"
        elif event == "200m":
            event_num = "3"
        elif event == "400m":
            event_num = "5"
        elif event == "800m":
            event_num = "7"
        elif event == "1500m":
            event_num = "9"
        elif event == "5000m":
            event_num = "14"
        elif event == "10000m":
            event_num = "16"
        elif event == "3000msc":
            event_num = "24"
        elif event == "100mh":
            event_num = "25"
        elif event == "400mh":
            event_num = "26"
        elif event == "long-jump":
            event_num = "29"
        elif event == "triple-jump":
            event_num = "30"
        elif event == "high-jump":
            event_num = "27"
        elif event == "pole-vault":
            event_num = "28"
        elif event == "discus-throw":
            event_num = "32"
        elif event == "shot-put":
            event_num = "31"
        elif event == "hammer-throw":
            event_num = "33"
        elif event == "javelin-throw":
            event_num = "34"
        elif event == "heptathlon":
            event_num = "35"
        elif event == "race-walking":
            event_num = "39"
        elif event == "marathon":
            event_num = "22"


        sys.stdout = open('/Users/newmac/Desktop/Programs and Code/Toplist_female' + '_' + event + '_CommsRank' + '.txt', 'wt') # want to automate the folder selection process
        #bot for clicking cookie button and opening row1
        PATH = Service("/Applications/chromedriver") # want to find chromedriver on local device runnig program
        driver = webdriver.Chrome(service=PATH)
        driver.get("https://www.worldathletics.org/records/toplists/")  # EVENT URL fetching commonwealth toplist for 2022
        time.sleep(1)
        cookie_button = driver.find_element(By.XPATH, '/html/body/div[7]/div')
        cookie_button.click()
        
        #Apply filters for XPATHs based on the event
        #selecting senior
        age_category = driver.find_element(By.XPATH, '//*[@id="ageCategory"]')
        age_category.click()
        senior = driver.find_element(By.XPATH, '//*[@id="ageCategory"]/option[1]')
        senior.click()
        #selecting outdoor
        in_outdoor = driver.find_element(By.XPATH, '//*[@id="environment"]')
        in_outdoor.click()
        outdoor = driver.find_element(By.XPATH, '//*[@id="environment"]/option[2]')
        outdoor.click()
        #selecting season
        season = driver.find_element(By.XPATH, '//*[@id="season"]')  # change this in some way to grab 2021 data then merge/match the two 
        season.click()
        year = driver.find_element(By.XPATH, '//*[@id="season"]/option[1]')  # option 2 is the previous year
        year.click()
        #selecting gender
        gender = driver.find_element(By.XPATH, '//*[@id="gender"]')
        gender.click()
        female = driver.find_element(By.XPATH, '//*[@id="gender"]/option[2]')  # option 1 is male
        female.click()
        #selecting event
        event_filter = driver.find_element(By.XPATH, '//*[@id="disciplineCode"]')
        event_filter.click()
        event_variable = driver.find_element(By.XPATH, '//*[@id="disciplineCode"]/option['+event_num+']') #this should be determined by the event variables 
        event_variable.click()
        time.sleep(1.5) # allows for loading table data if stale element error produced
        countries = driver.find_element(By.XPATH, '//*[@id="regionType"]')  # only after this is clicked can we get the dropdown for groups
        countries.click()
        group_countries = driver.find_element(By.XPATH, '//*[@id="regionType"]/option[4]')
        group_countries.click()
        time.sleep(1) # allows for loading
        group_click = driver.find_element(By.XPATH, '//*[@id="region"]')
        group_click.click()
        commgames = driver.find_element(By.XPATH, '//*[@id="region"]/option[6]')
        commgames.click()
        time.sleep(1.5) # allowing for table load time


        
        #driver.get("https://www.worldathletics.org/records/toplists/" + event_group + "/" + event + "/outdoor/women/senior/2022?regionType=country-group&region=commonwealth%20games")  # EVENT URL fetching commonwealth toplist for 2022

        # now retrieve only AUS athlete data
        counter = 1
        str(counter)
        while counter < 101:
            try:  # Nationality IF statements are unique to the envent because the columnb ordering changes between events
                #athlete_tab = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']')  # tr1 needs to increase each run
                if event == "100m" or event == "200m" or event == "100mh":
                    nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[6]').text  # checking tr6 for AUS
                elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh":
                    nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text  # checking tr5 for AUS
                

            except:
                break
            # these if/try statements check the athlete is Australian
            # If false add 1 to the counter in order to move through the list to the next ranked athlete
            if nat_check == "AUS":
                try:
                    # rank will always be in column 1 so this dosen't need to be determed with an IF statement
                    grab_rank = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[1]').text
                    
                    # fetaching names based on event
                    if event == "100m" or event == "200m" or event == "100mh":
                        grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text  # 4th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh":
                        grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[3]').text  # 3rd column for middle-long dist
                    
                    # fetching DOB based on event
                    if event == "100m" or event == "200m":
                        grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text  # 5th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh":
                        grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text  # 5th column for middle-long dist
                    
                    # fetching score based on event
                    if event == "100m" or event == "200m":
                        grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[11]').text  # 11th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh":
                        grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[10]').text  # 10th column for middle-long dist


                    print(grab_name, ":", event, ":", grab_DOB, ":", grab_score, ":", grab_rank)
                    counter = counter + 1  # prints to txt file then adds 1 to counter to move down list
                except NoSuchElementException:
                    break

            else:
                counter = counter + 1
                # add 1 to the counter to move down list if athlete not AUS

    break
