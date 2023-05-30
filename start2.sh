run_test() {
    python3 data_prep2.py $shrinking $expansion
    ./run_java.sh dml_scripts/t1.dml data/words_$expansion.csv data/words_dictionary_$shrinking.csv data/embeddings_$shrinking.csv results2/$1.csv
}

run_test_multi() {
    python3 data_prep2.py $shrinking $expansion
    ./run_java2.sh dml_scripts/t1.dml data/words_$expansion.csv data/words_dictionary_$shrinking.csv data/embeddings_$shrinking.csv results2/$1.csv -m
}

shrinking=1
expansion=120
run_test 10

exit 0



expansion=40
run_test 5

expansion=80
run_test 6

expansion=120
run_test 7

expansion=160
run_test 8

expansion=200
run_test 9

expansion=240
run_test 10

python3 plot.py w:400K:results/5.csv \
    w:800K:results/6.csv w:1200K:results/7.csv w:1600K:results/8.csv w:2000K:results/9.csv w:2400K:results/10.csv \