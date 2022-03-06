#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os

write_to_csv_file = 'million_song_subset.csv'

csv_file_read = open(write_to_csv_file,'r')
csv_file_write = open(write_to_csv_file,'a')


while True:
    next_line = csv_file_read.readline()

    if not next_line:
        break
    
    csv_file_size = os.path.getsize(write_to_csv_file)
    print("file size: {}".format(str(csv_file_size/1048576)))
    
    # if the csv file larger than or euqal to 5GB exist for loop
    if csv_file_size >= 5368709120:
        break
                
    if next_line.startswith("song_id"):
        continue
    
    csv_file_write.write(next_line)
    print("appended: {}".format(next_line))

csv_file_read.close()
csv_file_write.close()


# In[ ]:




