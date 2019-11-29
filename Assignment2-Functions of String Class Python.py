#!/usr/bin/env python
# coding: utf-8

# In[3]:


#CAPITALIZED STRING()

string = "i love Pakistan"
capitalized_string = string.capitalize()
print("Written String: ",string)
print("Capitalized String: ",capitalized_string)


# In[8]:


#EXPAND TABS()
#Without Arguments passing

str = 'i\tlove\tPakistan'
result = str.expandtabs()
print(result)


# In[10]:


#EXPAND TABS()
#With Arguments passing

str = 'i\tlove\tPakistan'
print('Print Original String:', str)

#tabsize 2
print('Tabsize 2: ', str.expandtabs(2))

#tabsize 4
print('Tabsize 4: ', str.expandtabs(4))


# In[11]:


#Encode to Default utf-8 Encoding

#Unicode String
string = 'python!'
print('String Is: ', string)

#Default Encoding to utf-8
string_utf = string.encode()
print('Encoded String Is: ', string_utf)


# In[13]:


#LowerCase String

string = "PAKISTAN"
print(string.lower())


# In[14]:


#UpperCase String

string = "pakistan"
print(string.upper())


# In[17]:


#Reversed of String

#String
Simple_String = "PAKISTAN"
print(list(reversed(Simple_String)))

#Tuple String
Tuple_String = ('P','A','K','I','S','T','A','N')
print(list(reversed(Tuple_String)))

#Range String
String_Range = (2,10)
print(list(reversed(String_Range)))

#List string
String_List = [0,1,2,3,4,5,6,7]
print(list(reversed(String_List)))


# In[18]:


#String Lenght

Name = "Pakistan"
print(len(Name))


# In[21]:


x = " P a k i s t a n "
x * 3


# In[22]:


#Predefined Strings

Name = "Qais_Abbas"
dir(Name)

