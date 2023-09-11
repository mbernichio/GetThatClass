Overview:
This is a python script that out logs-in and registers for the class you want so you can quickly get the class you want before all of the slots fill up.

Before running script:

    Download the selenium driver:

    cd /tmp
    wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_mac64.zip 
    unzip chromedriver_mac64.zip -d /usr/local/bin

    pip3 install selenium

    This driver is needed to run the login script.

Steps:

    1. Fill out info.json with correct info using text editor.
        - username = your netid
        - password = your password
        - department = department code of class you are trying to get into - Ex. "ECE"
        - class_num = the number your class appears starting from "0" (zero-indexed) at the top of the page to "n" at the bottom of the page, the page being the classic registration page after you pick your department and all of the courses in that department are listed. - Ex. If you are trying to get into ECE 110, you would put 0. If you are trying to get into ECE 210, you would put 6, since it is 7 spots down.
        - crn = list of all crn numbers you are trying to get into, put them all in there. Ex. If you just are trying to get into a lecture, you would put "lecture_crn in the brackets. If you need a discussion + lecture, you would put "lecture_crn","discussion_crn" into the brackets. If lecture_crn = 2020 and dicussion_crn was 2021 it would look like this "crn" = ["2020","2021"]. 
        
    2. Run Script
        - python3 register.py

    3. Get that class!
