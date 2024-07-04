import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info('Reading data as dataframe')
            df=pd.read_csv('notebook\data\data.csv')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            logging.info("Saving raw data")

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Initiating split of data into Train & test")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            logging.info("Saving training data in csv to artifacts folder")
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            logging.info("  Saving testing data as csv to artifacts folder")
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("*** Data Ingestion Completed ***")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data,test_data=obj.initiate_data_ingestion()


    # logging.info('2. ENTERING DATA_TRANSFORMATION MODULE')
    # data_transformation=DataTransformation()
    # train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)


    # logging.info('3. ENTERING MODEL_TRAINER MODULE')
    # modeltrainer=ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

