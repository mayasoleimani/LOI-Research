# Life of Introspection -- Personal NLP Research Project 📖
## Maya Soleimani
### Summer I&II     -     University of Michigan - Dearborn

# 

### This project parses through 300 diary entries in a 10 year range, capable of different statistics of your choosing of emotional polarity vs. specified independent variables.
#
### Requirements:
#
#### + Written in *Python*
#### Libraries used: 
#### + import datetime
#### + from matplotlib import pyplot as plt
#### + from nltk.sentiment import SentimentIntensityAnalyzer
#### Files Needed:
#### + loi.py
#### + .txt file with your entries where each line follows this format: 
####    “05/17/2014 1853 Today was such a bad day, and I’m just not feeling well overall. For some reason, it’s been so hard to wake up in the morning. 1906”
#### (date, start time, entry, end time)
#### + .txt with manually labeled polarity score with entry to test accuracy. Amount of lines should be a decent chunk of original entries, in this project I used approximately 1/10th of original data. The format of this file follows this format:
#### "negative Today was such a bad day, and I’m just not feeling well overall. For some reason, it’s been so hard to wake up in the morning."

## Instructions:

<img width="600" alt="image" src="https://github.com/mayasoleimani/LOI-Research/assets/82066258/9843c3b3-c521-4c50-964e-33180f43f9b7">

# 

* In this section, you may type: 'Year range','Winter', 'Summer', 'Spring', 'Fall', 'Words', 'Started', OR 'Duration' without quotations marks.

#

<img width="420" alt="image" src="https://github.com/mayasoleimani/LOI-Research/assets/82066258/a3e13921-dadc-403b-b84f-d4821738a5d9">

#

* Let say you've chosen the year range 2016-2019, you will be then asked for two events A & B.

#

<img width="450" alt="image" src="https://github.com/mayasoleimani/LOI-Research/assets/82066258/ed662ef1-426c-4bef-8381-fbc02956abc0">

#

* Here you will enter input based on what the options say. After that you will receive a bayes probability and a plot of polarity vs. the indepdent variable you selected previously.

#

<img width="400" alt="image" src="https://github.com/mayasoleimani/LOI-Research/assets/82066258/3a7072d5-ddb5-4148-8fe2-599cca4a49ef">

# 
<img width="476" alt="image" src="https://github.com/mayasoleimani/LOI-Research/assets/82066258/4baf923f-5a11-4890-a72f-c36d30938697">

#

* Boom! You have instant insight results on your emotional polarity, based on your personal writing!

#

### Current known errors:
#####
##### * In second I/O request from user (Bayes functionality), no error checking for user input ('Event A= ' & 'Event B= ')
