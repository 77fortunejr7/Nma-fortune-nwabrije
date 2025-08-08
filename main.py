import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace with your path if needed)
df = pd.read_csv("exam_malpractice_dataset.csv")

# Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create new column for Year-Month for time series graph
df['YearMonth'] = df['Date'].dt.to_period('M')

# Set plot style and figure size
plt.style.use("ggplot")
figsize = (10, 6)

# 1. Count of Malpractice Types
plt.figure(figsize=figsize)
df['Malpractice_Type'].value_counts().plot(kind='bar')
plt.title("Count of Malpractice Types")
plt.xlabel("Malpractice Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 2. Gender Distribution
plt.figure(figsize=figsize)
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 3. Malpractice Reports by Gender
plt.figure(figsize=figsize)
df.groupby('Gender')['Malpractice_Type'].count().plot(kind='bar')
plt.title("Malpractice Reports by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 4. Malpractice by Education Level
plt.figure(figsize=figsize)
df['Education_Level'].value_counts().plot(kind='bar')
plt.title("Malpractice by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 5. Caught vs Not Caught
plt.figure(figsize=figsize)
df['Caught'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Caught vs Not Caught")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 6. Malpractice by Exam Type
plt.figure(figsize=figsize)
df['Exam_Type'].value_counts().plot(kind='bar')
plt.title("Malpractice by Exam Type")
plt.xlabel("Exam Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 7. Malpractice by Location
plt.figure(figsize=figsize)
df['Location'].value_counts().plot(kind='bar')
plt.title("Malpractice by Location")
plt.xlabel("Location")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 8. Malpractice Trends Over Time
plt.figure(figsize=figsize)
df.groupby('YearMonth').size().plot()
plt.title("Malpractice Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.tight_layout()
plt.show()

# 9. Age Distribution
plt.figure(figsize=figsize)
df['Age'].plot(kind='hist', bins=15)
plt.title("Age Distribution of Students")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
