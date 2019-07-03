# CornerNet-Squeeze

## Setup
1. First things first, you should install the CornerNet-Lite according to the official installation.
The Readme in the CornerNet subdirectory has all of that relevant information. 
Anaconda is not required but makes the setup process much easier. 

2. Place the DAC dataset (95 classes) into data/dac/images.

## Seeing Results
1. If the model hasn't been trained, then the provided bash scripts will allow for training and validation.
If the model has been pretrained, then follow the instructions below on how to place the pretrained model's pkl file.

2. Using python test\_iou.py, you can get the evaluation of IoU on the validation. 
It will give the average IoU of the validation set.

## Pretrained model usage
1. Download the data partition and the trained model by the link I give you.

2. mv the dac folder into the data folder and mkdir images folder into the dac. Then put the DAC dataset (95 classes) into the images.

3. mv the CornerNet\_Squeeze\_310000.pkl into the cache/nnet/CornerNet\_Squeeze

4. If you don't find the cache/nnet/CornerNet\_Squeeze folder, you can mkdir it into the CornerNet-Lite-master folder.

