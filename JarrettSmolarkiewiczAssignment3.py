"""
INF360 VA - Programming with Python
Jarrett Smolarkiewicz
Assignment 3

(1/1 points) Initial Comments.
"""

"""
Instructor Zeller... I did my best on this assignment but got stumped on questions 4 and 6 and could not figure them out before the assignment was due.
I understand I will not be getting credit for these, but will follow up with you via email to see if we could meet via zoom and work through them together so I know where I went wrong. 
"""
import pprint

# STEP 1: (5/5 points) Create a dictionary for each vehicle that contains the fields/keys and values listed above (in Blackboard).
car1 = {"Name":                                 "Ka",
        "Year Introduced":                      "1996",
        "Production of the Current Model":      "2014",
        "Generation":                           "3rd",
        "Vehicle Information":                  "Developed by Ford Brazil as a super mini car"
        }
car2 = {"Name":                                 "Fiesta",
        "Year Introduced":                      "1976",
        "Production of the Current Model":      "2017",
        "Generation":                           "7th",
        "Vehicle Information":                  "Ford's long running subcompact line based on global B-car Platform"
        }
car3 = {"Name":                                 "Focus",
        "Year Introduced":                      "1998",
        "Production of the Current Model":      "2018",
        "Generation":                           "3rd",
        "Vehicle Information":                  "Ford's Compact car based on global C-car platform"
        }
car4 = {"Name":                                 "Mondeo",
        "Year Introduced":                      "1992",
        "Production of the Current Model":      "20212",
        "Generation":                           "2nd",
        "Vehicle Information":                  "Mid sized passenger sedan with \"One-Ford\" design based on CD4 platform"
        }
car5 = {"Name":                                 "Fusion",
        "Year Introduced":                      "2005",
        "Production of the Current Model":      "2014",
        "Generation":                           "5th",
        "Vehicle Information":                  "Similar to Mondero"
        }
car6 = {"Name":                                 "Taurus",
        "Year Introduced":                      "1986",
        "Production of the Current Model":      "2009",
        "Generation":                           "6th",
        "Vehicle Information":                  "Full sized car based on D3 platform"
        }
car7 = {"Name":                                 "Fiesta ST",
        "Year Introduced":                      "2013",
        "Production of the Current Model":      "2013",
        "Generation":                           "1st",
        "Vehicle Information":                  "Fiesta's high performance factory tune"
        }
car8 = {"Name":                                 "Focus RS",
        "Year Introduced":                      "2015",
        "Production of the Current Model":      "2015",
        "Generation":                           "1st",
        "Vehicle Information":                  "Special high performance Focus developed by SVT"
        }
car9 = {"Name":                                 "Mustang",
        "Year Introduced":                      "1964",
        "Production of the Current Model":      "2014",
        "Generation":                           "6th",
        "Vehicle Information":                  "Ford's long running pony/muscle car"
        }
car10 = {"Name":                                "GT",
        "Year Introduced":                      "2004",
        "Production of the Current Model":      "2016",
        "Generation":                           "2nd",
        "Vehicle Information":                  "Ford's limited production super car inspired by the legendary race car GT40"
        }

cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

# STEP 2: (5/5 points) Write a function that will take a list of these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
def newDictionary(carlist):
        new_dictionary = {}
        for car in carlist:
                new_dictionary[car["Name"]] = car
        return new_dictionary

newDictionary(cars)

# STEP 3: (5/5 points) Write a function that will go through the newly created dictionary and return a list of all the car's names, sorted alphabetically.
def carSort(new_dictionary):
        new_dictionary = (newDictionary(cars))
        nameList = list(new_dictionary)
        nameList.sort()
        for name in nameList:
                new_dictionary[name] = name
        return nameList

carSort(newDictionary(cars))

"""
I did not figure out STEP 4 but included as far as I got in testing...
# STEP 4: (5/5 points) Write a function that will go through the newly created dictionary and return a dictionary of all the cars names and year introduced.
def carYear(new_dictionary): # newDictionary(cars)
        #print(new_dictionary.values())
        for name, year in new_dictionary.values():
                name = str(new_dictionary.get("Name", 0))
                year = str(new_dictionary.get("Year Introduced", 0))
                print(name)
        #name = for key in new_dictionary.values()
        
        #name = [key["Name"] for key in new_dictionary]
        #year = [value["Year Introduced"] for value in new_dictionary]
        #pprint.pprint(name)
                
                #car_year_dictionary[value["Year Introduced"]] = value
                #value = this_dictionary.get(value["Year Introduced"])
                #result = {key: value}
                #print(x)
        #for key in car_year_dictionary.keys():
        #        key = key
        #for value in car_year_dictionary.values():
                #value = value["Year Introduced"]
        #car_year_dictionary = this_dictionary.items()
        
        #for key, value in car_year_dictionary.items():
                #key = list(key[value])
                #value = list(car_year_dictionary)
                #value = value["Year Introduced"]
                #print(key["Name"])
                #value = list(car_year_dictionary[value["Year Introduced"]])
                #x = car_year_dictionary.get(key)
                #y = car_year_dictionary.get(value["Year Introduced"])
        
        #new_dictionary = {}
        #for key, value in car_year_dictionary:
        #        new_dictionary[key["Name"]] = key
        #        new_dictionary[values["Year Introduced"]] = values
        
        #print({key: value})
        #print({key: value})
        #print({key: value})
        #print(new_dictionary)
        #print(key)
        #print(value)
        #pprint.pprint(new_dictionary[value])
        

#carYear(newDictionary(cars))
#pprint.pprint(cars)
#pprint.pprint(newDictionary(cars))
#print(carSort(newDictionary(cars)))
#print(carYear(newDictionary(cars)))
"""

# STEP 5: (5/5 points) Use a print statement to show the results of the function from step 3, each on their own line.
print(* carSort(newDictionary(cars)), sep= "\n")

"""
I did not figure out STEP 6 but included as far as I got in testing...
# STEP 6: (5/5 points) Use a print statement to show the results of the function from step 4 to display in the format: year : name. Sort by year introduced.
"""
#print(carYear(newDictionary(cars)))
