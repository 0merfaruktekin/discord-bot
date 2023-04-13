import requests
import discord
import random
from discord.ext import commands
import praw
import wikipediaapi


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
weather_api="...."
reddit = praw.Reddit(client_id ='....',
                     client_secret ="...",
                     username = "..."
                     password = "...",
                     user_agent = "...", )

client = commands.Bot(command_prefix = '.')
@client.event
async def on_ready():
    print('Bot Hazır!')
@client.command()
async def sa(ctx):
    await ctx.channel.send('as')

@client.command()
async def kur(ctx):
    dol = requests.get('https://api.exchangeratesapi.io/latest?base=USD&symbols=TRY')
    dol_=dol.json()
    eu = requests.get('https://api.exchangeratesapi.io/latest?base=EUR&symbols=TRY')
    eu_ = eu.json()
    asd ='Dolar =',dol_['rates'],'Euro =',eu_['rates']
    await ctx.send(asd)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')

@client.command()
async def usd(ctx):
    usd = requests.get('https://api.exchangeratesapi.io/latest?base=USD&symbols=TRY')
    usd_ = usd.json()
    await ctx.send(usd_['rates'])

@client.command()
async def eur(ctx):
    eur = requests.get('https://api.exchangeratesapi.io/latest?base=EUR&symbols=TRY')
    eur_=eur.json()
    await ctx.send(eur_['rates'])

@client.command()
async def zarat(ctx,zar = 6):
    await ctx.send(random.randint(1,int(zar)))

@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("TurkeyJerky")
    all_subs = []

    top = subreddit.top(limit=200)


    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title

    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)
    await ctx.send(embed = em)
@client.command()
async def ayıplı(ctx):
    subreddit = reddit.subreddit("porngifs")
    all_subs = []

    top = subreddit.hot(limit=200)
    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    url = random_sub.url


    await ctx.send(url)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send('Mesajlar silindi')
@client.command()
async def filmoneri(ctx):
    f = open('data.txt', 'r')
    for i in range(0, random.randint(1, 251)):
        film = f.readline()
    index = int(film.find('https'))
    f.close()
    await ctx.send(film[index:index + 36])
@client.command()
async def corona(ctx):
    c=requests.get('https://api.apify.com/v2/key-value-stores/28ljlt47S5XEd1qIi/records/LATEST?disableRedirect=true')
    corona=c.json()
    xcz='Toplam Vaka:',corona['infected'],'\nToplam Ölüm:',corona['deceased']
    await ctx.send('Türkiye Koronavirus İstatistikleri\nToplam Vaka:'+str(corona['infected'])+'\nToplam Ölüm:'+str(corona['deceased'])+'\nGünlük Vaka:'+str(corona['dailyInfected'])+'\nGünlük Can Kaybı:'+str(corona['dailyDeceased']))

@client.command()
async def wiki(ctx,*konuu):
    yas = '✔️'
    nay = '❌'
    konu=""
    for i in range(len(konuu)):
        if i==0:
            konu=konu+konuu[i]
        else:
            konu=konu+"_"+konuu[i]
    print(konu)
    wiki_tr = wikipediaapi.Wikipedia('tr')
    wiki_eng = wikipediaapi.Wikipedia("en")
    if wiki_tr.page(konu).exists() is True:
        sayfa=wiki_tr.page(konu)
    elif wiki_eng.page(konu).exists() is True:
        #message = await ctx.send("Aradığınız sayfa türkçe olarak bulunamadı ingilizce aramak ister misiniz?")
        #await message.add_reaction(yas)
        #await message.add_reaction(nay)
        sayfa=wiki_eng.page(konu)
    else:
        await ctx.send('aradığınız sayfa bulunmamaktadır')
    await ctx.send(sayfa.summary)
@client.command()
async def komutlar(ctx):
    embed=discord.Embed(title="Komutlar")
    embed.add_field(name="kur", value="mevcut kur değerlerini gösterir")
    embed.add_field(name="zarat",value="belirlediğiniz değerde rastgele bir sayı verir")
    embed.add_field(name="clear",value="belirlediğiniz sayıda mesajı sohbetten temizler")
    embed.add_field(name="filmoneri", value="imdb üzerinde en yüksek puan almış filmlerden rastgele bir film önerir")
    embed.add_field(name="corona", value="günlük koronavirüs istatistiklerini gösterir")
    embed.add_field(name="meme", value="rastgele bir meme gösterir")
    embed.add_field(name="wiki", value="girdiğiniz başlığın wikipedia sayfasını gösterir")
    embed.add_field(name="havadurumu", value="hava durumunu gösterir")
    await ctx.send(embed=embed)
@client.command()
async def havadurumu(ctx):
    panel = discord.Embed()
    hava_ist=requests.get("https://api.openweathermap.org/data/2.5/weather?id=745042&APPID=1d1df4adf1362f3fb122f785152c0341")
    hava_ank=requests.get("https://api.openweathermap.org/data/2.5/weather?id=323786&APPID=1d1df4adf1362f3fb122f785152c0341")
    hava_iz=requests.get("https://api.openweathermap.org/data/2.5/weather?id=311044&APPID=1d1df4adf1362f3fb122f785152c0341")
    hava_ant=requests.get("https://api.openweathermap.org/data/2.5/weather?id=323776&APPID=1d1df4adf1362f3fb122f785152c0341")
    hava_ist=hava_ist.json()
    hava_ist_icon=hava_ist["weather"]
    ist_id=hava_ist_icon[0]
    hava_ist=hava_ist["main"]
    if ist_id["id"]>=801:
        ist_icon=":cloud:"
    elif ist_id["id"]==801:
       ist_icon=":white_sun_cloud:"
    elif ist_id["id"]==800:
        ist_icon=":sunny:"
    elif ist_id["id"]>=700:
        ist_icon=":fog:"
    elif ist_id["id"]>=600:
        ist_icon=":cloud_snow:"
    elif ist_id["id"]>=300:
        ist_icon=":cloud_rain:"
    elif ist_id["id"]>=200:
        ist_icon=":thunder_cloud_rain:"
    value=hava_ist["temp"]-273.15
    value=round(value,2)
    value=str(value)
    panel.add_field(name="İstanbul", value=value + "°C" + ist_icon, inline="False")
    hava_ank = hava_ank.json()
    hava_ank_icon = hava_ank["weather"]
    ank_id = hava_ank_icon[0]
    hava_ank = hava_ank["main"]
    if ank_id["id"] >= 801:
        ank_icon = ":cloud:"
    elif ank_id["id"] == 801:
        ank_icon = ":white_sun_cloud:"
    elif ank_id["id"] == 800:
        ank_icon = ":sunny:"
    elif ank_id["id"] >= 700:
        ank_icon = ":fog:"
    elif ank_id["id"] >= 600:
        ank_icon = ":cloud_snow:"
    elif ank_id["id"] >= 300:
        ank_icon = ":cloud_rain:"
    elif ank_id["id"] >= 200:
        ank_icon = ":thunder_cloud_rain:"
    value_ank = hava_ank["temp"] - 273.15
    value_ank = round(value_ank, 2)
    value_ank = str(value_ank)
    panel.add_field(name="Ankara", value=value_ank + "°C" + ank_icon, inline="False")
    hava_iz = hava_iz.json()
    hava_iz_icon = hava_iz["weather"]
    iz_id = hava_iz_icon[0]
    hava_iz = hava_iz["main"]
    if iz_id["id"] >= 801:
        iz_icon = ":cloud:"
    elif iz_id["id"] == 801:
        iz_icon = ":white_sun_cloud:"
    elif iz_id["id"] == 800:
        iz_icon = ":sunny:"
    elif iz_id["id"] >= 700:
        iz_icon = ":fog:"
    elif iz_id["id"] >= 600:
        iz_icon = ":cloud_snow:"
    elif iz_id["id"] >= 300:
        iz_icon = ":cloud_rain:"
    elif iz_id["id"] >= 200:
        iz_icon = ":thunder_cloud_rain:"
    value_iz = hava_iz["temp"] - 273.15
    value_iz = round(value_iz, 2)
    value_iz = str(value_iz)
    panel.add_field(name="İzmir", value=value_iz+"°C"+iz_icon,inline="False")
    hava_ant = hava_ant.json()
    hava_ant_icon = hava_ant["weather"]
    ant_id = hava_ant_icon[0]
    hava_ant = hava_ant["main"]
    if ant_id["id"] >= 801:
        ant_icon = ":cloud:"
    elif ant_id["id"] == 801:
        ant_icon = ":white_sun_cloud:"
    elif ant_id["id"] == 800:
        ant_icon = ":sunny:"
    elif ant_id["id"] >= 700:
        ant_icon = ":fog:"
    elif ant_id["id"] >= 600:
        ant_icon = ":cloud_snow:"
    elif ant_id["id"] >= 300:
        ant_icon = ":cloud_rain:"
    elif ant_id["id"] >= 200:
        ant_icon = ":thunder_cloud_rain:"
    value_ant = hava_ant["temp"] - 273.15
    value_ant = round(value_ant, 2)
    value_ant = str(value_ant)
    panel.add_field(name="Antalya", value=value_ant+"°C"+ant_icon,inline="False")
    await ctx.send(embed=panel)
"""@client.command(pass_context=True)
async def play(ctx,url):
    channel = ctx.author.voice.channel
    await channel.connect()
    with youtube_dl.YoutubeDL({}) as ydl:
        video=ydl.download([url])
    await channel.play(video)"""
client.run('....')
