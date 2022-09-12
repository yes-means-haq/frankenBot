import keyboard  
while True:  
    try:  
        if keyboard.is_pressed('up'):  
            print('You Pressed up!')
            break  
    except:
        break  