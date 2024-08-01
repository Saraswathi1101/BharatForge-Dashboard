import streamlit as st

st.set_page_config(
    page_title="BFL Recruitment Tracker",
    page_icon="kgpng.png"  # Path to image file
)

# URL for the Power BI report
powerbi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiODNlNjY0ZTctOTllNi00YjA3LTljYWQtMmNmM2M2MzJkNjZkIiwidCI6ImE2YjQ2MzBjLTIwMjktNDk2OC1iMjMxLTRkODM1NmNhODFkMCJ9"

# iframe_width = "1380px"  # Adjust to fit your screen
# iframe_height = "800px"  # Adjust to fit your screen

# iframe_code = f'''
# <div style="position: absolute; top: 0; left: 0; width: {iframe_width}; height: {iframe_height}; margin: 0; padding: 0; box-sizing: border-box;">
#     <iframe src="{powerbi_url}" frameborder="0" allowFullScreen="true" style="width: 100%; height: 100%; border: none; margin: 0; padding: 0;"></iframe>
# </div>
# '''
iframe_code = f'''
<div style="width: 1385px; box-sizing: border-box; margin-left: -335px; margin-top: -100px; background-color: white;">
    <iframe width="100%" height="680" src="{powerbi_url}" frameborder="0" allowFullScreen="true" style="margin-top: 62px; background-color: white;"></iframe>
</div>
'''

# Inject the iframe_code into the Streamlit app
st.markdown(iframe_code, unsafe_allow_html=True)
