class Solution:
    def __init__(self):
        self.head = None
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Carry=0
        l3 = None
        while l1 or l2:
                if l1 ==None:
                    if l3 == None:
                        if(int(l1.val)+int(l2.val)+Carry)>9:
                            l3=ListNode((int(l2.val)+Carry)%10)
                            Carry=1
                        else:
                            l3=ListNode(int(l2.val)+Carry)
                            Carry=0
                        self.head=l3
                    else:
                        t=self.head
                        while t.next!=None:
                            t=t.next
                        if(int(l2.val)+Carry)>9:
                            t.next=ListNode((int(l2.val)+Carry)%10)
                            Carry=1
                            if(l2.next==None):
                                t.next.next=ListNode(1)
                        else:
                            t.next=ListNode(int(l2.val)+Carry)
                            Carry=0
                elif l2==None:
                    if l3 == None:
                        if(int(l1.val)+int(l2.val)+Carry)>9:
                            l3=ListNode((int(l1.val)+Carry)%10)
                            Carry=1
                        else:
                            l3=ListNode(int(l1.val)+Carry)
                            Carry=0
                        self.head=l3
                    else:
                        t=self.head
                        while t.next!=None:
                            t=t.next
                        if(int(l1.val)+Carry)>9:
                            t.next=ListNode((int(l1.val)+Carry)%10)
                            Carry=1
                            if(l1.next==None):
                                t.next.next=ListNode(1)
                        else:
                            t.next=ListNode(int(l1.val)+Carry)
                            Carry=0
                else:
                    if l3 == None:
                        if(int(l1.val)+int(l2.val)+Carry)>9:
                            l3=ListNode((int(l1.val)+int(l2.val)+Carry)%10)
                            Carry=1
                            if(l1.next==None and l2.next==None):
                                l3.next=ListNode(1)
                        else:
                            l3=ListNode(int(l1.val)+int(l2.val)+Carry)
                            Carry=0
                        self.head=l3
                    else:
                        t=self.head
                        while t.next!=None:
                            t=t.next
                        if(int(l1.val)+int(l2.val)+Carry)>9:
                            t.next=ListNode((int(l1.val)+int(l2.val)+Carry)%10)
                            Carry=1
                            if(l1.next==None and l2.next==None):
                                t.next.next=ListNode(1)
                        else:
                            t.next=ListNode(int(l1.val)+int(l2.val)+Carry)
                            Carry=0
                if l1!=None:
                    l1=l1.next  
                if l2!=None:
                    l2=l2.next
        return l3