counter=0
mcounter=0
plot_args=""
run_test() {
    counter=$((counter + 1))
    plot_args="$plot_args $1:results/$counter.csv"
    python3 data_prep2.py $shrinking $expansion
    ./run_java.sh dml_scripts/t1.dml data/words_$expansion.csv /home/arnab/datasets/wiki_embeddings/wiki_csv /home/arnab/datasets/wiki_embeddings/wiki_metaframe results/$counter.csv
}

run_test2() {
    counter=$((counter + 1))
    plot_args="$plot_args n$1:results/$counter.csv"
    python3 data_prep2.py $shrinking $expansion
    ./run_java2.sh dml_scripts/t2.dml data/words_$expansion.csv data/words_dictionary_$shrinking.csv data/embeddings_$shrinking.csv results/$counter.csv
}