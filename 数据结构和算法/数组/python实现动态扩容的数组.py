#  python实现支持动态扩容的数组


class DynamicArr:
    def __init__(self, capacity=20):
        """
        构造函数
        :param capacity: 数组容量默认为20
        """
        self._capacity = capacity
        self._length = 0  # 数组的有效长度
        # 基于列表实现，通过赋值None实现底层具有连续内存的空间，容量固定的数组
        self._data = [None] * self._capacity

    def __getitem__(self, index):
        """使得Dynamic类实例化的对象支持索引随机访问"""
        return self._data[index]

    def __setitem__(self, index, value):
        """实例化对象可直接赋值"""
        self._data[index] = value

    def get_length(self):
        """返回数组长度"""
        return self._length

    def get_capacity(self):
        """返回数组容量"""
        return self._capacity

    def add(self, index, value):
        """
        往数组增加一个元素
        :param index:待添加元素在数组的目标下标
        :param value:待添加元素的值
        """
        if index < 0 or index > self._length:
            raise Exception('invaild index')
        if self._length == self._capacity:
            # 将数组容量扩充至两倍
            self._resize(self._capacity * 2)
        for i in range(self._length, index-1, -1):  # 移动元素
            self._data[i+1] = self._data[i]
        self._data[index] = value
        self._length += 1

    def add_last(self, value):
        """在末尾插入元素"""
        return self.add(self._length, value)

    def _resize(self, newCapacity):
        """
        重构数组的容量
        :param newCapacity:新的容量
        """
        new_arr = DynamicArr(newCapacity)
        for i in range(self._length):  # 移动元素到新的数组
            new_arr.add_last(self._data[i])
        self._capacity = new_arr._capacity
        self._data = new_arr._data
