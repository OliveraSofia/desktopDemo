import pytest
import os
from apps.paint import PaintApp
from actions.paint_actions import DrawSquareAction, SaveScreenshot

@pytest.fixture
def paint_app():
    app = PaintApp()
    app.start()
    return app

def test_draw_square_and_save_screenshot(paint_app):
    # Dibuja un cuadrado
    draw_square_action = DrawSquareAction(start_x=184, start_y=260, size=100)
    draw_square_action.execute()

    # Toma una captura de pantalla de la región donde se dibujó el cuadrado

    region = (144, 78, 1217, 669)
    save_path = 'D:\\screenshot\\demo_dibujo.png'
    save_screenshot = SaveScreenshot(region, save_path)
    save_screenshot.execute()

    # Verifica que la captura de pantalla se guardó
    assert os.path.exists(save_path), "La captura de pantalla no se guardó correctamente."

if __name__ == "__main__":
    pytest.main()
