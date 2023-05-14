#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Author:Nithyasree
#code to perform the operations of python
stack = []           #declare a empty list 
print("select a choice")
n = int(input("1.push\n,2.pop\n3.display\n4.Exit\nEnter: "))
n=0
while(n!=4):
    if(n==1):
        num=int(input("enter the number to be inserted"))
        stack.append(num)
        print("the element is inserted")
    elif(n==2):
        if(stack==[]):
            print("stack is empty")
        else:    
        
            b = stack.pop()
            print("the element popped is ",b)
    elif(n==3):
        print(stack)
        


# In[ ]:




