#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast 
file_reader = open( 'german_dictionary.txt', 'r' )
german_dic  = ast.literal_eval( file_reader.read( ) )

x =''
while x != 'x':
    x = input('Enter a word in German or press x to quit:')
    check =x in german_dic
    if x == 'x':
        break
    elif check == True:
        print ('The meaning is:', german_dic[x])    
    else:
        german_dic[x] = input("Not found. Enter the word in English to be added:")
        print ('Sucessfully added!')
    
file_writer = open( 'german_dictionary.txt', 'w+' )
file_writer.write(str(german_dic))
file_writer.close()
print ('Danke! Tschüss!')



# In[ ]:




