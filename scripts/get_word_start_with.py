"""
Get Word
"""
import requests

ENCRYPTED = '8cfdb188e722949be89507bfe658bebdaeb32e0931f893b8'
WHEN = '2022-07-24T09:04:33.174Z'
START_WITH='s'
WORDS_WITH_DATA_FILE_NAME = "./docs/words-with-data-start-with-"+START_WITH+".txt"
WORDS_WITHOUT_DATA_FILE_NAME = "./docs/words-without-data-start-with-"+START_WITH+".txt"

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

# Words
wordsText = read_file("./docs/words.txt")
words = wordsText.split('\n')
startWithWords = list(filter(lambda word: word.lower()[0] == START_WITH, words))
startWithWords.sort()
print(len(startWithWords))
# Words with Data
wordsWithDataText = read_file(WORDS_WITH_DATA_FILE_NAME)
wordsWithData = wordsWithDataText.split("\n")
wordsWithData.sort()
# Words without Data
wordsWithoutDataText = read_file(WORDS_WITHOUT_DATA_FILE_NAME)
wordsWithoutData = wordsWithoutDataText.split("\n")
wordsWithoutData.sort()

if len(startWithWords) == 0:
    print("No Word to Crawl")
else:
    for word in startWithWords:
        if word in wordsWithData or word in wordsWithoutData:
            continue
        URL = 'https://www.wordsapi.com/mashape/words/'+word+'?when='+WHEN+'&encrypted='+ENCRYPTED
        response = None
        try:
            response = requests.get(URL, timeout=10)
        except ConnectionResetError as error:
            print(word, "ConnectionResetError", error)
        except: # pylint: disable=bare-except
            print(word, "Something went wrong")
        if response is None:
            continue
        print(word, response.status_code)
        if response.status_code == 200:
            responseJson = response.json()
            queryWord = responseJson['word']
            first = queryWord[0]
            wordsWithData.append(word)
            WORDS_WITH_DATA_CONTENT = "\n".join(wordsWithData)
            write_file(WORDS_WITH_DATA_FILE_NAME, WORDS_WITH_DATA_CONTENT)
            wordFileName = './data/' + first + '/' + queryWord.replace(" ", "_") + '.json'
            write_file(wordFileName, response.text)
        else:
            wordsWithoutData.append(word)
            WORDS_WITHOUT_DATA_CONTENT = "\n".join(wordsWithoutData)
            write_file(WORDS_WITHOUT_DATA_FILE_NAME, WORDS_WITHOUT_DATA_CONTENT)
