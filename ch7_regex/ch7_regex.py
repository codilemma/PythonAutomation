# Shorthand Codes for common Regex Character Classes
#============================================================================================#
# Shorthand | Represents                                                                     #
#============================================================================================#
# '\d'      | Any numeric digit from 0 to 9.                                                 #
# -------------------------------------------------------------------------------------------#
# '\D'      | Any character that is NOT a numeric digit from 0 to 9.                         #
# -------------------------------------------------------------------------------------------#
# '\w'      | Any letter, numeric digit, or the underscore character                         #
# -------------------------------------------------------------------------------------------#
# '\W'      | Any character that is NOT a letter, numeric digit, or the underscore character #
# -------------------------------------------------------------------------------------------#
# '\s'      | Any space, tab, or newline character                                           #
# -------------------------------------------------------------------------------------------#
# '\S'      | Any character that is NOT a space, tab, or newline character                   #
# -------------------------------------------------------------------------------------------#
# '?'       | Matches zero or one of the preceding group                                     #
# -------------------------------------------------------------------------------------------#
# '*'       | Matches zero or more of the preceding group                                    #
# -------------------------------------------------------------------------------------------#
# '+'       | Matches one or more of the preceding group                                     #
# -------------------------------------------------------------------------------------------#
# '{n}'     | Matches exactly n of the preceding group                                       #
# -------------------------------------------------------------------------------------------#
# '{n,}'    | Matches n or more of the preceding group                                       #
# -------------------------------------------------------------------------------------------#
# '{,m}'    | Matches 0 to m of tghe preceding group                                         #
# -------------------------------------------------------------------------------------------#
# '{n,m}'   | Matches at least n and at most m of the preceding group                        #
# -------------------------------------------------------------------------------------------#
# '{n,m}?' or '*?' or '+?' | preforms non-greedy match of the preceeding group               #
# -------------------------------------------------------------------------------------------#
# '^spam'   | means the string must begin with spam                                          #
# -------------------------------------------------------------------------------------------#
# 'spam$'   | means the string must end with spam                                            #
# -------------------------------------------------------------------------------------------#
# '.'       | matches any character, except newline characters                               #
# -------------------------------------------------------------------------------------------#
# '[abc]'   | matches any character between the brackets (such as a,b, or c)                 #
# -------------------------------------------------------------------------------------------#
# '[^abc]'  | matches any character that isn't between the brackets                          #
# -------------------------------------------------------------------------------------------#

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
# findall() without groups 
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# returns a list of all phone numbers found
nums = phoneNumRegex.findall('Cell: 415-555-9999, Work: 212-555-0000') # No groups
print(nums)

# findall() with groups
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
# returns a list of tuples that contain (areaCode, mainNumber) of all phone numbers found
nums = phoneNumRegex.findall('Cell: 415-555-9999, Work: 212-555-0000') # No groups
print(nums)

#  Making your own Character Classes --------------------------------------------
# \d is shorthand for (0|1|2|3|4|5|6|7|8|9)
vowelRegex = re.compile(r'[aeiouAEIOU]') # will find uppper and lowercase vowels
vo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vo)

# Negative character class
# will find all characters that are NOT upper and lowercase vowels
consonantRegex = re.compile(r'[^aeiouAEIOU]')
co = consonantRegex.findall('RoboCop eats babyfood. BABY FOOD.')
print(co)

#  The Caret and Dollar Sign Characters --------------------------------------------
# use '^' to indicate that match must occur at beginning
# use '$' to indicate that match must occur at end
beginsWithHello = re.compile(r'^Hello')
bh = beginsWithHello.search('Hello, World!')
print(bh)

bh2 = beginsWithHello.search('He said Hello.')
print(bh2 == None)

# "r'^\d+$'" searches for strings that both begin and end with one or more numerics
wholeStringIsNum = re.compile(r'^\d+$')
ws = wholeStringIsNum.search('123456')
print(ws)

ws2 = wholeStringIsNum.search('12456wsd4546')
print(ws2 == None)

#  The Wildcard Character "." --------------------------------------------
# Matches any character except for a newline
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

#  Matching Everything with Dot-Star  --------------------------------------------
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al  Last Name: Swigart')
print(mo.group(1))
print(mo.group(2))

# Non-greedy mode
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#  Matching Newlines with the Dot Character  --------------------------------------------
# will match everything except the newline.  
# re.DOTALL: will match all characters, including the newline character
noNewLineRegex = re.compile('.*')
print(noNewLineRegex.search('Serve the public trust. \nProtect the innocent.').group())

newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('Serve the public trust. \nProtect the innocent').group())


#  Case-Insensitive Matching  --------------------------------------------
# to make regex case-insensitive, pass re.IGNORECASE or re.I as a second argument
robocop = re.compile(r'robocop',re.I)
print(robocop.search('RoboCop is part man, part machin, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())

#  Substituting strings with the sub() method  --------------------------------------------
# substitute new text in place of patterns
namesRegex = re.compile(r'Agent \w+')
# sub(replace_with_this, string_to_search)
print(namesRegex.sub('Censored', 'Agent Alice gave the secret documents to Agent Bob.'))

#Censor the names of the agents by abreviating their name. \1 replaces the (\w) group
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# Managing Compex Regexes -------------------------------------------
# instead of this
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# You can do this!
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
)''', re.VERBOSE)
nums = phoneRegex.findall('Cell: 415-555-9999, Work: 212-555-0000') # No groups
print(nums)
print(nums[0][0])

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE-------------------------------------
someRegexValue = re.compile('foo',re.IGNORECASE|re.DOTALL|re.VERBOSE)


