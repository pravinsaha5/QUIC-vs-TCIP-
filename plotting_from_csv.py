import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.pyplot import figure
import numpy as np



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







