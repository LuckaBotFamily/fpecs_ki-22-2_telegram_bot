import random
import time
from create_bot import bot
from aiogram import types
from . import tools


async def slot(message: types.Message):
     j = 0
     up = "╔═══════════╗\n"
     down = "╚═══════════╝"
     line1 = line2 = line3 = "◼◼◼◼◼"
     text = up + "║" + line1 + "║⋘ x3\n║" + line2 + "║⋘ x5\n║" + line3 + "║⋘ x3\n" + down
     if message.get_args().split(' ')[0] == '':
          money = 100
     else:
          try:
               money =int(message.get_args().split(' ')[0])
          except:
               await bot.send_message(chat_id=message.chat.id,
                                      text="Введіть ціле число!")
     if money > 0:
          mess = await bot.send_message(chat_id=message.chat.id, text=text)
          while(j < 10):
               text = ""
               i = 0
               while(i < 5):
                    text += getFruit()
                    i = i + 1
               if random.randint(1, 10) % 3 == 0:
                    text = list(text)
                    text[0] = text[1] = text[2] = text[3] = getFruit()
                    text = str(text[0] + text[1] + text[2] + text[3] + text[4])
               line3 = line2
               line2 = line1
               line1 = text
               j = j + 1
               text = up + "║" + line1 + "║⋘ x3\n║" + line2 + "║⋘ x5\n║" + line3 + "║⋘ x3\n" + down
               if j == 2 or j == 4 or j == 6 or j >= 8:
                    last_mess = await bot.edit_message_text(chat_id=mess.chat.id, message_id=mess.message_id, text=text)
          if j == 10:
               time.sleep(0.5)
               line3 = list(line3)
               line2 = list(line2)
               line1 = list(line1)
               x = 1
               last_text = f"На жаль, ви програли {money}"
               tools.delMoney(message.from_user.id, money)
               if line2[0] == line2[1] == line2[2] == line2[3] == line2[4]:
                    x = 5 + getMultiply(line2[0])
                    line2[0] = line2[1] = line2[2] = line2[3] = line2[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               elif line1[0] == line1[1] == line1[2] == line1[3] == line1[4]:
                    x = 3 + getMultiply(line1[0])
                    line1[0] = line1[1] = line1[2] = line1[3] = line1[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               elif line3[0] == line3[1] == line3[2] == line3[3] == line3[4]:
                    x = 3 + getMultiply(line3[0])
                    line3[0] = line3[1] = line3[2] = line3[3] = line3[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               elif line1[0] == line2[1] == line3[2] == line2[3] == line1[4]:
                    x = 2 + getMultiply(line1[0])
                    line1[0] = line2[1] = line3[2] = line2[3] = line1[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               elif line3[0] == line2[1] == line1[2] == line2[3] == line3[4]:
                    x = 2 + getMultiply(line3[0])
                    line3[0] = line2[1] = line1[2] = line2[3] = line3[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               elif line2[0] == line3[1] == line3[2] == line3[3] == line2[4]:
                    x = 2 + getMultiply(line2[0])
                    line2[0] = line3[1] = line3[2] = line3[3] = line2[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               elif line2[0] == line1[1] == line1[2] == line1[3] == line2[4]:
                    x = 2 + getMultiply(line2[0])
                    line2[0] = line1[1] = line1[2] = line1[3] = line2[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               elif line3[0] == line1[1] == line1[2] == line1[3] == line3[4]:
                    x = 2 + getMultiply(line3[0])
                    line3[0] = line1[1] = line1[2] = line1[3] = line3[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               elif line1[0] == line3[1] == line3[2] == line3[3] == line1[4]:
                    x = 2 + getMultiply(line1[0])
                    line1[0] = line3[1] = line3[2] = line3[3] = line1[4] = str('✅')
                    money = money * x
                    last_text = f"Ви вийграли {money}"
                    tools.addMoney(message.from_user.id, money)
               else:
                    last_text = f"На жаль, ви програли {money}"
                    tools.delMoney(message.from_user.id, money)
               line1 = str(line1[0] + line1[1] + line1[2] + line1[3] + line1[4])
               line2 = str(line2[0] + line2[1] + line2[2] + line2[3] + line2[4])
               line3 = str(line3[0] + line3[1] + line3[2] + line3[3] + line3[4])
               await bot.edit_message_text(chat_id=mess.chat.id, message_id=mess.message_id,
                                           text= up + "║" + line1 + "║⋘ x3\n║" + line2 + "║⋘ x5\n║" + line3 + "║⋘ x3\n" + down + "\n\n"+ last_text + "💷")
     else:
          await bot.send_message(chat_id=message.chat.id,
                                 text="Введіть ціле число!")


def getMultiply(char):
     if char == '🍏':
          x = 0
     if char == '🍒':
          x = 2
     if char == '🍋':
          x = 5
     if char == '🍇':
          x = 10
     return x

def getFruit():
     num = random.randint(1, 100)
     if num <= 40:
          char = '🍏'
     if num > 40 and num <= 70:
          char = '🍒'
     if num > 70 and num <= 90:
          char = '🍋'
     if num > 90:
          char = '🍇'
     return char