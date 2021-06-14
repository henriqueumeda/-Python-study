###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_copy = list(sorted(cows.items(), key=lambda item: item[1], reverse=True))
    spaceship = []
    spaceship_trip = []
    while len(cows_copy) != 0:
        trip_weight = 0
        key = 0
        while key < len(cows_copy):
            if cows_copy[key][1] + trip_weight <= limit:
                spaceship_trip.append(cows_copy[key][0])
                trip_weight += cows_copy[key][1]
                cows_copy.pop(key)
                key -= 1
                if trip_weight == limit:
                    break
            key += 1
        spaceship.append(spaceship_trip[:])
        spaceship_trip.clear()
    return spaceship
    # cows_copy = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))
    # spaceship = []
    # spaceship_trip = []
    # while len(cows_copy) != 0:
    #     trip_weight = 0
    #     for key in list(cows_copy):
    #         if cows_copy[key] + trip_weight <= limit:
    #             spaceship_trip.append(key)
    #             trip_weight += cows_copy[key]
    #             del cows_copy[key]
    #             if trip_weight == limit:
    #                 break
    #     spaceship.append(spaceship_trip[:])
    #     spaceship_trip.clear()
    # return spaceship


# Problem 2
def brute_force_cow_transport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    travel_options = get_partitions(list(cows))
    for spaceship in sorted(travel_options, key=len):
        valid_spaceship = True
        for spaceship_trip in spaceship:
            spaceship_trip_weight = 0
            for cow in spaceship_trip:
                cow_weight = cows[cow]
                spaceship_trip_weight += cow_weight
            if spaceship_trip_weight > limit:
                valid_spaceship = False
                break
        if valid_spaceship == True:
            return spaceship

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    print('Greedy algorithm')
    start = time.time()
    print('Number of trips:', len(greedy_cow_transport(cows, limit)))
    end = time.time()
    print('Time:', end - start)
    print()
    print('Brute force algorithm')
    start = time.time()
    print('Number of trips:', len(brute_force_cow_transport(cows, limit)))
    end = time.time()
    print('Time:', end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()
