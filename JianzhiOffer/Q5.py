
class LinkNode:
    def __init__(self):
        self.val = None
        self.nxt = None

def ReversePrintLinkedList(llist):
    if llist is None:
        return
    ReversePrintLinkedList(llist.nxt)
    print llist.val


def build_linkedList(a):
    prev = LinkNode()
    h = prev
    for e in a:
        cur = LinkNode()
        cur.val = e
        prev.nxt = cur
        prev = cur
    return h.nxt


ll = build_linkedList([1,2,3,4,5,6])
ReversePrintLinkedList(ll)
