# действия бота после захода в ВМ
import pyautogui
import time
from functions import loading_linear
from functions import loading_linear_times
from functions import scroller
x = ""
y = ""

time.sleep(3)

def VM_start():
    if loading_linear_times('recycle', 25, 5, 20):
        x, y = pyautogui.locateCenterOnScreen('VMBOT//img//recycle.png')
        pyautogui.moveTo(x,y+100,duration=1)  # перемещение к браузеру
        pyautogui.doubleClick(interval=0.1)
        pyautogui.press('enter')
        time.sleep(3)
        if loading_linear_times('profile_OK', 2, 1, 4):
            x, y = pyautogui.locateCenterOnScreen('VMBOT//img//profile_OK.png')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()
            if loading_linear('support_me',3,2):
                x, y = pyautogui.locateCenterOnScreen('VMBOT//img//support_me.png')
                pyautogui.moveTo(x,y,duration=0.5)
                pyautogui.click()
        # if loading_linear_times('cross',5,2,8):
        #     x, y = pyautogui.locateCenterOnScreen('VMBOT//img//cross.png')
        #     pyautogui.moveTo(x,y,duration=0.5)
        #     pyautogui.click()
        if loading_linear("brave_logo", 2, 1):
            x, y = pyautogui.locateCenterOnScreen('VMBOT//img//brave_logo.png')
            pyautogui.moveTo(x,y+100,duration=1) # перемещение под лого Brave
            pyautogui.scroll(-200)
            time.sleep(1)
            downloadLoc = pyautogui.locateOnScreen('VMBOT//img//download.png')
            if isinstance(downloadLoc, tuple):
                x,y = pyautogui.locateCenterOnScreen('VMBOT//img//download.png')
                pyautogui.moveTo(x,y,duration=1)
                pyautogui.click()
                if loading_linear_times('cancel', 2, 1, 10):
                    x,y = pyautogui.locateCenterOnScreen('VMBOT//img//cancel.png')
                    pyautogui.moveTo(x-100,y,duration=0.5)
                    pyautogui.click()
                    if loading_linear_times('saved', 3, 1, 10):
                        x,y = pyautogui.locateCenterOnScreen('VMBOT//img//saved.png')
                        pyautogui.moveTo(x,y,duration=0.5)
                        pyautogui.tripleClick(interval=0.1)
                        if loading_linear('minimize',1,1):
                            x,y = pyautogui.locateCenterOnScreen('VMBOT//img//minimize.png')
                            pyautogui.moveTo(x,y,duration=0.5)
                            pyautogui.doubleClick()
                            if loading_linear_times('run', 5, 2, 10):
                                x,y = pyautogui.locateCenterOnScreen('VMBOT//img//run.png')
                                pyautogui.moveTo(x,y,duration=1)
                                pyautogui.click()
                                if loading_linear_times('triangle1', 60, 15, 25):
                                    x,y = pyautogui.locateCenterOnScreen('VMBOT//img//triangle1.png')
                                    pyautogui.moveTo(x,y,duration=1)
                                    pyautogui.click()
                                    if loading_linear('privacy_policy', 2, 2):
                                        x,y = pyautogui.locateCenterOnScreen('VMBOT//img//privacy_policy.png')
                                        pyautogui.moveTo(x,y,duration=1)
                                        pyautogui.click()
                                        if loading_linear('triangle', 3, 3):
                                            x,y = pyautogui.locateCenterOnScreen('VMBOT//img//triangle.png')
                                            pyautogui.moveTo(x,y,duration=1)
                                            pyautogui.click()
                                            if loading_linear_times('join_rewards', 2, 1, 10):
                                                x,y = pyautogui.locateCenterOnScreen('VMBOT//img//join_rewards.png')
                                                pyautogui.moveTo(x,y,duration=1)
                                                pyautogui.click()
                                                time.sleep(5)
                                                if loading_linear('close', 3, 3):
                                                    x,y = pyautogui.locateCenterOnScreen('VMBOT//img//close.png')
                                                    pyautogui.moveTo(x+10,y,duration=1)
                                                    pyautogui.click()
                                                    if loading_linear('pusk', 1, 3):
                                                        x,y = pyautogui.locateCenterOnScreen('VMBOT//img//pusk.png')
                                                        pyautogui.moveTo(x,y,duration=0.5)
                                                        pyautogui.click()
                                                        if loading_linear('shutdown', 1, 3):
                                                            x,y = pyautogui.locateCenterOnScreen('VMBOT//img//shutdown.png')
                                                            pyautogui.moveTo(x,y,duration=0.5)
                                                            pyautogui.click()
                                                            if loading_linear_times('clon_OK', 15, 10, 7):
                                                                x,y = pyautogui.locateCenterOnScreen('VMBOT//img//clon_OK.png')
                                                            else:
#                                                               print('clon_OKLoc не обнаружен. Выход из программы...')
                                                                exit()
                                                        else:
#                                                           print('shurdownLoc не обнаружен. Выход из программы...')
                                                            exit()
                                                    else:
#                                                       print('puskLoc не обнаружен. Выход из программы...')
                                                        exit()
                                                else:
    #                                               print('closeLoc (Brave) не обнаружен. Выход из программы...')
                                                    exit()
                                        else:
    #                                       print("triangleLoc не обнаружен. Выход из программы...")
                                            exit()
                                    else:
    #                                   print("privacyPolicyLoc не обнаружен. Выход из программы...")
                                        exit()
                                else:
    #                               print("triangle1Loc не обнаружен. Выход из программы...")
                                    exit()
                            else:
    #                           print("runLoc не обнаружен. Выход из программы...")
                                exit()
                        else:
#                           print('minimizeLoc не обнаружен. Выход из программы...')
                            exit()
                    else:
#                       print("savedLoc не обнаружен. Выход из программы...")
                        exit()
                else:
#                   print("saveLoc не обнаружен. Выход из программы...")
                    exit()
            else:
#               print("downloadLoc не обнаружен. Выход из программы...")
                exit()
        else:
#           print("Слишком долгая загрузка страницы браузера. Выход из программы...")
            exit()
    else:
#       print("Слишком долгая загрузка ВМ. Выход из программы...")
        exit()