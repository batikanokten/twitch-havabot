from twitchio.ext import commands
import havad

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='...ACCESS TOKEN...', prefix='!', initial_channels=['...CHANNEL NAME...'])
        #Get token from https://twitchtokengenerator.com/ "Access Token"
        #Prefix is the command prefix ex. !weather
    async def event_ready(self):
        #Loggs in to twitch chat test
        print(f'Logged in as | {self.nick}')

    @commands.command(name="weather") #!weather City
    async def weather(self, ctx):
        msg = ctx.message.content[8:]
        hava = havad.weather(msg)
        await ctx.send(hava)

bot = Bot()
bot.run()