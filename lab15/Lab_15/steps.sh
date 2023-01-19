#!/usr/bin/env bash

time python3 task_1.py
echo "Чистый питон"
echo " "
time ./task
echo "Чистый си"
echo " "
time ./task_1.bin
echo "Nuitka"
echo " "
time python3 task_4.py
echo "So"
echo " "
# gcc -Wall task_2.c -o task -lm
# python3 -m nuitka task_1.py
# gcc task_4_lib_c.c -fPIC -shared -o c_shared_lib.so -lm -Ofast -march=native
