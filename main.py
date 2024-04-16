import discord
import os

from discord import message

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
name = None
did_ask_for_name = False
greeted_users = set()

@bot.event
async def on_message(message):
    global name, did_ask_for_name, greeted_users

    if message.author == bot.user:
        return

    print('[New message]', message.content)

    # Überprüfe, ob der Benutzer bereits begrüßt wurde, und ignoriere seine Nachrichten
    if message.author in greeted_users:
        return

    # Wenn der Bot den Namen des Benutzers bereits kennt, füge ihn zu greeted_users hinzu
    if name and message.author == name:
        greeted_users.add(name)

    if did_ask_for_name:
        name = message.content
        did_ask_for_name = False
        await message.channel.send('Willkommen auf Pano´s Server ' + str(name) + ', fühl dich wie Zuhause und habe Spaß.')
        greeted_users.add(name)
        return

    if not name:
        did_ask_for_name = True
        await message.channel.send('Hallo, ich kenne deinen Namen noch nicht. Wie heißt du?')



bot.run(os.environ['Discord_Token'])
