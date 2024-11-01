import asyncio
import time
from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import Bot, Event
from datetime import datetime #24小时
from nonebot.adapters import MessageTemplate
def convert_seconds(seconds):#将秒转换为时钟和分钟和秒
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

usebot_id = 1904568840 #使用者的QQ

w = on_keyword(keywords={"撸管"},priority=5)
@w.handle()
async def leet00code(bot: Bot, event: Event):
    await bot.send(event=event, message="撸管虽一时愉悦，却潜藏身心危害。为了健康，请自控自律，培养良好习惯，让生活更加充实精彩。拒绝沉迷，拥抱健康人生。")

w = on_keyword(keywords={"已经完成"},priority=5)
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() != str(usebot_id)):
        return
    time_ = time.time()
    with open('timestamp.txt', 'w') as file:
        file.write(str(time_))
    await bot.send_private_msg(user_id=usebot_id,message="不错不错，继续加油。")

w = on_keyword(keywords={"我有多久没有"},priority=5)
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
w = on_command(cmd="start",priority=5)
# #timestamp.txt需要提前创建一个，然后在里面随便打点数字，因为我没有做初始化
leetcode_state:bool = False
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() == str(usebot_id)):
        global leetcode_state
        if leetcode_state:
            await bot.send_private_msg(user_id=usebot_id,message="已经启动，请勿重复操作。")
            return
        await bot.send_private_msg(user_id=usebot_id,message="已经启动。")
        while True:
            leetcode_state = True
            time_ = time.time()
            now = datetime.now()
            with open('timestamp.txt', 'r') as file:
                time_read = float(file.read())
            if (time_ - time_read) > 259200:
                await bot.send_private_msg(user_id=usebot_id,message="已经三天没有写算法了，今天必须写了，我会一直发，直到写了为止。")
            elif (time_ - time_read) > 172800 and ((datetime.now().hour == 12 and datetime.now().minute >= 30) or (datetime.now().hour == 13 and datetime.now().minute < 30)):
                await bot.send_private_msg(user_id=usebot_id,message="已经两天没有写算法了，快快快。")
            elif (time_ - time_read) > 86400 and ((datetime.now().hour == 12 and datetime.now().minute >= 30) or (datetime.now().hour == 13 and datetime.now().minute < 30)):
                await bot.send_private_msg(user_id=usebot_id,message="已经一天没有写算法了。")
            await asyncio.sleep(3600)  # 暂停 3600 秒后再进行下一次循环
