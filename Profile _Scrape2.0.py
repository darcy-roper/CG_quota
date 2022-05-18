# Version 2.0 of athlete profile scrape
# Separated into functions called in sequence


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import sys
from webdriver_manager.chrome import ChromeDriverManager


#Apply filters for XPATH based on the event
# #selecting senior male athletes in commonwealth for year 2021
def male_21_filters():
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
    event_variable = driver.find_element(By.XPATH, '//*[@id="disciplineCode"]/option[' + event_num + ']')  # this is determined by event variable
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

def open_profile_def():
    open_profile = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]/a')  # left `.txt` off this XPATH because we need .click operation
    open_profile.click()
    time.sleep(6)  # need some more appropriate function to call on for loading times replacing time.sleep operations eg= once loading complete continue through program
    cookie_button1 = driver.find_element(By.XPATH, '//*[@id="c-right"]/a')
    cookie_button1.click()
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
    # athlete's performances across all events in that year


# Event variables
# Txt to be called on using list operators [...]
event100 = str("100 Meters")
event200 = str("200 Meters")
event400 = str("400 Meters")
event800 = str("800 Meters")
event1500 = str("1500 Meters")
eventSC = str("3000 Metres Steeplechase")
event5K = str("5000 Meters")
event10K = str("10000 Meters")
event110H = str("110 Meter Hurdles")
event400H = str("400 Meter Hurdles")
eventLJ = str("Long Jump")
eventTJ = str("Triple Jump")
eventHJ = str("High Jump")
eventPV = str("Pole Vault")
eventDT = str("Discus Throw")
eventSP = str("Shot Put")
eventJT = str("Javelin Throw")
eventHT = str("Hammer Throw")
eventX10 = str("Decathlon")
event10kw = str("10,000 Meters Race Walk")
eventMAR = str("Marathon")
# make list from variables [event100, event200, event400, event800, event1500, eventSC, event5K, event10K, event110H, event400H, eventLJ, eventTJ, eventHJ, eventPV, eventDT, eventHT, eventJT, eventSP, event10kw, eventMAR, eventX10
# we use this comment list above to quickly paste in or over below list to begin running program from an event
# without rewriting all the events starting from event100 if that event executed correctly
event_list = [eventLJ]


# Variables for wind affected events in list [...]
windy_events = ["100 Meters", "200 Meters", "110 Meters Hurdles", "Long Jump", "Triple Jump"]
no_wind_events = ["400 Meters", "800 Meters", "1500 Meters", "3000 Meters Steeplechase", "5000 Meters", "10000 Meters", "400 Meter Hurdle", "Pole Vault", "High Jump", "Shot Put", "Discus Throw", "Javelin Throw", "Hammer Throw", "10,000 Meters Race Walk", "Marathon", "Decathlon"]
above_limit = ["+2.1", "+2.2", "+2.3", "+2.4", "+2.5", "+2.6", "+2.7", "+2.8", "+2.9", "+3.0", "+3.1", "+3.2", "+3.3", "+3.4", "+3.5", "+3.6", "+3.7", "+3.8", "+3.9", "+4.0", "+4.1", "+4.2", "+4.3", "+4.4", "+4.5", "+4.6", "+4.7", "+4.8", "+4.9", "+5.0", "+5.1", "+5.2", "+5.3", "+5.4", "+5.5", "+5.6", "+5.7", "+5.8", "+5.9", "+6.0"]

while True:
    for item in event_list:
            event = item
            # grouping events by numbers for the selection in the dropdown filter list the number becomes the option when the list drops after click()
            if event == "100 Meters":
                event_num = "2"
            elif event == "200 Meters":
                event_num = "3"
            elif event == "400 Meters":
                event_num = "5"
            elif event == "800 Meters":
                event_num = "7"
            elif event == "1500 Meters":
                event_num = "9"
            elif event == "5000 Meters":
                event_num = "14"
            elif event == "10000 Meters":
                event_num = "16"
            elif event == "3000 Meters Steeplechase":
                event_num = "24"
            elif event == "110 Meter Hurdles":
                event_num = "25"
            elif event == "400 Meter Hurdles":
                event_num = "26"
            elif event == "Long Jump":
                event_num = "29"
            elif event == "Triple Jump":
                event_num = "30"
            elif event == "High Jump":
                event_num = "27"
            elif event == "Pole Vault":
                event_num = "28"
            elif event == "Discus Throw":
                event_num = "32"
            elif event == "Shot Put":
                event_num = "31"
            elif event == "Hammer Throw":
                event_num = "33"
            elif event == "Javelin Throw":
                event_num = "34"
            elif event == "Decathlon":
                event_num = "35"
            elif event == "10,000 Meters Race Walk":
                event_num = "39"
            elif event == "Marathon":
                event_num = "22"


            sys.stdout = open('output/Toplist21_male' + '_' + event + '_CommsRank' + '.txt', 'wt')  # creates a txt file in folder location `output`
            # bot for clicking cookie button
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # should install chromedriver if not found
            driver.get("https://www.worldathletics.org/records/toplists/")  # EVENT URL fetching commonwealth toplist
            time.sleep(1)
            cookie_button = driver.find_element(By.XPATH, '/html/body/div[7]/div')
            cookie_button.click()

            counter = 1
            str(counter)
            while counter < 101:
                try:  # Nationality IF statements are unique to the event because the column ordering changes between wind-affected and non-wind-affected events
                    if event in windy_events:
                        nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[6]').text  # checking tr6 for AUS
                    elif event in no_wind_events:
                        nat_check = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text  # checking tr5 for AUS
                except:
                    break


                # If false add 1 to the counter in order to move through the list to the next ranked athlete
                while True:
                    try:
                        # rank will always be in column 1 so this doesn't need to be determined with an IF statement
                        grab_rank = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[1]').text

                        # performance always in column 2
                        grab_perf = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[2]').text

                        # fetching names based on event
                        if event in windy_events:
                            grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text  # 4th column for sprints
                        elif event in no_wind_events:
                            grab_name = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[3]').text  # 3rd column for middle-long dist

                        # fetching DOB based on event
                        if event in windy_events:
                            grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[5]').text  # 5th column for sprints
                        elif event in no_wind_events:
                            grab_DOB = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[4]').text  # 4th column for middle-long dist

                        # fetching score based on event
                        if event in windy_events:
                            grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[11]').text  # 11th column for sprints
                        elif event in no_wind_events:
                            grab_score = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[10]').text  # 10th column for middle-long dist

                        # fetching performance date to be used in SQL and filter by qualifying period
                        if event in windy_events:
                            temp_grab = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[10]').text  # 11th column for sprints
                        elif event in no_wind_events:
                            temp_grab = driver.find_element(By.XPATH, '//*[@id="toplists"]/div[3]/table/tbody/tr['+str(counter)+']/td[9]').text  # 10th column for middle-long dist


                        # number strip for date check
                        perf_mth = ''.join([i for i in temp_grab if not i.isdigit()])

                        if perf_mth == ' JUL ' or perf_mth == ' AUG ' or perf_mth == ' SEP ' or perf_mth == ' OCT ' or perf_mth == ' NOV ' or perf_mth == ' DEC ':  # performances post JUN in 2021 will count
                            grab_date = temp_grab
                            print(nat_check, "|", grab_name, "|", event, "|", grab_DOB, "|", grab_score, "|", grab_perf, "|", grab_date)  # If performance within period we print to txt file here
                            counter = counter + 1  # probably won't work for decathlon
                            break  # should break back to new row on list
                        elif perf_mth == ' JAN ' or perf_mth == ' FEB ' or perf_mth == ' MAR ' or perf_mth == ' APR ' or perf_mth == ' MAY ' or perf_mth == ' JUN ':  # if performances JAN-JUN then we open profile to search for next best
                            open_profile_def()

                        # now with profile open scrape all data in correct event table
                        tbl_rowcount = 1
                        tbl_count = 1
                        tblID = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div[2]/div/div[4]/div[2]/div[2]/div['+str(tbl_count)+']/div[2]').text  # will return top table event text
                        if tblID == event:










male_21_filters()
