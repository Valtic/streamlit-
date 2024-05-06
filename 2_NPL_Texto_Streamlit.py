# Core pkgs
import streamlit as st
st.set_page_config(page_title="NLP Web App",page_icon="🤩", layout="centered", initial_sidebar_state="auto")

#Viz Page
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use("Agg")
from wordcloud import WordCloud
#from deep_translator import GoogleTranslator

#NPL Pkgs
from textblob import TextBlob
#import neattext as nt
#import spacy

from collections import Counter
import re

#Summarization Functions

def sumarize_text(text, num_sentences=3):
    #Remove special characters and convert text to lowercase
    clean_text=re.sub('[^a-zA-Z]',' ',text).lower()
    
    #split the text into words
    words=clean_text.split()
    
    #Calculate the freequency in descending order
    word_freq=Counter(words)
    print(word_freq)
    
    #Sort the word based on their frequency in descenging order
    sorted_words = sorted(word_freq, key=word_freq.get, reverse=True)
    print(sorted_words)
    #Extract the top 'num_sentences' mos frequent words
    top_words = sorted_words[:num_sentences]
    
    #Create the summary by joining the top words
    summary = ' - '.join(top_words)
    
    return summary

def text_analyzer(text):
    datos={1:"a",3:"b",4:"c",5:"d"}
    return datos

def main():
    """ Web Con Streamlit """
    
    title_template="""
    <div style="background-color:blue; padding:8px;">
    <h1 style="color:cyan"> Web APP - by Streamlit</h1>
    </div> """
    
    st.markdown(title_template, unsafe_allow_html=True)
    
    subheader_template="""
    <div style="background-color:cyan; padding:8px;">
    <h3 style="color:blue"> Powered by Streamlit</h3>
    </div> """
    
    st.markdown(subheader_template, unsafe_allow_html=True)
    
    st.sidebar.image("logo.jpg", use_column_width=True)
    
    activity = ["Text Analysis","Translations","Sentiment Analysys","About"]
    choice= st.sidebar.selectbox("Menu",activity)
    
    if choice == "Text Analysis":
        st.subheader("Text Analysis")
        st.write("")
        
        raw_text= st.text_area("Write something","Enter a text in English...", height=200)
        
        if st.button("Analyze"):
            if(len(raw_text)) == 0:
                st.warning("Enter a text...")
            else:
                #blob = TextBlob(raw_text)
                st.info("Basic functions")
                col1,col2 = st.columns(2)
              
                with col1:
                    st.info("Text Stats")
                    #word_desc=nt.TextFrame(raw_text).word_stats()
                    word_desc={'Length of Text':20,'Num of Vowels':10,'Num of Consonants':5,'Num of Stopwords':4}
                    result_desc={"Length of Text":word_desc['Length of Text'],
                                  "Num of vowels":word_desc['Num of Vowels'],
                                  "Num of Consonants":word_desc['Num of Consonants'],
                                  "Num of Stopwords":word_desc['Num of Stopwords']}
                    st.write(result_desc)
                 
                    with st.expander("Stopwords"):
                        st.success("Stop Words List")
                        #stop_w=nt.TextExtractor(raw_text).extract_stopwords()
                        stop_w=['a','v','c']
                        st.error(stop_w)
               
                with col2:
                    with st.expander("Processed Text"):
                        st.success("Stop Words Ecluded Text")
                        #processed_text=str(nt.TextFrame(raw_text).remove_stopwords())
                        processed_text=['Hol','com','est']
                        st.write(processed_text)
                        
                    with st.expander("plot Wordcloud"):
                        st.success("Wordcloud")
                        #wordcloud= Wordcloud().generate(processed_text)
                        wordcloud=np.random.rand(5, 5)
                        fig=plt.figure(1,figsize=(20,10))
                        plt.imshow(wordcloud, interpolation='bilinear')
                        plt.axis('Off')
                        st.pyplot(fig)
                    st.write("")
                    st.write("")
                    st.info("Advaced features")
                    
                    col3, col4 = st.columns(2)
                    
    if choice == "About":
        st.subheader("About")
        st.write("")
        
        st.markdown("""
            ### Author info ###
            for more info:
            visit[streamlit](https://streamlit.io)
            """)
if __name__ == "__main__":
    main()
                   
            

