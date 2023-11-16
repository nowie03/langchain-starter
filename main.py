import langchain_helper as lch
import streamlit as st


st.title('Pets name generator')

animal_type = st.sidebar.selectbox('What is your pet?',('cat','dog','cow'))

if animal_type == 'cat':
    pet_color = st.sidebar.text_area(label='what color is your cat?',max_chars=10)

elif animal_type == 'dog':
    pet_color = st.sidebar.text_area(label='what color is your dog?',max_chars=10)
    
elif animal_type == 'cow':
    pet_color = st.sidebar.text_area(label='what color is your cow?',max_chars=10)
    

if pet_color:
    # response = lch.generate_pet_name(animal_type=animal_type,animal_color=pet_color)
    # st.text(response['pet_name'])
   
    st.text('response will be generated from chat gpt')
    
