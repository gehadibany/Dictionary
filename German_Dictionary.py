#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast
file_reader = open( 'german_dictionary.txt', 'r' )
german_dic  = ast.literal_eval( file_reader.read( ) )
dcontntinue = 'y'
while dcontntinue == 'y':
    x = input('Enter the word in German:')
    check =x in german_dic
    if check == True:
        print ('The meaning is', german_dic[x])
        
    else:
        german_dic[x] = input("Not found. Enter the word in English to be added:")
        print ('Sucessfully added!')
    
    dcontntinue = input('Do you want to continue? y/n')

file_writer = open( 'german_dictionary.txt', 'w+' )
file_writer.write(str(german_dic))
file_writer.close()
print ('Thank you! Come again later!')


# In[ ]:




