import platform
import time
import os
from pynput import keyboard


#comments are for loosers
lf = "lf.txt"
if not os.path.exists(lf):
    with open("lf.txt", "x") as file:
            file.write("")
else:
    with open("lf.txt", "r") as file:
        li = [line.strip() for line in file]

option = None

def on_press(key):
    global option
    try:
        if key.char in ['1', '2', '3', '4']:
            option = key.char  # Fixed: removed f-string
            return False
    except AttributeError:
        pass


def menu():
    clear_console()

    print("you're finally home ^^")
    time.sleep(1)
    
    print("view list (1)")
    time.sleep(0.5)
    
    print("add task (2)")
    time.sleep(0.5)
    
    print("remove task (3)")
    time.sleep(0.5)
    
    print("close (4)")
    time.sleep(1)
    
    print("take your chosing")
    
    global option
    option = None  # Reset option at start
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
    try:
        if option == "1":
            view()
            menu()  
        elif option == "2":
            add()
            menu()
        elif option == "3":
            remove()
            menu()
        elif option == "4":
            close()
        else:
            print("you're my silly goober")
            time.sleep(5)
            menu()
    except Exception as e:
        print(f"sowwy >< {e}")
        time.sleep(2)
        menu()


def view():
    clear_console()

    if not li:
        print("you're my silly goober")
        time.sleep(5)
        return
    else:
        for index, task in enumerate(li, start = 1):
            print(f"{index}. {task}")
        input("enter any input to continue")
    clear_console()


def add():
    clear_console()

    task = input("what dont you want to do")
    li.append(task)
    print(f"you dont want to do {task}")
    with open("lf.txt", "w") as file:
        for item in li:
            file.write(item + "\n")



def remove():
    clear_console()
    view()
    num = int(input("what did you finally decide to not do"))

    if 1 <= num <= len(li):
        remove = li.pop(num - 1)
        clear_console()
        print("task sucessfully avoided")
    else:
        clear_console()
        print("thinking ahead i like that pookie :3")
        time.sleep(1)
        print("but.....")
        time.sleep(2)
        print("i cant remove somthing that doent exist")
        time.sleep(3)
        print("sowwy >< 3:")
        with open("lf.txt", "w") as file:
            for item in li:
                file.write(item + "\n")


def close():
    clear_console()

    print("why")
    time.sleep(5)
    c1 = input("are you sure >< (y/n)")
    
    if c1 == "n":
        menu()
    if c1 == "y":
        c2 = input(":( really (y/n)")
        clear_console()
        if c2 == "n":
            menu()
        if c2 == "y":
            with open("lf.txt", "w") as file:
                for item in li:
                    file.write(item + "\n")
            print("okay")
            time.sleep(10)
            print("...fine")
            time.sleep(15)
            exit()


def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')




if __name__ == "__main__":
    menu()

