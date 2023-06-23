import seaborn as sns
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/semantic-segmentation-master/data.csv')
sns.displot(x = 'num_words_total', data = df)
