# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 01:00:59 2020

@author: Chaos
"""

import os
import re

# remove non: 0-9, a-z, A-Z, ' ', '-' characters
def cleantext(rawtext):
	return re.sub('[^0-9a-zA-Z -]+', '', rawtext)

# get file list
path = './wc_input'
files = os.listdir(path)


dictz = {}              # dict for word storage
line_word_count = []    # word count for each line, sorted line-wise
running_median = []     # the running median, running line-wise

for file in files: 
    # open files individually
    f = open(path + "/" + file)
    
    # process word count line-wise
    for line in f:
        line = line.lower()             # to lower case
        line = cleantext(line)           # clean text
        line = line.split(' ')          # split line by ' '
        words = []
        words_count = 0
        for word in line:
            # skip empty string
            if word == '':
                continue
            # add to the word list, increment the words_count
            words.append(word)
            words_count += 1

        # build dict
        for word in words:
            if word in dictz.keys():
                dictz[word] = dictz[word] +1
            else:
                dictz[word] = 1
        
        # insert the words_count into proper position in line_word_count
        if len(line_word_count) == 0:
            line_word_count.append(words_count)
        else:
            for i in range(0, len(line_word_count)):
                if words_count <= line_word_count[i]:
                    line_word_count.insert(i, words_count)
                    break
                
        # calculate the running median
        if len(line_word_count) % 2 == 0:
            running_median.append((line_word_count[round((len(line_word_count) + 1) / 2 - 0.1) - 1] + 
                                   line_word_count[round((len(line_word_count) + 1) / 2 + 0.1) - 1]) / 2)
        else:
            running_median.append(line_word_count[round((len(line_word_count) + 1) / 2 - 1)])

# sort and print wc dict
f = open('./wc_output/wc_result.txt', 'w')  
sorted_dict = sorted(dictz.items(), key=lambda a:a[0]) 
for item in sorted_dict:
    f.write(item[0] + ' : ' + str(item[1]) + '\n')

# print the med list
f = open('./wc_output/med_result.txt', 'w')  
for item in running_median:
    f.write(str(item) + '\n')   

# close f
f.close()

