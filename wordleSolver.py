import collections
import re


def getMostCommonLetters(wordList: list) -> dict:
    letterCounts = collections.Counter()
    for word in wordList:
        letterCounts.update(set(word))

    return {l[0]: l[1] for l in letterCounts.most_common()}


def getWordWeight(word: str, letterCounts: dict) -> int:
    wordWeight = 0
    for letter in set(word):
        wordWeight += getLetterWeight(letter, letterCounts)

    return wordWeight


def getLetterWeight(letter, letterCounts) -> int:
    try:
        weight = letterCounts[letter]
    except KeyError:
        weight = 0

    return weight


def getWeightedWordList(wordList: dict) -> dict:
    return {word: getWordWeight(word, getMostCommonLetters(wordList)) for word in wordList}


def getSortedWordList(weightedWords: dict) -> list:
    return [x[0] for x in sorted(weightedWords.items(), key=lambda item: item[1], reverse=True)]


def getRecommendation(pattern, wordList):
    try:
        pattern = re.compile(pattern)
        candidates = [word for word in wordList if pattern.match(word)]

        return candidates[0]
    except:
        print("Sad panda. Unable to compile the pattern.")


def __promptAndRespond(sortedList:list):
    knownLetters = input("Enter the word, using hyphens for letters you don't know.: ")
    exclusions = input("What letters are known to not appear in the word?: ")

    print(f"Try {getRecommendation(__buildPattern(knownLetters, exclusions), sortedList)}")


def __buildPattern(knownLetters: str, exclusions = None):

    if exclusions:
        newPattern = knownLetters.replace('-', f'[^{exclusions}]{{1}}')
    else:
        newPattern = knownLetters.replace('-', '.')

    return newPattern


if __name__ == "__main__":
    print("Booting up. Just a sec while I load all the things.")

    wordList = [word.rstrip() for word in open('/Users/barrett/Desktop/wordleSolver/dictionary.txt')]
    sortedList = getSortedWordList(getWeightedWordList(wordList))

    print(f"Ready to go. Start with {sortedList[0]}")
    while True:
        try:
            __promptAndRespond(sortedList)
        except KeyboardInterrupt:
            print("Bye")
            exit()