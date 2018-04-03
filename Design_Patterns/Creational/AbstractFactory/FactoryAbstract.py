# === Interfaces ===


class IShape2d:
    def draw(self): pass


class IShape3d:
    def build(self): pass


# === Concrete classes ===


class Circle(IShape2d):
    def draw(self):
        print('Circle drawn')


class Square(IShape2d):
    def draw(self):
        print('Square drawn')


class Sphere(IShape3d):
    def build(self):
        print('Sphere built')


class Cube(IShape3d):
    def build(self):
        print('Cube built')


# === Abstract Shape Factory ===


class IShapeFactory:
    @staticmethod
    def get_shape(sides): pass


# === Concrete Shape Factories ===


class Shape2dFactory(IShapeFactory):
    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, 'Bad 2d shape creation: shape not defined for %s sides' % sides


class Shape3dFactory(IShapeFactory):
    @staticmethod
    def get_shape(sides):
        """ Here sides refer to the number of faces """
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, 'Bad 3d shape creation: shape not defined for %s sides' % sides


factory_2d = Shape2dFactory()
object1 = factory_2d.get_shape(1)
print('type of object: %s' % type(object1))
object1.draw()
object2 = factory_2d.get_shape(4)
print('type of object: %s' % type(object2))
object2.draw()

factory_3d = Shape3dFactory()
object3 = factory_3d.get_shape(1)
print('type of object: %s' % type(object3))
object3.build()
object4 = factory_3d.get_shape(6)
print('type of object: %s' % type(object4))
object4.build()
