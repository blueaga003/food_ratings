"""Restaurant rating lister."""


# put your code here
import sys

import_file = open(sys.argv[1], "r")

restaurant_ratings_by_name = {}

for line in import_file:
    line = line.strip().split(":")
    print(line)
    dictionary_key = line[0]
    dictionary_value = line[1]
    restaurant_ratings_by_name[dictionary_key] = dictionary_value
    print(restaurant_ratings_by_name)
    