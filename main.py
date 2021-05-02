import pandas as pd
import numpy as np
import nltk
import json
from nltk.corpus import stopwords


def decode(s):
    numbers = []
    num = 0
    for i in s:
        if i >= '0' and i <= '9':
            num = num*10 + int(i)
        else:
            if num != 0:
                numbers.append(num)
            num = 0
    return numbers

data = pd.read_csv('./data.csv')
std  = pd.read_csv('./std.csv')

ids = data['id']
texts = data['text']

id2text = {1: "2"}
id2text[ids[0]] = texts[0]

for i in range(1, len(ids)):
    id2text[ids[i]] = texts[i]

questionID = std['questionID']
duplicates = std['duplicates']

description_x = []
description_y = []
flag = []
cnt = 0

canpair = {0 : 0}

for i in range(0, len(duplicates)):
    numbers = decode(duplicates[i])
    for j in range(0, len(numbers)):
        if cnt == 1000:
            break
        description_y.append(id2text[int(numbers[j])])
        description_x.append(id2text[int(questionID[i])])
        canpair[int(numbers[j])] = int(questionID[i])
        canpair[int(questionID[i])] = int(numbers[j])
        flag.append("TRUE")
        cnt+=1
    if cnt == 1000:
        break

row = data['text']
dataCount = 1200

# Bad data maker
for i in range(0, len(ids)):
    for j in range(i + 1, len(ids)):
        if cnt >= 1200:
            break
        if i in canpair:
            if canpair[i] == j:
                continue
        description_x.append(texts[i])
        description_y.append(texts[j])
        flag.append("FALSE")
        cnt+=1
test_id = [i for i in range(0, dataCount)]



outfile = pd.DataFrame({"": test_id, "description_x": description_x, "description_y": description_y, "same_security": flag})
outfile.to_csv("train.csv", index = False)

test_data = pd.DataFrame({"test_id": test_id, "description_x": description_x, "description_y": description_y})
test_data.to_csv("test.csv", index = False)
