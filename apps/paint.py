import subprocess
import time
import pyautogui



class PaintApp:
    def __init__(self):
        self.app_path = 'mspaint.exe'

    def start(self):
        subprocess.Popen(self.app_path)
        time.sleep(3)  # Esperar a que Paint se abra

    def click_button(self, x, y): 
        pyautogui.moveTo(x, y, duration=1) 
        pyautogui.click()

