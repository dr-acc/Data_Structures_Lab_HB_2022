#https://github.com/jciafardone/data-structure-lab.git

"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    opened_file = open(filename)
    
    species = set()
    
    for line in opened_file:
        villager = line.split("|")
        species.add(villager[0])

    #print(species)
    return species
    
all_species("villagers.csv")   


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    opened_file = open(filename)

    villagers = []

    if search_string == "All":
        for line in opened_file:
            villager = line.split("|")
            villagers.append(villager[0])
    else:
        for line in opened_file:
            villager = line.split("|")
            if villager[1] == search_string:
                villagers.append(villager[0])

    # TODO: replace this with your code
    #print(sorted(villagers))
    return sorted(villagers)

get_villagers_by_species("villagers.csv", search_string="All")


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    hobbies = ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    opened_file = open(filename)

    main_list = []
    villagers = []

    for line in opened_file:
        villager = line.split("|")
        villagers.append(villager)

    for hobby in hobbies:
        names = []
        for villager in villagers:
            if hobby == villager[3]:
                names.append(villager[0])
        main_list.append(names)
    
    # print(sorted(main_list[0]))
    # print(sorted(main_list[1]))
    return sorted(main_list)

all_names_by_hobby("villagers.csv")


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    main_list = []
    opened_file = open(filename)
    for line in opened_file:
        villager = line.split("|")
        villager = tuple(villager)
        main_list.append(villager)

    # print(main_list)
    return main_list
all_data("villagers.csv")


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    opened_file = open(filename)

    villagers = []

    for line in opened_file:
        villager = line.split("|")
        villagers.append(villager)

    for villager in villagers:
        if villager_name == villager[0]:
            #print(villager[4])
            return(villager[4])
    
    return None

find_motto("villagers.csv", "Johnny")


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    opened_file = open(filename)
    villagers = []
    personality = None
    likeminded = set()

    for line in opened_file:
        villager = line.split("|")
        villagers.append(villager)
    
    for villager in villagers:
        if villager[0] == villager_name:
            personality = villager[2]
    
    for villager in villagers:
        if villager[2] == personality:
            likeminded.add(villager[0])
    
#find villager in list that is in the input parameter, then store their personality as its own variable
#then iterate over list of lines looking for same personality 
#add names to set "likeminded"
    print(likeminded)
    return(likeminded)
find_likeminded_villagers("villagers.csv", "Cyrano")

