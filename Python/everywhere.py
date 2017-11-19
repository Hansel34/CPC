testCase = int(input())

for x in range(testCase):
	city = []
	cities = int(input())
	for y in range(cities):
		newCity = input()
		if newCity not in city:
			city.append(newCity)
	print(len(city))


	 