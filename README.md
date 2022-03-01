# CG_quota
Programs for scraping world athletics webpage to determine Australia's top athletes eligible for selection in the 2022 Birmingham Commonwealth Games. 

Before running main program files locally ensure chrome driver is installed on your device
Download links are available here: https://chromedriver.chromium.org/downloads

Also check you have installed selenium to run the webdriver:
- use pip to install selenium 

## Current workflow process to update www.commonwealthgames-quota.com.au:
  1. Run main program files to fetch data:
      
      a. `Aus_male21_event_Toplist.py` -> this obtains Aus 2021 male rankings in all events by best performance on Toplist and prints to txt file
      
      b. `Aus_male22_event_Toplist.py` -> this obtains Aus 2022 male rankings in all events by best performance on Toplist and prints to txt file

      c. `Aus_female21_event_Toplist.py` -> this obtains Aus 2021 female rankings in all events by best performance on Toplist and prints to txt file

      d. `Aus_female22_event_Toplist.py` -> this obtains Aus 2022 female rankings in all events by best performance on Toplist and prints to txt file

      e. `Toplist21_male_Commonwealth.py` -> this obtains 2021 male Comminwealth rankings in all events by best performance on Toplist and prints to txt file

      f. `Toplist22_male_Commonwealth.py` -> this obtains 2022 male Comminwealth rankings in all events by best performance on Toplist and prints to txt file

      g. `Toplist21_female_Commonwealth.py` -> this obtains 2021 female Comminwealth rankings in all events by best performance on Toplist and prints to txt file

      h. `Toplist22_female_Commonwealth.py` -> this obtains 2022 female Comminwealth rankings in all events by best performance on Toplist and prints to txt file

      i. `Aus_male_event_list.py` -> this obtains Aus male rankings in all events by Av. points score and prints to txt file (Using this to check Autos as it returns multiple performance per athlete)
      
      j.`Aus_female_event_list.py` -> this obtains Aus female rankings in all events by Av. points score and prints to txt file (Using this to check Autos as it returns multiple performance per athlete)

  2. Combine individual event txt files:
      
      a. `Combine21_AUS_male_list.py` -> this combines all `AUS_male21_event_Toplist` individual event txt files into one txt file to serve as a data source for the xls.

      b. `Combine22_AUS_male_list.py` -> this combines all `AUS_male22_event_Toplist` individual event txt files into one txt file to serve as a data source for the xls.

      c. `Combine21_AUS_female_list.py` -> this combines all `AUS_female21_event_Toplist` individual event txt files into one txt file to serve as a data source for the xls.

      d. `Combine22_AUS_female_list.py` -> this combines all `AUS_female22_event_Toplist` individual event txt files into one txt file to serve as a data source for the xls.

#continue from here
      e. `Combine21_Comms_male_list.py` -> this combines all Aus male commonwealth ranked athletes into one txt file
      
      d. `Combine_Comms_female_list.py` -> this combines all Aus female commonwealth ranked athletes into one txt file

a. `Combine_male_list.py` -> this combines all Aus male events into one txt file
      
b. `Combine_female_list.py` -> this combines all Aus female events into one txt file
      
     
  3. Open `Commonwealth Ranking Variables.xlsx` and connect sheets to their respective (Combined) txt files using 'Get data from txt file query'.
  4. Reorder columns in Aus_male_list & Aus_female_list in Av. score ascending order
  5. Copy top 75 in male and female lists in columns B-F then paste (values only) into 'Final List' sheet green columns C-G. Reorder C-G in ascending order again once Final list contains top 75 male and female athletes. 
      
      **Note:** Blue coloured columns contain formulae to match athlete and pull their commonwealth rank and auto qual information. 
  6. Insert calculated age column next to DOB column.
  4. Save sheet as .html file under a new name for final formatting of cell colour and style. Don't forget to save the original spreadsheet file back to .xls workbook format
  5. Copy html file code from the saved sheet and pase in Wordpress webpage editor before Thursday 12pm.  


## Objectives for project development:
  - [ ] fully automate above processes to achieve the desired results. Reducing margin for human error and data sorting mistakes
  - [ ] update webscraping program files to pull data from https://www.worldathletics.org/records/toplists/ 
  - [ ] better reflect the selection policy rules instead of relying on world ranking points system 
  - [ ] edit main program files to be able to save files on any device. Currently file paths are saving to my desktop (/Users/`my laptop`/Desktop/`my folder name`/)
  - [ ] edit main program files to run chrome driver on any device. Currently it runs chromedriver by finding the application in my laptop Application folder 

