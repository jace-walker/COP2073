# Jace Walker      Programming Exercise 13

# This program contains the population numbers of ten FL cities. Then, simulates the pop growth of the cities over 20
# years and graphs the results. The user can pick which city gets graphed.

# need to import numpy for the arrays and matplotlib for the graphing
import numpy as np
import matplotlib.pyplot as mpl

# create for later
population = {}


# function that contains city population data
def population_JW():
    fl_cities = {  'Tallahassee': 202221,
        'Lakeland': 133364,
        'Gainesville': 145812,
        'Sarasota': 57602,
        'Parkland': 37911,
        'Kissimmee': 81269,
        'Miami': 455924,
        'Tampa': 403463,
        'Jacksonville': 985843,
        'Orlando': 320742 }

# creates array for each city
    for city, pop in fl_cities.items():
        population[city] = np.array([[2023, pop]])


# simulates 2% growth for each city in the database
# the old and new populations get saved for graphing
def simulate_growth():
    for city in population:
        city_data = population[city]
        for year in range(2024, 2024 + 20):
            old_population = city_data[-1, 1]
            new_population = int(old_population * 1.02)
            new_row = np.array([[year, new_population]])
            city_data = np.vstack((city_data, new_row))
        population[city] = city_data


# this function asks user for input and graphs their chosen city
def graph_growth():
    cities = list(population.keys())

# found enumerate online to display cities neater
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    print()
# i title cased it automatically bc was tired of having to capitalize everytime
    choice = input('Which city would you like to see grow?: ').title()

# incase user makes mistake
    if choice not in cities:
        print('error')
        return

    city_data = population[choice]
# years row of array
    years = city_data[:, 0]
# pop row of array
    populations = city_data[:, 1]

# graphs chosen city's population growth
    mpl.plot(years, populations)
    mpl.title(f"{choice}'s Population Growth")
    mpl.ylabel('Population')
    mpl.xlabel('Year')
    mpl.show()

# main function that calls all previous functions
def main():

# cosmetics
    print('Florida City Population Growth Simulator')
    print('--------------------------------')

    population_JW()
    simulate_growth()
    graph_growth()

main()
