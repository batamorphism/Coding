import math


def main():
    bot, hei, vol = map(int, input().split())
    # 2次元で考える
    vol /= bot
    if vol >= (bot*hei)/2:
        # 半分以上を占めているときは、ちょっとしか傾けない
        rem_vol = (bot*hei)-vol
        x = rem_vol/bot*2
        # bot, xを辺に持つ直角三角形のなす角度
        tan_ = x/bot
        theta = math.atan(tan_)
        deg = math.degrees(theta)
        print(deg)
    else:
        # 半分以下の場合は、たくさん傾ける
        x = vol/hei*2
        # hei, xを辺に持つ直角三角形のなす角度
        tan_ = hei/x
        theta = math.atan(tan_)
        deg = math.degrees(theta)
        print(deg)


main()

