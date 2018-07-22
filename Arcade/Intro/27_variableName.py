import string 

def variableName(name):
    a = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    if name[0] in '0123456789': return False
    for i in range(len(name)):
        if name[i] not in a: return False
    return True
    