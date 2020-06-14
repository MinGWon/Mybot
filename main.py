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
    await client.change_presence(game=discord.Game(name="대규모완료", type=1))

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    if message.content.startswith('/명령어'):
        embed=discord.Embed(title="명령어 목록", description="명령어 목록을 확인하실 수 있습니다.")
        embed.add_field(name="짤 목록 보기", value="/짤", inline=False)
        embed.add_field(name="문의하기", value="contact@myplaynetwork.ga", inline=False)
        embed.set_footer(text="Copyright 2020. Myplay All Rights Reserved.")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/짤'):
        embed=discord.Embed(title="짤 목록", description="짤 목록을 확인하실 수 있습니다.")
        embed.add_field(name="토이스토리 감자", value="/감자", inline=False)
        embed.add_field(name="우릭", value="/우릭", inline=False)
        embed.add_field(name="모마 이겨따", value="/이겨따", inline=False)
        embed.add_field(name="문의하기", value="contact@myplaynetwork.ga", inline=False)
        embed.set_footer(text="Copyright 2020. Myplay All Rights Reserved.")
        await client.send_message(message.channel, embed=embed)      

    if message.content.startswith('딱대'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302321086201897/721303461110480906/cd152ce4fd7f7708.jpg')

    if message.content.startswith('잘가'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302321086201897/721303421701062758/3b5dc9a978fd8d40.jpg')

    if message.content.startswith('턱길이주작'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302321086201897/721303702937534514/jujak.jpg')

    if message.content.startswith('후레쉬맨'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302321086201897/721302698300932157/hureshiman.PNG')

    if message.content.startswith('법규산도'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302321086201897/721302513697030195/bupyouman.png')

    if message.content.startswith('말이안나오는얼굴'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302717485678652/721302805251489792/dududunga.png')

    if message.content.startswith('관짝한결근데이제스노우를곁들인'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302181164351500/721303375525838928/gwanjjakbutincludesnow.jpg')    
        
    if message.content.startswith('잉'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302190794211348/721302441051553792/ing.png')

    if message.content.startswith('납작이'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302181164351500/721303646608031744/sda.jpg')
        
    if message.content.startswith('네모'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721301986472886346/721302645771599923/nemo.png')

    if message.content.startswith('홀리쥇더웅성이'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721303007542771773/721303052090605618/holyhouse.png')

    if message.content.startswith('힛'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302321086201897/721305670581747772/20200604_223546.jpg')

    if message.content.startswith('원따봉'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302190794211348/721305837699596369/image0-2.jpg')

    if message.content.startswith('당황'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302190794211348/721306040695652392/20200426_093421.jpg')
        
    if message.content.startswith('웅성'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302717485678652/721553252247666778/20200611_182017.gif')
    ---                         
    if message.content.startswith('헤헿'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302181164351500/721559375747088405/20200614_113700.png')

    if message.content.startswith('엄'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721303007542771773/721559916053266432/0d84877b6dc9b363.png')
        
    if message.content.startswith('콱마씨'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302321086201897/721560070533546034/20200614_101431.png')
                       
    if message.content.startswith('어'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/721302190794211348/721560330844635197/20200614_101846.png')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
