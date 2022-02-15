import pandas as pd
import itertools
import csv

'''
 Script that generates dataset of two sets that have 100.000 numbers
 and one of the possible bijections between them
'''

evenList = []
oddList = []
count = 0


for i in range(1,200001):
    if i%2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
        count = count + 1

bijectionList = []
loop_control = 0
for p in itertools.permutations(evenList):
    bijectionList.append(sorted(zip(oddList,p)))
    break


df = pd.DataFrame()

#it creates a dataframe for converting it to csv
df = pd.DataFrame({'Set1': oddList,
    'Set2': evenList,
    'Bijection': bijectionList[0]})

#it converts the df to csv
df.to_csv('learning_bijections_dataset.csv',index= False, quoting = csv.QUOTE_NONE, escapechar =' ')
