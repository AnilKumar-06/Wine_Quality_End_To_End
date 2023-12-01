from WineQuality.components.data_transformation import DataTransformation
from WineQuality.config.configuration import ConfigurationManager
from WineQuality import logger
from pathlib import Path

stage_03 = "Data Transformation satage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
            if status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transform = DataTransformation(config=data_transformation_config)
                data_transform.train_test_split()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            print(e)
            
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>{stage_03} started >>>>>>>")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>{stage_03} completed >>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e
                    