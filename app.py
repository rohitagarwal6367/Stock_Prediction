import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

from flask import Flask, render_template, request, send_file
import datetime as dt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import os
import gdown

plt.style.use("fivethirtyeight")

app = Flask(__name__)

# ==============================
# ✅ MODEL DOWNLOAD SECTION
# ==============================

MODEL_PATH = "stock_dl_model.h5"

def download_model():
    file_id = "1MMKiKCT72ZONfsSzFEZtUdjdQPWQgknq"
    url = f"https://drive.google.com/uc?id={file_id}"
    print("Downloading model from Google Drive...")
    gdown.download(url, MODEL_PATH, quiet=False, fuzzy=True)

# Download only if not exists
if not os.path.exists(MODEL_PATH):
    download_model()

# Load model AFTER download
model = load_model(MODEL_PATH)
print("✅ Model loaded successfully")

# ==============================

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    stock = request.form.get('stock')
    if not stock:
        stock = 'POWERGRID.NS'
    
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime.now()   # 🔥 dynamic date

    df = yf.download(stock, start=start, end=end)

    if df.empty:
        return render_template('result.html', error="No data found for this stock ticker!")

    data_desc = df.describe()

    # EMA
    ema20 = df.Close.ewm(span=20, adjust=False).mean()
    ema50 = df.Close.ewm(span=50, adjust=False).mean()
    ema100 = df.Close.ewm(span=100, adjust=False).mean()
    ema200 = df.Close.ewm(span=200, adjust=False).mean()
    
    # Train/Test split
    data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
    data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):])

    scaler = MinMaxScaler(feature_range=(0,1))
    data_training_array = scaler.fit_transform(data_training)

    past_100_days = data_training.tail(100)
    final_df = pd.concat([past_100_days, data_testing], ignore_index=True)

    input_data = scaler.transform(final_df)

    x_test, y_test = [], []
    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100:i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)

    # Prediction
    y_predicted = model.predict(x_test)

    scale_factor = 1 / scaler.scale_[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Ensure static folder exists
    os.makedirs("static", exist_ok=True)

    # Plot 1
    fig1, ax1 = plt.subplots(figsize=(12,6))
    ax1.plot(df.Close, label='Closing Price')
    ax1.plot(ema20, label='EMA 20')
    ax1.plot(ema50, label='EMA 50')
    ax1.legend()
    ema_chart_path = "static/ema_20_50.png"
    fig1.savefig(ema_chart_path)
    plt.close(fig1)

    # Plot 2
    fig2, ax2 = plt.subplots(figsize=(12,6))
    ax2.plot(df.Close, label='Closing Price')
    ax2.plot(ema100, label='EMA 100')
    ax2.plot(ema200, label='EMA 200')
    ax2.legend()
    ema_chart_path_100_200 = "static/ema_100_200.png"
    fig2.savefig(ema_chart_path_100_200)
    plt.close(fig2)

    # Plot 3
    fig3, ax3 = plt.subplots(figsize=(12,6))
    ax3.plot(y_test, label='Original Price')
    ax3.plot(y_predicted, label='Predicted Price')
    ax3.legend()
    prediction_chart_path = "static/stock_prediction.png"
    fig3.savefig(prediction_chart_path)
    plt.close(fig3)

    # Save CSV
    csv_file_path = f"static/{stock}_dataset.csv"
    df.to_csv(csv_file_path)

    return render_template('result.html',
                           plot_path_ema_20_50=ema_chart_path,
                           plot_path_ema_100_200=ema_chart_path_100_200,
                           plot_path_prediction=prediction_chart_path,
                           data_desc=data_desc.to_html(classes='table table-bordered'),
                           dataset_link=csv_file_path)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(f"static/{filename}", as_attachment=True)

# ==============================
# ✅ PRODUCTION FIX (VERY IMPORTANT)
# ==============================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses PORT
    app.run(host="0.0.0.0", port=port)