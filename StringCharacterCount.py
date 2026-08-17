if __name__ == "__main__":
    s = "Dhee1 Codin$ #@B"
    s = s.lower()
    v = ['a','e','i','o','u']
    count_d = 0
    count_sp = 0
    count_s = 0
    count_v = 0
    count_c = 0
    for ch in s:
        if ch.isalpha():
            if ch in v:
                count_v += 1
            else:
                count_c += 1
        elif ch.isdigit():
            count_d += 1
        elif ch == " ":
            count_s += 1
        else:
            count_sp += 1
    print(count_v)
    print(count_c)
    print(count_d)
    print(count_s)
    print(count_sp)
        