#!/usr/bin/env python3

# Open all *.log files in the current directory

import os
import re

for filename in os.listdir("."):
    if filename.endswith(".log"):
        with open(filename) as f:
            count = 0
            ok = 0
            fail = 0
            total = 0
            
            for line in f:
                # use a regex to extract the timestamp, status, and elapsed time
                
                match = re.search(r": (\w+)\s+([\d+.]+)\s+seconds", line)    
                
                if match:
                    status, elapsed = match.groups()
                    count += 1
                    if status == "OK":
                        ok += 1
                        total += float(elapsed)
                    else:
                        fail += 1

            print(f"{filename}: Success Rate: {100 * (ok / count):.2f}% Tests Executed: {count} Average Time: {total/ok:.2f} seconds")