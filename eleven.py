#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:09:22 2020

@author: jaswithareddy

Encrypt a plain text using Row(Columnar) Transposition.
"""

def encrypt(message, keyword):
  matrix = createEncMatrix(len(keyword), message)
  keywordSequence = getKeywordSequence(keyword)

  ciphertext = "";
  for num in range(len(keywordSequence)):
    pos = keywordSequence.index(num+1)
    for row in range(len(matrix)):
      if len(matrix[row]) > pos:
        ciphertext += matrix[row][pos]
  return ciphertext


def createEncMatrix(width, message):
  r = 0
  c = 0
  matrix = [[]]
  for pos, ch in enumerate(message):
    matrix[r].append(ch)
    c += 1
    if c >= width:
      c = 0
      r += 1
      matrix.append([])

  return matrix


def getKeywordSequence(keyword):
  sequence = []
  for pos, ch in enumerate(keyword):
    previousLetters = keyword[:pos]
    newNumber = 1
    for previousPos, previousCh in enumerate(previousLetters):
      if previousCh > ch:
        sequence[previousPos] += 1
      else:
        newNumber += 1
    sequence.append(newNumber)
  return sequence

if __name__=="__main__":
    keyword=input("Enter Key: ")
    message=input("Enter Plain Text: ")
    cipher=encrypt(message,keyword)
    print("Cipher Text: ",cipher)
