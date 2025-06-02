import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# App title
st.title("🥿 Shoe Sales Dashboard")

# File uploader
uploaded_file = st.file_uploader("SHOES.csv", type="csv")

# Load and clean the data if a file is uploaded
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Data cleaning
        df['Sales'] = df['Sales'].replace('[, $]', '', regex=True).astype('int64')
        df['Inventory'] = df['Inventory'].replace('[, $]', '', regex=True).astype('int64')
        df['Returns'] = df['Returns'].replace('[, $]', '', regex=True).astype('int64')

        # Region dropdown
        regions = df['Region'].unique()
        selected_region = st.selectbox("🌍 Select a Region", regions)

        # Filtered data
        reg = df[df['Region'] == selected_region]

        # Display barplot
        st.subheader(f"📊 Sales by Subsidiary in {selected_region}")
        fig, ax = plt.subplots(figsize=(10, 5))
        sb.barplot(x='Subsidiary', y='Sales', data=reg, ax=ax)
        ax.set_xlabel("Subsidiary")
        ax.set_ylabel("Sales")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Optional: show filtered data
        if st.checkbox("🔍 Show data table"):
            st.dataframe(reg)

    except Exception as e:
        st.error(f"⚠️ An error occurred while processing the file: {e}")
else:
    st.info("📌 Please upload your `SHOES.csv` file to get started.")
