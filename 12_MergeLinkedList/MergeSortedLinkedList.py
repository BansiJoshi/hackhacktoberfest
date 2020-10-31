class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        #print("val: {} next: {}".format(self.val, self.next))
        return "ListNode{val: " + str(self.val) + ", next: " + str(self.next) + "}"

def mergeTwoLists(l1, l2):
    """
    Traverse each list
    keep track of value
    
    check whose first value is less initialize ind to it
    if next value in other list is greater than current value
    then push current value to result and increase ind on same list
    
    if next value in other list is less than current value in current list
    then push value of other list to result and increase ind on other list
    
    i -> l1
    j -> l2
    """
    i = l1
    j = l2
    result = None
    last = None
    
    while j and i:
        if i.val < j.val:
            val = i.val
            i = i.next
        else:
            val = j.val
            j = j.next

        if result == None:
            result = ListNode(val)
            last = result
        else:
            last.next = ListNode(val)
            last = last.next if last.next != None else last
    
    while j != None:
        if last != None:
            last.next = ListNode(j.val)
            last = last.next
        else:
            result = ListNode(j.val)
            last = result
        j = j.next

    while i != None:
        if last != None:
            last.next = ListNode(i.val)
            last = last.next
        else:
            result = ListNode(i.val)
            last = result
        i = i.next
    
    return result

a = ListNode(3,ListNode(5,ListNode(6)))
b = ListNode(4, ListNode(5,ListNode(19)))

print(a,b)
print(mergeTwoLists(a,b))


