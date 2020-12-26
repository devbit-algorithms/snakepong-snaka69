from canvas import Canvas

def test_Canvas_print():
    playfield = Canvas(2, 2)
    playfield.draw(0, 0, "a")
    playfield.draw(1,1,"b")
    playfield.print()
    assert playfield.getCanvas() == "a \n b\n"

def test_Canvas_clear():
    playfield = Canvas(2, 2)
    playfield.draw(0, 0, "a")
    playfield.draw(1,1,"b")
    playfield.clear()
    assert playfield.getCanvas() == "  \n  \n"

    