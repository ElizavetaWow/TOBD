from collections import Counter

def count_letters(file):
    with open(file, 'r') as fp:
        return Counter(fp.read().lower())
