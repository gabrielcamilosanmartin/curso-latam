import sys

sys.argv.pop(0)
print (sorted(map(int, sys.argv))[2])