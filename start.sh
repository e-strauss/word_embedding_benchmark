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

expansion=100
shrinking=50
run_test2 d:0.2K

shrinking=10
run_test2 d:1K

expansion=100
shrinking=50
run_test d:0.2K

shrinking=10
run_test d:1K

echo "python3 plot.py $plot_args"
python3 plot.py $plot_args
exit 0

#start tests, non multi

expansion=100
shrinking=50
run_test d:0.2K

shrinking=10
run_test d:1K

shrinking=2
run_test d:5K

shrinking=1
run_test d:10K

expansion=40
run_test w:400K

expansion=80
run_test w:800K

expansion=160
run_test w:1600K

expansion=240
run_test w:2400K

#new encoder
expansion=100
shrinking=50
run_test2 d:0.2K

shrinking=10
run_test2 d:1K

shrinking=2
run_test2 d:5K

shrinking=1
run_test2 d:10K

expansion=40
run_test2 w:400K

expansion=80
run_test2 w:800K

expansion=160
run_test2 w:1600K

expansion=240
run_test2 w:2400K

echo "python3 plot.py $plot_args"
python3 plot.py $plot_args

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