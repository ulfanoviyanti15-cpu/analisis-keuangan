import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Aplikasi Analisis Keuangan",
    layout="wide"
)

st.title("📊 Aplikasi Analisis Keuangan")
st.write("Unggah laporan keuangan Excel untuk melihat dan menganalisis datanya.")

uploaded_file = st.file_uploader(
    "Pilih file Excel",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:
    try:
        excel_file = pd.ExcelFile(uploaded_file)

        sheet_name = st.selectbox(
            "Pilih sheet",
            excel_file.sheet_names
        )

        df = pd.read_excel(
            uploaded_file,
            sheet_name=sheet_name
        )

        st.subheader("Pratinjau Data")
        st.dataframe(df, use_container_width=True)

        if len(df.select_dtypes(include="number").columns) > 0:
            numeric_columns = df.select_dtypes(
                include="number"
            ).columns.tolist()

            selected_column = st.selectbox(
                "Pilih kolom angka untuk grafik",
                numeric_columns
            )

            st.subheader("Grafik")
            fig = px.bar(
                df,
                y=selected_column,
                title=f"Grafik {selected_column}"
            )
            st.plotly_chart(fig, use_container_width=True)

    except Exception as error:
        st.error(f"File Excel tidak dapat dibaca: {error}")
else:
    st.info("Belum ada file Excel yang dipilih.")
