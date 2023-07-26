counter=0
mcounter=0
plot_args=""
run_test() {
    counter=$((counter + 1))
    plot_args="$plot_args $1:results/$counter.csv"
    python3 data_prep2.py $shrinking $expansion
    ./run_java.sh dml_scripts/t1.dml data/words2_$expansion.csv data/words_dictionary2_$shrinking.csv data/embeddings2_$shrinking.csv results/$counter.csv
}

run_test2() {
    counter=$((counter + 1))
    plot_args="$plot_args n$1:results/$counter.csv"
    python3 data_prep2.py $shrinking $expansion
    ./run_java2.sh dml_scripts/t2.dml data/words2_$expansion.csv data/words_dictionary2_$shrinking.csv data/embeddings2_$shrinking.csv results/$counter.csv
}

run_test_multi() {
    counter=$((mcounter + 1))
    plot_args="$plot_args m$1:results/m$mcounter.csv"
    python3 data_prep2.py $shrinking $expansion
    ./run_java.sh dml_scripts/t1.dml data/words2_$expansion.csv data/words_dictionary2_$shrinking.csv data/embeddings2_$shrinking.csv results/m$mcounter.csv -m
}

#start tests, non multi
shrinking=1
expansion=1
run_test2 w:2.5M

exit 0
run_test w:2.5M

echo "python3 plot.py $plot_args"
source myenv/bin/activate
python3 plot.py $plot_args
deactivate
exit 0

echo "python3 plot.py $plot_args"
python3 plot.py $plot_args