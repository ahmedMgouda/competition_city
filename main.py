class Point:
    def __init__(self, pid, x, y, city):
        self.Id = pid
        self.X = x
        self.Y = y
        self.City = city 
class City:
     def __init__(self, name, leftUpperCorner, rightLowerCorner):
        self.Name = name
        self.LeftUpperCorner = leftUpperCorner
        self.RightLowerCorner  = rightLowerCorner
class Operation:
    import csv
    #This function for reading CSV files 
    #Type could be 'cities' or 'points'
    def ReadFile(self, fileName, type):
        items = []
        with open(fileName) as csv_file:
            csv_reader = self.csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if type == "cities":
                        items.append(City(row[0], Point("",row[1], row[2], row[0]), Point("", row[3], row[4], row[0])))
                    else:
                        items.append(Point(row[0], row[1], row[2], ""))
                    line_count += 1
        return items
    #This Function for writing points withs it city name in csv file
    #It takes csv file name and array of points
    def WriteFile(self, fileName, points):
        with open(fileName, mode='w') as csv_file:
            fieldnames = ['ID', 'X', 'Y', 'City']
            writer = self.csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for point in points:
                writer.writerow({'ID':point.Id, 'X':point.X, 'Y':point.Y, 'City':point.City})
    #This funtion is used for check if the point lay inside the city or not 
    #by represent city as rectangle and divide it for foure triangle with point as the triangles head
    #check if the combines triangles area area equal or higher than the rect area
    def CheckPoint(self, cities, points):
        for point in points:
            for city in cities:
                longSide = abs(int(city.LeftUpperCorner.X) - int(city.RightLowerCorner.X))
                narrowSide = abs(int(city.LeftUpperCorner.Y) - int(city.RightLowerCorner.Y))
                rectArea = abs(longSide * narrowSide)
                triArea = abs(0.5 * longSide * (int(city.LeftUpperCorner.Y) - int(point.Y))) 
                triArea += abs(0.5 * longSide * (int(city.RightLowerCorner.Y) - int(point.Y)))
                triArea += abs(0.5 * narrowSide * (int(city.LeftUpperCorner.X) - int(point.X)))
                triArea += abs(0.5 * narrowSide * (int(city.RightLowerCorner.X) - int(point.X)))
                if triArea > rectArea:
                    point.City = "None"
                else:
                    point.City = city.Name
                    break
        return points

operation = Operation()
cities = operation.ReadFile("cities.csv", "cities")
points = operation.ReadFile("points.csv", "points")
operation.WriteFile("PointsWithCityName.csv", operation.CheckPoint(cities, points))