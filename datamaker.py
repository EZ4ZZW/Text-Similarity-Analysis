import pandas as pd
import numpy as np
import nltk

test_id = [i for i in range(0, 200)]
description_x = []
description_y = []

data = pd.read_csv('./data.csv')

ids = data['id']
text = data['text']

cnt = 0

for i in  range(0, 100):
    for j in range(i+1, 100):
        if cnt >= 200:
            break
        cnt+=1
        description_x.append(text[i])
        description_y.append(text[j])
print(len(description_x))
print(len(description_y))
outfile = pd.DataFrame({"test_id": test_id,"description_x": description_x, "description_y": description_y})
outfile.to_csv("badData.csv", index = False)
