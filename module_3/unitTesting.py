
import requests
import os
import os.path
import sys
from bs4 import BeautifulSoup

def has_url():
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
    
    if(contains_com(urls)):
        #print("found urls")
        return urls
    
    else:
        print("No urls")
        sys.exit()

    
def has_title(soup):
              
    title = soup.find('title').get_text()
    if(bool(title)):
        #print("title found")
        return title
    else:
        title = "title not found"
        return title

def contains_com(input_array: list[str]) -> list[bool]:
    #"""Check if each string in the input array contains '.com'."""
    return [".com" in string for string in input_array]

def has_equal_index():
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
    
    url_count= len(urls)

    output_dir = 'Data/ai_gen'
    
    output_files = [file for file in os.listdir(output_dir) if file.startswith('output_') and file.endswith('.txt')]
    output_count = len(output_files)

    if(url_count == output_count):
        return True
    else:
        print("Uneven Count")
        sys.exit()
    
def has_content(soup):
    try:                                                    #attempts to get the article and put it into content
                content = soup.find('article').get_text()
                return content
    except:
                content = "There was no article in this "
                return content

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
        return space_count


