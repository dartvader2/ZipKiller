#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importing Required modules

import time
import optparse
import zipfile
import os

# Banner for Zip Killer

xyz = \
    '''\033[1;35m
            /$$                 /$$       /$$ /$$ /$$                    
          |__/                | $$      |__/| $$| $$                    
 /$$$$$$$$ /$$  /$$$$$$       | $$   /$$ /$$| $$| $$  /$$$$$$   /$$$$$$ 
|____ /$$/| $$ /$$__  $$      | $$  /$$/| $$| $$| $$ /$$__  $$ /$$__  $$
   /$$$$/ | $$| $$  \ $$      | $$$$$$/ | $$| $$| $$| $$$$$$$$| $$  \__/
  /$$__/  | $$| $$  | $$      | $$_  $$ | $$| $$| $$| $$_____/| $$      
 /$$$$$$$$| $$| $$$$$$$/      | $$ \  $$| $$| $$| $$|  $$$$$$$| $$      
|________/|__/| $$____/       |__/  \__/|__/|__/|__/ \_______/|__/      
              | $$                                                      
              | $$                                                      
              |__/                
                                      
                        \033[1;31mCrack Zip File Password \033[1;33m
              

-------OPTIONS-------

[1] Crack Zip File
[2] Exit Tool        
\033[0m                                                                          
'''
print(xyz)


# Main Function

def main():
    x = input('[+] Select an Option : ')
    if x == 1:

    # Input path for zip file

        file_path = raw_input('[+] Enter Zip File Path : ')
        file_path = file_path.replace(' ', '')

    # Input path for wordlist file

        word_list = raw_input('[+] Enter Wordlist Path : ') \
            or '/usr/share/wordlists/rockyou.txt'  # Default Rockyou dictionary file
        word_list = word_list.replace(' ', '')
        z_file = zipfile.ZipFile(file_path)
        pwd_list = open(word_list)
        message1 = "\033[\n1;32m[+] Brute Force Initiated ..."
        print(message1)
        message2 = "\033[\n1;36m[+] Checking For Correct Password ..."
        print(message2)
        for line in pwd_list.readlines():
            passwd = line.strip('\n')

    # Password Brute Forcing

            try:
                z_file.extractall(pwd=passwd)
                message3 = "\033[\n1;31m[+] Congrats!! Password Found: " \
                    + passwd + "\n\033[0m"
                print(message3)
                if passwd != '':
                    quit()
            except Exception:
                pass
        message4 = """
\033[1;31m[+] Password Not Found in Given Wordlist
\033[0m"""
        print(message4)
    else:
        message5 = """\033[1;31m
Thank You !!
\033[0m"""
        print(message5)
        time.sleep(1)
        quit()


if __name__ == '__main__':
    main()

