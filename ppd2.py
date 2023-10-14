import pandas as pd 
import os 
import streamlit as st
import os
#from multiapp import MultiApp
#from streamlit_multipage import MultiPage
import matplotlib.pyplot as plt

current_file_path = os.path.dirname(__file__)
csv_file_path = current_file_path + "\\T_Products_2020 - December2.csv"



df = pd.read_csv(csv_file_path)
df = df.dropna(axis=0,how='all')
print(df["code"])


# making dirs
for item in df['code']:

    item = item.replace('/', '\\')
    item = item.replace(' ', '')
    item = item.replace('\n', '')
    try:
        path = os.path.join(current_file_path, item)
        os.makedirs(path)
    except:
        print(f"{item} folder already exists")
        #print(df['code'].count)

imgarr = []

# get paths for products folders
for item in df['code']:
    item = str(item)
    item = item.replace('/', '\\')
    item = item.replace(' ', '')
    item = item.replace('\n', '')
    for dirpath, dirnames, filenames in os.walk(current_file_path + '\\' + item):  
        for filename in filenames:  
            #print(filename)
            #print(item)
            path = item + '\\' + filename
            #print(path)
            imgarr.append(path)

typearr=[]

# define products types
for item in df['code']:
    item = str(item)
    if "71111" in item:
        type="Chandelier"
    elif "71113" in item:
        type="Plafonier"
    elif "71114" in item:
        type="Wall Lamp"
    elif "71115" in item:
        type="Lantern"
    elif "71116" in item:
        type="Table Lamp"
    typearr.append(type)
                        
# put types and paths in df
df['image_path'] = imgarr
df['Type'] = typearr

# set page config and title
st.set_page_config(page_title='Product Portfolio Dashboard',layout='wide',initial_sidebar_state='expanded')
st.title("Product Portfolio")

st.sidebar.header("Filter")



product_type = st.sidebar.multiselect( "Product Type", options=df['Type'].unique(), default=df['Type'].unique() )

price_list = df['Price'].apply(pd.to_numeric)
price_slider = st.sidebar.slider('Filter by Product Price', 0, int(price_list.max()), int(price_list.max()) )
product_color = st.sidebar.multiselect( "Product Finish", options=df['Plating'].unique(), default=df['Plating'].unique() )

code_selector = df['code']

# button click action
def button_clicked(code_in):
    df_selection=df.query("code==@code_in")
    with st.container():
        st.write("---")
        st.write("Selected Product Details")
        st.dataframe(df_selection)
        st.write("---")

# first selection
df_selection=df.query(
    "Plating==@product_color & Type==@product_type & code==@code_selector & Price<@price_slider"
    )

tab1, tab2, tab3 = st.tabs(["Catalogue", "Charts", "Statistics"])

with tab1:
    
    st.write("---")
    
    clm1,clm2,clm3 = st.columns(3)
    with clm1:
        for elem in range(int(len(df_selection)/3)):
            imgpath=df_selection.iloc[elem]['image_path']
            st.image(imgpath,width=130)
            imgcode=df_selection.iloc[elem]['code']
            st.write(imgcode)
            with st.expander('Expand Product Details'):
                df_selection2=df.query("code==@imgcode")
                df_selection2=df_selection2.dropna(axis=1)
                df_selection2=df_selection2.drop(columns=['image_path'])
                df_selection2=df_selection2.drop(columns=['code'])
                with st.container():
                    st.write("---")
                    st.write("Selected Product Details")
                    count = df_selection2.shape[1]
                    count_unit = int(count/6)
                    df1 = df_selection2.iloc[:, 0:count_unit ]
                    df2 = df_selection2.iloc[:, count_unit:count_unit*2 ]
                    df3 = df_selection2.iloc[:, count_unit*2:count_unit*3 ]
                    df4 = df_selection2.iloc[:, count_unit*3:count_unit*4 ]
                    df5 = df_selection2.iloc[:, count_unit*4:count_unit*5 ]
                    df6 = df_selection2.iloc[:, count_unit*5:count_unit*6 ]
                    
                    st.dataframe(df1.set_index(df1.columns[0]))
                    st.dataframe(df2.set_index(df2.columns[0]))
                    st.dataframe(df3.set_index(df3.columns[0]))
                    st.dataframe(df4.set_index(df4.columns[0]))
                    st.dataframe(df5.set_index(df5.columns[0]))
                    st.dataframe(df6.set_index(df6.columns[0]))
                    
    with clm2:
        for elem in range(int(len(df_selection)/3), int(len(df_selection)*2/3), 1):
            imgpath=df_selection.iloc[elem]['image_path']
            st.image(imgpath,width=130)
            imgcode=df_selection.iloc[elem]['code']
            st.write(imgcode)
            with st.expander('Expand Product Details'):
                df_selection2=df.query("code==@imgcode")
                df_selection2=df_selection2.dropna(axis=1)
                df_selection2=df_selection2.drop(columns=['image_path'])
                df_selection2=df_selection2.drop(columns=['code'])
                with st.container():
                    st.write("---")
                    st.write("Selected Product Details")
                    count = df_selection2.shape[1]
                    count_unit = int(count/6)
                    df1 = df_selection2.iloc[:, 0:count_unit ]
                    df2 = df_selection2.iloc[:, count_unit:count_unit*2 ]
                    df3 = df_selection2.iloc[:, count_unit*2:count_unit*3 ]
                    df4 = df_selection2.iloc[:, count_unit*3:count_unit*4 ]
                    df5 = df_selection2.iloc[:, count_unit*4:count_unit*5 ]
                    df6 = df_selection2.iloc[:, count_unit*5:count_unit*6 ]
                    
                    st.dataframe(df1.set_index(df1.columns[0]))
                    st.dataframe(df2.set_index(df2.columns[0]))
                    st.dataframe(df3.set_index(df3.columns[0]))
                    st.dataframe(df4.set_index(df4.columns[0]))
                    st.dataframe(df5.set_index(df5.columns[0]))
                    st.dataframe(df6.set_index(df6.columns[0]))


    with clm3:
        for elem in range(int(len(df_selection)*2/3),int(len(df_selection)),1):
            imgpath=df_selection.iloc[elem]['image_path']
            st.image(imgpath,width=130)
            imgcode=df_selection.iloc[elem]['code']
            st.write(imgcode)
            with st.expander('Expand Product Details'):
                df_selection2=df.query("code==@imgcode")
                df_selection2=df_selection2.dropna(axis=1)
                df_selection2=df_selection2.drop(columns=['image_path'])
                df_selection2=df_selection2.drop(columns=['code'])
                with st.container():
                    st.write("---")
                    st.write("Selected Product Details")
                    count = df_selection2.shape[1]
                    count_unit = int(count/6)
                    df1 = df_selection2.iloc[:, 0:count_unit ]
                    df2 = df_selection2.iloc[:, count_unit:count_unit*2 ]
                    df3 = df_selection2.iloc[:, count_unit*2:count_unit*3 ]
                    df4 = df_selection2.iloc[:, count_unit*3:count_unit*4 ]
                    df5 = df_selection2.iloc[:, count_unit*4:count_unit*5 ]
                    df6 = df_selection2.iloc[:, count_unit*5:count_unit*6 ]
                    
                    st.dataframe(df1.set_index(df1.columns[0]))
                    st.dataframe(df2.set_index(df2.columns[0]))
                    st.dataframe(df3.set_index(df3.columns[0]))
                    st.dataframe(df4.set_index(df4.columns[0]))
                    st.dataframe(df5.set_index(df5.columns[0]))
                    st.dataframe(df6.set_index(df6.columns[0]))


# markdown to hide expansion arrows of streamlit
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)


# markdown to attempt change of sidebar
side_bar_wd = '''
    <style>
    section[data-testid="stSidebar"] .css-ng1t4o {{width: 10rem;}}
    </style>
'''

st.markdown(side_bar_wd, unsafe_allow_html=True)




# Second Tab


with tab2:
    
    # diff method of plotting
#     fig, ax = plt.subplots()
#     ax.bar(df_type['Type'], df_type['code'])
#     st.pyplot(fig)

    col1, col2 = st.columns(2)
    
    df_type = df_selection.groupby('Type').count().reset_index()
    df_type = df_type.rename(columns={"code": "Quantity"})

    df_color = df_selection.groupby('Color').count().reset_index()
    df_color = df_color.rename(columns={"code": "Quantity"})
    
    df_mat = df_selection.groupby('Material').count().reset_index()
    df_mat = df_mat.rename(columns={"code": "Quantity"})
    
    df_pack = df_selection.groupby('Package Dimensions').count().reset_index()
    df_pack = df_pack.rename(columns={"code": "Quantity"})
    
    #col1.bar_chart(df_type, x='Type', y='Quantity', color=None, width=0, height=0, use_container_width=True)
    
    fig, ax = plt.subplots()
    ax.pie(df_type['Quantity'],labels=df_type['Type'], autopct='%1.1f%%', radius=0.6)
    col1.write('Distribution of Products Types')
    col1.pyplot(fig)
    
    col2.write('Distribution of Materials Used')
    col2.write('')
    col2.write('')
    col2.bar_chart(df_mat, x='Material', y='Quantity', color=None, width=0, height=500, use_container_width=True)
    
    st.write('Summary of Products Prices')
    st.scatter_chart(df_selection, x='Height (cm)', y='Price', color='Type', size='Width (cm)', width=0, height=0, use_container_width=True)
    
    st.bar_chart(df_color, x='Color', y='Quantity', color=None, width=0, height=0, use_container_width=True)


    st.bar_chart(df_pack, x='Package Dimensions', y='Quantity', color=None, width=0, height=500, use_container_width=True)
    
with tab3:
    
    df_selection = df_selection.drop(columns=['Product Image','Chain Length (cm)'])
    df_stats = df_selection.describe()
    
    st.dataframe(df_stats)