ts = [7,-10,13,8,4,-7.2,-12,-3.7,3.5,-9.6,6.5,-1.7,-6.2,7]

def closestToZero(temperatures):
    if temperatures:
        return min(temperatures, key=abs)
    else:
        return 0

print "Result: ", closestToZero(ts)
