
# coding: utf-8

# In[108]:


import re
from timeit import default_timer as timer
from datetime import timedelta
start = timer()


# In[109]:


filename="bible_new.txt"
keyword = "evening.*"


# In[110]:


textfile = open(filename, 'r')
filetext = textfile.read()


# In[111]:


end = timer()
print("Time taken to open and read file: ", timedelta(seconds=end-start))
start = timer()


# In[112]:


count = 0
for line in open(filename).readlines(  ): count += 1
    
textfile.close()

print("Number of line in the file: ", count)


# In[113]:


end = timer()
print("Time taken to count lines: ", timedelta(seconds=end-start))
start = timer()


# In[114]:


count=0
for line in re.findall(keyword, filetext):
    count +=1
#    print(line)


# In[115]:


end = timer()
print("Count of Keyword occurrence: ", count)
print("Time taken to search keyword: ", timedelta(seconds=end-start))

