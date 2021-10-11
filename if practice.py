# # A condition-controlled loop uses a true or false condition to control the number of times that it repeats, 
# # like asking a user if they want to continue with their online shopping after they add something to their "basket." 
# # This type of loop is also called a while loop.

# # A count-controlled loop repeats a specific number of times depending on the conditions, 
# # such as getting all the items in a list. This type of loop is also called a for loop.


# #While Loop
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# #For loop

# counties = ["Arapahoe","Denver","Jefferson"]

# for county in counties:
#     print(county)


# for i in range(len(counties)):
#     print(counties[i])

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)


# for num in range(5):
#     print(num)

# #Iterate through a dictionary

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# # # To get only the keys from a dictionary using a for loop, the loop can be written like we are iterating over a list or tuple.

# for county in counties_dict:
#     print(county)

# #To get the values of a dictionary, we iterate over the dictionary using the values() method, just like we used the keys() method.    

# for voters in counties_dict.values():
#     print(voters)


# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

#     # Get the Key-Value Pairs of a Dictionary

#     for key, value in dictionary_name.items():
#     print(key, value)

#     for county, voters in counties_dict.items():
#     print(county, voters)

#     When iterating over a dictionary:

# The first variable declared in the for loop is assigned to the keys.
# The second variable is assigned to the values.

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


#If we only want to print the county name from each dictionary, we can use county_dict['county'] in the print statement for the for loop.

for county_dict in voting_data:
    print(county_dict['county'])