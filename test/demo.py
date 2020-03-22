#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/chatopera.xinli/alchemist/app.py
# Author: Hai Liang Wang
# Date: 2020-03-19:10:10:06
#
# ===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2020-03-19:10:10:06"

import os
import sys


curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

import sys
sys.path.append('gen-py')
sys.path.append('../')

import json
from tnj import JsonThriftConverter, ThriftJsonConverter

thrift_file = 'demo.thrift'
json2thrift = JsonThriftConverter(thrift_file).convert
thrift2json = ThriftJsonConverter(thrift_file).convert


def fake_obj():
    from space.demo.ttypes import Enum, Task, Worker, Group
    task = Task(id=727, msgs={"msg"}, status=0, action=Enum.UP, valid=True)
    worker = Worker(id=999, tasks=[task])
    group = Group(worker_map={worker.id : worker})
    return group

def test():
    obj = fake_obj()
    print('fake_obj:', obj)

    js = thrift2json(obj, 'Group')
    js_str = json.dumps(js)
    print('to_json:', js_str)

    obj = json2thrift(json.loads(js_str), 'Group')
    print('to_obj:', obj)

if __name__ == '__main__':
    test()
