import streamlit as st
import uuid
from utils import *
from datetime import datetime
from dotenv import load_dotenv
import os


if 'unique_id' not in st.session_state:
    st.session_state["unique_id"]=''

pinecone_apikey= os.environ.get("PINECONE_APIKEY")
pinecone_environment= os.environ.get("PINECONE_ENVIRONMENT")
pinecone_index_name= os.environ.get("PINECONE_INDEX_NAME")


def main():
    load_dotenv()

    
    st.set_page_config(page_title="Resume Screening Assistance")
    st.title("HR - Resume Screening Assistance...")
    st.subheader("I can help you with resume screening process...")

    job_description=st.text_area("Please Provide Job Description Here...", key="1")
    document_count=st.text_input("No. of Resumes to return", key="2")

    pdf=st.file_uploader("Upload Resumes here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)
    submit=st.button("Help me with the analysis")
    
    
    if submit:
        with st.spinner("Wait, It's in progress...."):
            # st.write("It's here...")

            #create a unique ID, so that we can use to query and get only the user uploaded documents from Pinecone vector
            #store
            st.session_state['unique_id']=uuid.uuid4().hex
            # st.write(st.session_state['unique_id'])

            
            #create a documents list out of all the user uploaded pdf files
            docs=create_docs(pdf,st.session_state["unique_id"])
            # st.write(docs)

            #display the count of resumes that have been uploaded
            st.write(len(docs))

            #create embeddings instance
            embeddings=create_embeddings_load_data()

            #push data to pinecone
            push_to_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings,docs)
            

            #fetch relevant data from Pinecone
            relevant_docs=similar_docs(job_description,document_count,pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings, st.session_state['unique_id'])
            # st.write(relevant_docs)
            
            # introducing line separator
            st.write(":heavy_minus_sign:" * 30)

            #display different documents on the UI.
            for item in range(len(relevant_docs)):
                st.subheader("👉"+str(item+1))
                #display filepath
                st.write("**File** : "+relevant_docs[item][0].metadata['name'])
                

                #introduce expander feature
                with st.expander("Show Me 👀"):
                    st.info("**Match Score** : "+ str(relevant_docs[item][1]))

                    summary=get_summary(relevant_docs[item][0])
                    st.write("Summary: ", summary)


        st.success("Hope I saved your Time!!!!")
            

main()
