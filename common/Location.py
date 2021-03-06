# 记录位置信息的类
import time


class Location:
    auto_adb = None
    temp_rel_path = None
    pos_x = None
    pos_y = None

    # 默认等待时间
    wait_time = 0.5

    def __init__(self, auto_adb, temp_rel_path, pos_x, pos_y):
        self.auto_adb = auto_adb
        self.temp_rel_path = temp_rel_path
        self.pos_x = pos_x
        self.pos_y = pos_y

    def is_valuable(self):
        return self.pos_x is not None and self.pos_y is not None

    def click(self, wait_time=wait_time):
        if self.pos_x is None:
            return False

        self.auto_adb.run('shell input tap %s %s' % (self.pos_x, self.pos_y))
        print('click [%d:%d] %s' % (self.pos_x, self.pos_y, self.temp_rel_path))
        time.sleep(wait_time)
        return True


