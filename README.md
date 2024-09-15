

# Efficient Data Stream Anomaly Detection


Project Description
--------------------
This project implements an anomaly detection system for continuous data streams using Python. The data stream simulates real-time floating-point sequences representing metrics like financial transactions or system performance. The primary goal is to detect anomalies such as unusual spikes or deviations from regular patterns.


Table of Contents
------------------
- Installation
- Anomaly Detection Algorithm and Effectiveness
- Explanation of Key Components
- Real-Time Visualization
- Output
- Future Improvements

Installation
------------
1. Clone the repository:
   git clone https://github.com/Priyanshu172000/Anomaly_detection.git

2. Navigate to the project directory:
   cd Anomaly_detection

3. Install the required libraries:
   pip install -r requirements.txt

Anomaly Detection Algorithm
---------------------------
**Algorithm Selection:**
The project uses a Z-score based anomaly detection method:
- Z-score: Measures how far a data point deviates from the mean in terms of standard deviations.
- Sliding Window: A window of recent data points is used to adapt to concept drift in the data.
- Anomalies: Detected if the Z-score exceeds a specified threshold.

**Effectiveness:** The Z-score method is effective for data streams with normal distribution, where most data points cluster around a central value (mean). It handles seasonal variations (sinusoidal patterns) and detects outliers effectively.

Explanation of Key Components
-----------------------------
Data Stream Simulation
- Seasonality: A sinusoidal wave mimics recurring patterns in real-world data.
- Noise: Random noise is added for realism.
- Outliers: Occasional large values simulate anomalous events (e.g., fraud, system failure).


Real-Time Visualization
-----------------------
The data stream is visualized in real-time with matplotlib. Detected anomalies are highlighted in red. The x-axis shifts to show the most recent 300 data points, simulating a continuous flow.

Output
------
- Plot: A live plot visualizes the data stream with anomalies marked as red dots.

Future Improvements
-------------------
- Advanced Algorithms: Integrate machine learning-based approaches like Isolation Forest or One-Class SVM.
- Performance Optimization: Explore multi-threading or asynchronous programming to handle larger data streams.


