import discord
import os

client = discord.Client()

# sensitive info
token = os.environ.get('DISCORD_TOKEN')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------')


# 333841395959857184 is T4T
# 561667887698411541 is BTL

@client.event
async def on_message(message):
    id = client.get_guild(333841395959857184)
    cameron_id = 171359348503609345
    channels = ["bot-testing"]
    valid_users = ["SpockMemes#0361", "Finrod Felagund#2710", "Bunf#4858", "Schopix#6692"]
    # TODO: Add admin commands
    admin_users = ["SpockMemes#0361"]  # for special commands

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send(f"What's up, {message.author.mention}?")
        elif message.content == "!users":
            await message.channel.send(f"# of members: {id.member_count}")
        elif message.content == "!cameron":
            await message.channel.send(f"{(client.get_user(cameron_id)).mention} is lame")
        elif message.content == "!insult":
            await message.channel.send(
                f"{message.author.mention}, your mother was a hamster and your father smelt of elderberries")
        elif message.content == "!timothy":
            await message.channel.send("Timothy is very helpful")
        elif message.content == "!mokelembembe":
            await message.channel.send("The Mokele-mbembe is a fictional creature that first appeared in Congo River Basin mythology. It does not exist.")
        elif message.content == "!helpscb":
            embed = discord.Embed(title="help for superCoolBot1.9", description="henlo idiot, here are the commands")
            embed.add_field(name="!hello", value="Greets the user")
            embed.add_field(name="!users", value="Prints number of users")
            embed.add_field(name="!cameron", value="States facts about Cameron")
            embed.add_field(name="!insult", value="Mercilessly insults you")
            await message.channel.send(content=None, embed=embed)

#hi
client.run(token)
