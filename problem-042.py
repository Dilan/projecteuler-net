#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and
# adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number
# then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
# nearly two-thousand common English words, how many are triangle words?

def word_value(word, letters):
    return reduce(lambda x,y: x+letters.index(y.lower()), word, 0)

def triangle_numbers(limit):
    return [int((n*(n+1)*0.5)) for n in range(1, limit+1)]

def is_triangle_word(word, letters, list):
    return word_value(word, letters) in list

def solution(file_path):
    letters = [''] + list(map(chr, range(97, 123)))
    f = open(file_path, 'r')
    words = f.read().strip('"').split('","')

    result = 0
    for word in words:
        result += 1 if is_triangle_word(word, letters, triangle_numbers(500)) else 0

    return result

print 'Answer is:', solution('data/p042_words.txt')
