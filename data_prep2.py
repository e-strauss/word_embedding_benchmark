import csv, random, sys

def expand_list(input_list, factor):
    expanded_list = []
    for _ in range(factor):
        expanded_list.extend(random.sample(input_list, len(input_list)))
    return expanded_list

if len(sys.argv) != 3:
    print("please specify shrinking and extension factor, e.g. python3 data_prep.py 2 10")
else:
    with open("data/words.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        words = [word[0] for word in reader]
    length = int(len(words) / int(sys.argv[1]))
    words = words[:int(len(words) / int(sys.argv[1]))]

    with open("data/words_dictionary.csv", 'r', newline='') as rfile:
        with open("data/words_dictionary_{}.csv".format(sys.argv[1]), 'w', newline='') as wfile:
            for i in range(length):
                wfile.write(rfile.readline())

    with open("data/embeddings.csv", 'r', newline='') as rfile:
        with open("data/embeddings_{}.csv".format(sys.argv[1]), 'w', newline='') as wfile:
            for i in range(length):
                wfile.write(rfile.readline())

    words = expand_list(words, int(sys.argv[1])*int(sys.argv[2]))
    words = [[word] for word in words]
    with open("data/words_{}.csv".format(sys.argv[2]), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(words)


