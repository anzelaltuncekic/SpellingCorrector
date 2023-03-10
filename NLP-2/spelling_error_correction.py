# -*- coding: utf-8 -*-
"""Spelling Error Correction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cbh0u6d8_wYGm3hH6trzy9CwkDUz1GxR
"""

from google.colab import drive
drive.mount('/content/drive')

#corpus_path='/content/drive/My Drive/NLP-2/corpus.txt'
uncorrect_words_path='/content/drive/My Drive/NLP-2/test-words-misspelled.txt'
correct_words_path='/content/drive/My Drive/NLP-2/test-words-correct.txt'

words=[]
uncorrectwords=[]
with open(correct_words_path ) as file:
  for line in file:
    for word in line.lower().split():
      words.append(word)

with open(uncorrect_words_path ) as file:
  for x in file:
    for word in x.lower().split():
      uncorrectwords.append(word)      
print(words)

import re  
def frequency(x):  #finding frequencies of strings
  frequency = {}
  match_pattern = re.findall(r'\b[a-z]{1,20}\b', str(x))
  for w in match_pattern:
    count = frequency.get(w, 0)
    frequency[w] = count + 1
  return frequency

frequency(words)

import numpy as np 
def edit_min_distance(first_word,second_word):
 
  target_list = []
  for x in first_word:
    target_list.append(x)
  #print(target_list)
  
  source_list=[]
  for y in second_word:
    source_list.append(y)
  #print(source_list)

  matrix = np.zeros((len(second_word) , len(first_word)))

  matrix[0]=[j for j in range(len(first_word))]
  matrix[:,0]=[j for j in range(len(second_word))]
  

  if target_list[1] != source_list[1]:
    matrix[1,1] = 2

  for c in range(1,len(first_word)):
    for r in range(1,len(second_word)):
      if target_list[c] != source_list[r]:
        matrix[r,c] = min(matrix[r-1,c] , matrix[r,c-1])+1
       
      else:
        matrix[r,c]=matrix[r-1,c-1]
  #return matrix
  return int(matrix[r][c])

edit_min_distance('anzel','anzek')#for example

i=0
j=0
count=0
countx=0
for j in uncorrectwords: 
  for i in words:
    if edit_min_distance(i,j)==0 :
      count=1
    elif edit_min_distance(i,j)==1 :         
      count=2
      newcorrect=i
      
    elif edit_min_distance(i,j)==2:     
      count=3
      new1correct=i  

  if count==1:
    print(j+'  is correctly spelled')
    countx+=1
  elif count==2:
    print('correct spelling of '+j+' is = '+newcorrect)
  elif count==3:
    print('correct spelling of '+j+' is = '+new1correct)
  else :
    print('       ')
print(countx)
