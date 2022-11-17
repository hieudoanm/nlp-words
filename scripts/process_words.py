"""
Process Words
"""
import os
import json


COUNT = 0

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

wordsAPI = []
wordsWithDefinitions = []

for root_dir, cur_dir, files in os.walk('./data'):
    jsonFiles = list(filter(lambda file: '.json' in file, files))
    for file in jsonFiles:
        filePath = root_dir + "/" + file
        fileContent = read_file(filePath)
        wordJson = json.loads(fileContent)
        word = wordJson['word']
        results = wordJson.get('results')
        print(word, results)
        wordsAPI.append(word)
        if results is not None:
            wordsWithDefinitions.append(word)
    COUNT += len(jsonFiles)

print('COUNT:', COUNT)

wordsWithDefinitions.sort()
WORDS_WITH_DEFINITIONS_CONTENT = "\n".join(wordsWithDefinitions)
write_file("./docs/words-with-definitions.txt", WORDS_WITH_DEFINITIONS_CONTENT)

wordsAPI.sort()
WORDS_API_CONTENT = "\n".join(wordsAPI)
write_file("./docs/words-api.txt", WORDS_API_CONTENT)
