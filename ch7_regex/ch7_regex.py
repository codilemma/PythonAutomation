import re

# Finding patterns of text without regular expressions-----------------------------
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber('415-555-4242'))
print(isPhoneNumber('lksdjflksdjflksdjf'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# Finding patterns of text using regular expressions-----------------------------
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # or '\d{3}-\d{3}-\d{4}'
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# Grouping with Parantheses -----------------------------
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Area Code: ' + mo.group(1))
print('Phone Number: ' + mo.group(2))

areaCode, mainNumber = mo.groups() # mo.groups() returns a tuple
print(areaCode + "-" + mainNumber)

# Matching Multiple Groups with the Pipe -----------------------------
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# Optional Matching with the Question Mark -----------------------------
batRegex = re.compile(r'Bat(wo)?man') # 'wo' is the optional part of the pattern
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# look for phone numbers with or without area code -----------------------------
phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

#  Matching Zero or More (repeated text) with Star --------------------------------------------
#  Does not require text in the parenthesis
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventure of Batwowowowoman')
print(mo3.group())

#  Matching One or More (repeated text) with Plus --------------------------------------------
#  Requires the text in the parenthesis
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventrures of Batman')
print(mo3 == None)

#  Matching Specific Repetitions with Braces --------------------------------------------
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

# match specific repetitions in a range
haRegex = re.compile(r'(Ha){3,5}')
mo2 = haRegex.search('HaHaHaHa')
print(mo2.group())

# will return True
mo3 = haRegex.search('Ha')
print(mo3 == None)

#  Greed and non-greedy matching --------------------------------------------
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nonGreedyHaRegex = re.compile(r'(Ha){3,5}?') 
mo2 = nonGreedyHaRegex.search('HaHaHaHaHa') # returns HaHaHa
print(mo2.group())

#  the findall() method --------------------------------------------