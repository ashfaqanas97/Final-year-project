import os
import sys

sys.path.append('model')
sys.path.append('preprocess')
DIR  = os.getcwd()

from modelTrain import ModelTrainer

if __name__ == '__main__':
	#sampleData(os.path.join(DIR, 'data' + os.sep + 'database.sqlite'))
	trainer = ModelTrainer()
	trainer.mainTrain()
