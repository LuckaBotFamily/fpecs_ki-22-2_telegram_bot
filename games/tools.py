import gspread
from create_bot import bot
from aiogram import types

worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1ZLodGxsGLLxDdzVbpING0jcJImsyOAW1S9y8NcAs2_w/edit#gid=2127480627').get_worksheet(1)

async def casino(message: types.Message):
    if str(message.from_user.id) in worksheet.col_values(1):
        await bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}, ти вже є у базі даних")
    else:
        x = 2
        while(True):
            if str(worksheet.acell(f"B{x}").value) == "None":
                worksheet.update(f"B{x}", str(message.from_user.id))
                worksheet.update(f"A{x}", str(message.from_user.username))
                worksheet.update(f"C{x}", str(10000))
                break
            x = x + 1
        x = 2
        await bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}, обліковий запис успішно доданий до бази даних")

async def balance(messge: types.Message):
    await bot.send_message(chat_id=messge.chat.id, text=f"{messge.from_user.first_name}, твій баланс: {getBalance(messge.from_user.id)} 💷")

async def addmoney(message: types.Message):
    try:
        if str(message.from_user.id) == "602838745":
            username = str(message.get_args().split(' ')[0][1:-0])
            money = int(message.get_args().split(' ')[1])
            addMoney(getId(username), money)
            await bot.send_message(chat_id=message.chat.id, text=f"Користувачеві @{username} додано {money}💷")
    except:
        await bot.send_message(chat_id=message.chat.id, text="Помилка!")
def addMoney(id, money):
    id = worksheet.find(str(id)).row
    money = int(worksheet.acell(f"C{id}").value) + money
    worksheet.update(f"C{id}", str(money))

def delMoney(id, money):
    id = worksheet.find(str(id)).row
    money = int(worksheet.acell(f"B{id}").value) - money
    worksheet.update(f"C{id}", str(money))

def getBalance(id):
    id = worksheet.find(str(id)).row
    return worksheet.acell(f"C{id}").value

def getId(username):
    username = worksheet.find(str(username)).row
    return worksheet.acell(f"B{username}").value