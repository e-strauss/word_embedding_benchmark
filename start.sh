counter=0
mcounter=0
plot_args=""
run_test() {
    counter=$((counter + 1))
    plot_args="$plot_args $1:results/$counter.csv"
    python3 data_prep2.py $shrinking $expansion
    ./run_java.sh dml_scripts/t1.dml data/words_$expansion.csv data/words_dictionary_$shrinking.csv data/embeddings_$shrinking.csv results/$counter.csv
}

run_test2() {
    counter=$((counter + 1))
    plot_args="$plot_args n$1:results/$counter.csv"
    python3 data_prep2.py $shrinking $expansion
    ./run_java2.sh dml_scripts/t2.dml data/words_$expansion.csv data/words_dictionary_$shrinking.csv data/embeddings_$shrinking.csv results/$counter.csv
}

run_test_multi() {
    counter=$((mcounter + 1))
    plot_args="$plot_args m$1:results/m$mcounter.csv"
    python3 data_prep2.py $shrinking $expansion
    ./run_java.sh dml_scripts/t1.dml data/words_$expansion.csv data/words_dictionary_$shrinking.csv data/embeddings_$shrinking.csv results/m$mcounter.csv -m
}

#start tests, non multi
shrinking=1

expansion=240
run_test w:2.4M

expansion=360
run_test w:3.6M

expansion=480
run_test w:4.8M

expansion=600
run_test w:6.0M

expansion=720
run_test w:7.2M

#new encoder

expansion=240
run_test2 w:2.4M

expansion=360
run_test2 w:3.6M

expansion=480
run_test2 w:4.8M

expansion=600
run_test2 w:6.0M

expansion=720
run_test2 w:7.2M

echo "python3 plot.py $plot_args"
source myenv/bin/activate
python3 plot.py $plot_args
deactivate
exit 0


#multi-threaded

expansion=100
shrinking=50
run_test_multi d:0.2K

shrinking=10
run_test_multi d:1K

shrinking=2
run_test_multi d:5K

shrinking=1
run_test_multi d:10K

expansion=40
run_test_multi w:400K

expansion=80
run_test_multi w:800K

expansion=160
run_test_multi w:1600K

expansion=240
run_test_multi w:2400K

echo "python3 plot.py $plot_args"
python3 plot.py $plot_args
