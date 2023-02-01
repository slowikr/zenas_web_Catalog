import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena's Amazing Athleisure Catalog") 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

option = streamlit.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))

streamlit.write('You selected:', option)
