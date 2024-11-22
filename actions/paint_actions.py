import pyautogui
import os

class DrawSquareAction:
    def __init__(self, start_x, start_y, size):
        self.start_x = start_x
        self.start_y = start_y
        self.size = size

    def execute(self):
        pyautogui.moveTo(self.start_x, self.start_y, duration=1)
        pyautogui.mouseDown()
        pyautogui.moveTo(self.start_x + self.size, self.start_y, duration=1)  # Derecha
        pyautogui.moveTo(self.start_x + self.size, self.start_y + self.size, duration=1)  # Abajo
        pyautogui.moveTo(self.start_x, self.start_y + self.size, duration=1)  # Izquierda
        pyautogui.moveTo(self.start_x, self.start_y, duration=1)  # Arriba
        pyautogui.mouseUp()



class SaveScreenshot:
    def __init__(self, region, save_path):
        self.region = region
        self.save_path = save_path

    def execute(self):
        if not os.path.exists(os.path.dirname(self.save_path)):
            os.makedirs(os.path.dirname(self.save_path))

        screenshot = pyautogui.screenshot(region=self.region)
        try:
            screenshot.save(self.save_path)
            print(f"Captura de pantalla guardada exitosamente en {self.save_path}")
        except Exception as e:
            print(f"Error al guardar la captura de pantalla: {e}")
