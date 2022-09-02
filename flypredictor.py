from discord.ext import commands
import discord
import random 

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot in online and ready to use!")

@bot.command()
async def mines(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await ctx.send("invalid round id")
    elif round_length == 36:
        mine1,mine2,mine3,mine4,mine5,mine6,mine7,mine8,mine9,mine10,mine11,mine12,mine13,mine14,mine15,mine16,mine17,mine18,mine19,mine20,mine21,mine22,mine23,mine24,mine25, = ':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',':question:',
        
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = ":green_square: "
        elif a == 2:
            mine2 = ":green_square:"
        elif a == 3:
            mine3 = ":green_square:"
        elif a == 4:
            mine4 = ":green_square:"
        elif a == 5:             
            mine5 = ":green_square:"
        elif a == 6:
            mine6 = ":green_square:"
        elif a == 7:
            mine7 = ":green_square:"
        elif a == 8:
            mine8 = "green_square:"
        elif a == 9:
            mine9 = ":green_square:"
        elif a == 10:
            mine10 = ":green_square:"
        elif a == 11:
            mine11 = ":green_square:"
        elif a == 12:
            mine12 = ":green_square:"
        elif a == 13:
            mine13 = ":green_square:"
        if c == 14:
            mine14 = ":green_square:"
        elif c == 15:
            mine15 = ":green_square:"
        elif c == 16:
            mine16 = ":green_square:"
        elif c == 17:
            mine17 = ":green_square:"
        if d == 18:
            mine18 = ":green_square:"
        elif d == 19:
            mine19 = ":green_square:"
        elif d == 20:
            mine20 = ":green_square:"
        elif d == 21:
            mine21 = ":green_square:"
        elif d == 22:
            mine22 = ":green_square:"
        elif d == 23:
            mine23 = ":green_square:"
        elif d == 24:
            mine24 = ":green_square:"
        elif d == 25:
            mine25 = ":green_square:"

        row1 = mine1 + mine2 + mine4 + mine5 + mine6
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        
        info = str(random.randint(75, 100))
        pfp = 'https://cdn.discordapp.com/attachments/1014638738023907431/1015217971725094912/IMG_0079.jpg'
        em = discord.Embed(color = 0x66FFCC)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Coco thinks its...")
        em.add_field(name="Mines predictor", value=row1 + "\n" + row2+ "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + "**Accuracy**" + "\n" + info + "%")
        await ctx.send(embed=em)

bot.run('MTAwMDE4OTMxNTU3NTQ1NTc3NA.GtM9Kq.IU4msiM4c7sOCOkpLWI43SRBWkX7upyyJycGgM')