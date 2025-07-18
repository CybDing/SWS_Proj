BASE_DIR = '/Users/ding/Desktop/NUS-proj/'
DATA_DIR = '/Users/ding/Desktop/NUS-proj/dataV2/'

IMG_SIZE = (224, 224)
CLASS_NUM = 5
HIDDEN_LAYER_PERCEPTRONS = [512]
DROPOUT = 0.32
CUSTOM_LAYERS = 2 + 3 * len(HIDDEN_LAYER_PERCEPTRONS) + 1
CHECKPOINT_INDEX = 3
FROZEN_LAYERS = 10


# TrainingSet test results:
#               precision    recall  f1-score   support

#       Pallas       0.99      0.99      0.99       760
#      Persian       0.90      0.82      0.86      1365
#     Ragdolls       0.78      0.90      0.84      1006
#    Singapura       0.98      0.94      0.96       664
#       Sphynx       0.99      0.98      0.98      1553

#     accuracy                           0.92      5348
#    macro avg       0.93      0.93      0.93      5348
# weighted avg       0.93      0.92      0.92      5348


# 训练集总体准确率: 0.9213