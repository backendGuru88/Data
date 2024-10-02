import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Suppress warnings for a cleaner output
warnings.simplefilter(action='ignore', category=FutureWarning)

# Manually extracted dataset (full)
data = {
    'ProductID': [5874, 5875, 5876, 5877, 5878, 5879, 5880, 5881, 5882, 5883],
    'ProductCategory': ['Smartphones', 'Smart Watches', 'Tablets', 'Smartphones', 'Tablets', 'Smart Watches', 'Tablets', 'Smartphones', 'Smartphones', 'Smart Watches'],
    'ProductBrand': ['Other Brands', 'Samsung', 'Samsung', 'Samsung', 'Sony', 'Samsung', 'Sony', 'Other Brands', 'Samsung', 'Samsung'],
    'ProductPrice': [312.949668, 980.389404, 2606.718293, 870.395450, 1798.955875, 1500.52534, 899.23456, 1020.4956, 1750.34978, 825.6475],
    'CustomerAge': [18, 35, 63, 63, 57, 28, 42, 19, 33, 45],
    'CustomerGender': [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    'PurchaseFrequency': [2, 7, 1, 10, 17, 5, 8, 2, 12, 9],
    'CustomerSatisfaction': [1, 2, 5, 3, 3, 4, 4, 1, 2, 4],
    'PurchaseIntent': [0, 1, 1, 1, 0, 1, 0, 0, 1, 1]
}

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Streamlit app
st.title('Electronics Sales Data Analysis')

# First row - displaying dataset preview and basic data
col1, col2 = st.columns(2)

with col1:
    st.subheader('Dataset Preview')
    st.dataframe(df)

with col2:
    st.subheader('Missing Values')
    missing_values = df.isnull().sum()
    st.write(missing_values)

# Second row - Data types and renaming columns
st.subheader('Data Types')
st.write(df.dtypes)

st.subheader('Rename Columns')
new_columns = [st.text_input(f'Column {i+1}', col) for i, col in enumerate(df.columns)]
df.columns = new_columns
st.write('Updated Columns:')
st.write(df.head())

# Correlation and scatter plots
st.subheader('Correlation and Scatter Plots')

col3, col4 = st.columns(2)

# Correlation matrix heatmap in col3
with col3:
    st.subheader('Correlation Matrix')
    numeric_df = df.select_dtypes(include='number')
    correlation_matrix = numeric_df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(plt)

# Scatter plots in col4
with col4:
    st.subheader('Scatter Plots')
    plt.figure(figsize=(15, 10))

    # Scatter plot: Product Price vs Customer Satisfaction
    plt.subplot(2, 2, 1)
    sns.scatterplot(data=df, x='ProductPrice', y='CustomerSatisfaction', hue='CustomerGender', palette='coolwarm')
    plt.title('Product Price vs Customer Satisfaction')

    # Scatter plot: Product Price vs Customer Age
    plt.subplot(2, 2, 2)
    sns.scatterplot(data=df, x='ProductPrice', y='CustomerAge', hue='CustomerGender', palette='coolwarm')
    plt.title('Product Price vs Customer Age')

    # Scatter plot: Customer Age vs Customer Satisfaction
    plt.subplot(2, 2, 3)
    sns.scatterplot(data=df, x='CustomerAge', y='CustomerSatisfaction', hue='CustomerGender', palette='coolwarm')
    plt.title('Customer Age vs Customer Satisfaction')

    plt.tight_layout()
    st.pyplot(plt)

# Bar charts and histograms
st.subheader('Bar Charts and Histograms')

col5, col6 = st.columns(2)

# Bar charts in col5
with col5:
    st.subheader('Bar Charts')
    plt.figure(figsize=(15, 10))

    # Bar chart for Product Category
    plt.subplot(3, 1, 1)
    sns.countplot(data=df, x='ProductCategory', palette='deep')
    plt.title('Count of Products by Category')
    plt.xticks(rotation=45)

    # Bar chart for Product Brand
    plt.subplot(3, 1, 2)
    sns.countplot(data=df, x='ProductBrand', palette='deep')
    plt.title('Count of Products by Brand')
    plt.xticks(rotation=45)

    # Bar chart for Customer Gender
    plt.subplot(3, 1, 3)
    sns.countplot(data=df, x='CustomerGender', palette='deep')
    plt.title('Count of Customers by Gender')

    plt.tight_layout()
    st.pyplot(plt)

# Histograms in col6
with col6:
    st.subheader('Histograms')
    plt.figure(figsize=(15, 10))

    # Histogram for Product Price
    plt.subplot(3, 1, 1)
    sns.histplot(df['ProductPrice'].dropna(), bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Product Price')

    # Histogram for Customer Age
    plt.subplot(3, 1, 2)
    sns.histplot(df['CustomerAge'].dropna(), bins=30, kde=True, color='lightgreen')
    plt.title('Distribution of Customer Age')

    # Histogram for Customer Satisfaction
    plt.subplot(3, 1, 3)
    sns.histplot(df['CustomerSatisfaction'].dropna(), bins=30, kde=True, color='salmon')
    plt.title('Distribution of Customer Satisfaction')

    plt.tight_layout()
    st.pyplot(plt)
