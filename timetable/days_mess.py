from datetime import datetime
import gspread
worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1ZLodGxsGLLxDdzVbpING0jcJImsyOAW1S9y8NcAs2_w/edit#gid=2127480627').get_worksheet(0)


def day_mess(day, week):
    if int(week) % 2 != 0:
        if str(day) == "monday":
            text = "    ◀ Понеділок ▶ 🔶  \n"
            x = 4
        if str(day) == "tuesday":
            text = "    ◀ Вівторок ▶ 🔶  \n"
            x = 16
        if str(day) == "wednesday":
            text = "    ◀ Середа ▶ 🔶  \n"
            x = 28
        if str(day) == "thursday":
            text = "    ◀ Четвер ▶ 🔶  \n"
            x = 40
        if str(day) == "friday":
            text = "    ◀ П'ятниця ▶ 🔶  \n"
            x = 52
    else:
        if str(day) == "monday":
            text = "    ◀ Понеділок ▶ 🔷  \n"
            x = 3
        if str(day) == "tuesday":
            text = "    ◀ Вівторок ▶ 🔷  \n"
            x = 15
        if str(day) == "wednesday":
            text = "    ◀ Середа ▶ 🔷  \n"
            x = 27
        if str(day) == "thursday":
            text = "    ◀ Четвер ▶ 🔷  \n"
            x = 39
        if str(day) == "friday":
            text = "    ◀ П'ятниця ▶ 🔷 \n"
            x = 51
    first = str(worksheet.acell('C' + str(x) + ':F' + str(x) + '').value)
    second = str(worksheet.acell('C' + str(x + 2) + ':F' + str(x + 2) + '').value)
    third = str(worksheet.acell('C' + str(x + 4) + ':F' + str(x + 4) + '').value)
    fourth = str(worksheet.acell('C' + str(x + 6) + ':F' + str(x + 6) + '').value)
    fifth = str(worksheet.acell('C' + str(x + 8) + ':F' + str(x + 8) + '').value)
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
    if fifth != "None":
        text += "Ⅴ. [14.20 - 15.40] <b>" + fifth + "</b>\n"
        pass
    return text

def getLine(day, color, line):
    if color == 0:
        "🔶 - четная"
        if day == 1:
            x = 4
        if day == 2:
            x = 16
        if day == 3:
            x = 28
        if day == 4:
            x = 40
        if day == 5:
            x = 52
    else:
        "🔷 - нечетная"
        if day == 1:
            x = 3
        if day == 2:
            x = 15
        if day == 3:
            x = 27
        if day == 4:
            x = 39
        if day == 5:
            x = 51
    if line == 1:
        text = str(worksheet.acell('C' + str(x) + ':F' + str(x) + '').value)
    if line == 2:
        text = str(worksheet.acell('C' + str(x + 2) + ':F' + str(x + 2) + '').value)
    if line == 3:
        text = str(worksheet.acell('C' + str(x + 4) + ':F' + str(x + 4) + '').value)
    if line == 4:
        text = str(worksheet.acell('C' + str(x + 6) + ':F' + str(x + 6) + '').value)
    if line == 5:
        text = str(worksheet.acell('C' + str(x + 8) + ':F' + str(x + 6) + '').value)
    return text

def getFullDay(day):
    z = 1
    text = ""
    if day == 1:
        text += "\n\n    ◀ Понеділок ▶   \n"
    if day == 2:
        text += "\n\n    ◀ Вівторок ▶   \n"
    if day == 3:
        text += "\n\n    ◀ Середа ▶   \n"
    if day == 4:
        text += "\n\n     ◀ Четвер ▶   \n"
    if day == 5:
        text += "\n\n    ◀ П'ятниця ▶   \n"
    text += "════════════════\n"
    while (z < 6):
        up = str(getLine(day=day, color=1, line=z))
        down = str(getLine(day=day, color=0, line=z))
        if up != "None" or down != "None":
            if z == 1:
                text += "Ⅰ.   [08.00 - 09.20]\n"
            if z == 2:
                text += "Ⅱ.  [09.35 - 10.55]\n"
            if z == 3:
                text += "Ⅲ. [11.10 - 12.30]\n"
            if z == 4:
                text += "Ⅳ. [12.45 - 14.05]\n"
            if z == 5:
                text += "Ⅴ. [14.20 - 15.40]\n"
            if up == down:
                text += up + "\n"
            else:
                if not ("None" in up):
                    text += up + "\n"
                if not ("None" in down):
                    text += down + "\n"
        z = z + 1
    return text
