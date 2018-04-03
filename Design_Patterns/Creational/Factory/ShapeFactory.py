class IShape:
    def draw(self): pass


class Circle(IShape):
    def draw(self):
        print('Circle drawn')


class Square(IShape):
    def draw(self):
        print('Square drawn')


class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == 'circle':
            return Circle()
        if shape_type == 'square':
            return Square()
        assert 0, 'Could not recognize shape ' + shape_type


f = ShapeFactory()
f.get_shape('square').draw()
f.get_shape('circle').draw()
f.get_shape('triangle').draw()
