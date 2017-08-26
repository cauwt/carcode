# -*- coding: utf-8 -*-


import math


# 牛顿冷却公式
# 建议遗忘系数：-Math.Log(0.254, Math.E) / (6天 * 24小时 * 60分钟 *60秒 *7每秒阅读字数);
def calcNetonCooling(parameter, interval):
    return math.exp(-1 * parameter * interval)

# 以偏移量模拟时间流逝的遗忘公式
# offsetCount:偏移量
# 此处第二个参数没有使用，原因是已经将相关计算合并进遗忘系数中，此处保留为兼容代码。
def calcRemeberValue(offsetCount, minuteOffsetSize):
    parameter = -math.log(0.254)/(6*24*60*60*7)
    return calcNetonCooling(parameter,offsetCount)


if __name__=='__main__':
    pass