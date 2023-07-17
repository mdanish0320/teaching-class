# method replace
"""
Definition: The replace() method replaces a specified phrase with another specified phrase.
"""

txt = "hello world"
txt = txt.replace("world", "universe")

print(txt) # Hello universe


# it replaces multiple occurances of words
txt = "hello world, this is my world"
txt = txt.replace("world", "universe")

print(txt) # hello universe, this is my universe


# specify the occurances on how many words you want to replaces. replace will start from left most
# this will repalce only one occurance from the left
txt = "hello world, this is my world"
txt = txt.replace("world", "universe", 1)

print(txt) # hello universe, this is my world





