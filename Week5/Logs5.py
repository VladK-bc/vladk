#!/usr/bin/python3
#Vlad K Logs5.py



import re
import csv
from collections import defaultdict

input_file = "wafeventlog"
output_file = "redirect.csv"

redirect_pattern = re.compile(r'\[msg "REDIRECT: (.*?) to (.*?)"]')
exclude_terms = ["ActiveSync", "Basic"]

with open(input_file, "r") as file:
    lines = file.readlines()

redirects = defaultdict(int)

for line in lines:
    if not any(term in line for term in exclude_terms):
        redirect_match = redirect_pattern.search(line)

        if redirect_match:
            from_domain = redirect_match.group(1)
            to_url = redirect_match.group(2)
            redirects[(from_domain, to_url)] += 1

with open(output_file, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Count", "From", "To"])
    for (from_domain, to_url), count in redirects.items():
        csvwriter.writerow([count, from_domain, to_url])
