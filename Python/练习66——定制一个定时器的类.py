#如果开始计时的时间为（2022年2月22日16:30:30），停止时间是（2025年1月23日15:30:30）
#那按照我们用停止时间减去开始时间的计算方式就会出现负数，应该对此做一些转换。

import time as t

class MyTimer:
    def __init__(self):
        self.prompt = "未开始计时"
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
        self.default_timer = t.perf_counter
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了%0.2f秒" % result
        return prompt
    def start(self):
        self.begin = self.default_timer()
        self.prompt = "提示：请先调用stop()停止计时！"
        print("计时开始！")
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()运行计时！")
        else:
            self.end = self.default_timer()
            self._calc()
            print("计时结束")
    def _calc(self):
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了%0.2f秒" % self.lasted
        print(self.prompt)
        self.begin = 0
        self.end = 0

    def set_timer(self, timer):
        if timer == 'process_time':#perf_counter()返回计时器的精准时间（系统的运行时间）
            self.default_timer = t.process_time
        elif timer == 'perf_counter':#process_time()返回当前进程执行CPU的时间总和
            self.default_timer = t.perf_counter
        else:
            print("输入无效")
