import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Online")
    game = discord.Game("마산잉 서버에 공식 봇 입니다")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("테스트"):
        await message.channel.send("네?")

client.run("OTA5MDg4MDkyMTU2MTk4OTgz.YY_MQw.oiBKY_9PdEyKH6zcJ1AqF5GTXyk")
