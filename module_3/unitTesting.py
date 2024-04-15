import os.path
import sys

def TestKey(key):                                           #tests if a key exists
    if(bool(key)):
       return True
    else:
        return False
    
def Outputs():                                             #tests if the first output goes through to make file
        if(os.path.isfile("Data/ai_gen/output_0.txt")):
            print("")
        else:
            print("First output failed, please try again")
            sys.exit()

def UrlFileExists():                                        #tests if the urls.txt file exists at all
    if(os.path.isfile("urls.txt")):
       print("")
    else:
        print("No urls.txt file found.")
        sys.exit()

def CountWords(filename):                                   #tests the number of spaces in summary to see how many words are used.(should be <=49)
    with open(filename, 'r') as file:
        lines = file.readlines()
        second_line = lines[1]
        space_count = second_line.count(' ')
        print(space_count)
        return space_count

