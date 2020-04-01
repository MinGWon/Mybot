import asyncio
import discord
import os

client = discord.Client()

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "your_token"

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="짤 목록을 보려먼 /짤", type=1))

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    if message.content == "/명령어":
        embed = discord.Embed(title="명령어 목록", description="Updated On 2020-04-01", color=0x00ff00)
        embed.add_field(name="소제목", value="설명", inline=false)
        embed.add_field(name="소제목", value="설명", inline=false)
        embed.add_field(name="소제목", value="설명", inline=false)
        await client.send_message(embed=embed)
        
    if message.content.startswith('/감자'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/416968282470350858/694842481686216734/toystorygamza.jpg')
        

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
