#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      owner
#
# Created:     30/05/2015
# Copyright:   (c) owner 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from collections import Counter
import string

#from nltk import stopwords why won't this work

#frequency

def word_frequency(text):
    mystopwords = ["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their",
    "theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but",
    "if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over",
    "under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very",
    "s","t","can","will","just","don","should","now","the"]
    wordlist = []
    for line in text:

        for word in line.split():
            word = word.lower()
            if word not in mystopwords:
                word = word.strip(string.punctuation)

                wordlist.append(word)
    words = str(Counter(wordlist))
    return(words)

def main():
    linguistics_text = open("C:/Users/owner/Desktop/Programming/test-repo-online/linguistics_text_dump.txt","r", encoding='utf-8')
    ling_freq = open('C:/Users/owner/Desktop/Programming/test-repo-online/linguistics_frequencies.txt', 'w+', encoding='utf-8') #things written to a file gotta be strings! Or binary? But usually strings for me!
    ling_freq.write(word_frequency(linguistics_text))
    linguistics_text.close()
    ling_freq.close()

    control_text = open("C:/Users/owner/Desktop/Programming/test-repo-online/wiki_random_dump.txt","r", encoding='utf-8')
    control_freq = open('C:/Users/owner/Desktop/Programming/test-repo-online/control_frequencies.txt', 'w+', encoding='utf-8')
    control_freq.write(word_frequency(control_text))
    control_text.close()
    control_freq.close()

    print("You did it!")

if __name__ == '__main__':
    main()
