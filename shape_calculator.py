class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,new_width):
        self.width = new_width
    
    def set_height(self,new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2*self.width)+(2*self.height)

    def get_diagonal(self):
        return ((self.width ** 2)+(self.height ** 2)) ** .5

    def get_picture(self):
        pic = ''
        if self.width >50 or self.height >50:
            return "Too big for picture."
        else:
            for j in range(self.height):
                pic += "*"*self.width+'\n'
        return pic

    def get_amount_inside(self,shape):
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height
        print(vertical_fit, horizontal_fit)
        return vertical_fit*horizontal_fit

    def __str__(self):
        return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'


class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = width

    def set_side(self,width):
        self.width = width
        self.height = width

    def __str__(self):
        return 'Square(side='+str(self.width)+')'

    def set_width(self,width):
        self.width = width
        self.height = width
    
    def set_height(self,width):
        self.width = width
        self.height = width

