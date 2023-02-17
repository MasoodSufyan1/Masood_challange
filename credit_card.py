import re

creditcard_regex = re.compile(r'[4-6][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}')

def check_consecutive(s):
    ch = s[0]
    count = 1
    for i in xrange(1, len(s)):
        if s[i] == '-':
            continue
        if s[i] == ch:
            count += 1
            if count == 4:
                return False
        else:
            ch = s[i]
            count = 1
    return True

def check_dash(s):
    if s.count('-') == 0 or s.count('-') == 3:
        return True
    else:
        return False

N = input("Input credit card count: ")
for _ in xrange(N):
    s = raw_input("Enter credit card number: ").strip()
    if creditcard_regex.match(s) and check_consecutive(s) and check_dash(s):
        print 'Valid'
    else:
        print 'Invalid'