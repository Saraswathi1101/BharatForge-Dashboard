import streamlit as st

st.set_page_config(
    page_title="Tropicana Facebook Campaigns Performance",
    page_icon="logo-lion.png"  # Path to image file
)

# URL for the Power BI report
powerbi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiODNlNjY0ZTctOTllNi00YjA3LTljYWQtMmNmM2M2MzJkNjZkIiwidCI6ImE2YjQ2MzBjLTIwMjktNDk2OC1iMjMxLTRkODM1NmNhODFkMCJ9"

iframe_code = f'''
<div style="position: absolute; top: 0; left: 0; width: 100vw; height: 100vh; margin: 0; padding: 0; box-sizing: border-box;">
    <iframe src="{powerbi_url}" frameborder="0" allowFullScreen="true" style="width: 100vw; height: 100vh; border: none; margin: 0; padding: 0;"></iframe>
</div>
'''

# Inject the iframe_code into the Streamlit app
st.markdown(iframe_code, unsafe_allow_html=True)
