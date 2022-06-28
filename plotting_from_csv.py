

import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.pyplot import figure
import numpy as np





content =pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\Wprofx CSV data\\Wprofx CSV data\\cloudflare_h2_wprofx.csv')


content1= pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\Wprofx CSV data\\Wprofx CSV data\\cloudflare_h3_wprofx.csv')





endtime=content['endTime']
starttime=content['startTime']
delay=endtime-starttime
xaxis=[]
for i in range(len(delay)):
    xaxis.append(i)
 


f = plt.figure()
f.set_figwidth(10)
f.set_figheight(5)
plt.plot(xaxis,delay,label="delay using TCP")



endtime1=content1['endTime']
starttime1=content1['startTime']
delay1=endtime1-starttime1
xaxis1=[]
for i in range(len(delay1)):
    xaxis1.append(i)
    
plt.xticks([0,5,10,15,20,25,30,35,40,45,50,55])
plt.plot(xaxis1,delay1,label="delay using QUIC")

plt.title('CloudFare Hit-latency')
plt.legend()
plt.xlabel('nth time Hit')
plt.ylabel('Delay in ms')



plt.show()





content =pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\Wprofx CSV data\\Wprofx CSV data\\facebook_h2_wprofx.csv')

content1= pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\Wprofx CSV data\\Wprofx CSV data\\facebook_h3_wprofx.csv')





endtime=content['endTime']
starttime=content['startTime']
delay=endtime-starttime
xaxis=[]
for i in range(len(delay)):
    xaxis.append(i)
 


f = plt.figure()
f.set_figwidth(10)
f.set_figheight(5)
plt.plot(xaxis,delay,label="delay using TCP")



endtime1=content1['endTime']
starttime1=content1['startTime']
delay1=endtime1-starttime1
xaxis1=[]
for i in range(len(delay1)):
    xaxis1.append(i)
    
plt.xticks([0,5,10,15,20,25,30,35,40,45,50,55])
plt.plot(xaxis1,delay1,label="delay using QUIC")

plt.title('Facebook Hit-latency')
plt.legend()
plt.xlabel('nth time Hit')
plt.ylabel('Delay in ms')



plt.show()





content =pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\Wprofx CSV data\\Wprofx CSV data\\google_h2_wprofx.csv')

content1= pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\Wprofx CSV data\\Wprofx CSV data\\google_h3_wprofx.csv')





endtime=content['endTime']
starttime=content['startTime']
delay=endtime-starttime
xaxis=[]
for i in range(len(delay)):
    xaxis.append(i)
 


f = plt.figure()
f.set_figwidth(10)
f.set_figheight(5)
plt.plot(xaxis,delay,label="delay using TCP")



endtime1=content1['endTime']
starttime1=content1['startTime']
delay1=endtime1-starttime1
xaxis1=[]
for i in range(len(delay1)):
    xaxis1.append(i)
    
plt.xticks([0,5,10,15,20,25,30,35,40,45,50,55])
plt.plot(xaxis1,delay1,label="delay using QUIC")

plt.title('Google Hit-latency')
plt.legend()
plt.xlabel('nth time Hit')
plt.ylabel('Delay in ms')



plt.show()





cloud_quic=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\cwnd CSV data\\5MB\\cloudflare_5mb_h3_cwnd.csv')
facebook_quic=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\cwnd CSV data\\5MB\\facebook_5mb_h3_cwnd.csv')
google_quic=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\cwnd CSV data\\5MB\\google_5mb_h3_cwnd.csv')





yaxis_cloud=cloud_quic['init_cwnd_mss']
yaxis_facebook=facebook_quic['init_cwnd_mss']
yaxis_google=google_quic['init_cwnd_mss']
xaxis=[]
for i in range(len(yaxis_cloud)):
    xaxis.append(i)
    

f = plt.figure()
f.set_figwidth(10)
f.set_figheight(7)
plt.plot(xaxis,yaxis_cloud,label="congestion-window for Cloud-fare connection",marker='.')
plt.plot(xaxis,yaxis_facebook,label="congestion-window for Facebook connection",marker='.')
plt.plot(xaxis,yaxis_google,label="congestion-window for google connection",marker='.')
plt.ylabel('window MSS')
plt.xlabel('Transmission rounds')
plt.title('5Mb website')
plt.legend()
plt.yscale('log')
plt.show()


# In[30]:


cloud_quic=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\cwnd CSV data\\100 KB\\cloudflare_h3_cwnd.csv')
facebook_quic=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\cwnd CSV data\\100 KB\\facebook_h3_cwnd.csv')
google_quic=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\cwnd CSV data\\100 KB\\google_h3_cwnd.csv')


# In[33]:


yaxis_cloud=cloud_quic['init_cwnd_mss']
yaxis_google=google_quic['init_cwnd_mss']
xaxis=[]
for i in range(len(yaxis_cloud)):
    xaxis.append(i)
    

f = plt.figure()
f.set_figwidth(10)
f.set_figheight(7)
plt.plot(xaxis,yaxis_cloud,label="congestion-window for Cloud-fare connection",marker='.')
plt.ylabel('window MSS')
plt.xlabel('Transmission rounds')
plt.title('100KB website')
plt.legend()
plt.yscale('log')
plt.show()





yaxis_facebook=facebook_quic['init_cwnd_mss']
xaxis=[]
for i in range(len(yaxis_facebook)):
    xaxis.append(i)
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(7)
plt.plot(xaxis,yaxis_facebook,label="congestion-window for Facebook connection",marker='.')
plt.ylabel('window MSS')
plt.xlabel('Transmission rounds')
plt.title('100KB website')
plt.legend()
plt.yscale('log')
plt.show()





yaxis_google=google_quic['init_cwnd_mss']
xaxis=[]
for i in range(len(yaxis_google)):
    xaxis.append(i)
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(7)
plt.plot(xaxis,yaxis_google,label="congestion-window for Google connection",marker='.')
plt.ylabel('window MSS')
plt.xlabel('Transmission rounds')
plt.title('100KB website')
plt.legend()
plt.yscale('log')
plt.show()





quic_data=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\processed\\quic_data.csv')
tcp_data=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\QUIC_GRAPHS\\processed\\tcp_data.csv')
tcp_data.head()




initial_time=quic_data['In_time']
final_time=quic_data['Fi_time']
x_axis=(final_time-initial_time)*1000000
y_axis_quic=quic_data['avg b/w']*8/10000
y_axis_tcp=tcp_data['avg b/w']/100000


f = plt.figure()
f.set_figwidth(10)
f.set_figheight(7)
plt.xlabel('Time in seconds')
plt.ylabel('Throughput (Mbps)')
plt.plot(x_axis,y_axis_tcp,label="TCP",marker='x')
plt.plot(x_axis,y_axis_quic,label="QUIC",marker='.')
plt.legend()
plt.title('Throughput comparison: Bandwidth 100 Mbps')
plt.show()





x_axis=[100]

y_axis_tcp=tcp_data['Overhead']/1000000
y_axis_quic=quic_data['Overhead']/1000000
sum_tcp=0
sum_quic=0
for i in y_axis_tcp:
    sum_tcp+=i
sum_tcp=-1*sum_tcp    
avg_tcp=sum_tcp/len(y_axis_tcp)

for i in y_axis_quic:
    sum_quic+=i
sum_quic=-1*sum_quic
avg_quic=sum_quic/len(y_axis_quic)



f = plt.figure()
f.set_figwidth(10)
f.set_figheight(7)


plt.plot(x_axis,avg_quic,'o',label='QUIC')
plt.plot(x_axis,avg_tcp,'o',label='TCP')
plt.legend()
plt.xlabel('Bandwidth (Mbps)')
plt.ylabel('Throughput (Mbps)')
plt.title('Throughput vs Bandwidth comparison')

plt.show()







