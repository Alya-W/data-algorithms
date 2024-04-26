"""
Name: Aliya Kerimbekova
CLass: BDA350
Date: December 6th, 2021
Assignment: Final Project

---Anagrams---
"""
import string
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords


def punctuation_removal(file):
    """Remove all punctuation marks"""
    table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    without_punc = [file.translate(table)]
    clean_file = " ".join(without_punc)
    return clean_file.split()


def stopwords_removal(file):
    """Remove all English stop words"""
    words = [word for word in file if word.lower() not in stopwords.words('english')]
    return words


def digits_removal(file):
    """Remove all digits as they are not words"""
    return [x for x in file if not x.isdigit()]


def relevant_words(file):
    """Exclude all one-letter-words"""
    file = punctuation_removal(file)
    file = stopwords_removal(file)
    file = digits_removal(file)
    final = []
    for i in file:
        if len(i) > 1:
            final.append(i.lower())
    return final


def get_key(word):
    """Hash function to get a unique key for one group of anagrams"""
    return "".join(sorted(word))


def get_anagrams(words):
    """Traverse through the list of words and find anagrams with their frequencies"""
    anagrams = {}  # output
    frequency = {}

    for word in words:
        key = get_key(word)
        if key in anagrams:
            anagrams[key].add(word)
            frequency[key] += 1
        else:
            anagrams[key] = set()
            anagrams[key].add(word)
            frequency[key] = 1
    return anagrams, frequency


def print_anagrams(anagrams, limit=None):
    """Print anagrams in a desired format.
    Precondition: get_anagrams must be called first
    Limit can be set to print specific number of anagrams"""
    index = 0

    if len(anagrams) != 2:  # check that input is tuple with 2 values - anagrams, frequency dicts
        raise ValueError
    else:
        for key, value in anagrams[0].items():
            print(", ".join(list(value)), '--', anagrams[1][key])
            index += 1
            if index == limit:
                break


def search(word, anagrams):
    """Based on the hashing key the function finds an anagram if it exists"""
    key = get_key(word)
    try:
        anagram = ", ".join(anagrams[0][key])
        freq = anagrams[1][key]
        print('Anagram', word, 'is found!\n', anagram, '--', freq)
        return anagram, freq
    except KeyError:
        print("Not found")
        return None


def main():
    with open('adventures.txt', 'r', encoding='utf-8-sig') as f:
        file = f.read()

    preprocess = relevant_words(file)  # prepare text for further actions

    anagrams = get_anagrams(preprocess)  # find anagrams in a list of words
    print_anagrams(anagrams, limit=20)  # print first 20 anagrams

    print('-----------------')
    search('girns', anagrams)
    print('-----------------')
    search('dongle', anagrams)
    print('-----------------')
    search('shand', anagrams)

    print('-----------------')
    search('helicopter', anagrams)
    print('-----------------')
    search('phone', anagrams)
    print('-----------------')
    search('petite', anagrams)


if __name__ == "__main__":
    main()
