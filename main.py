import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("telco_customer_churn.csv")


df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

# Set Streamlit page configuration
st.set_page_config(page_title="Telco Churn Analysis", layout="wide")

# Streamlit app title
st.title("📊 Telco Customer Churn Dashboard")
st.markdown("### An interactive and visually appealing dashboard to explore customer churn insights.")


st.sidebar.header("🔍 Filter Data")
st.sidebar.markdown("Use the dropdowns below to filter the dataset:")

contract_filter = st.sidebar.multiselect(
    "📜 Select Contract Type", 
    options=df["Contract"].unique(), 
    default=df["Contract"].unique(),
    help="Choose one or multiple contract types to filter the data."
)

payment_filter = st.sidebar.multiselect(
    "💳 Select Payment Method", 
    options=df["PaymentMethod"].unique(), 
    default=df["PaymentMethod"].unique(),
    help="Choose one or multiple payment methods to filter the data."
)


filtered_df = df[(df["Contract"].isin(contract_filter)) & (df["PaymentMethod"].isin(payment_filter))]


custom_palette = ["#3E7CB1", "#E63946"]


col1, col2 = st.columns(2)

# Churn Distribution
with col1:
    st.subheader("📉 Churn Distribution")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(data=filtered_df, x="Churn", palette=custom_palette, ax=ax)
    ax.set_title("Churn Distribution", fontsize=14)
    ax.set_facecolor("#f5f5f5")
    fig.patch.set_alpha(0.8)
    fig.patch.set_facecolor("#ffffff")
    st.pyplot(fig)


with col2:
    st.subheader("💰 Monthly Charges Distribution")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(filtered_df["MonthlyCharges"], bins=30, kde=True, color='#4CAF50', ax=ax)
    ax.set_title("Distribution of Monthly Charges", fontsize=14)
    ax.set_facecolor("#f5f5f5")
    fig.patch.set_alpha(0.8)
    fig.patch.set_facecolor("#ffffff")
    st.pyplot(fig)


col3, col4 = st.columns(2)


with col3:
    st.subheader("📜 Churn by Contract Type")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(data=filtered_df, x="Contract", hue="Churn", palette=custom_palette, ax=ax)
    ax.set_title("Churn by Contract Type", fontsize=14)
    ax.set_facecolor("#f5f5f5")
    fig.patch.set_alpha(0.8)
    fig.patch.set_facecolor("#ffffff")
    st.pyplot(fig)


with col4:
    st.subheader("📆 Tenure Distribution by Churn")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(filtered_df, x="tenure", hue="Churn", multiple="stack", palette=custom_palette, ax=ax)
    ax.set_title("Tenure Distribution by Churn", fontsize=14)
    ax.set_facecolor("#f5f5f5")
    fig.patch.set_alpha(0.8)
    fig.patch.set_facecolor("#ffffff")
    st.pyplot(fig)


st.subheader("🔗 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
ax.set_title("Feature Correlation Heatmap", fontsize=14)
ax.set_facecolor("#f5f5f5")
fig.patch.set_alpha(0.8)
fig.patch.set_facecolor("#ffffff")
st.pyplot(fig)


st.markdown("## Key Business Insights:")
st.markdown("✔️ Customers on **month-to-month contracts** have a higher churn rate.")
st.markdown("✔️ Customers paying via **electronic check** tend to churn more.")
st.markdown("✔️ Long-tenured customers are less likely to churn.")

# Footer
st.markdown("---")
st.markdown("**Built with Streamlit & Seaborn | Designed for data-driven insights**")
