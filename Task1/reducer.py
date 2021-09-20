# assignment 1 tast 1
import sys

(last_key, count) = (None, 0)


for line in sys.stdin:

    (key, value) = line.strip().split(" ")

    if last_key and last_key != key:

        print(last_key, count)

        (last_key, count) = (key, int(value))

    else:

        (last_key, count) = (key, count + int(value))
