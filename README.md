# CG_quota
Programs for scraping world athletics webpage to determine Australia's top athletes eligible for selection in the 2022 Birmingham Commonwealth Games. 

Main program files should install chrome driver if not found. If error:
Download links are available here: https://chromedriver.chromium.org/downloads

Also check you have installed selenium to run the webdriver:
- use pip to install selenium 

As noted in issues you will have to edit file save/print paths and folder names of stored txt files for the program to run without errors (because I am yet to discover how to run a python script that identifies a local device username then determines subsequent folder pathways...?)

P.S. I apologise in advance if anything is unclear. I've never worked on any collaborative projects before having only completed introductory programming courses at uni as electives for a bit of fun. 

## Current workflow process to update www.commonwealthgames-quota.com.au:
  ![Workflow](https://user-images.githubusercontent.com/85177676/156756871-8fc30f0b-89cc-43e9-be9c-be1996a01f14.png)

  1. Run main program files to fetch data:
      
      a. `Toplist21_male_Commonwealth.py` -> this obtains 2021 male Comminwealth rankings in all events by best performance on Toplist and prints to txt file

      b. `Toplist22_male_Commonwealth.py` -> this obtains 2022 male Comminwealth rankings in all events by best performance on Toplist and prints to txt file

      c. `Toplist21_female_Commonwealth.py` -> this obtains 2021 female Comminwealth rankings in all events by best performance on Toplist and prints to txt file

      d. `Toplist22_female_Commonwealth.py` -> this obtains 2022 female Comminwealth rankings in all events by best performance on Toplist and prints to txt file

      e. `Aus_male_event_list.py` -> this obtains Aus male rankings in all events by Av. points score and prints to txt file (Using this to check Autos as it returns multiple performance per athlete)
      
      f.`Aus_female_event_list.py` -> this obtains Aus female rankings in all events by Av. points score and prints to txt file (Using this to check Autos as it returns multiple performance per athlete)

  2. Combine individual event txt files:
      
      a. `Toplist_male_21_22_Combine.py` -> this combines all 'Commonwealth event ranking information' into one txt file to serve as a data source for the xls. (this combines 2021 and 2022 toplist data)

      b. `Toplist_male_21_22_Combine.py` -> this combines all 'Commonwealth event ranking information' into one txt file to serve as a data source for the xls. (this combines 2021 and 2022 toplist data)
      
      c. `Combine_male_lists.py` -> this combines all Aus Av points information for all males in all events into one txt file to serve as a data source for the xls. There is no need to run seperate years as the Av. points only includes performances within the last 12-months
      
      d. `Combine_female_lists.py` -> this combines all Aus Av points information for all males in all events into one txt file to serve as a data source for the xls. There is no need to run seperate years as the Av. points only includes performances within the last 12-months

      
     
  3. Open `Comms_Quota_FINAL.xlsx` and connect sheets to their respective (Combined) txt files using 'Get data from txt file query'.
  4. Reorder columns in Aus_male_points_list & Aus_female_points_list in Av. score ascending order to see if new Auto Quals have been identified
  5. Copy top ALL in male and female top lists then paste (values only) into 'Final List' sheet green columns C-G. 
      
      **Note:** Orange coloured columns contain formulae to match athlete and pull their toplist rank, commonwealth rank and auto qual information. 
  6. Save sheet as .html file under a new name for final formatting of cell colour and style. Don't forget to save the original spreadsheet file back to .xls workbook format
  7. Copy html file code from the saved sheet and pase in Wordpress webpage editor before Thursday 12pm.  


## Objectives for project development:
  - [ ] fully automate above processes to achieve the desired results. Reducing margin for human error and data sorting mistakes
  - [X] update webscraping program files to pull data from https://www.worldathletics.org/records/toplists/ 
  - [X] better reflect the selection policy rules instead of relying on world ranking points system 
  - [ ] edit main program files to be able to save files on any device. Currently file paths are saving to my desktop (/Users/`my laptop`/Desktop/`my folder name`/)
  - [ ] edit main program files to run chrome driver on any device. Currently it runs chromedriver by finding the application in my laptop Application folder 

