# -*- coding: cp1252 -*-

import tenmails
import mailpython
import constcheck
import unseenmail

def main():

  while True:
    unseen = unseenmail.show_unseen()

    print("Gmail Reader UI")
    print("Unreaded Messages:", unseen)
    print("\n(Ten) Check ten most newest emails\n(All) Read all emails\n(Unreaded/Unseen) Show unreaded emails\n(Quit) Shut down program")
    us_answer = input("What is your command? ")

    if us_answer in ("Ten", "ten", "10"):
      action = tenmails.read_gmail()
    elif us_answer in ("All", "all", "Everything"):
      action = mailpython.all_gmail()
    elif us_answer in ("Unreaded", "ureaded", "unseen", "Unseen"):
      action = unseenmail.read_unseen()
    elif us_answer in ("Quit", "quit", "End", "end", "Stop", "stop"):
      print ("Shutting down")
      return False
    else:
      print ("Unknown command")
      
    


if __name__ == '__main__':
    main()