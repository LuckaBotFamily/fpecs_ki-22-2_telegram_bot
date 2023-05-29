from aiogram.utils import executor
from create_bot import dp

from timetable import commands, days, notify, timetable
from games import main as games
from miscellaneous import main as miscellaneous

commands.register_handlers_commands(dp)
#days.register_handlers_days(dp)
#notify.register_handlers_notify(dp)
#timetable.register_handlers_days(dp)
games.register_handlers_games(dp)
miscellaneous.register_handlers_misc(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)