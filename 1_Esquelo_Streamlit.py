# Core pkgs
import streamlit as st
st.set_page_config(page_title="Esqueleto Streamlit",page_icon="🤩", layout="centered", initial_sidebar_state="auto")

#Viz Page
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use("Agg")

def main():
    """ Web Con Streamlit """
    
    title_template="""
    <div style="background-color:rgb(3,4,94); padding:8px;">
    <h1 style="color:rgb(0, 119, 182)"> Web APP - by Streamlit</h1>
    </div> """
    
    st.markdown(title_template, unsafe_allow_html=True)
    
    subheader_template="""
    <div style="background-color:rgb(0, 180, 216); padding:8px;">
    <h3 style="color:rgb(202, 240, 248)"> Powered by Streamlit</h3>
    </div> """
    
    st.markdown(subheader_template, unsafe_allow_html=True)
    
    st.sidebar.image("logo.jpg", use_column_width=True)
    
    activity = ["menu 1","menu 2","menu 3","menu 4"]
    choice= st.sidebar.selectbox("Menu",activity)
    
    if choice == activity[0]:
        st.subheader("Entrada de Texto")
        st.write("")
        
        raw_text= st.text_area("Write something","Enter a text in English...", height=200)
        
        if st.button("Mostrar Resultados"):
            if(len(raw_text)) <= 3:
                st.warning("No Engought text, 3 char min \n- Enter more/a text...")
            else:
                st.info("Basic functions")
                col1,col2 = st.columns(2)
              
                with col1:
                    with st.expander("Col 1 - Expander up"):
                        st.info("Col 1 - Longitud: ")
                        st.write(len(raw_text))
                     
                    with st.expander("Col 1 - Expander down"):
                        st.success("Success message ")
                        st.error("Error message")
               
                with col2:
                    with st.expander("Column 2"):
                        st.success("Success message col 2")
                        st.write("Text message col 2")
                        
                    with st.expander("Plotting  - col 2"):
                        st.success("Plotting graphs")
                        rand_num=np.random.rand(5, 5)
                        fig=plt.figure(1,figsize=(20,10))
                        plt.imshow(rand_num, interpolation='bilinear')
                        plt.axis('On')
                        st.pyplot(fig)

                st.info("Advaced features")
                col3, col4 = st.columns(2)
                
                # Colum 1 ( 3 ), under Advanced features.
                with col3:
                    with st.expander("Adv. Col 3 "):
                        st.info("Advanced 3 ")
                        st.write(" -- Block 3 --")
                        
                # Colum 2 ( 4 ), under Advanced features.                       
                with col4:
                    with st.expander("Adv. Col 4 "):
                        st.success("Advanced 4 ")
                        st.write(" -- Block 4 --")
                    
    if choice == activity[1]: #About
        st.subheader(str(activity[1]))
        st.write(" -- MENU 1 --")

    if choice == activity[2]: #About
        st.subheader(str(activity[2]))
        st.write(" -- MENU 2 --")

    if choice == activity[3]: #About
        st.subheader("About")
        st.write("")
        
        st.markdown("""
            ### Author info ###
            for more info:
            visit [streamlit](https://streamlit.io)
            """)
        
if __name__ == "__main__":
    main()
                   
            

