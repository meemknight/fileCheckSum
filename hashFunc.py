import sys
import hashlib

def hashFunc(s):
    return hashlib.sha224(s.encode()).hexdigest()

def assertionTool(val, msg):
    if not val:
        print(msg)
        sys.exit(0)