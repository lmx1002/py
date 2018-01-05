#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@author: simon
@file: t5
@time: 2017/6/28 22:13
@software: PyCharm
"""
import wmi
import os
import sys
import platform
import time

c = wmi.WMI()
for s in c.Win32_OperatingSystem():
    print("系统版本", s.Caption)
    print("发行版本", s.BuildNumber)
    print("系统位数", s.OSArchitecture)
    print("进程数", s.NumberOfProcesses)

for p in c.Win32_Processor():
    print("cpu信息", p.Name)

mem_list = []
for m in c.Win32_PhysicalMemory():
    gg = int(m.Capacity) / 1024 / 1024 / 1024
    mem_list.append(gg)
    # print(m.PartNumber)
print("内存大小", sum(mem_list))

for n in c.Win32_NetworkAdapterConfiguration():
    if n.MACAddress is not None and n.IPAddress is not None:
        print("MAC", n.MACAddress)
        print("IP", n.IPAddress)

for d in c.Win32_DiskDrive():
    # print(d)
    # print(d.Caption)
    print("硬盘名称", d.Caption, "大小", int(d.Size) / 1024 / 1204)

for d1 in c.Win32_LogicalDisk():
    if d1.FreeSpace and d1.Size:
        print("分区", d1.Name, "空闲大小", int(d1.FreeSpace) / int(d1.Size) * 100)

print("操作系统", platform.system())
print("cpu平台", platform.machine())
print("python版本", platform.python_version())
