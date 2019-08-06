#Test to see if the functions and text files work correctly

#testing the load_art function from main.py
def draw_test(pallet,pixels):
    goto_origin(myPen)
    for list in pixels:
        for elem in list:
            myPen.color(pallet[int(elem)])
            box(boxSize)
        myPen.penup()
        myPen.right(90)
        myPen.forward(boxSize)
        myPen.right(90)
        myPen.forward(boxSize*len(list))
        myPen.right(180)
        myPen.end_fill()


from main import load_art
def load_art_test(pallet,pixels):
    pallet, pixels = load_art('banana.txt')
    print("Color Pallet:")
    print(pallet)
    print("The pixels are:")
    print(pixels)