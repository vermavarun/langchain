#https://www.youtube.com/watch?v=nAmC7SoVLd8
from langchain.llms import OpenAI # instead of OpenAI you can use HuggingFace or any other llm
import os
os.environ['OPENAI_API_KEY'] = ''
llm = OpenAI(temperature = 0.6)
# name = llm("Who is Srk?")
# print(name)
#######################################################################################################
from langchain.prompts import PromptTemplate
prompt_template_about = PromptTemplate(
    input_variables=['name'],
    template="Who is {name}'s wife?"
)
# prompt_template_about.format(name="amitabh bachchan")
# print(prompt_template_about)

prompt_template_net_worth = PromptTemplate(
    input_variables=['wife_name'],
    template="What is total net worth of {wife_name}"
)
# prompt_template_net_worth.format(wife_name="amitabh bachchan")
# print(prompt_template_net_worth)

#######################################################################################################
from langchain.chains import LLMChain
about_chain = LLMChain(llm=llm, prompt=prompt_template_about)
#answer_about = about_chain.run("Bill Gates")
#print(answer_about)

from langchain.chains import LLMChain
net_worth_chain = LLMChain(llm=llm, prompt=prompt_template_net_worth)
#answer_net_worth = net_worth_chain.run("Bill Gates")
#print(answer_net_worth)

#######################################################################################################
# from langchain.chains import SimpleSequentialChain # this will not give output from chain 1 (who is wife but only give output from chain 2. To get output from chain 1 and 2 use Sequential Chain)
# chain = SimpleSequentialChain(chains=[about_chain,net_worth_chain])
# response = chain.run("jeff bezos")
# print(response)
#######################################################################################################
from langchain.chains import LLMChain
about_chain = LLMChain(llm=llm, prompt=prompt_template_about,output_key="wife_name")


from langchain.chains import LLMChain
net_worth_chain = LLMChain(llm=llm, prompt=prompt_template_net_worth,output_key="net_worth")

from langchain.chains import SequentialChain
chain = SequentialChain(
    chains=[about_chain,net_worth_chain],
    input_variables=["name"],
    output_variables=["wife_name","net_worth"]
    )
response = chain({'name':'jeff bezos'})
print(response)