import collections
import re

def read_time_machine():
    with open('./timemachine.txt', 'r', encoding='utf-8') as f:
        print(f)
        lines = [re.sub('[^a-z]+','',line.strip().lower()) for line in f]
    return lines

lines = read_time_machine()
lines