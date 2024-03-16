
# Python Regular Expression
# Regular Expression, is a sequence of characters that forms a search pattern.

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # Search string to starts with "The" and ends with "Spain":

if x:
    print("YES! We have a match!")
else:
    print("No match")

