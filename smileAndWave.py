#! python3
# Mouse nudging to keep a screen alive

import pyautogui, time

def smileAndWave():
    nudgeCount = 0
    print("Smile and wave, boys!")
    try:
        while True:
            currentPos = pyautogui.position()
            time.sleep(10)
            newPos = pyautogui.position()
            if newPos == currentPos:
                if nudgeCount % 2 == 0:
                    pyautogui.moveRel(2,0, duration=0.25)
                    print("Keep waving!")
                else:
                    pyautogui.moveRel(-2,0, duration=0.25)
                    print("Keep smiling!")
                nudgeCount = nudgeCount + 1
    except KeyboardInterrupt:
        print("You had " + str(nudgeCount) + " nudges")

smileAndWave()
        
