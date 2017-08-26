# -*- coding: utf-8 -*-

class MemoryMDL:
    def __init__(self):
        self.validCount =0 #遗忘累频
        self.totalCount =0 #累计次数
        self.updateOffsetCount =0#最后一次更新时的系统总偏移量（用于模拟计时）
        self.validDegree =0#有效程度（成熟度）,成熟度的物理含义：成熟的标志是遗忘的量与出现的量基本一致

if __name__=='__main__':
    print "class MemoryMDL"
    pass