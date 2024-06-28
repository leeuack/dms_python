#!/usr/bin/env python
# coding: utf-8

# In[1]:


def distance(pt0, pt1):
    '''pt0 and pt1 means points and are represented by [x,y]'''
    dist = ((pt1[0]-pt0[0])**2 + (pt1[1]-pt0[1])**2)**0.5
    return dist


# In[2]:


def circleArea(circle):
    '''circle is represented by (x,y,r)'''
    area = circle[-1]**2*3.141592
    return area

