import random, sys, os

def expand_list(input_list, factor):
    expanded_list = []
    for _ in range(factor):
        expanded_list.extend(random.sample(input_list, len(input_list)))
    return expanded_list

if len(sys.argv) != 3:
    print("please specify shrinking and extension factor, e.g. python3 data_prep.py 2 10")
else:
    with open("data_default/words2.csv", 'r', newline='') as file:
        words = file.readlines()
    length = int(len(words) / int(sys.argv[1]))
    words = words[:int(len(words) / int(sys.argv[1]))]

    file_name = "data/words_dictionary2_{}.csv".format(sys.argv[1])
    if not os.path.exists(file_name):
        with open("data_default/words_dictionary2.csv", 'r', newline='') as rfile:
            with open(file_name, 'w', newline='') as wfile:
                for i in range(length):
                    wfile.write(rfile.readline())

    file_name = "data/word_embeddings2_{}.csv".format(sys.argv[1])
    if not os.path.exists(file_name):
        with open("data_default/word_embeddings2.csv", 'r', newline='') as rfile:
            with open(file_name, 'w', newline='') as wfile:
                for i in range(length):
                    wfile.write(rfile.readline())

    file_name = "data/words2_{a}_{b}.csv".format(a=sys.argv[1],b=sys.argv[2])
    if not os.path.exists(file_name):
        words = expand_list(words, int(sys.argv[2]))
        with open(file_name, 'w', newline='') as file:
            for w in words:
                    file.write(w)