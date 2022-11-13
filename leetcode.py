'''
1.两数之和.给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
'''
from typing import Optional


class Solution:
    def twoSum(self, nums: list[int], target: int):
        hash_map = {}
        for k, v in enumerate(nums):
            # print(k,v)
            if target - v in hash_map:
                return [hash_map[target - v], k]
            hash_map[v] = k
        pass


'''
2.两数相加.给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化个位节点，先不做进位
        newPoint = ListNode(l1.val + l2.val)
        # rt用来作为最后return的节点，tp用来遍历节点
        rt, tp = newPoint, newPoint
        # l1,l2只要后面还有节点，就继续往后遍历；或者新链表还需要继续往后进位
        while (l1 and (l1.next != None)) or (l2 and (l2.next != None)) or (tp.val > 9):
            l1, l2 = l1.next if l1 else l1, l2.next if l2 else l2
            tmpsum = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # 计算新链表下个节点的值（当前节点的进位+当前l1 l2的值之和），先不做进位
            tp.next = ListNode(tp.val // 10 + tmpsum)
            # 新链表当前节点的值取个位
            tp.val %= 10
            # 新链表往后遍历一个节点
            tp = tp.next
        return rt
'''


def addTwoNumbers(l1, l2):
    l1.reverse()
    l2.reverse()
    s1 = [str(x) for x in l1]
    res1 = int("".join(s1))
    print(res1)
    s2 = [str(x) for x in l2]
    res2 = int("".join(s2))
    print(res2)
    ans = res1 + res2
    ans1 = [int(x) for x in str(ans)]
    ans1.reverse()
    print(ans1)


def lengthOfLongestSubstring(s: str):
    st = {}
    i, k = 0, 0
    for j in range(len(s)):
        # print(st)
        if s[j] in st:
            i = max(st[s[j]], i)
        k = max(k, j - i + 1)
        print(k)
        st[s[j]] = j + 1
    print(st)
    print(k)
    return k


def findMedianSortedArrays(nums1, nums2) -> float:
    l = nums1 + nums2
    l.sort()
    t = len(l)
    a = t / 2
    b = int(a)
    if a - b == 0:
        c = (l[b] + l[b - 1]) / 2
    else:
        c = l[b]
    print(c)
    return c


if __name__ == '__main__':
    # nums = [5, 4, 7]
    # target = 11
    # print(Solution().twoSum(nums, target))
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    # addTwoNumbers(l1,l2)
    # s='pwwekw'
    # lengthOfLongestSubstring(s)
    nums1 = [1, 2]
    nums2 = [3, 4]
    findMedianSortedArrays(nums1, nums2)
