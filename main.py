from aiogram.utils import executor
from create_bot import dp

from timetable import commands, days, notify, timetable
from games import main

commands.register_handlers_commands(dp)
days.register_handlers_days(dp)
notify.register_handlers_notify(dp)
timetable.register_handlers_days(dp)
main.register_handlers_games(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)