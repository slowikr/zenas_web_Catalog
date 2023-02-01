import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena's Amazing Athleisure Catalog") 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select distinct color_or_style from ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website;")
my_data_rows = my_cur.fetchall()
df=pandas.DataFrame(my_data_rows)

option = streamlit.selectbox('Pick a sweatsuit color or style', list(df[0].values.tolist()))
my_cur.execute("select distinct direct_url from ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website where color_or_style='" + option +"';")
streamlit.image(my_cur.fetchone()[0],width=400,caption='Test')

