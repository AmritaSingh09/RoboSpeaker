import os

if __name__ == '__main__':
    print("Welcome to Robo  Speaker 1.1")
    os.system('say "Welcome to Robo  Speaker 1.1"')
    os.system('say "Enter what you want me to speak And I will speak for u"')

    while(True):
        x = input("Enter what you want me to speak: ")
        if x == "q":
            break
        command = f"say {x}"
        os.system(command)

