from WineQuality.config.configuration import ConfigurationManager
from WineQuality import logger
from WineQuality.components.model_trainer import ModelTrainer

stage_04 = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_training_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> {stage_04} started >>>>>>>>")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> {stage_04} completed >>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e