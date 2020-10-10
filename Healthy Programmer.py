

# Healthy Programmer
# This program helps by reminding a person to drink water, do physical exercise and relax eyes at regular intervals of time

"""
9 am - 5 pm
Reminder to drink water - play water.mp3 - 3.5 litres daily - "Drank" to stop - Log
Reminder to rest eyes - play eyes.mp3 - every 30 min - "EyDone" to stop - log
Reminder for physical exercise - play physical.mp3 - every 45 min - "ExDone" to stop - log
"""

from datetime import datetime    # For current hour and logging
from pygame import mixer         # For playing alarm
import time                      # For current time in seconds


def reminder(music_file, stopper, log_text, task_name):
    # Stopper is the msg the user inputs to stop the alarm
    # Task name is displayed to the user

    print(f"\n\n{task_name}")
    while True:
            mixer.init()
            mixer.music.load(str(music_file))
            mixer.music.play()
            stp = input(f"\nEnter {str(stopper)} if task done: ")
            if stp == stopper:
                lg = open("Logs.txt", "a")
                lg.write(str(datetime.now()) + " : " + str(log_text)+ "\n") #logger
                lg.close()
                print("Data Logged!!")
                break
            else:
                continue



water_every = 70*60  # Water drunk after every 70 mins = 70 x 60 seconds
eye_every = 30*60 # Eye exercise every 30 mins converted to secs
phy_every = 45*60 # Physical exercise every 45 mins or 45*60 secs
time_hr = datetime.now().hour #Current time in hour
last_water = time.time()  # Water , eye and physical exercise last done. Update constant
last_eye= time.time()
last_phy = time.time()

while time_hr<17 and time_hr>=9:
    # set for 9 a.m to 5 pm
    ctime = time.time()
    time_hr = datetime.now().hour

    if ctime >= (water_every+last_water):
        reminder("water.mp3", "drunk" , "Drunk Water", "********** DRINK WATER **********")

    elif ctime >= (eye_every+last_eye):
        reminder("eye.mp3", "done", "Relaxed Eyes", "********** DO SOME EYE EXERCISE **********")

    elif ctime >= (phy_every+last_phy):
        reminder("physical.mp3", "done", "Physical exercise done", "********** GET UP, DO SOME PHYSICAL EXERCISE **********")

