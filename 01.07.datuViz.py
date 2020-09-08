#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


from pandas import ExcelWriter
from pandas import ExcelFile


# In[4]:


exceldata = pd.read_excel('C:/Users/Katja/Downloads/IDG010.xlsx')


# In[5]:


exceldata


# # Dzimušo skaita Latvijā (2010.g.-2019.g.) interaktīva vizualizācija

# In[19]:


# Import the necessaries libraries
import plotly.offline as pyo
import plotly.graph_objs as go
# Set notebook mode to work in offline
pyo.init_notebook_mode()

data = [go.Bar(x=exceldata.Gads,
            y=exceldata.Dzimusie)]

pyo.iplot(data, filename='jupyter-basic_bar')


# # Mirušo skaita Latvijā (2010.g.-2019.g.) interaktīva vizualizācija

# In[21]:


# Import the necessaries libraries
import plotly.offline as pyo
import plotly.graph_objs as go
# Set notebook mode to work in offline
pyo.init_notebook_mode()

data = [go.Bar(x=exceldata.Gads,
            y=exceldata.Mirusie)]

pyo.iplot(data, filename='jupyter-basic_bar')


# # Mirušo un dzimušo skaita atspoguļojums

# In[6]:


# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# Data
df=pd.DataFrame({'Dzimušie': exceldata.Dzimusie, 'Mirušie': exceldata.Mirusie})
 
# multiple line plot
plt.plot( 'Dzimušie', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'Mirušie', data=df, marker='', color='black', linewidth=4)


# # Vizualizācijas piemērs - slikts piemērs

# In[32]:


# library
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
# Your x and y axis
x=exceldata.Gads
y=exceldata.Dzimusie
z=exceldata.Mirusie
 
# use a known color palette (see..)
pal = sns.color_palette("Set1")
plt.stackplot(x,y,z, labels=['Dzimusie','Mirusie'], colors=pal, alpha=0.4 )
plt.legend(loc='upper right')
plt.show()
 
# create your palette
pal = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71"]
plt.stackplot(x,y,z, labels=['Dzimusie','Mirusie'], colors=pal, alpha=0.4 )
plt.legend(loc='upper right')


# # Vizualizācijas piemērs, lai atspoguļotu starpību starp dzimušajiem un mirušajiem

# In[40]:


# library
import numpy as np
import matplotlib.pyplot as plt
 
# create data
x=exceldata.Gads
y=exceldata.Dzimusie
z=exceldata.Mirusie
 
# Change the color and its transparency
plt.fill_between( x, y, z, color="skyblue", alpha=0.4)
plt.show()


# # Papildināts vizualizācijas piemērs

# In[42]:


# library
import numpy as np
import matplotlib.pyplot as plt
 
# create data
x=exceldata.Gads
y=exceldata.Dzimusie
z=exceldata.Mirusie
 
# Change the color and its transparency
plt.fill_between( x, y, z, color="skyblue", alpha=0.4)
plt.title("Starpības atspoguļojums", loc="left")
plt.xlabel("Gads")
plt.ylabel("Starpība")
plt.show()


# # Dzimušie (Bubble Chart)

# In[85]:


import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=exceldata.Gads, 
    y=exceldata.Dzimusie,
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)',
              'rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)',
              'rgb(93, 164, 214)', 'rgb(255, 144, 14)'],
        opacity=[1, 1, 1, 1, 1, 1, 1,1,1,1],
        size=[20, 10, 25, 30, 40, 45, 65, 40, 15, 10],
    )
)])

fig.show()


# In[89]:


import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=exceldata.Gads, 
    y=exceldata.Mirusie,
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)',
              'rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)',
              'rgb(93, 164, 214)', 'rgb(255, 144, 14)'],
        opacity=[1, 1, 1, 1, 1, 1, 1,1,1,1],
        size=[70, 35, 45, 40, 35, 35, 40, 45, 50, 15],
    )
)])

fig.show()


# # Bubble Chart with Colorscale

# In[102]:


import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=exceldata.Gads,
    y=exceldata.Dzimusie,
    mode='markers',
    marker=dict(
        color=[150, 165, 160, 140, 125, 120, 120, 135, 155, 165],
        size=[15, 30, 55, 70, 75, 80, 100, 65, 35, 15],
        showscale=False
        )
)])

fig.show()


# In[110]:


import matplotlib.pyplot as plt
import pandas as pd
exceldata = pd.read_excel('C:/Users/Katja/Downloads/IDG010.xlsx')

x = exceldata.Dzimusie
y = exceldata.Mirusie
gads = exceldata.Gads
plt.scatter(gads, x, label='Dzimušo skaits', color='r')
plt.scatter(gads, y, label='Mirušo skaits', color='g')
plt.title('Scatter Plot')
plt.xlabel('Gads')
plt.ylabel('Skaits')
plt.legend()
plt.show()


# In[ ]:




