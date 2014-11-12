from time import gmtime, strftime

def now():
    return strftime("%m/%d/%Y %H:%M:%S", gmtime())
