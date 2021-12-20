import csv
import time
import re

start_time = time.time()


def newlist(user_input, used):  # make list of words from user input
    wordlist = []
    freqlist = {}
    with open("unigram_freq.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            wordlist.append(row[0])
            freqlist[row[0]] = row[1]
    wordlist_new = []
    reg = re.compile(user_input)
    for word in wordlist:
        if bool(re.fullmatch(reg, word)):
            wordlist_new.append(word)  # wordlist_new is list with parameters
    return predict_letter(wordlist_new, used, freqlist)


def predict_letter(wordlist_new, used, freqlist):  # keep count of letters used
    D = {}
    listy = []
    for word in wordlist_new:
        for letter in word:
            if letter not in used:
                D[letter] = D.get(letter, 0) + 1 + 1 + 0.000000000001*float(freqlist[word])

    for key in D:
        setty = (D[key], key)
        listy.append(setty)
    # print("listy start")
    # for i in listy:
    #     print("listy entry", end=" ")
    #     print(listy)
    listy.sort(reverse=True)
    Most_freq_letter = listy[0][1]
    # print(listy)
    return Most_freq_letter
