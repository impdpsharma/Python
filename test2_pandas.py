import matplotlib.pyplot as pt
import pandas as pd

data=pd.read_csv('RS_Session_248.csv')
#print(data.head())

#print(data['Slum Households'])
#pt.plot(data['Slum Households'],data['Slum Population'],color='orange') # data is huge so there will be a problem displaying data

#take top 20 data
data=data.head(20)

'''print(data['Slum Households'],data['Slum Population'])
pt.plot(data['Slum Households'],data['Slum Population'],color='orange',label="line graph")
pt.scatter(data['Slum Households'],data['Slum Population'],color='blue',label='Scatter')
pt.legend()
pt.xlabel('Slum Households',color='green')
pt.ylabel('Slum Population',color='green')
pt.title('Slum Households Vs Slum Population',color='purple')
pt.show()'''



# Bar graph

'''pt.bar(data['Slum Households'],data['Slum Population'],color='blue',label='Bar')
pt.legend()
pt.xlabel('Slum Households',color='green')
pt.ylabel('Slum Population',color='green')
pt.title('Slum Households Vs Slum Population',color='purple')
pt.show()'''

# Horizontal Bar graph
'''
pt.barh(data['Slum Households'],data['Slum Population'],color='blue',label=' Horizontal Bar')
pt.legend()
pt.xlabel('Slum Households',color='green')
pt.ylabel('Slum Population',color='green')
pt.title('Slum Households Vs Slum Population',color='purple')
pt.show()'''


# Bar graph with different colours

pt.bar(data['Slum Households'],data['Slum Population'],color=['blue','blue','red','green','yellow'],alpha=.7)
# alpha is basically the opacity of the color ranges from 0-1, default value is 1. It indicates the transparancy of the color

pt.legend()
pt.xlabel('Slum Households',color='green')
pt.ylabel('Slum Population',color='green')
pt.title('Slum Households Vs Slum Population',color='purple')
pt.show()


