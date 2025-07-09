import imageio.v3 as iio

filenames = ['hellokitty.png','hellokitty2.png','hellokitty3.png']  # ← change these to your file names
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('my-gif.gif', images, duration=500, loop=0)
