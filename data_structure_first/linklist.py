"""
实现单链表
"""


# 创建结点
class Node:
    """
    自定义的节点生成类，包含当前结点的值和指向下一个结点的引用
    """

    def __init__(self, val, next_node=None):
        self.val = val  # 当前结点的值
        self.next = next_node  # 对后一结点的引用


class LinkList:
    """
    生成节点后，进行增删改查操作
    通过定义方法完成相应操作
    """

    def __init__(self):
        """
        初始化链表，标记链表的开端，以便于获取后续结点
        """
        self.head = Node(None)

    def init_list(self, list_):
        """
        添加节点
        """
        p = self.head
        for item in list_:
            p.next = Node(item)
            p = p.next

    def traversing_list(self):
        """
        遍历链表

        """
        p = self.head.next
        while p is not None:
            print(p.val)
            p = p.next

    # 判断链表为空
    def is_empty(self):
        """
        头结点后无结点，可判定链表为空
        """
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        """
        使我们无法访问后续结点（但实际上那些结点还在）
        """
        self.head.next = None

    def append(self, value):
        """
        尾部插入结点

        """
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)

    def head_insert(self, value):
        """
        头部插入结点

        """
        node = Node(value)
        node.next = self.head.next
        self.head.next = node

    def insert(self, index, value):
        """
        在中间某一位置插入节点
        :param index:head后面第一个结点的index为0
        :param value:
        :return:
        """
        p = self.head
        for i in range(index):
            # 如果超过了链表的范围，就退出循环
            if p.next is None:
                break
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node

    def delete(self,value):
        """
        删除结点
        """
        p=self.head
        while p.next and p.next.value!=value:
            p=p.next
        if p.next is None:
            raise ValueError ('Value is not in linklist!')
        else:
            p.next=p.next.next
    def get_node(self,index):
        """
        获取结点的值
        :index:结点位置
        :return:
        """
        p=self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError('list index out of range')
            else:
                p=p.next
        return p.val






