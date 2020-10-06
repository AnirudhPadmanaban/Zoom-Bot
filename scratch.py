
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
    subprocess.Popen(r"C:\Users\com\AppData\Roaming\Zoom\bin\Zoom")
    time.sleep(10)


    join_button = pyautogui.locateOnScreen(r"C:/Users/com/AppData/Roaming/Zoom/bin/join_button_img.png")
    pyautogui.moveTo(join_button)
    pyautogui.click()
    print("Clicked Join Button")
    time.sleep(5)

    meeting_id = pyautogui.locateOnScreen(r"C:/Users/com/AppData/Roaming/Zoom/bin/meeting_id.png")
    pyautogui.moveTo(meeting_id)
    pyautogui.click()
    pyautogui.write(meetingid)
    print("Meeting id")
    time.sleep(5)

    meeting_name = pyautogui.locateOnScreen(r"C:/Users/com/AppData/Roaming/Zoom/bin/meeting_name.png")
    pyautogui.moveTo(meeting_name)
    pyautogui.click()
    pyautogui.typewrite('_17BTRMA006')
    print("Meeting name")
    time.sleep(5)

    join_btn =pyautogui.locateOnScreen(r"C:/Users/com/AppData/Roaming/Zoom/bin/join_meeting_button.png")
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    print("Joined")
    time.sleep(5)

schedule.every().day.at("08:30").do(sign_in,'933 7573 7333','')
schedule.every().day.at("09:45").do(sign_in,'7905281329','')
#schedule.every().day.at("04:20").do(meeting,1)

df/ewee
while True:
    schedule.run_pending()
    time.sleep(1)




















