from WineQuality.components.model_evaluation import ModelEvaluation
from WineQuality.config.configuration import ConfigurationManager
from WineQuality import logger

stage_05 = "Model Evaluation Satge"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> {stage_05} started >>>>>>>>")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> {stage_05} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e