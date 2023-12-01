from WineQuality import logger
from sklearn.linear_model import ElasticNet
import os
import joblib
import pandas as pd
from WineQuality.entity.config_entity import ModelTrainingConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        
    def train(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)
        
        x_train = train_df.drop([self.config.target_column], axis=1)
        x_test = test_df.drop([self.config.target_column], axis=1)
        
        y_train = train_df[[self.config.target_column]]
        y_test = test_df[[self.config.target_column]]
        
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(x_train, y_train)
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))