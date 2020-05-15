from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import urllib
import requests
import matplotlib.pyplot as plt


words = 'Docker Ansible Elasticsearch Python Pandas Keras Git Centos Ubuntu Java Windows Linux Server R tidyverse cluster regression classification Associations GitLab Logstash Filebeat Jupyter'
mask = np.array(Image.open(requests.get('https://www.quibiq.de/fileadmin/_processed_/0/a/csm_cloud-3331240_960_720_01_4b9dfbd4c4.png', stream=True).raw))



word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask).generate(words)
plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
plt.imshow(word_cloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
