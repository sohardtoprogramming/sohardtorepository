import os
import sys


def Parsing():
    Parsing_list = ['<< 1. id >>',
                    '<< 2. curl -s ifconfig.me >>',
                    '<< 3. ip addr >>',
                    '<< 4. arp -a >>']
    return Parsing_list
     

def Check():
    FL = list()
    if os.path.exists() != True:
        print("don't have File, Check your directory")
        
    else:
        FL = os.path.exists()
        Parser = Parsing()
        for i in FL:
            with open() as f:
                f.readlines
            

if __name__ == '__main__':
    pass