"""
Given s string, Find max size of a sub-string, in which no duplicate chars present.
"""


def find_max_substring(str):
    max_size = 0
    l = []
    current_size = 0
    if str:
        for e in str:
            if e in l:
                if current_size > max_size:
                    max_size = current_size
                current_size = 0
                l = []
            else:
                current_size += 1
                l.append(e)
    if current_size > max_size:
        max_size = current_size

    return max_size


if __name__ == "__main__":
    # read user input
    user_input = raw_input("Please input a string\n")
    max_size = find_max_substring(user_input)
    print("The max substring has a size of %d in string: \"%s\"" % (max_size, user_input))
