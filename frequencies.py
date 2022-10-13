"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        itemNew = str(item)
        if itemNew in frequencies:
            frequencies[itemNew]+=1
        else:
            frequencies[itemNew]=1
    return frequencies
