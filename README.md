# CG_quota
Programs for scraping world athletics webpage to determine Australia's top athletes eligible for selection in the 2022 Birmingham Commonwealth Games. 

Before running main program files locally ensure chrome driver is installed on your device
Download links are available here: https://chromedriver.chromium.org/downloads

Also check you have installed selenium to run the webdriver:
- use pip to install selenium 

Current workflow process to update www.commonwealthgames-quota.com.au:
  1. Run X, Y, Z
  2. Combine txt files using A, B, C
  3. Sync xls sheet(x) and format accoring to internal instructions
  4. Save sheet as .html file 
  5. Copy html source code and pase in Wordpress webpage editor before Thursday 12pm.  


Objectives for project development:
  - fully automate above processes to achieve the desired results. Reducing margin for human error and data sorting mistakes
  - update webscraping program files to pull data from https://www.worldathletics.org/records/toplists/ 
  - better reflect the selection policy rules instead of relying on world ranking points system 

