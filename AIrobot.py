import tensorflow as tf
import telebot
from telebot import types
import pyrogram

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# Load the pre-trained GAN model
model = tf.keras.models.load_model("gan_model.h5")

@bot.message_handler(commands=['start', 'generate'])
def generate_image("Hello \n I M AI Image Generator Bot \n\n Commands :- /start , /generate"):
    # Generate a random noise vector
    noise = tf.random.normal((1, 100))
    # Use the GAN to generate an image
    generated_image = model.predict(noise)
    # Reshape the image to (28, 28, 1)
    generated_image = generated_image.reshape(28, 28, 1)
    # Convert the image to a PNG file
    img_file = tf.keras.preprocessing.image.array_to_img(generated_image)
    img_file.save("@emAIImageGenerator_Bot Photo.png")
    # Send the generated image to the user
    with open("@emAIImageGenerator_Bot Photo.png", "rb") as image:
        bot.send_photo(message.chat.id, image)

bot.polling()
