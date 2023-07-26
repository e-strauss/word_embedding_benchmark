#python3 plot-single.py  w:0.1M:results/1.csv snw:0.1M:results/2.csv mbw:0.1M:results/3.csv mnw:0.1M:results/4.csv mtw:0.1M:results/5.csv w:0.5M:results/6.csv snw:0.5M:results/7.csv mbw:0.5M:results/8.csv mnw:0.5M:results/9.csv mtw:0.5M:results/10.csv w:1M:results/11.csv snw:1M:results/12.csv mbw:1M:results/13.csv mnw:1M:results/14.csv mtw:1M:results/15.csv w:2M:results/16.csv snw:2M:results/17.csv mbw:2M:results/18.csv mnw:2M:results/19.csv mtw:2M:results/20.csv w:4M:results/21.csv snw:4M:results/22.csv mbw:4M:results/23.csv mnw:4M:results/24.csv mtw:4M:results/25.csv w:6M:results/26.csv snw:6M:results/27.csv mbw:6M:results/28.csv mnw:6M:results/29.csv mtw:6M:results/30.csv 
#sn:singlethreaded_new_denseblock-mb:multithreaded_baseline-mn:multithreaded_new_denseblock-mt:multithreaded_new_denseblock2 "Different-input-sizes,-same-dictionary-size-(10K)" Input-size

import csv, sys
import matplotlib.pyplot as plt
from datetime import datetime

color_codes = ['orange', 'b', 'g', 'r', 'c', 'm', 'y', 'k']
folder = sys.argv[1]
with open(folder + '/meta.txt') as f:
    meta = f.readlines()

file_names = meta[0][:-1]
legend = meta[1][:-1].replace("_"," ")
title = meta[2].split(" ")[0].replace("-"," ")
xlabel = meta[2].split(" ")[1][:-1].replace("-"," ")

legend = {i.split(':')[0] : i.split(':')[1] for i in legend.split('-')}
data = {v : [] for v in legend.keys()}
data["test_name"] = []

for file_name in file_names.split(' '):
    splitted = file_name.split(':')
    test_type = splitted[0]
    test_name = splitted[1]
    file_name = folder + "/" + splitted[2]

    if not test_name in data['test_name']:
        data['test_name'].append(test_name)

    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        values = [float(row[0]) for row in reader]

    encoder_avg = sum(values[3:6]) / 3
    no_key = True
    for key in legend.keys():
        if key in test_type:
            data[key].append(encoder_avg)
            no_key = False
            break
    if no_key:
        print("no key found for [{}]".format(test_type))
        #baseline_avg = sum(values[6:9]) / 3
        #data['baseline'].append(baseline_avg)
        #data['encoder'].append(encoder_avg)

fig, axs = plt.subplots(1, 1, figsize=(12, 8), gridspec_kw={'hspace': 1, 'wspace': 2})


def plot_results(test_name, test_data, ax, color, name):
    ax.plot(test_name, test_data, color_codes[color] + 'o-', label=name)

color = 0
for key, value in legend.items():
    if len(data[key]) == 0:
        continue
    print("{a} - {b}".format(a=key,b=value))
    axs.plot(data["test_name"], data[key], c=color_codes[color], ls='dashdot', marker='o', label=value)
    color += 1

axs.legend(fontsize='small')
axs.set_ylim(0)
axs.set_xlabel(xlabel)
axs.set_ylabel('Exucution time in ms')
axs.set_title(title)
axs.grid(True)

for k in data:
    print("{} : {}".format(k, data[k]))

datetime_string = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Print the date and time string
print(datetime_string)
plt.savefig('plots/plot-{a}-{b}.pdf'.format(a=sys.argv[-1],b=datetime_string), format='pdf')

# Close the plot (optional)
plt.close()