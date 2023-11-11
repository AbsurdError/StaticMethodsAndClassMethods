# def my_decorator(func):
#     def wapper():
#         print('before decorator')
#         func()
#         print('actor decorator')
#     return wapper
#
# @my_decorator
# def hello():
#     print('hello')
#
# hello()

# class Vector:
#
#     '''hghjklkjhgf'''
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if Vector.validate(x): #and Vector.validate(y):
#             self.x = x
#             self.y = y
#         if self.validate(x):
#             self.x = x
#         if self.validate(y):
#             self.y = y
#         print(Vector.norm2(self.x, self.y))
#         print(self.norm2(self.x, self.y))
#
#     def get_cords(self):
#         return self.x, self.y
#
#
#     @staticmethod
#
#     def norm2(x, y):
#         return x ** 2 + y ** 3
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD < arg < cls.MAX_COORD
#
# v = Vector(1, 5)
# # print(v.norm2(1, 8))
# # print(v.__dict__)
# # print(Vector.__dict__)

# from math import pi
# class Cylinder:
#     @staticmethod
#     def make_area(d, h):
#         circle = pi * d ** 2 / 4
#         side = pi * d * h
#         return circle * 2 * side
#
#
#     def __init__(self, diam, high):
#         self.diam = diam
#         self.high = high
#         self.area = self.make_area(self.diam, self.high)
#
#     def __str__(self):
#         return f'diam = {self.diam}, high = {self.high}, area = {self.area}'
#
# c = Cylinder(2, 4)
# print(c)
# print(c.__dict__)

# class MyClass:
#     TOTAL_COUNTS = 0
#
#     def __init__(self):
#         MyClass.TOTAL_COUNTS = MyClass.TOTAL_COUNTS + 1
#
#     @classmethod
#     def total_counts(cls):
#         print('total counts', cls.TOTAL_COUNTS)
#
# class ChildClass(MyClass):
#     TOTAL_COUNTS = 0
#
#     def __init__(self):
#         ChildClass.TOTAL_COUNTS += 1
#
# m = MyClass()
# m1 = MyClass()
# MyClass.total_counts()
# cc = ChildClass()
# cc.total_counts()

# class Point:
#     MIN_COORD = 0
#     MAX_COORD = 100
#     z = 12484
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if self.MIN_COORD < x < self.MAX_COORD:
#             self.__x = x
#         if self.MIN_COORD < y < self.MAX_COORD:
#             self.y = y
#
#     @classmethod
#     def set_bound(cls, left):
#         cls.MIN_COORD = left
#
#     # def __getattribute__(self, item):
#     #     if item == '_Point__x':
#     #         raise ValueError('hjklnbhjjj')
#     #     # print('get attribute')
#     #     return object.__getattribute__(self, item)
#
#     def __str__(self):
#         return f'x = {self.__x}, y = {self.y}'
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise ValueError('NotTer')
#         else:
#             self.__dict__[key] = value
#         # print('setattr')
#         # object.__setattr__(self, key, value)
#     def __getattr__(self, item):
#         print('get attr' + item)
#
#     def __delattr__(self, item):
#         object.__delattr__(self, item)
#
#     def __del__(self):
#         print('no object')
#
#
#
# p = Point(1, 6)
# # p.MAX_COORD = 7000
# # p.set_bound(-100)
# # pl = Point(2, 7)
# # print(p.MAX_COORD)
# # p.set_coord(-2, 500)
# # # print(p)
# # print(Point.__dict__)
# # print(p.__Point__x)
# p.j = 15
# Point.__setattr__(p, 'k', 154)
# print(p.__dict__)
# del p.j
# print(p.__dict__)
# # print(pl.__dict__)

# class Snow:
#     def __init__(self, num):
#         self.num = num
#
#     def make_snow(self, el):
#         for i in range(self.num // el):
#             print('*' * el)
#         print('*' * (self.num % el))
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         res = other if isinstance(other, int) else other.num
#         return Snow(self.num + res)
#
#     def __sub__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         res = other if isinstance(other, int) else other.num
#         return Snow(self.num - res)
#
#     def __mul__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         res = other if isinstance(other, int) else other.num
#         return Snow(self.num * res)
#
#     def __truediv__(self, other):
#         if not isinstance(other, int):
#             raise TypeError
#         return Snow(self.num // other)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError('kijiuki')
#         res = other if isinstance(other, int) else other.num
#         return Snow(self.num // res)
#
#
# s = Snow(1000)
# s1 = Snow(10)
# # s.make_snow(20)
# s2 = s // s1
# s2.make_snow(100)

# class SnowFlake:
#     def __init__(self, side_square):
#         if side_square % 2 == 0:
#             raise ValueError("Число должно быть нечётным!")
#         self.side_square = side_square
#         self.matrix = [['-' for _ in range(side_square)] for _ in range(side_square)]
#         self.init_snowflake()
#
#     def init_snowflake(self):
#         center = self.side_square // 2
#         self.matrix[center][center] = '*'
#
#     def thaw(self, steps):
#         for _ in range(steps):
#             self.remove_edges()
#
#     def remove_edges(self):
#         for i in range(self.side_square):
#             self.matrix[i][0] = '-'
#             self.matrix[i][-1] = '-'
#             self.matrix[0][i] = '-'
#             self.matrix[-1][i] = '-'
#
#     def freeze(self, n):
#         side_square_new = self.side_square + 2 * n
#         new_matrix = [['-' for _ in range(side_square_new)] for _ in range(side_square_new)]
#
#         for i in range(n, n + self.side_square):
#             for j in range(n, n + self.side_square):
#                 new_matrix[i][j] = self.matrix[i - n][j - n]
#
#         self.side_square = side_square_new
#         self.matrix = new_matrix
#
#     def thicken(self):
#         new_matrix = [['-' for _ in range(self.side_square + 2)] for _ in range(self.side_square + 2)]
#
#         for i in range(self.side_square):
#             for j in range(self.side_square):
#                 new_matrix[i + 1][j + 1] = self.matrix[i][j]
#
#         self.side_square += 2
#         self.matrix = new_matrix
#
#     def show(self):
#         for row in self.matrix:
#             print(' '.join(row))
#
#
#
# snowflake = SnowFlake(9)
# snowflake.show()
#
# snowflake.thaw(1)
# snowflake.show()
#
# snowflake.freeze(1)
# snowflake.show()
#
# snowflake.thicken()
# snowflake.show()

# class Robot:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     def __init__(self, coord_x, coord_y):
#         self.coord_x = self.MIN_COORD <= coord_x <= self.MAX_COORD
#         self.coord_x = coord_x
#         self.coord_y = self.MIN_COORD <= coord_y <= self.MAX_COORD
#         self.coord_y = coord_y
#         self.coordinates = [(self.coord_x, self.coord_y)]
#
#     def move(self, commands):
#         for commands in commands:
#             if commands == 'N' and self.coord_y < self.MAX_COORD:
#                 self.coord_y += 1
#             elif commands == 'S' and self.coord_y > self.MIN_COORD:
#                 self.coord_y -= 1
#
#             elif commands == 'E' and self.coord_x < self.MAX_COORD:
#                 self.coord_x += 1
#
#             elif commands == 'W' and self.coord_x > self.MIN_COORD:
#                 self.coord_x -= 1
#
#         self.coordinates.append((self.coord_x, self.coord_y))
#         print(f'Координата х = {self.coord_x}, у = {self.coord_y}')
#     def path(self):
#         print(f'Координаты перемещения робота (x;y): {self.coordinates}')
#
# robot = Robot(50, 50)
#
# robot.move('N') # вверх
# robot.move('N')
# robot.move('E') # вправо
# robot.move('S') # вниз
# robot.move('W') # влево
# robot.move('W')
# robot.path()

# class Talking:
#     def __init__(self, name):
#         self.name = name
#         self.count_yes = 0
#         self.count_no = 0
#         self.current_response = "moore-moore"
#
#     def to_answer(self):
#         response = self.current_response
#         if self.current_response == "moore-moore":
#             self.current_response = "meow-meow"
#             self.count_yes += 1
#         else:
#             self.current_response = "moore-moore"
#             self.count_no += 1
#         return response
#
#     def number_yes(self):
#         return self.count_yes
#
#     def number_no(self):
#         return self.count_no
#
# tk = Talking('Pussy')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
#
#
# tk = Talking('Pussy')
# tk1 = Talking('Barsik')
# print(tk.to_answer())
# print(tk1.to_answer())
# print(tk1.to_answer())
# print(tk1.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
# print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no"{tk1.number_no()} times')
