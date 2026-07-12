class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class singlyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head
    def printList(self):
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
        print('None')
sll=singlyLinkedList()
sll.append(10)
sll.append(15)
sll.append(20)
sll.append(25)
sll.append(30)
sll.append(13)
sll.append(28)
sll.printList()
print(sll.oddEvenList(sll.head))
sll.printList()
