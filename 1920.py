import pyautogui
import time
import datetime

def logger(status):
    """Записывает в файл указанную информацию"""
    timenow = datetime.datetime.now()
    message = timenow.strftime("[%d.%m.%Y %H:%M:%S]") + ' ' + status
    with open('C:/Users/Rubix327/Desktop/python training/VMBOT v4.0/logs.txt', 'a') as file:
        file.write(message)

def scroller(times):
    """Прокручивает вниз указанное количество раз"""
    for i in range(times):
        pyautogui.scroll(-1000)
        i += 1
    # j = 0
    # while j < times:
    #     pyautogui.scroll(-1000)
    #     j += 1

def loading_linear(obj, xtime, secondtime):
    """Ищет объект несколько раз в течение указанного времени"""
    counter = 0
    print(obj + ': Тест №0')
    while counter < 5:
        objLoc = pyautogui.locateOnScreen('C:/Users/Rubix327/Desktop/python training/VMBOT v4.0/img/' + obj + '.png')
        if isinstance(objLoc, tuple):
            return 1
        else:
            print(obj + ': Тест №' + str(counter+1))
            counter += 1
            time.sleep(xtime)
            xtime = secondtime # xtime, secondtime, secondtime, ...
    print("Объект " + obj + " не обнаружен. Завершение поиска... ")
    return 0

referralCodes = []

amount = int(input('\nСколько машин хотите создать? '))
beginNumber = int(input('Какой первый номер машины? '))
city = input('\nКакой город используется в ВПН? ')
counterDecade = 0
createdTimes = 0
w, h = 597, 247

active = True
while active:
    add_this = input('Введите реферальный код или "q": ')
    if add_this == 'q':
        active = False
    else:
        referralCodes.append(add_this)

print('\n1. Убедитесь что иконка VirtualBox находится слева на панели задач!')
print('2. Убедитесь что VPN включен! Если все так, введите Y.')
ans = input('Все так? (Y/N) ')
if ans != 'Y':
    exit()
print('\n')

pyautogui.click(123, 1048, duration=1) # клик на иконку ВМ на панели задач

while amount > 0:
    logger('VM #' + str(beginNumber) + ' - Starting...\n')

    pyautogui.click(615, 1028, duration=1) # клик на скроллер
    scroller(10)
    pyautogui.moveTo(170, 882, duration=1) # движение к ВМ (4 снизу)
    pyautogui.click()

    logger('VM #' + str(beginNumber) + ' - Cloning VM...\n')

    pyautogui.hotkey('ctrl', 'o') # клик на клонировать

    name = 'Q' + str(beginNumber) + ' USA + ' + referralCodes[counterDecade] + ' (' + city + ') (bot)'
    pyautogui.typewrite(name, interval=0.2) # ввод названия машины
    pyautogui.press('enter', presses=2, interval=0.3) # два раза enter
    
    time.sleep(30) # ожидание клонирования

    logger('VM #' + str(beginNumber) + ' - VM cloned. Starting VM...\n')

    pyautogui.moveTo(170, 882, duration=1)
    pyautogui.click()

    time.sleep(1)

    pyautogui.rightClick()
    pyautogui.moveRel(20, -20, duration=1)
    pyautogui.click()

    pyautogui.scroll(-500)

    pyautogui.moveTo(158, 838, duration=1) # движение к ВМ (5 снизу)
    pyautogui.doubleClick() # запуск ВМ

    time.sleep(90)

    logger('VM #' + str(beginNumber) + ' - VM started. Opening browser link...\n')

    pyautogui.moveTo(w, h, duration=1)
    pyautogui.click() # клик на вкладку
    
    time.sleep(5)

    logger('VM #' + str(beginNumber) + ' - Link opened. Downloading browser file...\n')

    if loading_linear('download', 5, 3):
        x, y = pyautogui.locateCenterOnScreen('C:/Users/Rubix327/Desktop/python training/VMBOT v4.0/img/download.png')
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
    else:
        pyautogui.moveTo(660,720, duration=1)
        pyautogui.click()

    logger('VM #' + str(beginNumber) + ' - File downloaded. Opening file...\n')

    if loading_linear('brave_downloaded', 3, 3):
        x, y = pyautogui.locateCenterOnScreen('C:/Users/Rubix327/Desktop/python training/VMBOT v4.0/img/brave_downloaded.png')
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
    else:
        pyautogui.moveTo(1035,325, duration=1)
        pyautogui.click()

    if loading_linear('run', 3, 2):
        x, y = pyautogui.locateCenterOnScreen('C:/Users/Rubix327/Desktop/python training/VMBOT v4.0/img/run.png')
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
    else:
        pyautogui.moveTo(1013, 535, duration=1)
        pyautogui.click()

    time.sleep(420) # ожидание скачивания и установки

    logger('VM #' + str(beginNumber) + ' - File opened. Waiting for installing...\n')

    if loading_linear('installed', 5, 3):
        pyautogui.moveTo(1291, 250, duration=1)
        pyautogui.click()
    else:
        pyautogui.moveTo(1291, 250, duration=1)
        pyautogui.click()

    logger('VM #' + str(beginNumber) + ' - Browser installed. Final process...\n')

    pyautogui.moveTo(950, 470, duration=1)

    scroller(5) # скролл страницы вниз

    pyautogui.moveTo(950, 470, duration=1)
    pyautogui.click() # Let's go

    pyautogui.moveTo(1121, 630, duration=1)
    pyautogui.click(clicks=4, interval=0.3) # next, next, next, done

    pyautogui.moveTo(1332, 237, duration=1)
    pyautogui.click() # клик на крестик на браузере

    logger('VM #' + str(beginNumber) + ' - VM is ready. Shuting down...\n')

    pyautogui.moveTo(585, 810, duration=1)
    pyautogui.click() # клик на пуск

    pyautogui.moveTo(863, 760, duration=1)
    pyautogui.click() # клик на shut down

    time.sleep(10)
    
    # машина создана
    beginNumber += 1
    amount -= 1
    createdTimes += 1

    if createdTimes > 9:
        createdTimes = 0
        counterDecade += 1
        w += 52