from WineQuality import logger
from WineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQuality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WineQuality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from WineQuality.pipeline.stage_04_model_training_pipeline import ModelTrainerTrainingPipeline
from WineQuality.pipeline.stage_05_model_evaluation_pipeline import ModelEvaluationTrainingPipeline

logger.info("Welcome to our custom logging")

stage_01 = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> {stage_01} started >>>>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> {stage_01} completed >>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


stage_02 = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>{stage_02} started >>>>>>>>>\n")
    data_val = DataValidationTrainingPipeline()
    data_val.main()
    logger.info(f"\n>>>>>>>> {stage_02} completed >>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

stage_03 = "Data Transformation stage"

try:
    logger.info(f">>>>>>>>{stage_03} started >>>>>>>>")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>{stage_03} completed >>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

stage_04 = "Model Trainer stage"

try:
    logger.info(f">>>>>>>> {stage_04} started >>>>>>>>")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> {stage_04} completed >>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

stage_05 = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>> {stage_05} started >>>>>>>>")
    model_eval = ModelEvaluationTrainingPipeline()
    model_eval.main()
    logger.info(f">>>>>>>> {stage_05} completed >>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e