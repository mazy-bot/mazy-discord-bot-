import discord
import os

# ตั้งค่าสิทธิ์พื้นฐาน
intents = discord.Intents.default()
intents.message_content = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'น้อง {client.user} ออนไลน์แล้วนะ!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('สวัสดี'):
        await message.channel.send('สวัสดีเจ้ามนุษย์! เรา Mazy เองนะ 🐾')

# ดึง Token จาก Environment Variable (เพื่อความปลอดภัย)
token = os.getenv('DISCORD_TOKEN')
client.run(token)
