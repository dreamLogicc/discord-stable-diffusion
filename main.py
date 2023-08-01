import discord
from discord.ext import commands
import keras_cv
import io
from PIL import Image


def run():

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
    
    @bot.command()
    async def generate(ctx, prompt: str):
        image = Image.fromarray(model.text_to_image(prompt, batch_size=1)[0])
        print(image)
        bytes = io.BytesIO()
        image.save(bytes, format='PNG')
        bytes.seek(0)
        await ctx.send(prompt, file = discord.File(bytes, filename='image.png'))


    with open('./.token', 'r') as file:
        token = file.read()

    bot.run(token=token)

if __name__ == '__main__':
    run()

# Hello! I can generate images. For image generation type /generate and write your prompt