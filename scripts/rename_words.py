"""
Rename Words
"""
import os
import json

def read_file(file_name):
    """
    Read File
    """
    open_file = open(file_name, "r", encoding='utf-8')
    return open_file.read()

def write_file(file_name, content):
    """
    Write File
    """
    output = open(file_name, "w", encoding='utf-8')
    output.write(content)
    output.close()

for root_dir, cur_dir, files in os.walk('./data'):
    jsonFiles = list(filter(lambda file: '.json' in file, files))
    for file in jsonFiles:
        oldFilePath = root_dir + "/" + file
        fileContent = read_file(oldFilePath)
        wordJson = json.loads(fileContent)
        word = wordJson['word']
        first = word[0]
        newFilePath = './data/' + first + '/' + word.replace(" ", "_")+'.json'
        os.rename(oldFilePath, newFilePath)
