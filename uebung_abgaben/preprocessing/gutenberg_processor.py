#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tim Graf
#Notes: Korpus bestehend aus Also Sprach Zarathustra, Ecce Homo, Jenseits von Gut und Böse, Die Geburt der Tragödie, Götzen-Dämmerung.

from nltk import sent_tokenize, word_tokenize

def clean_gutenberg(filename):
    with open(filename, 'r') as infile, open('gutput.txt', 'w') as outfile:
        start = False
        for line in infile:
            if start == False:
                if line[:12] == '*** START OF':
                    #print(line)
                    start = True
            else:
                if line[:7] == '*** END':
                    #print(line)
                    start = False
                elif start == True and line.strip() != '':
                    #print(line)
                    outfile.write(line.strip() + ' ')

def Tokenize_and_plain(filename):
    with open(filename, 'r', encoding='utf-8') as infile, \
        open('gutput.tokenized', 'w') as outfile:
        text = infile.read()
        sentences = sent_tokenize(text)
        #print(sentences)
        for sentence in sentences:
            tokenized = word_tokenize(sentence)
            outfile.write(' '.join(tokenized) + '\n')

def main():
    clean_gutenberg('Gutenbergin.txt')
    Tokenize_and_plain('gutput.txt')

if __name__ == '__main__':
    main()

