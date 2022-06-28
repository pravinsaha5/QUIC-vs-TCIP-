import pandas as pd
import matplotlib.pyplot as plt


cloud_quic=pd.read_csv('cloudflare_5mb_h3_cwnd.csv')
facebook_quic=pd.read_csv('facebook_5mb_h3_cwnd.csv')
google_quic=pd.read_csv('google_5mb_h3_cwnd.csv')


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