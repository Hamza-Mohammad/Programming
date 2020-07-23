%%writefile gometry_module.py

def rectangle_area(length,breadth):
    area = length * breadth
    return area

def parallelogram_area(base,perpendicular):
    area = base * perpendicular
    return area


def curved_surface_of_cone_afrea(perpendicular, Radius):
    a = (perpendicular ** 2) + (Radius ** 2)
    import math as m 
    length = m.sqrt(a)
    pi = m.pi
    area = length * pi * Radius
    return area

def trapazium_area(parallel1,parallel2,height):
    x = parallel1 + parallel2
    d = x/2
    area = d * height
    return area

def circle_area(radius):
    import math as m
    area = (m.pi) * (radius ** 2)
    return area


def  curved_side_of_cylinder_area(radius,height):
    import math as m
    a = m.pi * 2
    area = (a * radius )* height
    return area

def shpere_area(Radius):
    import math as m
    a = m.pi * 4
    b = Radius ** 2
    area = a * b
    return area

def triangle_area(base,perpendicular):
    a = base / 2
    area = perpendicular * a
    return area

def circle_cicumference(radius):
    import math as m
    a = m.pi * 2
    area = a * radius
    return area

def cuboid_volume(length,breadth,height):
    area = length * breadth * height
    return area

def cylinder_volume(radius,height):
    import math as m
    a = m.pi
    b = radius ** 2
    area = a * b * height
    return area

def cone_volume(radius,perpendicular):
    import math as m
    a = m.pi
    b = radius ** 2
    c = a * b * perpendicular
    area = c / 3
    return area

def sphere_volume(radius):
    import math as m
    a = m.pi
    b = 4 / 3
    c = radius ** 3
    area = a * b * c
    return area

def pyramid_volume(height, side, base,perpendicular_of_base):
    if side == 3:
        a = base / 2
        b = perpendicular_of_base * a
        c = b / 3
        area = c * height
    elif side == 4:
        a = base * 4
        b = a ** 2
        c = b / 3
        area = c * height
    else:
        print('you can only enter \'3\' or \'4\'')
    return area
