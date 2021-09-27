class Solution:

    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next=pHead
            pHead.next = None
            print(newHead)
            return newHead


if __name__ == '__main__':
    s = Solution()
    s.ReverseList([1,2,34,5,6])