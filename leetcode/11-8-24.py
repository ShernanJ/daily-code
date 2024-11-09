# Reviewed Linked List


# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev



# -------------------------------------------------





# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy node
        outputNode = ListNode()
        output = outputNode

        while list1 and list2:
            if list1.val > list2.val:
                output.next = list2
                output = output.next
                list2 = list2.next
            else:
                output.next = list1
                output = output.next
                list1 = list1.next
        
        if list1 != None:
            output.next = list1
        
        if list2 != None:
            output.next = list2
        
        return outputNode.next
      



# -------------------------------------------------






# https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        i = 0
        curr = self.left.next
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr and curr != self.right and i == index:
            return curr.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        node, prevNode, nextNode = ListNode(val), self.left, self.left.next
        
        prevNode.next = node
        nextNode.prev = node

        node.prev = prevNode
        node.next = nextNode


    def addAtTail(self, val: int) -> None:
        node, prevNode, nextNode = ListNode(val), self.right.prev, self.right
        
        prevNode.next = node
        nextNode.prev = node

        node.prev = prevNode
        node.next = nextNode

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        curr = self.left.next
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr and i == index:
            node, prevNode, nextNode = ListNode(val), curr.prev, curr
            prevNode.next = node
            nextNode.prev = node
            node.prev = prevNode
            node.next = nextNode


    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.left.next
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr and curr != self.right and i == index:
            prevNode, nextNode = curr.prev, curr.next
            prevNode.next = nextNode
            nextNode.prev = prevNode


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)




# -------------------------------------------------






# https://leetcode.com/problems/design-browser-history

class Page:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Page(homepage)

    def visit(self, url: str) -> None:
        page = Page(url)
        page.prev = self.curr
        self.curr.next = page
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        # while steps is not 0 and history contains previous page
        while (steps and self.curr.prev):
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        # while steps is not 0 and history contains next page
        while (steps and self.curr.next):
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)