class Circle: pass
class Square: pass
class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "SQUARE":
            return Square()

factory = ShapeFactory()
shape = factory.get_shape("CIRCLE")
print(type(shape))