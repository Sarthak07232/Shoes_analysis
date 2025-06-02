import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Title
st.title("Shoe Sales Dashboard")

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv("../Datasets/SHOES.csv")
    df['Sales'] = df['Sales'].replace('[, $]', '', regex=True).astype('int64')
    df['Inventory'] = df['Inventory'].replace('[, $]', '', regex=True).astype('int64')
    df['Returns'] = df['Returns'].replace('[, $]', '', regex=True).astype('int64')
    return df

df = load_data()

# Show unique regions
regions = df['Region'].unique()
selected_region = st.selectbox("Select a Region", regions)

# Filter data
reg = df[df['Region'] == selected_region]

# Show barplot
st.subheader(f"Sales by Subsidiary in {selected_region}")
fig, ax = plt.subplots(figsize=(10, 5))
sb.barplot(x='Subsidiary', y='Sales', data=reg, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
