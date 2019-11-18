import time
import pyautogui

def loading_geom(obj, xtime, plustime):
    """Ищет объект несколько раз в течение указанного времени"""
    counter = 0
    objLoc = pyautogui.locateOnScreen('VMBOT//img//' + obj + '.png')
    while counter < 5:
        if isinstance(objLoc, tuple):
            return 1
        else:
            print(obj + ': Test №' + str(counter+1) + ' [Loading Geom]')
            counter += 1
            time.sleep(xtime) 
            xtime += plustime # xtime, xtime+plustime, xtime+plustime*2, ...
    print("Object " + obj + " could not been found. The search is canceled. ")
    return 0

def loading_linear(obj, xtime, secondtime):
    """Ищет объект несколько раз в течение указанного времени"""
    counter = 0
    print(obj + ': Тест №0')
    while counter < 5:
        objLoc = pyautogui.locateOnScreen('VMBOT//img//' + obj + '.png')
        if isinstance(objLoc, tuple):
            return 1
        else:
            print(obj + ': Тест №' + str(counter+1))
            counter += 1
            time.sleep(xtime)
            xtime = secondtime # xtime, secondtime, secondtime, ...
    print("Объект " + obj + " не обнаружен. Завершение поиска... ")
    return 0

def loading_linear_times(obj, xtime, secondtime, times):
    """Ищет объект несколько раз в течение указанного времени"""
    counter = 0
    print(obj + ': Тест №0')
    while counter < times:
        objLoc = pyautogui.locateOnScreen('VMBOT//img//' + obj + '.png')
        if isinstance(objLoc, tuple):
            return 1
        else:
            print(obj + ': Тест №' + str(counter+1))
            counter += 1
            time.sleep(xtime)
            xtime = secondtime # xtime, secondtime, secondtime, ...
    print("Объект " + obj + " не обнаружен. Завершение поиска... ")
    return 0

def scroller111():
    """Десять раз прокручивает скролл вниз"""
    scrollerLoc = pyautogui.locateOnScreen('VMBOT//img//scroller.png')
    if isinstance(scrollerLoc, tuple):
        x, y = pyautogui.locateCenterOnScreen('VMBOT//img//scroller.png')
        pyautogui.moveTo(x,y-15,duration=1)
        j = 0
        while j < 10:
            pyautogui.scroll(-1000)
            j += 1
            print("Scrolling")

def scroller(n):
    """Прокручивает вниз указанное количество раз"""
    print("Скроллим...")
    j = 0
    while j < n:
        pyautogui.scroll(-1000)
        j += 1
    print("Скролл завершен")
