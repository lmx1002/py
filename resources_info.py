#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@author: lmx1002
@file: resources_info.py
@time: 2017/6/20 17:21
@software: PyCharm
系统信息，cpu，内存，硬盘，网路，进程
"""
import datetime
import psutil
import platform

print("系统信息", platform.architecture())
print("操作系统", platform.system())
print("系统版本", platform.version())
print("系统cpu平台", platform.machine())
print("linux发行版本", platform.dist())
print("机器名称", platform.node())
print("系统信息", platform.uname())
print("python 版本", platform.python_version())

# 查看cpu信息
print("cpu的所有信息(分配情况):", psutil.cpu_times())
print("cpu的所有信息(逻辑):", psutil.cpu_times(percpu=True))
print("cpu核数(逻辑)：", psutil.cpu_count())
print("cpu物理个数：", psutil.cpu_count(logical=False))
print("cpu 使用率：", psutil.cpu_percent(interval=1))
print("cpu 每个的使用率：", psutil.cpu_percent(percpu=True))
print("cpu 用户时间比：", psutil.cpu_times().user)
# 查看内存
print("内存所有信息：", psutil.virtual_memory())
print("内存总大小：", psutil.virtual_memory().total)
print("已经使用的内存：", psutil.virtual_memory().used)
print("空闲内存：", psutil.virtual_memory().free)
print("swap信息", psutil.swap_memory())

# 磁盘信息
print("获取磁盘io信息", psutil.disk_io_counters())  # read_count(读IO数)，write_count(写IO数)
print("读IO数", psutil.disk_io_counters().read_count)
print("写IO数", psutil.disk_io_counters().write_count)
print("读IO字节数", psutil.disk_io_counters().read_bytes)
print("写IO字节数", psutil.disk_io_counters().write_bytes)
print("读磁盘时间", psutil.disk_io_counters().read_time)
print("写磁盘时间", psutil.disk_io_counters().write_time)

print("磁盘完整信息：", psutil.disk_partitions())
for i in psutil.disk_partitions():
    print("分区：{0}，挂载点:{1},文件类型:{2},权限：{3}".format(i.device, i.mountpoint, i.fstype, i.opts))
    if i.fstype:
        try:
            print("分区{0} - 状态{1}".format(i.device, psutil.disk_usage(i.device)))

        except Exception as e:
            print(e)

print("硬盘IO总数：", psutil.disk_io_counters(perdisk=True))  # windows 每个硬盘的io情况，linux 下每个分区的io情况

# 网路信息
print("网络IO信息", psutil.net_io_counters())
print("发送字节数", psutil.net_io_counters().bytes_sent)
print("接受字节数", psutil.net_io_counters().bytes_recv)
print("发送包数", psutil.net_io_counters().packets_sent)
print("接受包数", psutil.net_io_counters().packets_recv)
print("每个网卡的接口信息", psutil.net_io_counters(pernic=True))

# 用户
print("当前系统用户信息", psutil.users())

# 获取开机时间
print("获取开机时间", datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

# 系统进程管理
print("系统全部进程", psutil.pids())

# 查看单个进程信息
p = psutil.Process(4008)
try:
    print("进程名", p.name())
    print("进程的路径", p.exe())
    print("进程的工作目录", p.cwd())
    print("进程状态", p.status())
    print("进程创建时间", p.create_time())

    print("进程占用cpu信息", p.cpu_times())
    print("cpu亲和度(运行在哪个cpu上)", p.cpu_affinity())  # 设置直接将cpu号作为参数即可
    print("进程使用内存情况", p.memory_percent())
    print("进程内存rss,vms信息", p.memory_info())
    print("进程IO信息", p.io_counters())
    print("进程列表", p.connections())
    print("开启的线程数", p.num_threads())
    print("进程的线程对象", p.threads())
    print("是否运行", p.is_running())
    # print("挂起",p.suspend())
    # print("恢复运行",p.resume())
    # print("结束进程",p.kill())
    # print("进程uid信息", p.uids())
    # print("进程gid信息", p.gids())
except psutil.AccessDenied as e:
    print("无访问权限", e)
except psutil.NoSuchProcess as e:
    print(e)
except AttributeError as e:
    print(e)

# 程序跟踪
p = psutil.Popen(["python", "-c", "print('hello')"])
print(p.name())
print(p.username())

# print(psutil.cpu_freq())

import wmi

w = wmi.WMI()
