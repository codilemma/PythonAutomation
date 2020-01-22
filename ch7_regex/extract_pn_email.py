# Project: Phone Number and Email Address Extractor
# press CTRL-A to select all the text, press CTRL-C to copy it to the clipboard, and then run your program

# Steps----------------------------
# 1. Get the text off the clipboard.
# 2. Find all phone numbers and email addresses in the text.
# 3. Paste them onto the clipboard.

# Now do this in Code ----------------
# 1. Use the "pyperclip" module to copy and paste strings.
# 2. Create two regexes, one for matching phone numbers and other for matching email addresses.
# 3. Find all matches, not just the first match, of both regexes.
# 4. Neatly format the matched strings into a single string to paste.
# 5. Display some kind of message if no matches were found in the text.

# Step 1: Create Regex for Phone Numbers
# 
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

