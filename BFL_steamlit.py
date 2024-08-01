import streamlit as st

st.set_page_config(
    page_title="BFL Recruitment Tracker",
    page_icon="kgpng.png"  # Path to image file
)

# URL for the Power BI report
powerbi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiODNlNjY0ZTctOTllNi00YjA3LTljYWQtMmNmM2M2MzJkNjZkIiwidCI6ImE2YjQ2MzBjLTIwMjktNDk2OC1iMjMxLTRkODM1NmNhODFkMCJ9"


# iframe_code = f'''
# <div style="width: 1390px; box-sizing: border-box; margin-left: -340px; margin-top: -100px; background-color: white;">
#     <iframe width="100%" height="690" src="{powerbi_url}" frameborder="0" allowFullScreen="true" style="margin-top: 62px; background-color: white;"></iframe>
# </div>
# '''
iframe_code = f'''
<div style="width: 1380px; box-sizing: border-box; margin-left: -330px; margin-top: -100px; background-color: white; padding: 0; border: none;">
    <iframe width="100%" height="680" src="{powerbi_url}" frameborder="0" allowFullScreen="true" style="background-color: white; border: none;"></iframe>
</div>
'''

# Inject the iframe_code into the Streamlit app
st.markdown(iframe_code, unsafe_allow_html=True)
