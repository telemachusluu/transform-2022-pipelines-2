import random


def cart(render_template):
    number = random.randrange(0, 3)
    print(number)
    if number == 0:
        return (render_template("error.html"), 501)
    return render_template("index.html")
