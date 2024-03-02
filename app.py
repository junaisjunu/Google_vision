from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st
import PIL.Image



#get the google api key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#create model using gemini-pro-vision 
model=genai.GenerativeModel("gemini-pro-vision")

def main():
    st.title("Google Vision")
    st.header("Upload your image")
    img=st.file_uploader("Choose an image",type=["jpg","jpeg","png"])
    

    if img is not None:
        image=PIL.Image.open(img)
        if st.button("Submit"):
            st.write("Thanks for uploading image")
            st.image(image=image,width=400)
        st.header("Ask your question related to this picture")

        qstn=st.text_input("ask anything?")

        if st.button("click me"):
            response=model.generate_content([qstn,image],stream=True)
            response.resolve()
            st.header("Answer to your Question")
            st.write(response.text)
        

    else:
        st.info("please upload your image")
    

    
    



if __name__ == "__main__":
    main()





