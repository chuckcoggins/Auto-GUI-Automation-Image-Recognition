#! python 3
import pyautogui, time, os
cwd = os.getcwd()
os.chdir(cwd)

pyautogui.moveTo(2368, 341, duration=1.1)   # move to chrome maximize tab
pyautogui.click(2368, 341)
pyautogui.moveTo(332, 52, duration=1.1)     # move to search
pyautogui.click(332, 52)
pyautogui.typewrite('facebook.com', interval=0.1)
pyautogui.press('enter')
time.sleep(2)

charlie = pyautogui.locateCenterOnScreen('charlie.png')
pyautogui.moveTo(charlie, duration=0.5)
pyautogui.click(charlie)
time.sleep(1)

# Create Message
pyautogui.moveTo(1094, 653, duration=0.5)
pyautogui.click(1094, 653)
pyautogui.typewrite('I am the most Powerful Jedi Ever!', interval=0.2)

# add gif
pyautogui.moveTo(1435, 832, duration=1)
pyautogui.click(1435, 832)
time.sleep(1)
pyautogui.click(1092, 290)
pyautogui.typewrite('high ground ', interval=0.1)
time.sleep(3)
obiwan = pyautogui.locateCenterOnScreen('highground.png')
pyautogui.moveTo(obiwan, duration=0.5)
pyautogui.click(obiwan)
time.sleep(10)

# Post
pyautogui.moveTo(1265, 1020, duration=0.5)
pyautogui.click(1265, 1020)
pyautogui.click()
pyautogui.click(1192, 1020)
time.sleep(2)

# funny

pyautogui.moveTo(322, 55, duration=0.5)
pyautogui.click(322, 55)
pyautogui.typewrite(['w', 'w', 'w', '.', 'p', 'o', 'r', 'n', 'h', 'u', 'b', '.', 'c', 'o', 'm',
                     'backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace',
                     'backspace', 'backspace', 'backspace', 'backspace', 'backspace',
                     'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm'], interval=0.3)
pyautogui.press('enter')
time.sleep(2)

# wolcen
pyautogui.moveTo(1063, 446, duration=0.2)
pyautogui.click(1063, 446)
pyautogui.typewrite('Wolcen: Lords of Mayhem', interval=0.2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(243, 500, duration=0.1)
pyautogui.click(243, 500)


