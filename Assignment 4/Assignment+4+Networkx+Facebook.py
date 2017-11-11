
# coding: utf-8

# ## Assignment 4, Due Date 11.13.2017

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
fb = nx.read_edgelist('facebook.txt',create_using=nx.Graph(),nodetype=int)
print(nx.info(fb))


# In[2]:


plt.figure(figsize=(10,7))
plt.axis('off')
nx.draw_networkx(fb,with_labels=False,node_size=10)


# In[11]:


# The diameter is the maximum eccentricity.
diam = nx.diameter(fb)


# In[13]:


# The periphery is the set of nodes with eccentricity equal to the diameter.
periph = nx.periphery(fb)


# In[15]:


# The center is the set of nodes with eccentricity equal to radius.
center = nx.center(fb)


# In[16]:


# The eccentricity of a node v is the maximum distance from v to all other nodes in G.
eccentricity = nx.eccentricity(fb,567)


# ## Question 1: Present the shortest path from the most popular node to the center node

# In[78]:


mcenter = int(max(center))
dc = nx.degree_centrality(fb)
fbcenmax = max(zip(dc.values(), dc.keys()))[1]

print ("Most Popular:", max(zip(dc.values(), dc.keys()))[1])
print("Center:",mcenter)

path = nx.shortest_path(G,source=fbcenmax,target=mcenter)
print("Shortest Path:",path)


# ## Question 2: Present the nodes connected (1st) to the center node

# In[107]:


cenedges = nx.all_neighbors(fb, mcenter)
xx = list(cenedges)

#cenedges = nx.edges(fb,mcenter)
#xx = [x[1] for x in cenedges]
#print(xx)

print("Nodes Connected to Center Node:",xx)
print("Number of Nodes Connected to Center Node:",len(xx))


# ## Question 3: Present the Eigenvector Centrality 

# In[96]:


ec = nx.eigenvector_centrality(fb)
#print (dc)
print ("Eigenvector Centrality;", max(zip(ec.values(), ec.keys())))


# ## Question 4: Present the closeness centrality

# In[97]:


cc = nx.closeness_centrality(fb)
#print (dc)
print ("Betweenness Centrality;", max(zip(cc.values(), cc.keys())))


# ## Question 5: Present the betweenness centrality

# In[98]:


bc = nx.betweenness_centrality(fb)
#print (dc)
print ("Betweenness Centrality;", max(zip(bc.values(), bc.keys())))

