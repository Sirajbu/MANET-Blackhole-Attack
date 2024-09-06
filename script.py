import pandas as pd

# Load the CSV files
normal_file = 'normal.csv'
blackhole_file = 'blackhole.csv'

# Define a threshold for detecting a blackhole attack
threshold = 0.5  # Adjust this value based on your requirements

try:
    # Read the CSV files focusing on the 'ReceiveRate' column, skipping the first 100 rows
    df_normal = pd.read_csv(normal_file, skiprows=range(1, 101), usecols=['ReceiveRate'])
    df_blackhole = pd.read_csv(blackhole_file, skiprows=range(1, 101), usecols=['ReceiveRate'])

    # Calculate the average ReceiveRate for both files
    avg_receive_rate_normal = df_normal['ReceiveRate'].mean()
    avg_receive_rate_blackhole = df_blackhole['ReceiveRate'].mean()

    # Print the average receive rates for debugging
    print(f"Average ReceiveRate in normal: {avg_receive_rate_normal}")
    print(f"Average ReceiveRate in blackhole: {avg_receive_rate_blackhole}")

    # Calculate the difference
    receive_rate_diff = abs(avg_receive_rate_normal - avg_receive_rate_blackhole)

    # Check if the difference exceeds the threshold
    if receive_rate_diff > threshold:
        print("Blackhole attack is detected. Check nodes!")
    else:
        print("Everything is normal.")

except FileNotFoundError as e:
    print(f"Error: {e.strerror}. File '{e.filename}' not found.")
except pd.errors.EmptyDataError:
    print("Error: One of the CSV files is empty.")
except pd.errors.ParserError as e:
    print(f"Error parsing CSV file: {e}")
except KeyError as e:
    print(f"Error: Missing expected column {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
