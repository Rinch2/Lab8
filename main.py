def one():
    from PIL import Image
    filename = "123.jpg"
    image = Image.open(filename)
    image.show("123.jpg")

    filename = Image.open("123.jpg")

    cropped_image = filename.crop((200, 100, 900, 800))

    cropped_image.save("n123.JPG")
    cropped_image.show("n123.JPG")

def two():
    from PIL import Image

    holidays = {
        "Новый год": "new_yaer.jpg",
        "День рождения": "birthday.jpg",
        "9 мая": "9maya.jpg",
        "23 Февраля": "23F.png",
        "8 Марта": "8March.jpg"
    }

    holiday = input("К какому празднику вам нужна открытка? ")

    if holiday in holidays:
        image_path = holidays[holiday]
        image = Image.open(image_path)
        image.show()
    else:
        print("Праздник не найден")

def three():
    from PIL import Image, ImageDraw, ImageFont

    image = Image.open("birthday.jpeg")
    draw = ImageDraw.Draw(image)
    name = input("Введите имя: ")
    text = f"{name}, поздравляю!"

    font = ImageFont.truetype("ariblk.ttf", 40)

    color = (255, 0, 0)
    position = (image.width / 3 - 40, image.height / 2)

    draw.text(position, text, fill=color, font=font)

    image.save("sdr.png")
    image.show("sdr.png")

# one()
# two()
# three()
