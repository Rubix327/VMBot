import pyautogui
import time
from functions import loading_linear
from functions import loading_linear_times
x = ""
y = ""

def VPN_start(vpn):
    """Принимает номер сервера ВПН и включает его"""
    if loading_linear('nord_icon', 1, 1):
        x, y = pyautogui.locateCenterOnScreen('VMBOT//img//nord_icon.png')
        pyautogui.click(x,y,duration=1)
        if loading_linear('vpn//' + str(vpn), 1,1):
            x,y = pyautogui.locateCenterOnScreen('VMBOT//img//vpn//' + str(vpn) + '.png')
            pyautogui.click(x,y,duration=1)
            if loading_linear_times('connected',5,3,10):
                if loading_linear('VM',1,1):
                    x,y = pyautogui.locateCenterOnScreen('VMBOT//img//VM.png')
                    pyautogui.click(x,y,duration=1)
                else:
                    exit()
            else:
                exit()
        else:
            exit()
    else:
        exit()