'''
Team YushaDog: Yusha Aziz, Brian Chen, & Craig Chen
Soft Dev
K05 -- bistream
2022-09-29
time spent: 30 mins

DISCO:
When you split a String, there is a carriage return, with backslash n. We manually remove it from the last entry with [:-1]. If not, there will be an extra line when you return.
Use open('filename') as f to open a text file, and f.readline() to read a txt file with one line of text. 
You can assign random to a variable, in this case r.
When you use vim filename.py, you can ctrl+z to temp exit and % to go back !!. 

QCC:
...
'''


import random as r

with open('krewes.txt') as f:
    krewes = f.readline()

classes = {2:[],7:[],8:[]}

def get_devo(krewes):
    #split list into person
    person = krewes.split('@@@')
    person[-1] = person[-1][:-1] #strip carriage return

    for i in person:
        #split each person's information into [pd,name,ducky]
        pinfo = i.split('$$$')

        #classes[pd].append([name,ducky])
        classes[int(pinfo[0])].append([pinfo[1],pinfo[2]])

    #pick pd from .keys()
    pd = r.choice(list(classes.keys()))

    pchose = r.choice(classes[pd])
    return(f"{pd} : {pchose[0]}, ducky named: {pchose[1]}")

print(get_devo(krewes))