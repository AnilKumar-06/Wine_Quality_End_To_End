#from WineQuality.components.data_validation import DataValidation
from WineQuality.components.data_validation import DataValidation
from WineQuality.config.configuration import ConfigurationManager
from WineQuality import logger

stage_02 = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.Validiate_columns()
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>{stage_02} started>>>>>>>>\n")
        data_val = DataValidationTrainingPipeline()
        data_val.main()
        logger.info(f"\n>>>>>>> {stage_02} completed >>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e