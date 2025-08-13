import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    print("tkinter")
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    print("begin")
    (t, wn, map_bg_img) = irma_setup()
    print("begin")

    # your code to animate Irma here
    data = open ("data/irma.csv", "r")
    dataset = data. readlines ()
    category = 0
    for line in dataset [1:]:
        line = line.split (",")
        print (line [2:5])
        lat = float(line[2])
        lon = float (line [3])
        wind = float (line [4])
        t.speed(0)
        t. goto (lon, lat)
        t. color ("black")
    
        if wind < 74:
            t. color ("white")
            t. pensize (1)
            category = 1
        if 74<= wind <=95:
            t. color ("blue")
            t. pensize (2)
            t.write ("1")
        elif 96<= wind <= 110:
            t. color ("green")
            t. pensize (4)
            t.write("2")
        elif 111 <= wind <= 129:
            t. color ("yellow")
            t. pensize (8)
            t.write("3")
        elif 130<= wind <=  155:
            t. color ("orange")
            t. pensize (10)
            t.write("4")
        elif wind > 155:
            t. color ("red")
            t.pensize (15)
            t.write("5")
        
#turtle.done()

if __name__ == "__main__":
    irma()
