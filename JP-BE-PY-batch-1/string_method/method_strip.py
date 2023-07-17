# method strip
"""
Definition: The strip() method removes any leading, and trailing whitespaces.
            You can specify which character(s) to remove, if not, any whitespaces will be removed.
"""

# remove white spaces from left and right
txt = "    hello world     "
txt = txt.strip()
print(txt) # hello world



# remove specified characters from left and right
txt = "---hello world---"
txt = txt.strip("-")
print(txt) # hello world

txt = "$$$$hello world$$$$"
txt = txt.strip("$")
print(txt) # hello world


