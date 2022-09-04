from PIL import Image

words = Image.open('word_matrix.png')
mask = Image.open('mask.png')
mask = mask.resize((1015, 559))
# words.show()

# words.show()
mask.putalpha(50)
words.alpha_composite(mask)
words.show()
# words.show()
# words.show()

words.save("Working_with_images_hw.png")
