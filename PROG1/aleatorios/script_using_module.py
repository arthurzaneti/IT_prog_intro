from Polygon import point2D, Polygon, Polygons, load_from_file

p1 = point2D(0, 0)
p2 = point2D(-1, 1)
p3 = point2D(1, 1)
p4 = point2D(0, 3)
p5 = point2D(1, 2)
p6 = point2D(-1, 2)

hexagon = Polygon([p1,p2,p6,p4,p5,p3], "red")
triangle = Polygon([p1, p5, p6], color = "black")

polys = Polygons({"my_ugly_hexagon" : hexagon,
                  "my_weird_triangle" : triangle})

polys.save_to_file("polygons2")
polys_read = load_from_file("polygons2")

polys.plot()
