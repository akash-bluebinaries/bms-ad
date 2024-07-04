from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


if __name__=="__main__":

    logging.info('*** ENTERING DATA_INGESTION MODULE ***')
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()


    logging.info('*** ENTERING DATA_TRANSFORMATION MODULE ***')
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)


    logging.info('*** ENTERING MODEL_TRAINER MODULE ***')
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))