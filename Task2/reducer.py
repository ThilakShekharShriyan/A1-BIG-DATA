# assignment 1 tast 2


import sys
import json
flag_value = 1

for line in sys.stdin:
    line = line.strip()
    res = json.loads(line)
    city = res["city"]
    state = res["state"]

    if (flag_value == 1):
        s_count = 0

        print(state)

        p_state = state
        p_city = city
        c_count = 0
        flag_value = 0

    if (city == p_city and state == p_state):
        c_count += 1

    elif (city != p_city and state == p_state):
        s_count = s_count + c_count

        print(p_city, c_count)

        p_city = city
        c_count = 1

    elif (city != p_city and state != p_state):
        s_count = s_count + c_count
        print(p_city, c_count)

        print(p_state, s_count)

        s_count = 0
        p_state = state
        print(p_state)

        p_city = city
        c_count = 1

if (s_count != 0 and c_count != 0):
    s_count = s_count + c_count

    print(p_city, c_count)
    print(p_state, s_count)
