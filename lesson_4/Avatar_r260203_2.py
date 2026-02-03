from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()
cut_range = 50

coordinates_1 = (0, 0, image.width-cut_range, red.height)
red_cropped_1 = red.crop(coordinates_1)
coordinates_2 = (cut_range, 0, red.width, red.height)
red_cropped_2 = red.crop(coordinates_2)
red_overlay = Image.blend(red_cropped_1, red_cropped_2, 0.8)

coordinates_1 = (cut_range, 0, image.width, blue.height)
blue_cropped_1 = blue.crop(coordinates_1)
coordinates_2 = (0, 0, blue.width-cut_range, blue.height)
blue_cropped_2 = blue.crop(coordinates_2)
blue_overlay = Image.blend(blue_cropped_1, blue_cropped_2, 0.8)

coordinates_1 = (cut_range/2, 0, image.width-cut_range/2, green.height)
green_cropped_1 = green.crop(coordinates_1)

monro_result = Image.merge("RGB", (red_overlay, green_cropped_1, blue_overlay))
monro_result.save("monro_result.jpg")
monro_result.thumbnail((80, 80))
monro_result.save("monro_result_80.jpg")

