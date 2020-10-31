class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        #print("val: {} next: {}".format(self.val, self.next))
        return "ListNode{val: " + str(self.val) + ", next: " + str(self.next) + "}"

# 1. Recursive implementation
def reverse(origl, reversl=None):
    if origl == None:
        return reversl
    if reversl == None:
        return reverse(origl.next, ListNode(origl.val))

    temp = ListNode(origl.val)
    temp.next = reversl
    return reverse(origl.next, temp)

# 2. Without recursion, traverse full list
def reverseList(head):

    top = None

    while head != None:
        temp = ListNode(head.val)
        temp.next = top
        top = temp
        head = head.next

    return top

a = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
print("List: ", a)
print(reverse(a))

