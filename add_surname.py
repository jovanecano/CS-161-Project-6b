#Author: Jovane Cano
#GitHub Username: jovanecano
#Date: 05/08/2024
#Description:
"""This function add_surname takes as parameter a list of names and adds the surname "Kardashian" to each name that
starts with the letter K """


def add_surname(first_names):
    """this function uses a list comprehension to traverse a list of names in specified list
    and if name starts with K, it adds the surname "Kardashian to it. Returns only the names that start with K"""
    return [name + " " + "Kardashian" for name in names if name.startswith("K")]


#names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
#complete_names = add_surname(names)
#print(add_surname(complete_names))