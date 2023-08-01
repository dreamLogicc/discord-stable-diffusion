import keras_cv

model = keras_cv.models.StableDiffusion(img_width=32, img_height=32)

print(model.text_to_image('cat', batch_size=1))