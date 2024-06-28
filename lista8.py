#3)

def is_parenteses_valid(s):
    count = 0
    for char in s:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return(False)
    return(count == 0)
"""
print(is_parenteses_valid("(((((((()))"))
print(is_parenteses_valid("()()()(()())"))
print(is_parenteses_valid("[[[]]]"))
"""

#4 e 5)
import turtle

class point2D:
    def __init__(self, x, y):
        self.coord = (x,y)
    
    def __str__(self):
        return(str(self.coord))

class Polygon:
    def __init__(self, points, color):
        self.points = points
        self.color = color

#Achei mais eficiente usar um dicionário ao invés de uma lista para salvar os poligonos
#Também evita mais de um polígono com o mesmo nome
class Polygons:
    def __init__(self, polygons = {}):
        self.polygons = polygons
    
    def add_polygon(self, polygon, name):
        self.polygons[name : polygon]
    
    def remove_polygon(self, name):
        self.polygons.pop(name)

    def save_to_file(self, filename):
        open(filename, "w").write(self.str_saved())
        
    def str_saved(self):
        str_save = ""
        for name in self.polygons:
            str_save += f"{name}|{self.polygons[name].color}|" 
            for point in self.polygons[name].points:
                str_save += f"{str(point)};"
            str_save = str_save[0:len(str_save)-1] + "\n"
        str_save = str_save[0:len(str_save)-1]
        return(str_save)
    
    def load_from_file(self, filename):
        str_read = open(filename, "r").read()
        lines = str_read.split("\n")
        polygons = Polygons()
        for line in lines:
            line_split = line.split("|")
            points = line_split[2].split(";")
            for i in range(len(points)):
                point = eval(points[i])
                points[i] = point2D(point[0], point[1])
            polygon = Polygon(points, line_split[1])
            polygons.polygons[line_split[0]] = polygon
        return(polygons)
    
    def plot(self):
        screen = turtle.Screen()
        t = turtle.Turtle()
        t.speed(1)
        for name, polygon in self.polygons.items():
            t.color(polygon.color)
            t.penup()
            first_point = polygon.points[0].coord
            t.goto(first_point[0]*100, first_point[1]*100) 
            t.pendown()
            for point in polygon.points[1:]:
                t.goto(point.coord[0]*100, point.coord[1]*100)
            t.goto(first_point[0]*100, first_point[1]*100)
        screen.mainloop()
            
p1 = point2D(0,1)
p2 = point2D(0,0)
p3 = point2D(1,0)
p4 = point2D(1,1)
triangle = Polygon([p1,p2,p3], "blue")
square = Polygon([p1,p2,p3,p4], "red")
polygons = Polygons({"triangle" : triangle, "square" : square})
polygons.save_to_file("polygons")

print("Printando do modo que eu decidi salvar no arquivo \n nome|cor|pontos\n")
loaded_polygons = polygons.load_from_file("polygons")
print(loaded_polygons.str_saved())

loaded_polygons.plot()