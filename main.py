import pyautogui
import time
import datetime
from VM_start import VM_start
from VPN_start import VPN_start
from functions import loading_linear
from functions import loading_linear_times
from functions import scroller
x = ""
y = ""

number = int(input('\nВведите начальный номер ВМ: '))
N = int(input('\nСколько машин хотите создать?\n\
Доступные количества: [1-10], 20, 30..: '))
alphabet = ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
VPN = []
active = True
 
while active:
    add_this = input('\nВведите номер сервера VPN который хотите добавить.\n\
(или \'q\' чтобы закончить добавление): ')
    if add_this == 'q':
        active = False
    else:
        VPN.append(add_this)
dec = ", "
print("\nСписок серверов VPN: " + dec.join(VPN))

if N/10 > len(VPN):
    print('\nНа один сервер VPN может приходиться\n\
максимум 10 машин. Выход из программы...')
    exit()

# Буфер
time.sleep(3)

if N < 10:      #
    M = N       # Заставляет программу использовать
else:           # не больше 10 машин на одном сервере ВПН
    M = 10      #

for vpn in VPN:
    i = 0
    timenow = datetime.datetime.now()
    print("\n" + timenow.strftime("[%H:%M:%S]"), "Подключение сервера VPN " + str(vpn))
    #VPN_start(vpn)

    while i < M:
        timenow = datetime.datetime.now()
        print(timenow.strftime('\n' + "[%H:%M:%S]"), 'Начинаем создание машины ' + str(number) + ' [#' + str(i+1) + '] | VPN: ' + str(vpn))
        if loading_linear('scroller', 3, 3):
            x, y = pyautogui.locateCenterOnScreen('VMBOT//img//scroller.png')
            pyautogui.click(x-50,y-15,duration=1)   # кликнуть на нижнюю ВМ
            pyautogui.rightClick()                  # \
            pyautogui.moveRel(25,-15, duration=0.5) # сортировать
            pyautogui.click()                       # /
            scroller(20)                            # скроллить 20 раз
            pyautogui.click(x-50,y-15,duration=1)   # кликнуть на нижнюю ВМ 

            pyautogui.rightClick()                      # \
            pyautogui.moveRel(25,-320, duration=0.5)    # открыть окно клонирования
            pyautogui.click()                           # /

            # ввод названия машины #

            char = alphabet[number//100]
            date = datetime.date.today()
            name = str(char) + str(number) + " " + str(date.day) + "." + str(date.month) + " US " + str(vpn) + " + bot"
            pyautogui.typewrite(name, interval=0.25)

            # ввод названия завершен #

            pyautogui.press('enter', presses=2, interval=0.5)   # Enter 2 раза

            if loading_linear_times('clon_OK', 80, 15, 8):   # если клонирование закончилось
                pyautogui.moveTo(x-50,y-15,duration=1)      # двигаться к нижней ВМ
                pyautogui.rightClick()                      # \
                pyautogui.moveRel(25,-15, duration=0.5)     # сортировать
                pyautogui.click()                           # /
                scroller(20)                                # скроллить 20 раз

                pyautogui.moveTo(x-50,y-50,duration=0.5)

                print('Запускаем ВМ')
                pyautogui.doubleClick(interval=0.1)

                VM_start()      # модуль функции запуска ВМ и скачивания Brave

                timenow = datetime.datetime.now()
                print(timenow.strftime("[%H:%M:%S]"), 'Завершено создание машины ' + str(number) + ' [#' + str(i+1) + '] | VPN: ' + str(vpn) + '\n')

            else:
                print('Слишком долгое клонирование. Выход из программы...')
                exit()

        else:
            print('Oracle VM Virtual Box Manager сейчас закрыт. Выход из программы...')
            exit()

        i += 1
        number += 1

    else:
        print('Конец потока')