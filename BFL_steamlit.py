import streamlit as st

st.set_page_config(
    page_title="Tropicana Facebook Campaigns Performance",
    page_icon="logo-lion.png"  # Path to image file
)

# URL for the Power BI report
powerbi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiODNlNjY0ZTctOTllNi00YjA3LTljYWQtMmNmM2M2MzJkNjZkIiwidCI6ImE2YjQ2MzBjLTIwMjktNDk2OC1iMjMxLTRkODM1NmNhODFkMCJ9"

iframe_code = f'''
<div style="width: 100vw; height: 100vh; overflow: hidden; padding: 0; margin: 0; background-color: white;">
    <iframe width="100%" height="100%" src="{powerbi_url}" frameborder="0" allowFullScreen="true" style="border: none;"></iframe>
</div>
'''

# Inject the iframe_code into the Streamlit app
st.markdown(iframe_code, unsafe_allow_html=True)
