run_test() {
    python3 data_prep2.py $shrinking $expansion
    ./run_java.sh dml_scripts/t1.dml data/words_$expansion.csv data/words_dictionary_$shrinking.csv data/embeddings_$shrinking.csv results/$1.csv
}

run_test_multi() {
    python3 data_prep2.py $shrinking $expansion
    ./run_java.sh dml_scripts/t1.dml data/words_$expansion.csv data/words_dictionary_$shrinking.csv data/embeddings_$shrinking.csv results/$1.csv -m
}
shrinking=10
expansion=100
run_test 9

expansion=240
run_test 10

exit 0

expansion=100
shrinking=50
run_test 1

shrinking=10
run_test 2

shrinking=2
run_test 3

shrinking=1
run_test 4

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

#multi-threaded

expansion=100
shrinking=50
run_test_multi 11

shrinking=10
run_test_multi 12

shrinking=2
run_test_multi 13

shrinking=1
run_test_multi 14

expansion=40
run_test_multi 15

expansion=80
run_test_multi 16

expansion=120
run_test_multi 17

expansion=160
run_test_multi 18

expansion=200
run_test_multi 19

expansion=240
run_test_multi 20


python3 plot.py d:0.2K:results/1.csv d:1K:results/2.csv d:5K:results/3.csv d:10K:results/4.csv w:400K:results/5.csv \
w:800K:results/6.csv w:1200K:results/7.csv w:1600K:results/8.csv w:2000K:results/9.csv w:2400K:results/10.csv \
md:0.2K:results/11.csv md:1K:results/12.csv md:5K:results/13.csv md:10K:results/14.csv mw:400K:results/15.csv \
mw:800K:results/16.csv mw:1200K:results/17.csv mw:1600K:results/18.csv mw:2000K:results/19.csv mw:2400K:results/20.csv