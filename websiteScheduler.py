import webbrowser
import time

# specify a website in an input format
website = input("Enter the website without www. or .com. Just a word like google, facebook, etc: ")
page = f"https://www.{website}.com"
today = time.strftime('%X %x')

# Constantly check inputs for the time are numbers  

while True:
    hours = input("Enter the hour like 02, 11, 23, etc: ")
    minutes = input("Enter the minutes like 02, 45, 00, etc: ")
    seconds = input("Enter the seconds like 02, 45, 00, etc: ")
    day = input("Enter the day as a number like 02, 22, 31, etc: ")
    month = input("Enter the month as a number like 02 for February, 12 for December. etc: ")
    year = input("Enter the year as a 2 digit number like 21 for 2021: ")
    if hours.isnumeric() and minutes.isnumeric() and seconds.isnumeric() and day.isnumeric() and month.isnumeric() and year.isnumeric():
        break
    else:
        print('Hours, minutes, seconds, day, month and year should be numbers. Please try again!')


timeToOpen = f"{hours}:{minutes}:{seconds} {month}/{day}/{year}"


class Website():
    # a function to open a website and print opened
    def openWebsite():
        webbrowser.open_new(page)
        print(f"Success! {page} website opened")
        print(today)

    #a function to open 5 website after a 3 second wait
    def openFiveTabs():
        for i in range(5):
            webbrowser.open_new_tab(page)
            print(f"page {i} opened")
            time.sleep(3)
            print(today)

    # compares real live time with a specified time in a variable in 
    # the beginning

def setTime():
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


# call a function
setTime()
