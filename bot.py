import tweepy
from dotenv import load_dotenv
import os
import time

print("¡Bot iniciado en Render! 🔥")

load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Autenticación OAuth 1.0a
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)
api = tweepy.API(auth)

# Tweet de prueba (solo una vez al iniciar)
try:
    tweet_text = "¡Bot activo en Render! 🔥 Prueba desde @MrElFuckingKing: https://mejoreslatinas.com #nsfw #LatinasXXX"
    api.update_status(status=tweet_text)
    print("Tweet de prueba publicado con éxito!")
except tweepy.TweepyException as e:
    print("Error al publicar tweet de prueba:", e)

# Loop infinito para mantener vivo el proceso (Render necesita que corra siempre)
print("Entrando en loop infinito para mantener el servicio activo...")
while True:
    print("Bot vivo... esperando siguiente acción (cada 60 segundos)")
    time.sleep(60)  # Espera 60 segundos y repite
