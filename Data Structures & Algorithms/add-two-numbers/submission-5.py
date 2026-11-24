# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # traverse list add value, multiply by 10 and add prev

        # start with reversing list , dont reverse linked-list (takes more time)
        def listToNum(l1):
            if l1.val == 0:
                return 0

            res = 0
            pos = 1 # ones place, increment every next node
            while l1:
                # 1,2,3 --> 1 + 2*10 + 3*10^2 = 321
                res += l1.val * pos
                pos *= 10
                l1 = l1.next     
            return res
            
        num1, num2 = listToNum(l1), listToNum(l2)
        outputNum = num1 + num2

        # output must be in listNode format as well, 
            # requires re-reversing solution

        def numToList(num):
            if not num:
                return ListNode(val=0)
            
            # dummy -> head.val = v, head.next 
            dummy = ListNode(val=0, next = None)
            start = dummy
            # mod 10 would get 1s place
            # divide by 10 = drop remainder
            
            while num: 
                # print(f'{num=}')
                v = num % 10
                num = num // 10

                curr = ListNode(val=v)
                start.next = curr # first loop first item
                start = curr
                
            return dummy.next # head

        return numToList(outputNum)
