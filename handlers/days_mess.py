from datetime import datetime
import gspread
worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1ZLodGxsGLLxDdzVbpING0jcJImsyOAW1S9y8NcAs2_w/edit#gid=2127480627').get_worksheet(0)


def day_mess(day):
    if int(datetime.date(datetime.today()).strftime("%V")) % 2 == 0:
        if str(day) == "monday":
            text = "    ◀ Понеділок ▶ 🔶  \n"
            x = 4
        if str(day) == "tuesday":
            text = "    ◀ Вівторок ▶ 🔶  \n"
            x = 14
        if str(day) == "wednesday":
            text = "    ◀ Середа ▶ 🔶  \n"
            x = 24
        if str(day) == "thursday":
            text = "    ◀ Четверг ▶ 🔶  \n"
            x = 34
        if str(day) == "friday":
            text = "    ◀ П'ятниця ▶ 🔶  \n"
            x = 44
    else:
        if str(day) == "monday":
            text = "    ◀ Понеділок ▶ 🔷  \n"
            x = 3
        if str(day) == "tuesday":
            text = "    ◀ Вівторок ▶ 🔷  \n"
            x = 13
        if str(day) == "wednesday":
            text = "    ◀ Середа ▶ 🔷  \n"
            x = 23
        if str(day) == "thursday":
            text = "    ◀ Четверг ▶ 🔷  \n"
            x = 33
        if str(day) == "friday":
            text = "    ◀ П'ятниця ▶ 🔷 \n"
            x = 43
    first = str(worksheet.acell('C' + str(x) + ':F' + str(x) + '').value)
    second = str(worksheet.acell('C' + str(x + 2) + ':F' + str(x + 2) + '').value)
    third = str(worksheet.acell('C' + str(x + 4) + ':F' + str(x + 4) + '').value)
    fourth = str(worksheet.acell('C' + str(x + 6) + ':F' + str(x + 6) + '').value)
    text += "════════════════\n"
    if first != "None":
        text += "Ⅰ.   [08.00 - 09.20] <b>" + first + "</b>\n"
        pass
    if second != "None":
        text += "Ⅱ.  [09.35 - 10.55] <b>" + second + "</b>\n"
        pass
    if third != "None":
        text += "Ⅲ. [11.10 - 12.30] <b>" + third + "</b>\n"
        pass
    if fourth != "None":
        text += "Ⅳ. [12.45 - 14.05] <b>" + fourth + "</b>\n"
        pass
    return  text

def getLine(day, color, line):
    if color == 0:
        "🔶 - четная"
        if day == 1:
            x = 4
        if day == 2:
            x = 14
        if day == 3:
            x = 24
        if day == 4:
            x = 34
        if day == 5:
            x = 44
    else:
        "🔷 - нечетная"
        if day == 1:
            x = 3
        if day == 2:
            x = 13
        if day == 3:
            x = 23
        if day == 4:
            x = 33
        if day == 5:
            x = 43
    if line == 1:
        text = str(worksheet.acell('C' + str(x) + ':F' + str(x) + '').value)
    if line == 2:
        text = str(worksheet.acell('C' + str(x + 2) + ':F' + str(x + 2) + '').value)
    if line == 3:
        text = str(worksheet.acell('C' + str(x + 4) + ':F' + str(x + 4) + '').value)
    if line == 4:
        text = str(worksheet.acell('C' + str(x + 6) + ':F' + str(x + 6) + '').value)
    return text