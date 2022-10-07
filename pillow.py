from PIL import Image

mac = Image.open("mac.png")
print(type(mac))
# mac.show()
print(mac.size)
print(mac.filename)
print(mac.format_description)
cropped = mac.crop((800, 800, 1200, 1250))  # x y, w, h left right width height
mac.paste(cropped, (1000, 0))  # to paste image into image
mac = mac.resize((8000, 12000))  # to resize
# to show image
mac = mac.rotate(180)
# Color transperency RGBA
mac.putalpha(128)  # setting transperency
mac.save("working_with_images_image.png")
mac.show()
