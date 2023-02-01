import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena's Amazing Athleisure Catalog") 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select distinct color_or_style from ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website")
my_data_rows = my_cur.fetchall()

option = streamlit.selectbox('Pick a sweatsuit color or style', my_data_rows)
streamlit.write('You selected:', option)
