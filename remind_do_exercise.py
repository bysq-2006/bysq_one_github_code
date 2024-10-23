import asyncio
import time
from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import Bot, Event
from datetime import datetime #24小时
def convert_seconds(seconds):#将秒转换为时钟和分钟和秒
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

usebot_id = 12345678 #使用者的QQ

w = on_keyword(keywords={"已经完成"})
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() != str(usebot_id)):
        return
    time_ = time.time()
    with open('timestamp.txt', 'w') as file:
        file.write(str(time_))
    await bot.send_private_msg(user_id=usebot_id,message="不错不错，继续加油。")

w = on_keyword(keywords={"我有多久没有"})
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() != str(usebot_id)):
        return
    time_ = time.time()
    with open('timestamp.txt', 'r') as file:
        time_read = float(file.read())
    total_seconds = time_ - time_read
    hours, minutes, seconds = convert_seconds(total_seconds)
    await bot.send_private_msg(user_id=usebot_id,message=f"你有{int(hours)}小时 {int(minutes)}分钟 {int(seconds)}秒没有写题了。")
w = on_command(cmd="start")
# #timestamp.txt需要提前创建一个，然后在里面随便打点数字，因为我没有做初始化
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() == str(usebot_id)):
        await bot.send_private_msg(user_id=usebot_id,message="已经启动。")
        while True:
            time_ = time.time()
            now = datetime.now()
            with open('timestamp.txt', 'r') as file:
                time_read = float(file.read())
            if (time_ - time_read) > 129600:
                await bot.send_private_msg(user_id=usebot_id,message="已经三天没有写算法了，今天必须写了，我会一直发，直到写了为止。")
            elif (time_ - time_read) > 86400 and (datetime.now().hour == 12 and datetime.now().minute >= 30) and (datetime.now().hour == 13 and datetime.now().minute < 30):
                await bot.send_private_msg(user_id=usebot_id,message="已经两天没有写算法了，快快快。")
            elif (time_ - time_read) > 43200 and (datetime.now().hour == 12 and datetime.now().minute >= 30) and (datetime.now().hour == 13 and datetime.now().minute < 30):
                await bot.send_private_msg(user_id=usebot_id,message="已经一天没有写算法了。")
            await asyncio.sleep(3600)  # 暂停 3600 秒后再进行下一次循环

