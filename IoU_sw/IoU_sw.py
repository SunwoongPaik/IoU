import tensorflow as tf
import numpy as np

from matplotlib import pyplot as plt


# Mean IoU
for i in range(10):
  globals()['IoU_num_{}'.format(i)] = []
  for j in range(tf.shape(list_1)[0]):
    if j <= 1:
      globals()['n_{}'.format(j)] = np.array((globals()['GT_250_{}'.format(i+1)] * globals()['list_{}'.format(i+1)][j])).sum()
      globals()['u_{}'.format(j)] = np.array(np.around(((globals()['GT_250_{}'.format(i+1)] + globals()['list_{}'.format(i+1)][j])/2)+0.1)).sum()
    
      globals()['N_{}'.format(j)] = (489*489) - globals()['u_{}'.format(j)]
      globals()['U_{}'.format(j)] = (489*489) - globals()['n_{}'.format(j)]
    
    else :  
      globals()['n_{}'.format(j)] = np.array((globals()['GT_246_{}'.format(i+1)] * globals()['list_{}'.format(i+1)][j])).sum()
      globals()['u_{}'.format(j)] = np.array(np.around(((globals()['GT_246_{}'.format(i+1)] + globals()['list_{}'.format(i+1)][j])/2)+0.1)).sum()
    
      globals()['N_{}'.format(j)] = (489*489) - globals()['u_{}'.format(j)]
      globals()['U_{}'.format(j)] = (489*489) - globals()['n_{}'.format(j)]


    globals()['IoU_1_{}'.format(j)] = (globals()['n_{}'.format(j)]/globals()['u_{}'.format(j)])*100
    globals()['IoU_0_{}'.format(j)] = (globals()['N_{}'.format(j)]/globals()['U_{}'.format(j)])*100

    globals()['IoU_{}'.format(j)] = round((globals()['IoU_1_{}'.format(j)] + globals()['IoU_0_{}'.format(j)])/2,2)
    globals()['IoU_num_{}'.format(i)].append(globals()['IoU_{}'.format(j)])
    #print('IoU_',i+1,j+1)
    #print(globals()['IoU_{}'.format(j)])
    j = j+1
  i = i+1

  # Evaluation - meaniou
a = []
sum_=[]
for j in range(4):
  globals()['MeanIoU_sum_{}'.format(j)] = []
  for i in range(10):
    a.append(globals()['IoU_num_{}'.format(i)][j])
    i = i+1
  sum_.append(np.array(a).sum()/10) 
  globals()['MeanIoU_sum_{}'.format(j)].append(sum_)
  a = []
  sum_ = []
  j = j+1


  #Mean Acc
for i in range(10):
  globals()['MeanAcc_num_{}'.format(i)] = []

  globals()['GT_sum_250_{}'.format(i+1)] = globals()['GT_250_{}'.format(i+1)].sum()
  globals()['GT_sum_246_{}'.format(i+1)] = globals()['GT_246_{}'.format(i+1)].sum()

  globals()['GT_Nonsum_250_{}'.format(i+1)] =  (489*489) - globals()['GT_sum_250_{}'.format(i+1)]
  globals()['GT_Nonsum_246_{}'.format(i+1)] =  (489*489) - globals()['GT_sum_246_{}'.format(i+1)]

  for j in range(tf.shape(list_1)[0]):
    if j <= 1:
      globals()['n_{}'.format(j)] = np.array((globals()['GT_250_{}'.format(i+1)] * globals()['list_{}'.format(i+1)][j])).sum()
      globals()['u_{}'.format(j)] = np.array(np.around(((globals()['GT_250_{}'.format(i+1)] + globals()['list_{}'.format(i+1)][j])/2)+0.1)).sum()
    
      globals()['N_{}'.format(j)] = (489*489) - globals()['u_{}'.format(j)]
      globals()['U_{}'.format(j)] = (489*489) - globals()['n_{}'.format(j)]

      globals()['Acc_250_1_{}'.format(j)] = (globals()['n_{}'.format(j)]/globals()['GT_sum_250_{}'.format(i+1)]) *100
      globals()['Acc_250_0_{}'.format(j)] = (globals()['N_{}'.format(j)]/globals()['GT_Nonsum_250_{}'.format(i+1)]) *100

      globals()['MeanAcc_{}'.format(j)]  = round((globals()['Acc_250_1_{}'.format(j)] + globals()['Acc_250_0_{}'.format(j)])/2,2)
    
    else :  
      globals()['n_{}'.format(j)] = np.array((globals()['GT_246_{}'.format(i+1)] * globals()['list_{}'.format(i+1)][j])).sum()
      globals()['u_{}'.format(j)] = np.array(np.around(((globals()['GT_246_{}'.format(i+1)] + globals()['list_{}'.format(i+1)][j])/2)+0.1)).sum()
    
      globals()['N_{}'.format(j)] = (489*489) - globals()['u_{}'.format(j)]
      globals()['U_{}'.format(j)] = (489*489) - globals()['n_{}'.format(j)]

      globals()['Acc_246_0_{}'.format(j)] = (globals()['N_{}'.format(j)]/globals()['GT_Nonsum_246_{}'.format(i+1)]) *100
      globals()['Acc_246_1_{}'.format(j)] = (globals()['n_{}'.format(j)]/globals()['GT_sum_246_{}'.format(i+1)]) *100

      globals()['MeanAcc_{}'.format(j)]  = round((globals()['Acc_246_1_{}'.format(j)] + globals()['Acc_246_0_{}'.format(j)])/2,2)

    globals()['MeanAcc_num_{}'.format(i)].append(globals()['MeanAcc_{}'.format(j)])
  
    j=j+1
  i = i+1

  # Evaluation -meanacc
a = []
sum_=[]
for j in range(4):
  globals()['MeanAcc_sum_{}'.format(j)] = []
  for i in range(10):
    a.append(globals()['MeanAcc_num_{}'.format(i)][j])
    i = i+1
  sum_.append(np.array(a).sum()/10) 
  globals()['MeanAcc_sum_{}'.format(j)].append(sum_)
  a = []
  sum_ = []
  j = j+1


  # Pix ACC
for i in range(10):
  globals()['PixAcc_num_{}'.format(i)] = []
  for j in range(tf.shape(list_1)[0]):
    if j <= 1:
      globals()['n_{}'.format(j)] = np.array((globals()['GT_250_{}'.format(i+1)] * globals()['list_{}'.format(i+1)][j])).sum()
      globals()['u_{}'.format(j)] = np.array(np.around(((globals()['GT_250_{}'.format(i+1)] + globals()['list_{}'.format(i+1)][j])/2)+0.1)).sum()
    
      globals()['N_{}'.format(j)] = (489*489) - globals()['u_{}'.format(j)]
      globals()['U_{}'.format(j)] = (489*489) - globals()['n_{}'.format(j)]

      globals()['PixAcc_{}'.format(j)] = round((globals()['n_{}'.format(j)] + globals()['N_{}'.format(j)])/(489*489)*100,2)
    else :  
      globals()['n_{}'.format(j)] = np.array((globals()['GT_246_{}'.format(i+1)] * globals()['list_{}'.format(i+1)][j])).sum()
      globals()['u_{}'.format(j)] = np.array(np.around(((globals()['GT_246_{}'.format(i+1)] + globals()['list_{}'.format(i+1)][j])/2)+0.1)).sum()
    
      globals()['N_{}'.format(j)] = (489*489) - globals()['u_{}'.format(j)]
      globals()['U_{}'.format(j)] = (489*489) - globals()['n_{}'.format(j)]
      
      globals()['PixAcc_{}'.format(j)] = round((globals()['n_{}'.format(j)] + globals()['N_{}'.format(j)])/(489*489)*100,2)

    globals()['PixAcc_num_{}'.format(i)].append(globals()['PixAcc_{}'.format(j)])
    j = j+1
  i = i+1

  # Evaluation - Pix ACC

for i in range(tf.shape(list_)[0]):
  PixAcc_1 = (globals()['n_{}'.format(list_[i])])*100
  PixAcc_0 = (globals()['N_{}'.format(list_[i])])*100
  
  globals()['PixAcc_{}'.format(list_[i])] = round((PixAcc_1 + PixAcc_0)/(489*489),2)

  print(globals()['PixAcc_{}'.format(list_[i])])
  print('\n')