# "Divide linked list in half and connect in the opposite order
# input: a->b->c->d->e->f->g->h->i->null
# output: e->f->g->h->i->a->b->c->d->null"
from common.LinkedList import LinkedList


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
    print(ll)
    index_new_head = len(ll)//2
    position = 0
    for nd in ll:
        if(position < index_new_head):
            ll.add(nd.value)
            position += 1
    
    while(position>0):
        ll.remove_first_node()
        position -= 1
    
    print(ll) 
   
    
    # print(index_new_head)
    # ll.add('g')
    # print(ll)
    # print(len(ll)//2)
    
    # ll.remove_last_node()
    # print(ll)
    # ll.remove_first_node()
    # print(ll)
    # ll.remove_node_at_index(3)
    # print(ll)
    # for i in len 