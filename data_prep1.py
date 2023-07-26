import csv, random, sys

def expand_list(input_list, factor):
    expanded_list = []
    for _ in range(factor):
        expanded_list.extend(random.sample(input_list, len(input_list)))
    return expanded_list

if len(sys.argv) != 3:
    print("please specify shrinking and extension factor, e.g. python3 data_prep.py 2 10")
else:
    with open("/home/arnab/datasets/wiki_embeddings/wiki.en.vec.dict", 'r', newline='') as file:
        words = ['"{}"'.format(word[:-1]) if ',' in word else word[:-1] for word in file]
    length = int(len(words) / int(sys.argv[1]))
    words = words[:int(len(words) / int(sys.argv[1]))]

    with open("/home/arnab/datasets/wiki_embeddings/wiki_metaframe", 'r', newline='') as rfile:
        with open("data/words_dictionary2_{}.csv".format(sys.argv[1]), 'w', newline='') as wfile:
            for i in range(length):
                s = rfile.readline()
                if ',' in s:
                    s = s.split('·')
                    s = '"{a}"·{b}'.format(a=s[0], b=s[1])
                wfile.write(s)

    with open("/home/arnab/datasets/wiki_embeddings/wiki_csv", 'r', newline='') as rfile:
        with open("data/embeddings2_{}.csv".format(sys.argv[1]), 'w', newline='') as wfile:
            for i in range(length):
                wfile.write(rfile.readline())

    words = expand_list(words, int(sys.argv[1])*int(sys.argv[2]))
    words = [[word] for word in words]
    with open("data/words2_{}.csv".format(sys.argv[2]), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(words)


