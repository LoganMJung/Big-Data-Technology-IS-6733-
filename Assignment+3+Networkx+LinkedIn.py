
# coding: utf-8

# # Assignment 3, Due Date 11.13.2017

# In[285]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import warnings
from datetime import datetime
from collections import Counter
get_ipython().run_line_magic('matplotlib', 'inline')


# In[286]:


social = nx.read_gpickle('linkedin.gpickle')


# In[287]:


print(nx.info(social))


# In[288]:


nx.draw_networkx(social,node_color='r', node_size=10, with_labels=False)


# In[289]:


#get the node attributes
social.nodes(data=True)


# # Question 1: Write a program that presents the range of dates (earliest and last dates) during which these relationships were forged? 

# In[290]:


Q1 = social.edges(data=True)

#indexing the 3rd element of the list to strip out the date 
xx = [x[2] for x in social.edges(data="date")]
print("Earliest Date is", max(xx))
print("Latest Date is" ,min(xx))


# # Question 2: Write a program that demonstrates if node 5 and 25 are friends (directly or indirectly)

# In[291]:


#finding the if 5 has any edges 
#if node 5 doesn't have any edges then it's not connected to any nodes 
print("Edges:", nx.edges(social,5))
print("All Neighbors:",list(nx.all_neighbors(social,5)))
print("Neighbors:",list(social.neighbors(5)))
print("Node 5 does not have any friends, directly or indirectly")


# # Question 3: Write a program that lists direct friends of node 4

# In[292]:


# printing the info for node 4 
print(nx.info(social,4))

print("Neighbors V2",list(social.neighbors(4)))

se = nx.edges(social,4)

c = [el[1] for el in se]
c.append(4)

print("Direct Friends of Node 4 :",c)


# # Question 4: Write a program that presents the most popular person

# In[293]:


dc =nx.degree_centrality(social)
#print (dc)
print("The most popular person is Node", max(zip(dc.values(), dc.keys()))[1])

