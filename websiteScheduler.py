import webbrowser
import time


# a function to check input for int or str 

## Future idea: maybe create def checkInput():

# the default value is open one page


# specify a website in an input format

# check if the input isalphabet or a word not a number or anything else
while True:
    website = input("Enter the website without www. or .com. Just a word like google, facebook, etc: ")
    if website.isalpha():
        break
    else:
        print('The website name need to be word not a number. Please try again!')

page = f"https://www.{website}.com"
today = time.strftime('%X %x')

# asking which function to use wether to use one or five tabs option when opening a website

request = input('Type (1) if you want one new window or (2) for five tabs for the same website. The default value is (1): ')

if request != '2':
    print("Ok! I'll use the default which is one new window")
    request = 1
else:
    request = 2

# Constantly check inputs for the time are numbers  

while True:
    hours = input("Enter the hour like 02, 11, 23, etc: ")
    minutes = input("Enter the minutes like 02, 45, 00, etc: ")
    seconds = input("Enter the seconds like 02, 45, 00, etc: ")
    day = input("Enter the day as a number like 02, 22, 31, etc or if it's TODAY say yes to Skip: ")

# an option to skip adding the full day if it's the same day and just confirm. The is some number check sanitation

    if day == 'yes' or day == 'YES' or day == 'y' or day == 'Y':
        timeToOpen = f"{hours}:{minutes}:{seconds}" + time.strftime(' %x')
        if hours.isnumeric() and minutes.isnumeric() and seconds.isnumeric():
            break
        else:
            print('Hours, minutes, seconds, should be numbers. Please try again!')
            continue
    month = input("Enter the month as a number like 02 for February, 12 for December. etc: ")
    year = input("Enter the year as a 2 digit number like 21 for 2021: ")

# sanitise code by making sure the input is a number not anything else

    if hours.isnumeric() and minutes.isnumeric() and seconds.isnumeric() and day.isnumeric() and month.isnumeric() and year.isnumeric():
        timeToOpen = f"{hours}:{minutes}:{seconds} {month}/{day}/{year}"
        break
    else:
        print('Hours, minutes, seconds, day, month and year should be numbers. Please try again!')

# class website with open one website or several tabs same website methods to be called later

class Website():
    # a function to open a website and print opened
    def openWebsite():
        webbrowser.open_new(page)
        print(f"Success! {page} website opened")
        print(today)

    #a function to open 5 website after a 3 second wait
    def openTabs():
        for i in range(5):
            webbrowser.open_new_tab(page)
            print(f"Success! {page} tab number {i+1} opened")
            time.sleep(3)
            print(today)

    # compares real live time with a specified time in a variable in 
    # the beginning

def openOneWebsite():
    while time.strftime('%X %x') != timeToOpen:
        timeNow = time.strftime('%X %x')
# checks if local time is bigger than or equal the inputted time and opens the website if so
        if timeNow >= timeToOpen:
            print("It's A Match")
            print (timeNow + " vs " + timeToOpen)
            Website.openWebsite()
            break
        print("waiting!")
        print (timeNow + " vs " + timeToOpen)
        time.sleep(3)

def openFiveTabs():
    while time.strftime('%X %x') != timeToOpen:
        timeNow = time.strftime('%X %x')
# checks if local time is bigger than or equal the inputted time and opens the website if so
        if timeNow >= timeToOpen:
            print("It's A Match")
            print (timeNow + " vs " + timeToOpen)
            Website.openTabs()
            break
        print("waiting!")
        print (timeNow + " vs " + timeToOpen)
        time.sleep(3)

# call a function
if request == 2:
    openFiveTabs()
else:
    openOneWebsite()