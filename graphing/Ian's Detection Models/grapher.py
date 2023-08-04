import matplotlib.pyplot as plt
import pandas as pd

with open("data.csv", "r") as file:
    data = file.read().splitlines()

for x in range(len(data)):
    data[x] = data[x].split(",")

data = list(zip(*data[::-1]))

lineToAppend = []
columns = []

for line in data:
    for item in line:
        lineToAppend.append(float(item))
    columns.append(lineToAppend)
    lineToAppend = []

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=4, sharex="col")

ax1[0].set_title("BoxP")
ax1[1].set_title("R")
ax1[2].set_title("mAP50")
ax1[3].set_title("mAP50-95")

legend = False #This is a stupid workaround

for x in range(len(columns)):
    df = pd.DataFrame([['N', *columns[x][12:15]],
                       ['S', *columns[x][9:12]],
                       ['M', *columns[x][6:9]],
                       ['L', *columns[x][3:6]],
                       ['X', *columns[x][0:3]]],
                       columns=['Model Size', 'Open' if x < 4 else "", 'Closed' if x < 4 else "", 'Oyster' if x < 4 else ""])

    if x <= 3: #160
        df.plot(ax=ax1[x % 4],x='Model Size',kind='barh',stacked=False, legend=False)
    if x <= 7: #320
        df.plot(ax=ax2[x % 4],x='Model Size',kind='barh',stacked=False, legend=False)
    if x <= 11: #640
        df.plot(ax=ax3[x % 4],x='Model Size',kind='barh',stacked=False, legend=False)

ax1[0].set(ylabel="160")
ax2[0].set(ylabel="320")
ax3[0].set(ylabel="640")

plt.legend(bbox_to_anchor=(1.04, 3.5), loc="upper left")
plt.show()
