import requests
import os
from bs4 import BeautifulSoup

def has_url():
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
    
    if(contains_com(urls)):
        print("found urls")
        return urls
    
    else:
        print("No urls")

    
def has_title(soup):
              
    title = soup.find('title').get_text()
    if(bool(title)):
        print("title found")
        return title
    else:
        print("title not found")

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
        print("Equality")
        return True

    else:
        print("Uneven Count")
        return False
    
def has_content(soup):
    try:                                                    #attempts to get the article and put it into content
                content = soup.find('article').get_text()
                print("Content found")
    except:
                content = "There was no article in this "

