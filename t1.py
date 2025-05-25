import pandas as pd

# Function to load data
def load_data(file_name):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

# Function to convert specific columns to numeric
def convert_columns_to_numeric(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Function to fill missing values
def fill_missing_values(df):
    # Fill numeric columns with mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df[col].fillna(df[col].mean(), inplace=True)

    # Fill categorical columns with mode
    object_cols = df.select_dtypes(include=['object']).columns
    for col in object_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

# Function to remove duplicates
def remove_duplicates(df):
    df.drop_duplicates(inplace=True)
    df = df.loc[:, ~df.T.duplicated()]  # Remove duplicate columns
    return df

# Main function
def main():
    file_name = 'food_coded.csv'
    df = load_data(file_name)

    if df is not None:
        convert_columns_to_numeric(df, ['GPA', 'weight'])
        fill_missing_values(df)
        df = remove_duplicates(df)
        df.to_csv('cleanedd_food_coded.csv', index=False)
        print("Data cleaned and saved to 'cleaned_food_coded.csv'.")

# Run the main function
if __name__ == '__main__':
    main()

