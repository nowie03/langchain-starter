from urllib import response
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts  import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()


def generate_pet_name(animal_type,animal_color):
    llm = OpenAI(temperature=0.7)
    
    prompt_template_name = PromptTemplate(
        input_variables = ["animal_type","animal_color"],
        template = "i have a {animal_type} , which is {animal_color} in color suggest one good name for it"
    )
    
    name_chain = LLMChain(llm=llm,prompt=prompt_template_name,output_key='pet_name')
    response = name_chain({'animal_type':animal_type,'animal_color':animal_color})
    
    return response
    
    


if __name__ == "__main__":
    # print(generate_pet_name('dog'))
    print("done")
