import sys
sys.path.append('pyglet-2.1.16')
import pyglet
import time
import threading

sys.path.append('pyautogui-master')
import pyautogui

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the primary monitor.
mouseX, mouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
mouseSpd = 5.0 # Speed the mouse will move
    
def main():
    global mouseX, mouseY
    '''pyautogui.click() # Click the mouse at its current location.
    pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
    pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
    pyautogui.doubleClick() # Double click the mouse at the
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
    pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
    pyautogui.press('esc') # Simulate pressing the Escape key.
    pyautogui.keyDown('shift')
    pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
    pyautogui.keyUp('shift')
    pyautogui.hotkey('ctrl', 'c')
    
    screenW, screenH = pyautogui.size()'''
    
    controllers = pyglet.input.get_controllers()
    if len(controllers) > 0:
        controller = controllers[0]
        controller.open()
        #print(controller)

        @controller.event
        def on_stick_motion(controller, name, vector):
            global mouseX, mouseY
            if name == "leftstick":
                print("L: ("+str(vector.x)+", "+str(vector.y)+")")
                mouseX += vector.x * mouseSpd
                mouseY -= vector.y * mouseSpd
                pyautogui.moveTo(mouseX, mouseY) # Move the mouse to the x, y coordinates 100, 150.
            elif name == "rightstick":
                print("R: ("+str(vector.x)+", "+str(vector.y)+")")
        
        @controller.event
        def on_button_press(controller, button_name):
            if button_name == 'a':
                pyautogui.click()
            #elif button_name == 'b':
                # do something else

        pyglet.app.run()

main()


'''
    Pyglet docs: https://pyglet.readthedocs.io/en/latest/programming_guide/input.html
    PyAutoGUI docs: https://github.com/asweigart/pyautogui/tree/master
'''

