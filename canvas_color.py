class color:
    """
    Represents an RGB triple of floats, usually in the range 0 - 1.
    Can be multiplied on the left by a scalar or multiplied by another colour (which
    is done component wise).
    """

    def __init__(self, r=0, g=0, b=0):
        """
        initialized with a value of '0' for each colour component
        """
        # if values are inputted as a factor of 1, they should be multiplied to be factors of 255
        self.red = r
        self.green = g
        self. blue = b

    # def __str__(self):
    #     print('the colour combos are')
    #     print('%f: red, %f: green, %f: blue' %(self.red, self.green, self.blue))

    def __add__(self, other):
        """
        returns a new color, must add to itself if need to increase the self color values
        """
        return color(self.red + other.red, self.green + other.green, self.blue + other.blue)

    def __sub__(self, other):
        """
        returns a new color, must subtract to itself if need to increase the self color values
        """
        return color(self.red - other.red, self.green - other.green, self.blue - other.blue)

    def __str__(self):
        return '(r={}  g={}  b={})'.format(self.red, self.green, self.blue)

    def __mul__(self, other):
        """
        returns a new color, must subtract to itself if need to increase the self color values
        """
        return color(self.red * other, self.green * other, self.blue * other)

    def multiply(self, other):
        """
        returns a new color, must subtract to itself if need to increase the self color values
        """
        return color(self.red * other.red, self.green * other.green, self.blue * other.blue)


class canvas:
    def __init__(self, height, width,r=0,g=0,b=0):
        if width <= 0:
            raise ValueError('width cannot be less than 0')
        if height <= 0:
            raise ValueError('height cannot be less than 0')
        self.h = height
        self.w = width

        # append the color white to all the
        self.canvas = []
        for i in range(width):
            inner = []
            for j in range(height):
                inner.append(color(r, g, b))
            self.canvas.append(inner)

    def write_canvas(self, x, y, color=color()):
        if x < 0:
            raise ValueError('width cannot be less than 0')
        if y < 0:
            raise ValueError('height cannot be less than 0')
        self.canvas[x][y].red = color.red
        self.canvas[x][y].green = color.green
        self.canvas[x][y].blue = color.blue

    def to_ppm(self, filename='file'):
        header = "P3\n{} {}\n255".format(self.w, self.h)

        # Walk through each row and convert the colors to a line of text of
        # 3-tuples with spaces between values and a newline at the end of each
        # row.  Limit line length, not including newline, to 70 characters
        pixel_text = []
        for y in range(self.h):
            y_text = []
            for x in range(self.w):
                # if self.canvas[y][x].red < 0:
                #     self.canvas[y][x].red = 0
                # if self.canvas[y][x].red > 255:
                #     self.canvas[y][x].red = 255
                # if self.canvas[y][x].green < 0:
                #     self.canvas[y][x].green = 0
                # if self.canvas[y][x].green > 255:
                #     self.canvas[y][x].green = 255
                # if self.canvas[y][x].blue < 0:
                #     self.canvas[y][x].blue = 0
                # if self.canvas[y][x].blue > 255:
                #     self.canvas[y][x].blue = 255

                y_text.append("{} {} {}".format(self.canvas[x][y].red, self.canvas[x][y].green, self.canvas[x][y].blue))
            y_text = " ".join(y_text)

            # If the line is 70 or fewer characters in length, then just append
            # the line to the lines we have created.  Otherwise...break the
            # lines...
            if len(y_text) <= 420:
                pixel_text.append(y_text)
            else:
                # Note we assume well-formed lines.  A line of all spaces
                # would break this.

                # While there are more than 70 characters left in the line,
                # starting at character 71, walk backwards until we get to a
                # space.  Slice the string so that the front part (from
                # beginning to the last character before the space) is added
                # to the list of lines we already have and the back part (from
                # the first character after the space until the end is re-
                # assigned to the line we are working on.
                while len(y_text) > 420:
                    index = 420
                    while y_text[index] != ' ':
                        index -= 1
                    pixel_text.append(y_text[:index])
                    y_text = y_text[index + 1:]

                # Append anything left over to the list of lines we are
                # accumulating.
                pixel_text.append(y_text)

        # Combine the header plus each of the accumulated lines joined by a
        # newline to be the resulting PPM data.

        f = open("{}.ppm".format(filename), 'w+')
        f.write("{}\n{}\n".format(header, "\n".join(pixel_text)))
        f.close()
        return "{}\n{}\n".format(header, "\n".join(pixel_text))


# if __name__ == '__main__':
#     one = color(1,2,3)
#     two = color(3,1,4)
#     three = one+two
#     four = one-two
#     five = one*two
#     six = one.multiply(2)
#     print(three.red, three.green, three.blue)
#     print(four.red, four.green, four.blue)
#     print(five.red, five.green, five.blue)
#     print(six.red, six.green, six.blue)

    # makes an image with white background and a blue box towards the top left
    # x = canvas(800, 800, 0,0, 255)
    # print(x.canvas[7][7].red, x.canvas[7][7].green, x.canvas[7][7].blue)
    # for j in range(600, 800):
    #     for y in range(1, 300):
    #         x.write_canvas(j, y, color(244, 0, 200))
    # print(x.canvas[7][7].red, x.canvas[7][7].green, x.canvas[7][7].blue)
    # x.to_ppm()
