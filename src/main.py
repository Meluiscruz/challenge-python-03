# Resolve the problem!!

import re
import os

current_dir = os.path.dirname(os.path.realpath(__file__)) #Get the current dir: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
filepath = current_dir+"\encoded.txt"                     #Please make sure that the file encoded.txt is in the same dir.
def run():
    # Start coding here
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.readlines()
        str_text =''.join(content)
        answer = re.findall("[a-z]", str_text) #The atribute re.findall returns a list and only works with the RegEx and an string to be parsed 
        answer_str = ''.join(answer)           #https://www.w3schools.com/python/trypython.asp?filename=demo_regex_meta1
        print(answer_str)
    f.close()

if __name__ == '__main__':
    run()
