import re  # Needed for splitting text with a regular expression
from math import floor
import time


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("./data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("./data-files/AliceInWonderLand.txt")

    while True:
        print("\nMain Menu\n1: Spell Check a Word (Linear Search)\n2: Spell Check a Word (Binary Search)\n3: Spell Check Alice In Wonderland (Linear Search)\n4: Spell Check Alice In Wonderland (Binary Search)\n5: Exit")
        value = input("Enter a menu selection(1-5): ")

        print()

        match(value):
            case "1":
                wordSearch(dictionary, linearSearch)
            case "2":
                wordSearch(dictionary, binarySearch)
            case "3":
                aliceSearch(dictionary, aliceWords, linearSearch)
            case "4":
                aliceSearch(dictionary, aliceWords, binarySearch)
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Error! You must enter a value from 1 to 5!")


def wordSearch(dictionary, algorithm):
    searchString = input("Please enter a word: ").lower()
    print("\nLinear Search is starting...")

    start = getTime()
    result = algorithm(dictionary, searchString)
    end = getTime()

    if (result == -1):
        print(f"{searchString} is NOT IN the dictionary ({timeString(end-start)})")
    else:
        print(
            f"{searchString} is IN the dictionary at position {result} ({timeString(end-start)})")


def aliceSearch(dictionary, aliceWords, algorithm):
    print("\nLinear Search is starting...\n")
    notFound = 0
    length = len(aliceWords)

    start = getTime()

    for index, word in enumerate(aliceWords):
        print(f" {index}/{length}", end="\r")
        if (algorithm(dictionary, word.lower()) == -1):
            notFound += 1

    end = getTime()

    print(
        f"Number of words not found in the dictionary: {notFound} ({timeString(end-start)})")


def getTime():
    return floor(time.time() * 1000)


def timeString(value):
    return str(value) + 'ms' if (value < 1000) else str(value/1000) + 's'


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)


def binarySearch(array, item):
    lower = 0
    upper = len(array)-1
    while upper >= lower:
        middle = floor((upper+lower)/2)
        middleItem = array[middle]
        if middleItem == item:
            return middle
        elif item < middleItem:
            upper = middle-1
        else:
            lower = middle+1
    return -1


def linearSearch(array, item):
    for index, searchItem in enumerate(array):
        if searchItem == item:
            return index
    return -1


main()
