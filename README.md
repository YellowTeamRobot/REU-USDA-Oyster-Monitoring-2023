# Machine Learning and Computer Vision Techniques to Identify and Monitor *Ostreidae* Nondisruptively
<a href="./GettingStarted.md#anaconda"><img src="https://img.shields.io/badge/Run%20with%20Anaconda-h?logo=anaconda&labelColor=grey&color=%2344A833" /></a>
<a target="_blank" href="https://colab.research.google.com/github/YellowTeamRobot/REU-USDA-Oyster-Monitoring-2023/blob/main/OysterMonitoringYolo8-Colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
<a href="./GettingStarted.md"><img src="https://img.shields.io/badge/Getting%20Started%20-%20h?label=Not%20sure%20which%20to%20use%3F&labelColor=grey&color=darkviolet" /></a>

## This research was done at Salisbury University as a joint project between the NSF REU Summer 2023 Program and University of Maryland Eastern Shore USDA Smart Shellfish Farming grant:
- [Salisbury University Website](https://www.salisbury.edu/)
- [NSF REU Salisbury Homepage](http://faculty.salisbury.edu/~ealu/REU/Schedule.html)

## Faculty Mentors:
### - Dr. Yuanwei Jin
### - Dr. Enyue (Annie) Lu

## Research Participants:
### - Ian Rudy
### - Alexander Emmert
### - Alexander Mekovsky

# References & Acknowledgements: 
- [Last Year's Work - REU 2022](https://github.com/Zenny00/REU-Oyster_Orientation)
- [YOLOv8](https://github.com/ultralytics/ultralytics)
- [Detecting and Counting Oysters](https://arxiv.org/abs/2105.09758)
- [Oyster detection system](https://github.com/bsadr/oyster-detection)
- [Original Dataset Roboflow](https://universe.roboflow.com/newoysters/threestateoyster/dataset/34)

## Methods:

### - Dataset
The oyster detection datasets can be found under the datasets directory, two datasets are available, a multi-label with 1 base class and 2 states, and another using 3 state classes. The dataset is modified from prior work during [REU 2022](https://github.com/Zenny00/REU-Oyster_Orientation) which was compiled using 200 initially provided images and 800 images collected from various internet sources, it can be found on [Roboflow](https://universe.roboflow.com/newoysters/threestateoyster/dataset/34). All of the annotation was done using the online annotation tool [Roboflow](https://roboflow.com/). Changes to the original dataset include new images obtained at [Hornpoint Hatchery](https://hatchery.hpl.umces.edu/) being added to the dataset, as well as some relabeling of the original dataset.

The dataset contains images spanning various environments and camera angles to help increase the model's ability to generalize the features that make up an oyster. In the multi-label dataset, the oysters are all classified into a generic "Oyster" class, and for those where it is posible to tell, they are further labelled as either "Open" or "Closed".

The datasets in this repo were exported from Roboflow in Yolov8 format.

### - Training
The training for this research was done using a mix of [Google Colab](https://colab.research.google.com/), as well as local hardware obtained during the project, utilizing a 4080 gpu provided a roughly 10x increase in the training speed compared to the T4's provided by Colab, allowing us to run many more tests than was possible last year. 

### - Evaluation
The models were evaluated using these common metrics [precision](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall), [recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall), [average precision (AP)](https://link.springer.com/referenceworkentry/10.1007/978-0-387-39940-9_482), and [mean average precision (mAP)](https://www.v7labs.com/blog/mean-average-precision#:~:text=Average%20Precision%20is%20calculated%20as,mAP%20varies%20in%20different%20contexts.)

##### Mean Average Precision
<img src="./docs/mAP.jpg" width="400">

In addition to these metrics, the training and validation are evaluated using a [loss function](https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/). A loss function helps show how far the model is from the ground truth value (the correct answer). Graphs of both the training and validation loss can be seen below:

##### Training Loss
<img src="./docs/TrainLoss.jpg" width="400">

##### Validation Loss
<img src="./docs/ValidLoss.jpg" width="400">

### - Classification Problems
Last years work seeked to help improve classification of oysters that were hard to determine the state of by using their orientation. The work this year tried a different method. First, to improve accuracy, the three states of "Open", "Semi-Open", and "Closed" were pared down to "Open" and "Closed" by merging the "Open" and "Semi-Open" classes. Then, for all oysters that were difficult or impossible to determine if they were open or closed, we relabeled them as "Indeterminate". The hope with this was that the model would not be trying to find a pattern in features for oysters that can't reasonably be determined as open or closed, improving it's accuracy. However, using a third indeterminate class did not seem to help this. What did seem to help was instead, using multiple labels, where every oyster was labelled as "Oyster", and those that could have their state determined were also labelled as "Open" or "Closed". This allowed the model to detect the state when possible, and when it couldn't, the generic "Oyster" class would help fill in the gaps, as it always had the highest accuracy. Additionally, in some cases where the features of the "Oyster" class were to generic, sometimes the "Open" or "Closed" class were able to pick up on it, given their more specific features.

# Results

Below are some examples of inference run on various images, as well as some tracking done on video.

## Single-Label - Segmentation



https://github.com/YellowTeamRobot/REU-USDA-Oyster-Monitoring-2023/assets/107053197/42a468e6-3688-4ac4-afd6-89e6bff967b3




## Multi-Label - Segmentation



https://github.com/YellowTeamRobot/REU-USDA-Oyster-Monitoring-2023/assets/118875186/d47ffbb2-709c-4d63-9cf8-79b19f9f5112



## Multi-label - Detection



https://github.com/YellowTeamRobot/REU-USDA-Oyster-Monitoring-2023/assets/118875186/8fa7fd60-5a9d-417e-92f3-b3b6abfe2797




# Getting Started 

For information on running either training or inference using this project please refer to the [Getting Started](./docs/GettingStarted.md) document.

# Authors
```javascript
  Name  : Ian Rudy
  Institution：Susquehanna University
  Contact: rudyi@susqu.edu
  
  Name  : Alexander Emmert
  Institution: University of Maryland, College Park
  Contact: emmert@terpmail.umd.edu

  Name  : Alexander Mekovsky
  Institution: Salisbury University
  Contact: amekovsky1@gulls.salisbury.edu
```
