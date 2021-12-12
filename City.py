class City:
    """
    this class represents a city
    attributes:
        name - name of city
        x - x coordinate
        y - y coordinate
    """
    def __init__(self, line):
        tokens = line.split(" ")
        self.name = tokens[0]
        self.x = float(tokens[1])
        self.y = float(tokens[2])

    def distance(self, other):
        """
        calculates the distance between two cities
        input:
            self
            other - the other city
        output:
            distance between self and the other city
        """
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

    def __str__(self):
        """
        string representation of a city
        input:
            self
        output:
            string representing the city
        """
        return "name = " + str(self.name) + " x = " + str(self.x) + " y = " + str(self.y)

    @staticmethod
    def readFromFile(file, storage):
        """
        used to read in cities from file
        input:
            file - file from which to read
            storage - space into which cities are read
        output:
            NA
        """
        for line in file:
            city = City(line)
            storage[city.name] = city


#code for testing
if __name__ == '__main__':
    cityList = {}
    f = open("data_tsp.txt", 'r')
    City.readFromFile(f, cityList)
    print(cityList["1"])
    print(cityList["2"])
    print(cityList["1"].distance(cityList["2"]))
