import pandas as pd

url = 'https://raw.githubusercontent.com/SAI-SRINIVASA-SUBRAMANYAM/aps-sensor-fault-detection-subbu/main/aps_failure_training_set1.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))