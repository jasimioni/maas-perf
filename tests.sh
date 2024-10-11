#!/bin/bash

export MAAS_API_KEY="kUw3RSM7j5FFbk5gEw:Kq9HLFHVVT7m7TbChe:3J4SQmtLtRLkx29MnKHmrHqgJhYE5NTy"

# export MAAS_URL=http://192.168.122.122:5240/MAAS/
#   ./perf-test.py --parallel 1 --timeout 180 --duration 30 > p01_1c_4w_2cpu.log
#   sleep 15
#   ./perf-test.py --parallel 2 --timeout 180 --duration 30 > p02_1c_4w_2cpu.log
#   sleep 15
#   ./perf-test.py --parallel 4 --timeout 180 --duration 60 > p04_1c_4w_2cpu.log
#   sleep 15
#   ./perf-test.py --parallel 8 --timeout 180 --duration 90 > p08_1c_4w_2cpu.log
#   sleep 15
#   ./perf-test.py --parallel 16 --timeout 180 --duration 120 > p16_1c_4w_2cpu.log
#   sleep 15
#   ./perf-test.py --parallel 32 --timeout 180 --duration 120 > p32_1c_4w_2cpu.log
#   sleep 15

#    ./perf-test.py --parallel 1 --timeout 180 --duration 30 > p01_1c_8w_2cpu.log
#    sleep 15
#    ./perf-test.py --parallel 2 --timeout 180 --duration 30 > p02_1c_8w_2cpu.log
#    sleep 15
#    ./perf-test.py --parallel 4 --timeout 180 --duration 60 > p04_1c_8w_2cpu.log
#    sleep 15
#    ./perf-test.py --parallel 8 --timeout 180 --duration 90 > p08_1c_8w_2cpu.log
#    sleep 15
#    ./perf-test.py --parallel 16 --timeout 180 --duration 120 > p16_1c_8w_2cpu.log
#    sleep 15
#    ./perf-test.py --parallel 32 --timeout 180 --duration 120 > p32_1c_8w_2cpu.log
#    sleep 15

#   ./perf-test.py --parallel 1 --timeout 180 --duration 30 > p01_1c_8w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 2 --timeout 180 --duration 30 > p02_1c_8w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 4 --timeout 180 --duration 60 > p04_1c_8w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 8 --timeout 180 --duration 90 > p08_1c_8w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 16 --timeout 180 --duration 120 > p16_1c_8w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 32 --timeout 180 --duration 120 > p32_1c_8w_4cpu.log
#   sleep 15

#   export MAAS_URL=http://192.168.122.214/MAAS/
#   ./perf-test.py --parallel 1 --timeout 180 --duration 30 > p01_2c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 2 --timeout 180 --duration 30 > p02_2c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 4 --timeout 180 --duration 60 > p04_2c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 8 --timeout 180 --duration 90 > p08_2c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 16 --timeout 180 --duration 120 > p16_2c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 32 --timeout 180 --duration 120 > p32_2c_4w_4cpu.log
#   sleep 15

#   export MAAS_URL=http://192.168.122.214/MAAS/
#   ./perf-test.py --parallel 1 --timeout 180 --duration 30 > p01_3c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 2 --timeout 180 --duration 30 > p02_3c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 4 --timeout 180 --duration 60 > p04_3c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 8 --timeout 180 --duration 90 > p08_3c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 16 --timeout 180 --duration 120 > p16_3c_4w_4cpu.log
#   sleep 15
#   ./perf-test.py --parallel 32 --timeout 180 --duration 120 > p32_3c_4w_4cpu.log
#   sleep 15

export MAAS_URL=http://192.168.122.214/MAAS/
./perf-test.py --parallel 1 --timeout 180 --duration 30 > p01_3c_8w_4cpu.log
sleep 15
./perf-test.py --parallel 2 --timeout 180 --duration 30 > p02_3c_8w_4cpu.log
sleep 15
./perf-test.py --parallel 4 --timeout 180 --duration 60 > p04_3c_8w_4cpu.log
sleep 15
./perf-test.py --parallel 8 --timeout 180 --duration 90 > p08_3c_8w_4cpu.log
sleep 15
./perf-test.py --parallel 16 --timeout 180 --duration 120 > p16_3c_8w_4cpu.log
sleep 15
./perf-test.py --parallel 32 --timeout 180 --duration 120 > p32_3c_8w_4cpu.log
sleep 15
