import time

def print_cool_pattern():
    pattern = "Prabal Khare UPDATE"
    rows = 19  
    delay = 0.01 

    for i in range(rows):
        for j in range(i + 1):
            print(pattern[j % len(pattern)], end=' ')
            time.sleep(delay)
        print()
        time.sleep(delay)

print_cool_pattern()
