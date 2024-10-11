#!/usr/bin/env python3

from maasclient import MAASClient
import json
import sys
import argparse
import os
import time
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a performance test in MAAS")
    parser.add_argument('--apikey', help='MAAS API key. Can be provided using MAAS_API_KEY environment variable.')
    parser.add_argument('--url', help='MAAS URL. Can be provided using MAAS_URL environment variable.')
    parser.add_argument('--parallel', default=1, type=int, help='Number of parallel processes to run')
    parser.add_argument('--timeout', default=10, type=int, help='Request timeout')
    parser.add_argument('--duration', default=120, type=int, help='Test duration in seconds')
    args = parser.parse_args()
    
    apikey = args.apikey or os.environ.get('MAAS_API_KEY') 
    if not apikey:
        sys.exit("MAAS API key not provided")
    
    url = args.url or os.environ.get('MAAS_URL')
    if not url:
        sys.exit("MAAS URL not provided")

    client = MAASClient(apikey, url, timeout=args.timeout)
        
    test_duration = args.duration
    children = 0
    
    script_start = time.time()
    
    while True:
        elapsed = time.time() - script_start
        while children < args.parallel and elapsed < test_duration:
            pid = os.fork()
            if pid == 0:
                timed_out = False
                start = time.time()
                try:
                    machines = client.machines()
                except Exception as e:
                    timed_out = True
                end = time.time()
                elapsed = end - start
                
                result = "OK     " if not timed_out else "TIMEOUT"
                
                # timestamp in yyyy-mm-dd hh:mm:ss format
                ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                
                print(f"{ts}: {result} {elapsed:.2f} seconds")

                sys.exit(0)
            
            children += 1
        
        if children:
            pid, status = os.wait()
            children -= 1
        elif elapsed > test_duration:
            break
        