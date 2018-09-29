"""Restaurant rating lister."""


# put your code here
import sys

import_file = open(sys.argv[1], "r")

def create_sorted_dictionary_of_restaurant_ratings(rated_restaurants):
    """ Creates sorted dictionary of restaurant ratings. """

    restaurant_ratings_by_name = {}

    for line in rated_restaurants:
        line = line.strip().split(":")
        dictionary_key = line[0]
        dictionary_value = line[1]
        restaurant_ratings_by_name[dictionary_key] = dictionary_value

    restaurant_ratings_by_name_sorted = sorted(restaurant_ratings_by_name.items())
    return(restaurant_ratings_by_name_sorted)


sorted_ratings = create_sorted_dictionary_of_restaurant_ratings(import_file)

def print_ratings(sorted_dictionary):
    for line in sorted_dictionary:
        print("{} is rated at {}".format(line[0], line[1]))

(print_ratings(sorted_ratings))