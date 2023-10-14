import pandas as pd 
import os 
import streamlit as st
import os

current_file_path = os.path.dirname(__file__)
#xl_file_path = current_file_path + "\\T_Products_2020 - December.xlsx"
xl_file_path2 = current_file_path + "\\T_Products_2020 - December2.xlsx"


#df = pd.read_excel(xl_file_path)
df2 = pd.read_excel(xl_file_path2)
#print(df2)
print(df2["code"])

#i=0
imgarr = []
for item in df2["code"]:
    item = str(item)
    imagename = os.walk(current_file_path + item)
    print(imagename)
    print(item)
    print(current_file_path + item + imagename)
    path = current_file_path + item + imagename
    print(path)
    imgarr.append(path)
    #i+=1

# 
# for item in df2["code"]:
#     # Path  
#     path = os.path.join(current_file_path, item)
#     os.makedirs(path)  

st.set_page_config(page_title='Product Portfolio Dashboard',layout='wide',initial_sidebar_state='expanded')

st.write("Product Portfolio")

with st.container():
    st.write("---")
    clm1,clm2,clm3,clm4 = st.columns(4)
    with clm1:
        st.write('link1')
        for elem in range(50):
            st.image()
            st.write('test')
    with clm2:
        st.write('link2')
    with clm3:
        st.write('link3')
