import os
import pandas as pd
from WineQuality import logger
from WineQuality.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def Validiate_columns(self) -> bool:
        try:
            validation_status = None
            df = pd.read_csv(self.config.unzip_data_dir)
            cols = list(df.columns)
            #print(self.config.all_schema)
            all_schema = list(self.config.all_schema.keys())
            print(all_schema)
            print(cols)
            for col in cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    
            print(validation_status)
            return validation_status
        except Exception as e:
            raise e
                