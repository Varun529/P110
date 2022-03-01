import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
popluation_stdev=statistics.stdev(data)
print("Population Mean:",population_mean)
print("Population Standard Deviation:",popluation_stdev)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list): 
    df=mean_list 
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()
    
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(30)  
        mean_list.append(set_of_means)
    show_fig(mean_list) 
    
    mean=statistics.mean(mean_list)  
    print("Mean of sampling distribution:",mean)
    
setup()  