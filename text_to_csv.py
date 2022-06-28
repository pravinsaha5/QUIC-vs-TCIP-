import pandas as pd
import glob
# readinag given csv file
# and creating dataframe

folder_path = 'F:\_processed\_processed'
file_list = glob.glob(folder_path + "/*.txt")
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0], delimiter = ' '))

for i in range(1,len(file_list)//2):
    data = pd.read_csv(file_list[i], delimiter = ' ')
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe, df], axis=1)
    #main_dataframe.columns = ['blank', 'overhead', 'initial_time', 'final_time', 'avg_bw']
main_dataframe.to_csv('E:/quic_data.csv')

for i in range(len(file_list)//2, len(file_list)):
    data = pd.read_csv(file_list[i], delimiter = ' ')
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe, df], axis=1)

main_dataframe.to_csv('E:/tcp_data.csv')