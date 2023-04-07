#!/usr/bin/python3
#Vlad K Logs5.py



import re
import csv

input_file = "wafeventlog"
output_file = "redirect.csv"

count_pattern = re.compile(r"\[id \"(\d+)\"\]")
from_pattern = re.compile(r"\[client (\d+\.\d+\.\d+\.\d+)\]")
to_pattern = re.compile(r"\[hostname \"(\d+\.\d+\.\d+\.\d+)")
exclude_term = "ActiveSync"

with open(input_file, "r") as file:
    lines = file.readlines()

results = []

for line in lines:
    if exclude_term not in line:
        count_match = count_pattern.search(line)
        from_match = from_pattern.search(line)
        to_match = to_pattern.search(line)

        if count_match and from_match and to_match:
            count = count_match.group(1)
            from_ip = from_match.group(1)
            to_ip = to_match.group(1)
            results.append((count, from_ip, to_ip))

with open(output_file, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Count", "From", "To"])
    csvwriter.writerows(results)
