#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for
for i in range(5):
    print("Hello")


# In[2]:


for i in range(5):
    print(i)


# In[3]:


for i in range(1,6):
    print(i)


# In[4]:


fruits=["Apple","Banana","Mango"]
for fruit in fruits:
    print(fruit)



# In[7]:


#while loop
count=1
while count<=5:
    print(count)
    count+=1



# In[12]:


#break
for i in range(10):
    if i==5:
        break
    print(i)


# In[13]:


#continue
for i in range(5):
    if i==2:
        continue
    print(i)


# In[17]:


#pass
for i in range(5):
   pass 



# In[18]:


#nested loop
for i in range(3):
    for j in range(2):
      print(i,j)


# In[19]:


#Calculate the total sales

sales=[1000,2000,1500,3000]
total=0
for amount in sales:
    total+=amount
print(total)


# In[20]:


count=1
while count <= 5:
    print(count)
    count+=1


# In[22]:


#1
for i in range(1,11):
    print(i)


# In[29]:


#2

for i in range(2, 21,2):
    print(i)




# In[30]:


i = 2

while i <= 20:
    print(i)
    i += 2  


# In[31]:


sum = 0
i = 1

while i <= 100:
    sum += i
    i += 1

print(sum)  


# In[32]:


sum = 0

for i in range(1, 101):
    sum += i

print(sum) 


# In[33]:


# Define a sample list
fruits = ["apple", "banana", "cherry", "date"]


for fruit in fruits:
    print(fruit)


# In[38]:


num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



# In[ ]:




