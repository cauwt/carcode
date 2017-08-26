# -*- coding: utf-8 -*-
import sys
import os
import math
import DictionaryMDL.MemoryItemMDL
import MemoryDAL


# 计算当前关键词的成熟度
# 公式的意思是： 成熟度 = 成熟度衰减剩余量 + 本次遗忘与增加量的残差的绝对值
def calcValidDegree(memoryItemMDL, rememberValue):
    return memoryItemMDL.validDegree * rememberValue + abs(1 - memoryItemMDL.validCount * (1 - rememberValue))

# 计算候选项记忆剩余量
def calcRememberValue(key, memoryItemColl):
    if not memoryItemColl.coll.get(key):
        return 0
    memoryItemMDL = memoryItemColl.coll[key]
    rememberValue = MemoryDAL.calcRemeberValue(memoryItemColl.offsetTotalCount - memoryItemMDL.updateOffsetCount,
                                               memoryItemColl.minuteOffsetSize)
    return memoryItemMDL.validCount * rememberValue


# 计算邻键首项记忆剩余量
def calcRememberValue_Link_Head(key, memoryBondColl):
    if not memoryBondColl.coll.get(key):
        return 0
    memoryBondMDL = memoryBondColl.coll[key]
    memoryItemMDL = memoryBondMDL.keyItem
    rememberValue = MemoryDAL.calcRemeberValue(memoryBondColl.offsetTotalCount - memoryItemMDL.updateOffsetCount,
                                               memoryBondColl.minuteOffsetSize)
    return memoryItemMDL.validCount * rememberValue


# 计算邻键尾项记忆剩余量
def calcRememberValue_Link_Tail(keyHead,keyTail, memoryBondColl):
    if not memoryBondColl.coll.get(keyHead):
        return 0
    memoryBondMDL = memoryBondColl.coll[keyHead]
    memoryItemColl = memoryBondMDL.linkColl
    return calcRememberValue(keyTail,memoryItemColl)


# 判断键是否为有效关联键
def isBondValid(keyHead, keyTail,memoryBondColl):
    if not memoryBondColl.coll.get(keyHead) or not memoryBondColl.coll.get(keyTail):
        return False
    headValidCount = calcRememberValue_Link_Head(keyHead,memoryBondColl)
    tailValidCount = calcRememberValue_Link_Head(keyTail,memoryBondColl)

    totalValidCount = memoryBondColl.minuteOffsetSize
    if totalValidCount <=0:
        return True

    # 获得相邻项共现的频次
    memoryItemColl = memoryBondColl.coll[keyHead].linkColl
    if not memoryItemColl.coll.get(keyTail):
        return False
    shareValidCount = calcRememberValue_Link_Head(keyTail, memoryItemColl);

    # 返回计算的结果
    return shareValidCount / headValidCount > tailValidCount / totalValidCount;

