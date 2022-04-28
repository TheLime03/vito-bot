import keyboard


def loop():
    x = 1
    while True:
        print(x)
        x = x+1
        if keyboard.is_pressed('q'):
            print("q pressed")
            break


loop()
