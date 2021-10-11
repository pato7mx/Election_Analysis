print("What it is boiss")

#Dictionaries

#Initialize a dictonary:
# my_dictonary = {}
# my_dictonary2 = dict()

#If practice 
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# Operator	Meaning
# >	greater than
# >=	greater than or equal to
# <	less than
# <=	less than or equal to
# ==	equal to
# !=	not equal to


#Membership and logical operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
