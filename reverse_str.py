# 3. Reverse a string with some conditions :)
# a) Spaces and decimals should remain in the same location.
# b) Upper and lower cases must be maintained as original
# Eg: reverse_string("UPPER lower.") --> REWOL reppu.
# reverse_string("One.Three 1&3) --> 3&1.Eerht eno




def reverse_string():
    string = "Hello"
    rev_string = string[::-1]
    for i in rev_string:
        print(i)
        if i.isupper():
            i[0].upper()





reverse_string()