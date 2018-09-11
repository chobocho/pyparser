def hash(str):
    h = 0
    for s in str:
        h = h * 31 + ord(s)
        if (h > 100000007):
            h %= 100000007
    return h

def findemail(str):
    email = ""
    isPush = False

    for c in str:
        if c == '<':
            isPush = True
            continue
        elif c == '>':
            email += ';'
            isPush = False
            continue
        if isPush:
            email += c

    return email