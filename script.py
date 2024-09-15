import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

# -----------------------------
# 1. Data Stream Simulation
# -----------------------------
def generate_data_stream():
    """
    Simulates a real-time data stream with seasonal patterns, random noise, 
    and occasional outliers.
    
    Returns:
        Generator yielding floating-point numbers representing the data stream.
    """
    t = 0
    while True:
        seasonal = 10 * np.sin(2 * np.pi * t / 30)  # Seasonal variation (sin wave)
        noise = random.uniform(-2, 2)  # Random noise for realism
        outlier = random.uniform(-20, 20) if random.random() < 0.05 else 0  # 5% chance of an outlier
        value = seasonal + noise + outlier
        yield value
        t += 1


# ----------------------------------
# 2. Z-Score Based Anomaly Detection
# ----------------------------------
def detect_anomaly(data, window_size=50, threshold=1.8):
    """
    Detects anomalies in a real-time data stream using a Z-score method.
    The Z-score measures how many standard deviations a data point is from the mean.

    Args:
        data (deque): A fixed-length list of recent data points.
        window_size (int): The number of data points considered in the moving window.
        threshold (float): The Z-score threshold beyond which a point is considered an anomaly.

    Returns:
        bool: True if the most recent data point is an anomaly, False otherwise.
    """
    if len(data) < window_size:
        return False  # Not enough data to compute Z-score

    mean = np.mean(data)
    std = np.std(data)

    if std == 0:  # Avoid division by zero
        return False

    z_score = (data[-1] - mean) / std
    return abs(z_score) > threshold


# -----------------------------------------------------
# 3. Real-Time Data Visualization and Anomaly Detection
# -----------------------------------------------------
def real_time_plot():
    """
    Simulates a real-time data stream, detects anomalies, and visualizes the data
    in real-time. Anomalies are highlighted with red color on the plot.
    """
    window_size = 50  # Number of recent data points used to calculate the Z-score
    data_window = deque(maxlen=window_size)  # Sliding window of recent data points
    anomaly_points = []  # Store points where anomalies are detected

    # Initialize the real-time plot
    plt.ion()  # Interactive mode on
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_ylim(-50, 50)  # Adjusted for potential anomaly values
    ax.set_xlim(0, 300)  # Number of points to display on the x-axis
    ax.set_title("Real-Time Data Stream with Anomaly Detection")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")

    time_points = []  # Store time (x-axis)
    stream = generate_data_stream()  # Start data stream
    values = []  # Store data values (y-axis)

    for t in range(300):  # Simulate 200 time points
        data_point = next(stream)  # Get next value from the data stream
        data_window.append(data_point)  # Add to sliding window
        time_points.append(t)  # Track time steps
        values.append(data_point) # Track data values


        # Detect if the new data point is an anomaly
        if detect_anomaly(data_window):
            anomaly_points.append((t, data_point))  # Store anomaly point (time, value)

        # Update plot
        line.set_xdata(time_points)
        line.set_ydata(values)
        
        # Mark anomalies in red
        if anomaly_points:
            # print("here")
            anomaly_x, anomaly_y = zip(*anomaly_points)  # Unpack anomaly points
            
            ax.scatter(anomaly_x, anomaly_y, color="red")  # Plot anomalies as red circles

    plt.ioff()  # Turn off interactive mode
    plt.show()  # Display the final plot


# ---------------
# Run the Program
# ---------------
if __name__ == "__main__":
    try:
        real_time_plot()  # Start the real-time anomaly detection and visualization
    except Exception as e:
        print(f"An error occurred: {e}")  # Basic error handling for robustness
