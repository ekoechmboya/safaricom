import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
def load_and_explore_data(file_path):
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        
        # Display the first few rows
        print("\n--- First Five Rows ---")
        print(data.head())
        
        # Display dataset structure
        print("\n--- Dataset Info ---")
        print(data.info())
        
        # Check for missing values
        print("\n--- Missing Values ---")
        print(data.isnull().sum())
        
        # Clean the dataset
        data = data.dropna()  # Drop rows with missing values
        print("\n--- Dataset After Cleaning ---")
        print(data.info())
        
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
def basic_analysis(data):
    # Compute basic statistics
    print("\n--- Summary Statistics ---")
    print(data.describe())

    # Perform groupings
    if 'species' in data.columns:  # Example for the Iris dataset
        print("\n--- Grouped Statistics by Species ---")
        print(data.groupby('species').mean())

# Task 3: Data Visualization
def create_visualizations(data):
    # Visualization 1: Line chart (example: trends over time, using a 'time' column if available)
    if 'time' in data.columns and 'value' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='time', y='value', data=data, marker='o')
        plt.title('Trends Over Time')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.show()

    # Visualization 2: Bar chart (example: average petal length per species)
    if 'species' in data.columns and 'petal_length' in data.columns:
        plt.figure(figsize=(10, 6))
        data.groupby('species')['petal_length'].mean().plot(kind='bar', color='skyblue')
        plt.title('Average Petal Length by Species')
        plt.xlabel('Species')
        plt.ylabel('Average Petal Length')
        plt.show()

    # Visualization 3: Histogram (example: distribution of sepal length)
    if 'sepal_length' in data.columns:
        plt.figure(figsize=(10, 6))
        data['sepal_length'].hist(bins=20, color='purple', alpha=0.7)
        plt.title('Distribution of Sepal Length')
        plt.xlabel('Sepal Length')
        plt.ylabel('Frequency')
        plt.show()

    # Visualization 4: Scatter plot (example: sepal length vs petal length)
    if 'sepal_length' in data.columns and 'petal_length' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=data)
        plt.title('Sepal Length vs Petal Length')
        plt.xlabel('Sepal Length')
        plt.ylabel('Petal Length')
        plt.legend(title='Species')
        plt.show()

# Main function
def main():
    file_path = 'your_dataset.csv'  # Replace with your dataset path
    
    # Task 1: Load and Explore the Dataset
    data = load_and_explore_data(file_path)
    if data is None:
        return

    # Task 2: Basic Data Analysis
    basic_analysis(data)

    # Task 3: Data Visualization
    create_visualizations(data)

if __name__ == "__main__":
    main()
