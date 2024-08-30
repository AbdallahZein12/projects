from .constants import TOKEN
from .lyrica import Lyrica

async def setup(bot):
    await bot.add_cog(Lyrica(bot))