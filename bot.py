# bot.py
import os
import random
from math import floor

import discord
from discord.ext import commands
from dotenv import load_dotenv


champs = ["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Aphelios","Ashe","Aurelion Sol","Azir","Bard","Blitzcrank","Brand","Braum","Caitlyn","Camille","Cassiopeia","Cho","Corki","Darius","Diana","Dr.Mundo","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Gwen","Hecarim","Heimerdinger","Illaoi","Irelia","Ivern","Janna","Jarvan","Jax","Jayce","Jhin","Jinx","Kai","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kayn","Kennen","Kha'Zix","Kindred","Kled","Kog","LeBlanc","Lee","Leona","Lillia","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai","Master","Miss","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Neeko","Nidalee","Nocturne","Nunu","Olaf","Orianna","Ornn","Pantheon","Poppy","Pyke","Qiyana","Quinn","Rakan","Rammus","Rek","Rell","Renekton","Rengar","Riven","Rumble","Ryze","Samira","Sejuani","Senna","Seraphine","Sett","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain","Sylas","Syndra","Tahm","Taliyah","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","Twisted","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Vel'Koz","Vi","Viego","Viktor","Vladimir","Volibear","Warwick","Wukong","Xayah","Xerath","Xin","Yasuo","Yone","Yorick","Yuumi","Zac","Zed","Ziggs","Zilean","Zoe","Zyra"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='aram',help="Randomizes champions for two teams. 2 champions per player by default.")
async def roll_aram(ctx,nbr_of_players: int,rolls_per_player=2):
    draw = random.sample(champs,nbr_of_players*rolls_per_player)
    n = floor(nbr_of_players/2)*rolls_per_player
    team1 = draw[:n] 
    team2 = draw[n:]

    await ctx.send(nice_output(team1,team2))

def nice_output(t1,t2):
    l1 = len(max(t1,key=len))
    l2 = len(max(t2,key=len))
    tab = '    '
    if t2 > t1:
        t1 = t1 + [' ' * l1] * (len(t2)-len(t1))
    lines = ['Team1'.ljust(l1) + tab + 'Team2'.ljust(l2) + '\n' +
             '-'*(l1+l2+len(tab)) + '\n']
    longer = max(len(t1),len(t2))
    for i in range(longer):
        lines.append(t1[i].ljust(l1)+tab+t2[i].ljust(l2)+'\n')
    return('`'+''.join(lines)+'`')

bot.run(TOKEN)

