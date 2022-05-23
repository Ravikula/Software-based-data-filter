import pandas as pd 
from matplotlib import pyplot as plt

data_set = (r"..\sensor_data.csv") 
data = pd.read_csv(data_set)

x_original = list(data["x"])
y_original= list(data["y"])

window_size = [80,120,200,300]

plt.plot(x_original,y_original,label="Original")

for i in range(len(window_size)):
  x_avg=[]
  y_avg=[]
  for j in range(len(y_original)-window_size[i]): 
    avg = sum(y_original[j:j+window_size[i]])/window_size[i]
    y_avg.append(avg)
    
    x_val = sum(x_original[j:j+window_size[i]])/window_size[i]
    x_avg.append(x_val)
 plt.plot(x_avg,y_avg,label=str(window_size[i]))

plt.title("Filtered Signal with Different Window Sizes") 
plt.xlabel("Time(s)") #define labels
plt.ylabel("Encorder Position (rad)")
plt.legend(loc="upper right")

plt.show()
