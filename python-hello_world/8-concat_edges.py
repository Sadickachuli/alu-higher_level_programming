#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntax"
str = str[38:67].strip() + str[106:112] + str[0:6].strip()
print(str)
