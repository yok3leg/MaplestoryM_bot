import cv2
import numpy as np
import mss
from pyautogui import press, typewrite, hotkey
import win32gui
import time

def main():
    win_id = "yokbotting02"
    i=0
    print(i)
    ab_status = cv2.imread("ab_button.png", cv2.IMREAD_GRAYSCALE)
    ab_status2 = cv2.imread("ab_button2.png", cv2.IMREAD_GRAYSCALE)    
    accept_button = cv2.imread("accept_quest_button.png", cv2.IMREAD_GRAYSCALE)
    complete_button = cv2.imread("complete_quest_button.png", cv2.IMREAD_GRAYSCALE)
    speak_button = cv2.imread("speak_button.png", cv2.IMREAD_GRAYSCALE)
    claim_button = cv2.imread("claim_reward_button_after_quest.png", cv2.IMREAD_GRAYSCALE)
    confirm_lvlup_button = cv2.imread("confirm_lvlup_button.png", cv2.IMREAD_GRAYSCALE)        
    confirm_quest_button = cv2.imread("confirm_quest_button.png", cv2.IMREAD_GRAYSCALE) 

    while i<1000:
        # Load the reference image
        with mss.mss() as sct:
            # Get the screenshot
            sct_img = np.array(sct.grab(sct.monitors[0]))

            # Convert the screenshot to grayscale
            gray_img = cv2.cvtColor(sct_img, cv2.COLOR_BGR2GRAY)

            # Use template matching to find the area that matches the reference image
            ab_result = cv2.matchTemplate(gray_img, ab_status, cv2.TM_CCOEFF_NORMED)
            _, ab_max_val, _, _ = cv2.minMaxLoc(ab_result)
            ab_result2 = cv2.matchTemplate(gray_img, ab_status2, cv2.TM_CCOEFF_NORMED)
            _, ab_max_val2, _, _ = cv2.minMaxLoc(ab_result2)

            accept_button_result = cv2.matchTemplate(gray_img, accept_button, cv2.TM_CCOEFF_NORMED)
            _, accept_button_max_val, _, _ = cv2.minMaxLoc(accept_button_result)

            complete_button_result = cv2.matchTemplate(gray_img, complete_button, cv2.TM_CCOEFF_NORMED)
            _, complete_button_max_val, _, _ = cv2.minMaxLoc(complete_button_result)        

            speak_button_result = cv2.matchTemplate(gray_img, speak_button, cv2.TM_CCOEFF_NORMED)
            _, speak_button_max_val, _, _ = cv2.minMaxLoc(speak_button_result)

            claim_button_result = cv2.matchTemplate(gray_img, claim_button, cv2.TM_CCOEFF_NORMED)
            _, claim_button_max_val, _, _ = cv2.minMaxLoc(claim_button_result)

            confirm_lvlup_button_result = cv2.matchTemplate(gray_img, confirm_lvlup_button, cv2.TM_CCOEFF_NORMED)
            _, confirm_lvlup_button_max_val, _, _ = cv2.minMaxLoc(confirm_lvlup_button_result)

            confirm_quest_button_result = cv2.matchTemplate(gray_img, confirm_quest_button, cv2.TM_CCOEFF_NORMED)
            _, confirm_quest_button_max_val, _, _ = cv2.minMaxLoc(confirm_quest_button_result)

            # Send the key to the middle point
            if confirm_lvlup_button_max_val>0.8:
                # Get the window handle of the target window
                target_window = win32gui.FindWindow(None, win_id)
                # Focus the target window
                win32gui.SetForegroundWindow(target_window)   
                for i in range(2):         
                    press('6')  

            print(ab_max_val)
            print(ab_max_val2)
            if ab_max_val>0.6 or ab_max_val2>0.6:
                # Get the window handle of the target window
                target_window = win32gui.FindWindow(None, win_id)
                # Focus the target window
                win32gui.SetForegroundWindow(target_window)            
                press('7')
                i=i+1
                print(i)   
                time.sleep(1)   

            #print(speak_button_max_val)
            if speak_button_max_val>0.8:
                # Get the window handle of the target window
                target_window = win32gui.FindWindow(None, win_id)
                # Focus the target window
                win32gui.SetForegroundWindow(target_window)   
                for i in range(10):         
                    press('0') 
                time.sleep(1)         

            #print(accept_button_max_val)
            if accept_button_max_val>0.8 or complete_button_max_val>0.8 or confirm_quest_button_max_val>0.8:
                # Get the window handle of the target window
                target_window = win32gui.FindWindow(None, win_id)
                # Focus the target window
                win32gui.SetForegroundWindow(target_window)   
                for i in range(2):         
                    press('9')    

            if claim_button_max_val>0.8:
                # Get the window handle of the target window
                target_window = win32gui.FindWindow(None, win_id)
                # Focus the target window
                win32gui.SetForegroundWindow(target_window)   
                for i in range(2):         
                    press('8')  

            time.sleep(1)      

if __name__ == '__main__':
    main()        