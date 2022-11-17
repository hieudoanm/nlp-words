"""
Reprocess Words
"""
import os
import json
import requests

ENCRYPTED = '8cfdb188e722949be89507bfe658bebdaeb32e0931f893b8'
WHEN = '2022-07-24T09:04:33.174Z'
BASE_URL='https://www.wordsapi.com/mashape/words'
keys = [
    "synonyms",
    "antonyms",
    "typeOf",
    "hasTypes",
    "partOf",
    "hasParts",
    "instanceOf",
    "hasInstances",
    "inRegion",
    "regionOf",
    "usageOf",
    "hasUsages",
    "memberOf",
    "hasMembers",
    "substanceOf",
    "hasSubstances",
    "inCategory",
    "hasCategories",
    "also",
    "pertainsTo",
    "similarTo",
    "entails"
]


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
    try:
        output = open(file_name, "w", encoding='utf-8')
        output.write(content)
        output.close()
    except: # pylint: disable=bare-except
        print("write_file", "Something went wrong")

# Words
wordsText = read_file("./docs/words-with-definitions.txt")
words = wordsText.split('\n')
words.sort()
# words.reverse()

for root_dir, cur_dir, files in os.walk('./data'):
    jsonFiles = list(filter(lambda file: '.json' in file, files))
    for file in jsonFiles:
        filePath = root_dir + "/" + file
        fileContent = read_file(filePath)
        wordJson = json.loads(fileContent)
        word = wordJson['word']
        results = wordJson.get('results')
        if results is not None:
            for result in results:
                for key in keys:
                    groups = result.get(key, [])
                    print(groups)
                    for item in groups:
                        if item not in words:
                            URL = BASE_URL+'/'+item+'?when='+WHEN+'&encrypted='+ENCRYPTED
                            try:
                                response = requests.get(URL)
                            except: # pylint: disable=bare-except
                                print(item, "Something went wrong")
                            responseJson = response.json()
                            queryWord = responseJson['word']
                            if queryWord not in words:
                                first = queryWord[0]
                                wordFileName='./data/'+first+'/'+queryWord.replace(" ", "_")+'.json'
                                write_file(wordFileName, response.text)
