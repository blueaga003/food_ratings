"""Restaurant rating lister."""


# put your code here
import sys

import_file = open(sys.argv[1], "r")

def create_sorted_dictionary_of_restaurant_ratings(rated_restaurants):
    """ Creates sorted dictionary of restaurant ratings. """

    restaurant_ratings_by_name = {}

    for line in rated_restaurants:
        name, rating = line.strip().split(":")
        restaurant_ratings_by_name[name] = rating

    return sorted(restaurant_ratings_by_name.items())

sorted_ratings = create_sorted_dictionary_of_restaurant_ratings(import_file)

def print_ratings(sorted_dictionary):
    """ Print out sorted ratings dictionary. """

    for line in sorted_dictionary:
        print("{} is rated at {}".format(line[0], line[1]))

(print_ratings(sorted_ratings))