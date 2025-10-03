# 📈 Stock Predictor  

This is a **Stock Price Prediction Web Application** built using **Flask, TensorFlow/Keras, Pandas, Matplotlib, and yFinance**.  
The app allows users to enter a stock ticker (e.g., `AAPL`, `RELIANCE.NS`, `TCS.NS`) and get:  

✅ Stock trend graphs with moving averages  
✅ Predicted vs Actual stock prices  
✅ Descriptive analysis of stock data  
✅ Option to download dataset in CSV format  

---

## 🚀 Features
- Enter any stock ticker symbol.
- Fetches live stock market data using **yFinance**.
- Shows **20 & 50 Day EMA** and **100 & 200 Day EMA** trend charts.
- Predicts stock price trends using a pre-trained **Deep Learning Model (.h5)**.
- Interactive and clean frontend with Bootstrap.
- Downloadable dataset in CSV format.

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Flask (Python)  
- **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn, yFinance, TensorFlow/Keras  

---

## 📂 Project Structure
```

📦 stock_price_prediction
┣ 📂 static
┃ ┣ 📜 ema_20_50.png
┃ ┣ 📜 ema_100_200.png
┃ ┣ 📜 stock_prediction.png
┃ ┗ 📜 dataset.csv
┣ 📂 templates
┃ ┣ 📜 index.html
┃ ┗ 📜 result.html
┣ 📜 app.py
┣ 📜 requirements.txt
┣ 📜 stock_dl_model.h5
┣ 📜 .gitignore
┗ 📜 README.md

````

---

## ⚙️ Installation & Setup

1. **Clone this repository**
   ```
   git clone https://github.com/rohitagarwal6367/Stock_Prediction.git
   cd Stock_Prediction

2. **Create Virtual Environment**

   ```
   python -m venv venv
   ```

3. **Activate Environment**

   * On **Windows**:

     ```
     venv\Scripts\activate
     ```
   * On **Mac/Linux**:

     ```
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

5. **Run the Application**

   ```
   python app.py
   ```

6. Open your browser and go to:
   👉 `http://127.0.0.1:5000/`

---

## 📊 Example Tickers

* `AAPL` → Apple Inc.
* `TSLA` → Tesla Motors
* `RELIANCE.NS` → Reliance Industries (NSE India)
* `TCS.NS` → Tata Consultancy Services

---

## 📞 Contact

If you have any queries, suggestions, or issues regarding this project, feel free to reach out:

* 📧 Email: **[rohitagarwal.se@gmail.com](mailto:rohitagarwal.se@gmail.com)**
* 🌐 GitHub: [Follow Me](https://github.com/rohitagarwal6367)
* 🔗 LinkedIn: [Connect With Me](https://www.linkedin.com/in/rohit-agarwal6367/)

---
