import pyautogui
import time
import random
print(pyautogui.size())
count = 0
while count <10:
    current_position = pyautogui.position()
    time.sleep(200)    
    new_position = pyautogui.position()
    print(current_position,' -----> ',new_position)
    if current_position != new_position:
        time.sleep(10)
    else:
        if count%2 == 0:
            x = random.randint(955, 985)
        else:
            x = random.randint(1015, 1045)
        y = random.randint(455,545)
        d = random.randint(7, 20)
        print(pyautogui.position(),'--',d)
        pyautogui.moveTo(x,y,duration=d)
        mouse_x, mouse_y = pyautogui.position()
        print(pyautogui.position(),'--',d)
        pyautogui.scroll(d)
        count += 1