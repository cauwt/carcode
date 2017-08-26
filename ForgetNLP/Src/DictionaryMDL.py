# -*- coding: utf-8 -*-
import sys
import os

from MemoryMDL import MemoryMDL


class MemoryItemMDL(MemoryMDL):
    def __init__(self):
        super(MemoryItemMDL, self).__init__()
        self.key = ""

class MemoryItemColl:
    def __init__(self):
        self.offsetTotalCount = 0
        self.minuteOffsetSize = 0
        self.coll = {}




class MemoryBondMDL:
    def __init__(self):
        self.keyItem = MemoryItemMDL()
        self.linkColl = MemoryItemColl()


class MemoryBondColl:
    def __init__(self):
        self.offsetTotalCount = 0
        self.minuteOffsetSize = 0
        self.coll = {}
