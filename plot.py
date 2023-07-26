import csv, sys
import matplotlib.pyplot as plt
from datetime import datetime

color_codes = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

data =  {"Multi" :      {"w" : {"baseline" : [], "encoder" : [], "new denseblock" : [], "merged HashMaps" : [], "test_name" : []},
                         "d" : {"baseline" : [], "encoder" : [], "new denseblock" : [], "merged HashMaps" : [], "test_name" : []}}, 
         "Non-Multi" :  {"w" : {"baseline" : [], "encoder" : [], "new denseblock" : [], "test_name" : []},
                         "d" : {"baseline" : [], "encoder" : [], "new denseblock" : [], "test_name" : []}}}

for file_name in sys.argv[1:]:
    test_type = file_name.split(':')[0]
    test_name = file_name.split(':')[1]
    file_name = file_name.split(':')[2]

    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        values = [float(row[0]) for row in reader]

    encoder_avg = sum(values[3:6]) / 3
    mode = data['Multi'] if 'm' in test_type else data['Non-Multi']
    mode = mode['w'] if 'w' in test_type else mode['d']
    if not test_name in data['test_name']:
        data['test_name'].append(test_name)
    if 'n' in test_type:
        mode["new denseblock"].append(encoder_avg)
    elif 't' in test_type:
        mode["merged HashMaps"].append(encoder_avg)
    else:
        baseline_avg = sum(values[6:9]) / 3
        mode['baseline'].append(baseline_avg)
        mode['encoder'].append(encoder_avg)

fig, axs = plt.subplots(2, 2, figsize=(12, 8), gridspec_kw={'hspace': 1, 'wspace': 2})

def plot_results(baseline, encoder, test_name, ax, title, x_axis_label, denseblock=[], mergedmaps=[]):
    ax.plot(test_name, baseline, color_codes[0] + 'o-', label='baseline')
    ax.plot(test_name, encoder, color_codes[1] + 'o-', label='new encoder')
    if len(denseblock) > 0:
        ax.plot(test_name, denseblock, color_codes[2] + 'o-', label='new denseblock')
    if len(mergedmaps) > 0:
        ax.plot(test_name, mergedmaps, color_codes[3] + 'o-', label='merged HashMaps')
    ax.legend(fontsize='small')
    ax.set_ylim(0)
    ax.set_xlabel(x_axis_label)
    ax.set_ylabel('Exucution time in ms')
    ax.set_title(title)
    ax.grid(True)

if len(data['Non-Multi']['w']['test_name']) > 0:
    plot_results(data['Non-Multi']['w']['baseline'], data['Non-Multi']['w']['encoder'], data['Non-Multi']['w']['test_name'], axs[0][0],'Different input sizes, same dictionary size (10K)', 'Input size', data['Non-Multi']['w']['new denseblock'])
if len(data['Non-Multi']['d']['test_name']) > 0:
    plot_results(data['Non-Multi']['d']['baseline'], data['Non-Multi']['d']['encoder'], data['Non-Multi']['d']['test_name'], axs[0][1], 'Different dictionary sizes, same input size (5M)', 'Dictionary size', data['Non-Multi']['d']['new denseblock'])
if len(data['Multi']['w']['test_name']) > 0:
    plot_results(data['Multi']['w']['baseline'], data['Multi']['w']['encoder'], data['Multi']['w']['test_name'], axs[1][0],'Different input sizes, same dictionary size (10K), \n multi-threaded', 'Input size',data['Multi']['w']['new denseblock'], 'Dictionary size',data['Multi']['d']["merged HashMaps"])
if len(data['Multi']['d']['test_name']) > 0:
    plot_results(data['Multi']['d']['baseline'], data['Multi']['d']['encoder'], data['Multi']['d']['test_name'], axs[1][1], 'Different dictionary sizes, same input size (5M), \n multi-threaded', 'Dictionary size',data['Multi']['d']['new denseblock'], 'Dictionary size',data['Multi']['d']["merged HashMaps"])


#plt.title('Word Embedding Benchmark')
#plt.show()

datetime_string = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Print the date and time string
print(datetime_string)

plt.savefig('plots/plot-input+dict-{}.pdf'.format(datetime_string), format='pdf')

# Close the plot (optional)
plt.close()