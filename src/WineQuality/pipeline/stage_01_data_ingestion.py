from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.data_ingestion import DataIngestion
from WineQuality import logger

stage_1 = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> {stage_1} stage started >>>>>>>>")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> {stage_1} stage Completed >>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e