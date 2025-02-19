from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add_to_end(self, val):
        vpr = self
        while vpr.next:
            vpr = vpr.next
        vpr.next = ListNode(val)

    def print_list_node(self):
        print("LIST:", self.val, end=" ")
        node = self
        while node.next:
            node = node.next
            print(node.val, end=" ")


def transform(lst: list):
    if lst:
        r = ListNode(lst[0])
        for el in lst[1:]:
            # print(el)
            r.add_to_end(el)
        return r
    else:
        return None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            rez = ListNode()
            if list1.val < list2.val:
                rez.val = list1.val
                if list1.next:
                    rez.next = self.mergeTwoLists(list1.next, list2)
                else:
                    rez.next = list2
            else:
                rez.val = list2.val
                if list2.next:
                    rez.next = self.mergeTwoLists(list1, list2.next)
                else:
                    rez.next = list1
        elif not list1:
            return list2
        elif not list2:
            return list1
        return rez


my_list = [7, 8, 19, 23, 36, 37]
k = transform(my_list)

my_list2 = [8, 12, 19, 22, 38, 43]
k2 = transform(my_list2)

obj = Solution()
rrr = obj.mergeTwoLists(k, k2)
if rrr:
    rrr.print_list_node()
else:
    print("LIST: []")
