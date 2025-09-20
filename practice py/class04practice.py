#  Topic list
city_0 = "Anlanta"
city_1 = "Los Angles"
city_2 = "china"
city_3 = "california"
city_4 = "Japan"

address = id(city_0)
print(address)

address = id(city_4)
print(address)

list_cities = [ "Anlanta", "Los Angles", "china", "california", "Japan"]
print(type(list_cities) , id(list_cities))

list_cities.append("Islamabad")
print(list_cities)

list_cities.extend(["Karachi", "Australia", "Paris"]) # old list k saath ye new list add kr dyga last main old list k
print(list_cities)

list_cities.insert(0, "Russia")
print(list_cities)