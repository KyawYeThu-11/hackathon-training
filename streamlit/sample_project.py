import streamlit as st
from gtts import gTTS

def speak(input_text, lang):
    myobj = gTTS(text=input_text, lang=lang, slow=False)
    myobj.save('audio/output.wav')
    st.audio('audio/output.wav')

def main():
    _, col2, _ = st.columns(3)
    with col2:
        st.image("images/TPH_Icon.png", width=180)
    
    st.markdown("<h2 style='text-align: center;'>End-to-end Burmese Speech Synthesis</h2>", unsafe_allow_html=True)

    st.write("""
        You can type any Burmese sentences in Unicode and the model will try to synthesize the speech based on your inputs. 
        Synthesizing process may take a few seconds.
    """)
    language = st.radio('Pick language', ['my', 'en', 'ko'])
    input_text = st.text_input('Input Text', placeholder="Type here")
    
    container = st.container()
    error_placeholder = st.empty()

    if st.button('Synthesize'):
        if input_text == '':
            error_placeholder.error("Input text field must be filled!")
        else:
            error_placeholder.empty()
            col4, col5 = container.columns(2)

            with col4:
                st.subheader("Input Text")
                st.write(input_text)

            with col5:
                st.subheader("Output Audio")
                
                with st.spinner('Synthesizing...'):
                    speak(input_text, language)

                    with open('audio/output.wav', "rb") as file:
                        st.download_button(label="Download the audio file", data=file, file_name='speech.wav', mime='audio/wav')

if __name__ == "__main__":
    PAGE_CONFIG = {'page_title': 'Sample Project', 'page_icon': 'images/TPH_Icon.png', 'layout': 'centered'}
    st.set_page_config(**PAGE_CONFIG)
    main()