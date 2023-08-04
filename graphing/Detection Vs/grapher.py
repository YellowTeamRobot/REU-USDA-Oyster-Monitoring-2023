import matplotlib.pyplot as plt
import matplotlib as mpl

NUM_VERSIONS = 5

fileNames = ["resultsV{}.csv".format(x) for x in range(1,NUM_VERSIONS+1)]

files = []

valBoxLosses = []
map50s = []
map5095s = []

for x in fileNames:
    with open(x, "r") as file:
        files.append(file.readlines())
    files[-1] = [line.replace(" ", "") for line in files[-1]]
    
    valBoxLosses.append([])
    for line in files[-1]: #Box Loss
        if line.split(",")[8] != "val/box_loss":
            valBoxLosses[-1].append(float(line.split(",")[8]))

    map50s.append([])
    for line in files[-1]: #mAP50
        if line.split(",")[6] != "metrics/mAP50(B)":
            map50s[-1].append(float(line.split(",")[6]))

    map5095s.append([])
    for line in files[-1]: #mAP50-95
        if line.split(",")[7] != "metrics/mAP50-95(B)":
            map5095s[-1].append(float(line.split(",")[7]))

print(valBoxLosses[0])

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=NUM_VERSIONS, sharex="col", sharey="row")

cmap = mpl.cm.get_cmap('winter')

colors = [cmap(x/NUM_VERSIONS) for x in range(NUM_VERSIONS)]

for x in range(NUM_VERSIONS):
    c = colors[x]
    ax1[x].plot(valBoxLosses[x], color=c)
    ax2[x].plot(map50s[x], color=c)
    ax3[x].plot(map5095s[x], color=c)
    ax3[x].set(xlabel="Epoch")

ax1[0].set(ylabel="Validation Box Loss")
ax2[0].set(ylabel="mAP50")
ax3[0].set(ylabel="mAP50-95")

ax1[0].set_title("DetectionV1\nNoise, Rotation,\n Shear")
ax1[1].set_title("DetectionV2\nExposure, Blur,\n Cutout")
ax1[2].set_title("DetectionV3\nCutout, Rotation,\n Shear")
ax1[3].set_title("DetectionV4\nNone (+UIEB)\n ")
ax1[4].set_title("DetectionV5\nNone (+UIEB,\n <5% unannotated)")
#ax1[5].set_title("DetectionV6\nNoise, Rotation,\n Shear")

plt.show()