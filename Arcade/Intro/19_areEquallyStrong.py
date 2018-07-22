def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft+yourRight != friendsLeft+friendsRight: 
        return False
    elif min(yourLeft,yourRight) == min(friendsLeft,friendsRight):
        return True
    else: return False