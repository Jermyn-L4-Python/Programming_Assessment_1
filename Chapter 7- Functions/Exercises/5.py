#Create new function that takes two argument, a (city) and a default value (Greece)
def describe_city(city, country = "Greece"):
    print(f"{city} is located in {country}.")

#Print out "Athens" as the value of city
describe_city("Athens")

#Replace the values of the argument, city and country
describe_city("Amsterdam", "Netherlands")
describe_city("Tokyo", "Japan")