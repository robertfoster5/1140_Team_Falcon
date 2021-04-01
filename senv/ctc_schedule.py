from ctc_train import ctc_train
import csv

class ctc_schedule:
    train_set = []
 
 # Update        
    
test_ctc_schedule = ctc_schedule
test_ctc_schedule.train_set.append(ctc_train('Train 1', 20, 150, 'Block 1', 'Block 2'))
print(test_ctc_schedule.train_set[0].name)
