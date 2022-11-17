"""
Get Words
"""
import requests

URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

response = requests.get(URL)

wordsText = response.text
words = wordsText.split('\n')
uniqueWords = list(set(words))
uniqueWords = list(filter(lambda word: word != '', uniqueWords))
uniqueWords.sort()

wordsFile = open("./docs/words.txt", "w", encoding='utf-8')
wordsFile.write("\n".join(uniqueWords))
wordsFile.close()
