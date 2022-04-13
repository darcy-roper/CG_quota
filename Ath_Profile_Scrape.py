# program for scraping top lists and only returning results within Qual period
# Program scrapes event top list in 2021 THEN
# IF athlete's best performance is before start of qual period, the program will return all results
# in that athlete's profile within the period


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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
event_list = [eventLJ]


while True:
    for item in event_list:
        event = item
        # grouping events by numbers for the selection in the dropdown filter list the number becomes the option when the list drops after click()
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


        sys.stdout = open('output/Toplist21_male' + '_' + event + '_CommsRank' + '.txt', 'wt')  # creates a txt file in folder location `output`
        #bot for clicking cookie button and opening row1
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # should install chromedriver if not found
        driver.get("https://www.worldathletics.org/records/toplists/")  # EVENT URL fetching commonwealth toplist for 2022
        time.sleep(1)
        cookie_button = driver.find_element(By.XPATH, '/html/body/div[7]/div')
        cookie_button.click()

        #Apply filters for XPATH based on the event
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
        year = driver.find_element(By.XPATH, '//*[@id="season"]/option[2]')  # 1 = current year DESC
        year.click()
        #selecting gender
        gender = driver.find_element(By.XPATH, '//*[@id="gender"]')
        gender.click()
        male = driver.find_element(By.XPATH, '//*[@id="gender"]/option[1]')  # option 2 is female
        male.click()
        #selecting event
        event_filter = driver.find_element(By.XPATH, '//*[@id="disciplineCode"]')
        event_filter.click()
        event_variable = driver.find_element(By.XPATH, '//*[@id="disciplineCode"]/option['+event_num+']')  # this is determined by event variable
        event_variable.click()
        time.sleep(1.5)  # allows for loading table data if stale element error produced
        countries = driver.find_element(By.XPATH, '//*[@id="regionType"]')  # only after this is clicked can we get the dropdown for groups
        countries.click()
        group_countries = driver.find_element(By.XPATH, '//*[@id="regionType"]/option[4]')
        group_countries.click()
        time.sleep(1) # allows for loading
        group_click = driver.find_element(By.XPATH, '//*[@id="region"]')
        group_click.click()
        commgames = driver.find_element(By.XPATH, '//*[@id="region"]/option[6]')
        commgames.click()
        time.sleep(5) # allowing for table load time


        # now get all athletes
        counter = 1
        str(counter)
        while counter < 101:
            try:  # Nationality IF statements are unique to the event because the column ordering changes between events
                if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                    nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[6]').text  # checking tr6 for AUS
                elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh" or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon" or event == "decathlon":
                    nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text  # checking tr5 for AUS
            except:
                break
                # this break skips to new event

            # If false add 1 to the counter in order to move through the list to the next ranked athlete
            while True:
                try:
                    # rank will always be in column 1 so this doesn't need to be determined with an IF statement
                    grab_rank = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[1]').text

                    # fetching names based on event
                    if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                        grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text  # 4th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh" or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon" or event == "decathlon":
                        grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[3]').text  # 3rd column for middle-long dist

                    # fetching DOB based on event
                    if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                        grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text  # 5th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh" or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon" or event == "decathlon":
                        grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text  # 4th column for middle-long dist

                    # fetching score based on event
                    if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                        grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[11]').text  # 11th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh" or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon" or event == "decathlon":
                        grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[10]').text  # 10th column for middle-long dist


                    # fetching performance date to be used in SQL and filter by qualifying period
                    if event == "100m" or event == "200m" or event == "110mh" or event == "long-jump" or event == "triple-jump":
                        temp_grab = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[10]').text  # 11th column for sprints
                    elif event == "400m" or event == "800m" or event == "1500m" or event == "3000msc" or event == "5000m" or event == "10000m" or event == "400mh" or event == "pole-vault" or event == "high-jump" or event == "shot-put" or event == "discus-throw" or event == "javelin-throw" or event == "hammer-throw" or event == "20km-race-walking" or event == "marathon" or event == "decathlon":
                        temp_grab = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[9]').text  # 10th column for middle-long dist


                    # number strip for date check
                    perf_mth = ''.join([i for i in temp_grab if not i.isdigit()])

                    if 'JAN' or 'FEB' or 'MAR' or 'APR' or 'MAY' or 'JUN' in perf_mth:  # if performances JAN-JUN then we open profile to search for next best
                        open_profile = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]/a')  # left `.txt` off this XPATH because we need .click operation
                        open_profile.click()
                        time.sleep(8)
                        cookie_button = driver.find_element(By.XPATH, '//*[@id="c-right"]/a')
                        cookie_button.click()
                        time.sleep(2)
                        results_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div[1]/ul/li[4]/div')
                        results_button.click()
                        time.sleep(3)
                        year_select = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div[2]/div/div[4]/div[2]/div[1]/div/div[1]')
                        year_select.click()
                        time.sleep(1)
                        year_21 = driver.find_element(By.XPATH, '//*[@id="resultsYearSelect"]/option[2]')
                        year_21.click()
                        time.sleep(4)
                        # probably want some other counter and a while loop to iterate through table rows
                        # date
                        r1_c1 = '//*[@id="__next"]/div[3]/div/div[2]/div/div[4]/div[2]/div[2]/div/table/tbody/tr[1]/td[1]'
                        # event = event variable
                        r1_c3 = '//*[@id="__next"]/div[3]/div/div[2]/div/div[4]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]'
                        # performance score
                        r1_c9 = '//*[@id="__next"]/div[3]/div/div[2]/div/div[4]/div[2]/div[2]/div/table/tbody/tr[1]/td[8]'
                        # wind reading.... only for wind affected events







                    elif 'JUL' or 'AUG' or 'SEP' or 'OCT' or 'NOV' or 'DEC' in perf_mth:  # performances post JUN in 2021 will count
                        grab_date = temp_grab



                    print(nat_check, ":", grab_name, ":", event, ":", grab_DOB, ":", grab_score, ":", grab_date, ":", grab_rank)
                    if event == "decathlon":
                        counter = counter + 2  # prints to txt file then adds 2 to counter to move down list for multi events
                    else:
                        counter = counter + 1
                    break
                except NoSuchElementException or StaleElementReferenceException:
                    time.sleep(1.5)

    break
