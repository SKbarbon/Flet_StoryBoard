import sys

def is_phone_platform ():
    if "ios" in str(sys.platform):
        return True
    return False