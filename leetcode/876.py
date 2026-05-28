head = 0
ahead = head
while ahead and ahead.next:
     ahead += ahead.next.next
     head = head.next 

print(head)