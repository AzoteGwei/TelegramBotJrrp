# 使用 python3 main.py yourtoken 来启动，比如 python3 main.py 114514:ABCDEFGO_HIJKLMNOxE
import telebot
import random
from datetime import datetime, timedelta
import sys

GOOD_DAYS = [2024210, 202429, 202422, 202467, 202468, 202469, 202567, 202568, 202569]

bot = telebot.TeleBot(str(sys.argv[1]), parse_mode="MARKDOWN")


@bot.message_handler(commands=["jrrp"])
def send_jrrp(message):
    bot.reply_to(message, jrrp_text_init(from_input_get_score(message.from_user.id)))


def jrrp_text_init(nub_in):
    nub = int(nub_in)
    if nub == 100:
        return "今天的人品是：" + str(nub_in) + "\n" + "100 人品好评!!!"
    elif nub >= 90:
        return "今天的人品是：" + str(nub_in) + "\n" + "今天的人品非常不错呢"
    elif nub >= 70:
        return "今天的人品是：" + str(nub_in) + "\n" + "哇,人品还挺好的!"
    elif nub >= 60:
        return "今天的人品是：" + str(nub_in) + "\n" + "今天是 非常¿ 不错的一天呢!"
    elif nub > 50:
        return "今天的人品是：" + str(nub_in) + "\n" + "你的人品还不错呢"
    elif nub == 50:
        return "今天的人品是：" + str(nub_in) + "\n" + "五五开！"
    elif nub >= 40:
        return "今天的人品是：" + str(nub_in) + "\n" + f"还好还好只有 {nub}"
    elif nub >= 20:
        return "今天的人品是：" + str(nub_in) + "\n" + f"{nub} 这数字太....要命了"
    elif nub >= 0:
        return "今天的人品是：" + str(nub_in) + "\n" + "抽大奖¿"


def from_input_get_score(user_id):
    random.seed(int(when_is_now_in_utc_plus_8()) + int(user_id))
    score = random.randint(0, 100)

    # 给那些运气烂的家伙
    if score < 35:
        score += random.randint(23, 31)

    if when_is_now_in_utc_plus_8() in GOOD_DAYS:
        score += 100

    return score


def when_is_now_in_utc_plus_8():
    # 获取当前时间
    current_time = datetime.utcnow()

    # 将当前时间调整为东八区时间
    eastern_eight_time = current_time + timedelta(hours=8)

    # 提取年月日
    year = eastern_eight_time.year
    month = eastern_eight_time.month
    day = eastern_eight_time.day

    return int(str(year) + str(month) + str(day))


bot.infinity_polling()
