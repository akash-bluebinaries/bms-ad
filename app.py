from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                CellVoltage=float(request.form.get('CellVoltage(V)')),
                PackVoltage=float(request.form.get('PackVoltage(V)')),
                ChargingCurrent=float(request.form.get('ChargingCurrent(mA)')),
                DischargeCurrent=float(request.form.get('DischargeCurrent(mA)')),
                BatteryTemperature=float(request.form.get('BatteryTemperature(C)')),
                CellTemperature=float(request.form.get('CellTemperature(C)')),
                AmbientTemp=float(request.form.get('AmbientTemp(C)')),
                coolingSysTemp=float(request.form.get('coolingSysTemp(C)')),
                stateOfCharge=float(request.form.get('stateOfCharge(SOC)')),
                stateOfHealth=float(request.form.get('stateOfHealth(SOH)')),
                stateOfPower=float(request.form.get('stateOfPower(SOP)')),
                internalResistance=float(request.form.get('internalResistance(ohm)')),
                CycleCount=float(request.form.get('CycleCount')),
                Velocity=float(request.form.get('Velocity [km/h]')),
                Elevation=float(request.form.get('Elevation [m]')),
                Throttle=float(request.form.get('Throttle [%]')),
                MotorTorque=float(request.form.get('Motor Torque [Nm]')),
                LongitudinalAcceleration=float(request.form.get('Longitudinal Acceleration [m/s^2]')),
                RegenerativeBrakingSignal=float(request.form.get('Regenerative Braking Signal')),
                BatteryVoltage=float(request.form.get('Battery Voltage [V]')),
                BatteryCurrent=float(request.form.get('Battery Current [A]')),
                SoC=float(request.form.get('SoC')),
                # Route=request.form.get('Route'),
                # Weather=request.form.get('Weather')
            )
            
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            return render_template('home.html', results=results)

        except Exception as e:
            return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
