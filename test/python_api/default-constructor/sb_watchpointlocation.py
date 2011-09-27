"""
Fuzz tests an object after the default construction to make sure it does not crash lldb.
"""

import sys
import lldb

def fuzz_obj(obj):
    obj.GetID()
    obj.GetHardwareIndex()
    obj.GetWatchAddress()
    obj.GetWatchSize()
    obj.SetEnabled(True)
    obj.IsEnabled()
    obj.GetHitCount()
    obj.GetIgnoreCount()
    obj.SetIgnoreCount(5)
    obj.GetDescription(lldb.SBStream(), lldb.eDescriptionLevelVerbose)
