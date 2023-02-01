import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena's Amazing Athleisure Catalog") 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
color_or_style=my_cur.execute("select distinct color_or_style from ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


option = streamlit.selectbox('How would you like to be contacted?', color_or_style)
streamlit.write('You selected:', option)
