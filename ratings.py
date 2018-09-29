"""Restaurant rating lister."""


# put your code here
import sys

import_file = open(sys.argv[1], "r")

def create_sorted_dictionary_of_restaurant_ratings(rated_restaurants):
    restaurant_ratings_by_name = {}

    for line in rated_restaurants:
        line = line.strip().split(":")
        # print(line)
        dictionary_key = line[0]
        dictionary_value = line[1]
        restaurant_ratings_by_name[dictionary_key] = dictionary_value
        # print(restaurant_ratings_by_name)

    restaurant_ratings_by_name_sorted = sorted(restaurant_ratings_by_name.items())
    print(restaurant_ratings_by_name_sorted)
    # print(restaurant_ratings_by_name.items())

create_sorted_dictionary_of_restaurant_ratings(import_file)