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
    return max_size


if __name__ == "__main__":
    #read usr input
    str = raw_input("Please input a string\n")
    max_size = find_max_substring(str)
    print "The max substring has a size of %d in string: \"%s\"" % (max_size, str)
