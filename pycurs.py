#!/usr/bin/env python

from os import system
import curses

def getParam(prompt_str):
    myscr.clear()
    myscr.border(0)
    myscr.addstr(12, 25, 'Python Curses little program')
    myscr.refresh()
    choice  = myscr.getch(10, 10, 60)
    return choice

def execCmd(cmd_str):
    system("clear")
    a = system(cmd_str)
    print("")
    if a == 0:
        print("Command executed sucessfully")
    else:
        print("Error occurring")
    raw_input("Press enter to exit")
    print("")

x = 0

while x != ord('4'):
    myscr = curses.initscr()

    myscr.clear()
    myscr.border(0)
    myscr.addstr(2, 2, "Please enter a number ...")
    myscr.addstr(4, 4, "1 - Add a user")
    myscr.addstr(5, 4, "2 - Restart Apache")
    myscr.addstr(6, 4, "3 - Show Disk space")
    myscr.addstr(7, 4, "4 - Exit")
    myscr.refresh()

    x = myscr.getch()

    if x == ord('1'):
        username = getParam("Enter the username")
        homedir = getParam("Enter the home directory, eg /home/joe")
        groups = getParam("Enter comma-separated groups, eg adm,cdrom")
        shell = getParam("Enter the shell, eg /bin/bash:")
        curses.endwin()
        execCmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s" \
                + shell + " " + username)

    if x == ord('2'):
        curses.endwin()
        execCmd('apachectl restart')

    if x == ord('3'):
        curses.endwin()
        execCmd('df -h')

curses.endwin()
