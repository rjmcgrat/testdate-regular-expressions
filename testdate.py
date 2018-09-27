# Rodney McGrath
# 55352053
# CS141 Spring 2018
# Assignment 1 Part 2
# testdate.py

#^(?:(0?[13578]|1[02])(\/|-|\.)(31)(\/|-|\.)((?:1919|19[2-9][0-9]|200[0-9]|201[0-8]|\d\d)))$|^(?:(0?[13-9]|1[0-2])(\/|-|\.)(29|30)(\/|-|\.)((?:1919|19[2-9][0-9]|200[0-9]|201[0-8]|\d\d)))$|^(?:(0?2)(\/|-|\.)(29)(\/|-|\.)(?:(?:(?:(19))(?:[2468][048]|[3579][26])|(200[048]|201[26]|[2468][048]|[3579][26]|0[048]|1[26]))))$|^(?:(0?[1-9]|1[0-2])(\/|-|\.)(0?[0-9]|1[0-9]|2[0-8])(\/|-|\.)((?:1919|19[2-9][0-9]|200[0-9]|201[0-8]|\d\d)))$

import sys
import fileinput
import re

def findSplitter(date):
    for c in date:
        if c == '.':
            return c
        elif c == '/':
            return c
        elif c == '-':
            return c

if __name__ == "__main__":
    script = sys.argv[0]
    filenames = sys.argv[1:]
    # DD/MM/YYYY
    regexDDMMYYYY = re.compile(r'\b((?:(31)(\/|-|\.)(0?[13578]|1[02])(\/|-|\.)(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9]))|(?:(29|30)(\/|-|\.)(0?[13-9]|1[0-2])(\/|-|\.)(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9]))|(?:(29)(\/|-|\.)(0?2)(\/|-|\.)(19[2468][048]|19[3579][26]|200[048]|201[26]|[2468][048]|[3579][26]|0[048]|1[26]))|(0?[0-9]|1[0-9]|2[0-8])(?:(\/|-|\.)(0?[1-9]|1[0-2])(\/|-|\.)(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9])))\b')
    # MM/DD/YYYY
    regexMMDDYYYY = re.compile(r'\b((?:(0?[13578]|1[02])(\/|-|\.)(31)(\/|-|\.)(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9]))|(?:(0?[13-9]|1[0-2])(\/|-|\.)(29|30)(\/|-|\.)(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9]))|(?:(0?2)(\/|-|\.)(29)(\/|-|\.)(19[2468][048]|19[3579][26]|200[048]|201[26]|[2468][048]|[3579][26]|0[048]|1[26]))|(?:(0?[1-9]|1[0-2])(\/|-|\.)(0?[0-9]|1[0-9]|2[0-8])(\/|-|\.)(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9])))\b')
    # YYYY/MM/DD
    regexYYYYMMDD = re.compile(r'\b((?:(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9])(\/|-|\.)(0?[13578]|1[02])(\/|-|\.)(31))|(?:(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9])(\/|-|\.)(0?[13-9]|1[0-2])(\/|-|\.)(29|30))|(?:(19[2468][048]|19[3579][26]|200[048]|201[26]|[2468][048]|[3579][26]|0[048]|1[26])(\/|-|\.)(0?2)(\/|-|\.)(29))|(?:(1919|19[2-9][0-9]|200[0-9]|201[0-8]|[0-9][0-9])(\/|-|\.)(0?[1-9]|1[0-2])(\/|-|\.)(0?[0-9]|1[0-9]|2[0-8])))\b')

    print("testdate.py by Rodney McGrath 55352053")
    for filename in filenames:
        flag1 = 0
        dateList = []
        f = open(filename, 'r')
        for line in f.readlines():
            for m in re.finditer(regexMMDDYYYY, line):
                if flag1 == 0:
                    flag1 = 1
                    print(filename + ": contains dates", end = "")
                date = m.group()
                sep = findSplitter(date)
                sepD = date.split(sep)
                standardDate = ' ' + sepD[2] + '/' + sepD[0] + '/' + sepD[1]
                dateList.append(standardDate)
            for m in re.finditer(regexDDMMYYYY, line):
                if flag1 == 0:
                    flag1 = 1
                    print(filename + ": contains dates", end = "")
                date = m.group()
                sep = findSplitter(date)
                sepD = date.split(sep)
                standardDate = ' ' + sepD[2] + '/' + sepD[1] + '/' + sepD[0]
                dateList.append(standardDate)
            for m in re.finditer(regexYYYYMMDD, line):
                if flag1 == 0:
                    flag1 = 1
                    print(filename + ": contains dates", end = "")
                date = m.group()
                sep = findSplitter(date)
                sepD = date.split(sep)
                standardDate = ' ' + sepD[0] + '/' + sepD[1] + '/' + sepD[2]
                dateList.append(standardDate)
        if len(dateList) > 0:
            for date in dateList:
                print(date, end = "")
            print()
        else:
            print(filename + ": does not contain dates")
        f.close()
