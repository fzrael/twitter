import requests as s
import sys, os, time, signal, webbrowser, platform, subprocess
from time import sleep


def signal_handler(signal, frame):
    KURO()
    LOGO()
    print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')
    time.sleep(0)
    EXITMENU()


signal.signal(signal.SIGINT, signal_handler)


# ~~~ Function KURO ~~~~
def KURO():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# -------------------------------


def ketik(s):
    for ASU in s + '\n':
        sys.stdout.write(ASU)
        sys.stdout.flush()
        sleep(30. / 999)




print(' ')
ketik(
    "\033[0;31m Welcome To My tool Target Twitter account ...\033[0;31m")
sleep(0.0)

print('''
                        ==================================
                        |   [Target Twitter account]     |
                        |--------------------------------|
                        |       snapchat: xd0sry         |
                        |       github: fzrael           |
                        |--------------------------------|
	''')

base_url = 'https://twitter.com/users'
email_sub_url = '/email_available?email='
username_sub_url = '/username_available?username='

def main():
    while True:
        print("\n>---------------------------------------->\n1 Traget Twitter date"
              "\n2 Traget Old Msg \n3 Snapchat Me Arar ^_- \nPress { q } to quit.\n\n")
        option = input("Your Option: ")
        if option == 'q' or option == 'Q':
            break

        elif option == '1':
            username = input(" username: ")
            datamsg =  input ("Traget date 0000-00-00: ")

            webbrowser.open('https://twitter.com/search?q=from:'+ username + ' until:'+datamsg)

        elif option == '2':
            username = input(" username: ")
            traget = input("Traget old msg :")
            webbrowser.open('https://twitter.com/search?q=from:' + username + '  ' f'{traget}')

        elif option == '3':
            webbrowser.open('https://www.snapchat.com/add/xd0sry')

            continue


if __name__ == '__main__':
    main()