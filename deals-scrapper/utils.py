__author__ = 'rajatgoyal'

def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<128)

def key_lookup(d, lookup):
    for key, value in d.iteritems():
        if key in lookup:
            return value

    return ""