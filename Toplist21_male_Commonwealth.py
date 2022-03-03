# program for scraping the WA site for results
# Commonwealth event rank data
# Returning ALL!! athletes in top 100 in each event


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
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
event110H = str("110mh")
event400H = str("400mh")
eventLJ = str("long-jump")
eventTJ = str("triple-jump")
eventHJ = str("high-jump")
eventPV = str("pole-vault")
eventDT = str("discus-throw")
eventSP = str("shot-put")
eventJT = str("javelin-throw")
eventHT = str("hammer-throw")
eventX10 = str("decathlon")
event20kw = str("20km-race-walking")
eventMAR = str("marathon")
# make list from variables [event100, event200, event400, event800, event1500, eventSC, event5K, event10K, event110H, event400H, eventLJ, eventTJ, eventHJ, eventPV, eventDT, eventHT, eventJT, eventSP, event20kw, eventMAR, eventX10
# we use this comment list above to quickly paste in or over below list to begin running program from an event 
# without rewriting all the events starting from event100 if that event executed correctly
event_list = [event100, event200, event400, event800, event1500, eventSC, event5K, event10K, event110H, event400H, eventLJ, eventTJ, eventHJ, eventPV, eventDT, eventHT, eventJT, eventSP, event20kw, eventMAR, eventX10]


while True:
    for item in event_list:
        event = item
        # grouping events by numbers for the selection in the dropdown filter list the number becomes the option when the list drops down after click()
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
        elif event == "110mh":
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
        elif event == "decathlon":
            event_num = "35"
        elif event == "20km-race-walking":
            event_num = "39"
        elif event == "marathon":
            event_num = "22"


        sys.stdout = open('output/Toplist21_male' + '_' + event + '_CommsRank' + '.txt', 'wt') # want to automate the folder selection process
        #bot for clicking cookie button and opening row1
        driver = webdriver.Chrome(ChromeDriverManager().install())  # should install chromedriver if not found
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
        season = driver.find_element(By.XPATH, '//*[@id="season"]')  
        season.click()
        year = driver.find_element(By.XPATH, '//*[@id="season"]/option[2]')  # change this for a different year
        year.click()
        #selecting gender
        gender = driver.find_element(By.XPATH, '//*[@id="gender"]')
        gender.click()
        male = driver.find_element(By.XPATH, '//*[@id="gender"]/option[1]')  # option 2 is female
        male.click()
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
        time.sleep(4) # allowing for table load time



        # now get all athletes
        counter = 1
        str(counter)
        while counter < 101:
            try:  # Nationality IF statements are unique to the envent because the columnb ordering changes between events
                if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                    nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[6]').text  # checking tr6 for AUS
                elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh"  or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon"  or event == "decathlon":
                    nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text  # checking tr5 for AUS
            except:
                break
                # this will break and skip to new event

            # If false add 1 to the counter in order to move through the list to the next ranked athlete
        
            while True:
                try:

                    # rank will always be in column 1 so this dosen't need to be determed with an IF statement
                    grab_rank = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[1]').text

                    # fetaching names based on event
                    if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                        grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text  # 4th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh" or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon"  or event == "decathlon": 
                        grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[3]').text  # 3rd column for middle-long dist

                    # fetching DOB based on event
                    if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                        grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text  # 5th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh" or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon"  or event == "decathlon":
                        grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text  # 4th column for middle-long dist

                    # fetching score based on event
                    if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                        grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[11]').text  # 11th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh" or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon" or event == "decathlon":
                        grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[10]').text  # 10th column for middle-long dist


                    print(nat_check, ":", grab_name, ":", event, ":", grab_DOB, ":", grab_score, ":", grab_rank)
                    if event == "decathlon":
                        counter = counter + 2  # prints to txt file then adds 2 to counter to move down list for multi events
                    else:
                        counter = counter + 1
                    break
                except NoSuchElementException or StaleElementReferenceException:
                    time.sleep(1.5)

    break
