
import pyautogui
import subprocess
import time
import pandas as pd
from datetime import datetime
import xlrd
import openpyxl
import os
import csv
import pause
import schedule
import requests


def sign_in(meetingid, meetingpswd):

    now = datetime.now().strftime("%H:%M")
    print(now)
    subprocess.Popen(r"C:\Users\com\AppData\Roaming\Zoom\bin\Zoom")# Opens zoom app on Desktop. Goes to the location and finds the zoom app location
    time.sleep(10)


    join_button = pyautogui.locateOnScreen(r"C:/Users/com/AppData/Roaming/Zoom/bin/join_button_img.png")# Clicks Join logo. The image of the join button is stored in the given location, so pyautogui goes there and finds the image and compares it with the zoom app.If the images match, it will click the join logo, else return None.
    pyautogui.moveTo(join_button)
    pyautogui.click()
    print("Clicked Join Button")
    time.sleep(5)

    meeting_id = pyautogui.locateOnScreen(r"C:/Users/com/AppData/Roaming/Zoom/bin/meeting_id.png")# Inputs meeting id.The image of the meeting id button is stored in the given location, so pyautogui goes there and finds the image and compares it with the zoom app.If the images match, it will click the meeting id and inut the id, else return None.
    pyautogui.moveTo(meeting_id)
    pyautogui.click()
    pyautogui.write(meetingid)# Inputs meeting id
    print("Meeting id")
    time.sleep(5)

    meeting_name = pyautogui.locateOnScreen(r"C:/Users/com/AppData/Roaming/Zoom/bin/meeting_name.png")# Inputs meeting name.The image of the meeting name  is stored in the given location, so pyautogui goes there and finds the image and compares it with the zoom app.If the images match, it will click the meeting name, else return None.
    pyautogui.moveTo(meeting_name)
    pyautogui.click()
    pyautogui.typewrite('_17BTRMA006')# Inputs the meeting name. You can give any name within the quotes
    print("Meeting name")
    time.sleep(5)

    join_btn =pyautogui.locateOnScreen(r"C:/Users/com/AppData/Roaming/Zoom/bin/join_meeting_button.png") # Clicks Join Button. The image of the Join button is stored in the given location, so pyautogui goes there and finds the image and compares it with the zoom app.If the images match, it will click the join button, else return None.
    pyautogui.moveTo(join_btn)
    pyautogui.click() #Clicks the join button and logs in
    print("Joined")
    time.sleep(5)

schedule.every().day.at("08:30").do(sign_in,'933 7573 7333','') #Schedules meeting at a given time and calls sign_in function. Change id's accordingly for your class
schedule.every().day.at("09:45").do(sign_in,'7905281329','')  #Schedules meeting at a given time and calls sign_in function. Change id's accordingly for your class
#schedule.every().day.at("04:20").do(meeting,1)

while True:
    schedule.run_pending()
    time.sleep(1)























