import os
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
from pathlib import Path
from WineQuality.utils.common import save_json
import joblib
from WineQuality.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    
    def eval_metrics(self, actual, pred):
        
        rmse = np.sqrt(mean_absolute_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        x_test = test_data.drop([self.config.target_column], axis = 1)
        y_test = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_artifact_uri()).scheme
        
        with mlflow.start_run(nested=True):
            predicted_val = model.predict(x_test)
            (rmse, mae,r2) = self.eval_metrics(y_test, predicted_val)
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            
            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
                
            else:
                mlflow.sklearn.log_model(model, "model")
            
        