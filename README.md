# Machine Learning and Computer Vision Techniques to Identify and Monitor *Ostreidae* Nondisruptively


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

## Methods:

### - Dataset
The oyster detection datasets can be found under the datasets directory, two datasets are available, a multi-label with 1 base class and 2 states, and another using 3 state classes. The dataset is modified from prior work during [REU 2022](https://github.com/Zenny00/REU-Oyster_Orientation) which was compiled using 200 initially provided images and 800 images collected from various internet sources. All of the annotation was done using the online annotation tool [Roboflow](https://roboflow.com/). Changes to the original dataset include new images obtained at [Hornpoint Hatchery](https://hatchery.hpl.umces.edu/) being added to the dataset, as well as some relabeling of the original dataset.

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

## Single Label - Segmentation
<img src="./docs/InferenceTestImage9.jpg" width="300"> <img src="./docs/TestImg5.jpg" width="300">

## Single Label - Detection
<img src="./docs/InferenceTestImage1.jpg" width="300"> <img src="./docs/TestImg.jpg" width="300">

## Multi-label - Detection
<img src="./docs/InferenceTestImage4.jpg" width="300"> <img src="./docs/Before1.jpg" width="300">

## Multi-label - Detection
hhh

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
