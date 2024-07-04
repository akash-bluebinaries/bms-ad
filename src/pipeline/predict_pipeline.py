import os,sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            print(features)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            if preds[0] >0.5:
                outcome = "Anomaly"
            else:
                outcome= "Not Anomaly"
            return outcome
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self,CellVoltage:float,PackVoltage:float,ChargingCurrent:float,
        DischargeCurrent:float,BatteryTemperature:float,CellTemperature:float,
        AmbientTemp:float,coolingSysTemp:float,stateOfCharge:float,
        stateOfHealth:float,stateOfPower:float,internalResistance:float,
        CycleCount:float,Velocity:float,Elevation:float,Throttle:float,
        MotorTorque:float,LongitudinalAcceleration:float,RegenerativeBrakingSignal:float,
        BatteryVoltage:float,BatteryCurrent:float,SoC:float,
        # Route:str,Weather:str
        ):

        self.CellVoltage = CellVoltage
        self.PackVoltage = PackVoltage
        self.ChargingCurrent = ChargingCurrent
        self.DischargeCurrent = DischargeCurrent
        self.BatteryTemperature = BatteryTemperature
        self.CellTemperature = CellTemperature
        self.AmbientTemp = AmbientTemp
        self.coolingSysTemp = coolingSysTemp
        self.stateOfCharge = stateOfCharge
        self.stateOfHealth = stateOfHealth
        self.stateOfPower = stateOfPower
        self.internalResistance = internalResistance
        self.CycleCount = CycleCount
        self.Velocity = Velocity
        self.Elevation = Elevation
        self.Throttle = Throttle
        self.MotorTorque = MotorTorque
        self.LongitudinalAcceleration = LongitudinalAcceleration
        self.RegenerativeBrakingSignal = RegenerativeBrakingSignal
        self.BatteryVoltage = BatteryVoltage
        self.BatteryCurrent = BatteryCurrent
        self.SoC = SoC
        # self.Route = Route
        # self.Weather = Weather

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "CellVoltage": [self.CellVoltage],
                "PackVoltage": [self.PackVoltage],
                "ChargingCurrent": [self.ChargingCurrent],
                "DischargeCurrent": [self.DischargeCurrent],
                "BatteryTemperature": [self.BatteryTemperature],
                "CellTemperature": [self.CellTemperature],
                "AmbientTemp": [self.AmbientTemp],
                "coolingSysTemp": [self.coolingSysTemp],
                "stateOfCharge": [self.stateOfCharge],
                "stateOfHealth": [self.stateOfHealth],
                "stateOfPower": [self.stateOfPower],
                "internalResistance": [self.internalResistance],
                "CycleCount": [self.CycleCount],
                "Velocity": [self.Velocity],
                "Elevation": [self.Elevation],
                "Throttle": [self.Throttle],
                "MotorTorque": [self.MotorTorque],
                "LongitudinalAcceleration": [self.LongitudinalAcceleration],
                "RegenerativeBrakingSignal": [self.RegenerativeBrakingSignal],
                "BatteryVoltage": [self.BatteryVoltage],
                "BatteryCurrent": [self.BatteryCurrent],
                "SoC": [self.SoC],
                # "Route": [self.Route],
                # "Weather": [self.Weather]
            }
            returnData = pd.DataFrame(custom_data_input_dict)
            return returnData

        except Exception as e:
            raise CustomException(e, sys)
        

