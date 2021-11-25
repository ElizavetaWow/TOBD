import csv

def mean_steps_for_file_mp(file):
    with open(file, 'r') as fp:
        d = {}
        reader = csv.reader(fp, delimiter=';')
        for line in reader:
            if line[1] not in d.keys():
                d[line[1]] = [0, 0]
            d[line[1]][0] += int(line[2])
            d[line[1]][1] += 1
    return d 
