from langchain_core.prompts import PromptTemplate

class Langchain:
    def __init__(self, llm_model) -> None:
        self.model = llm_model

    def generate_context(self, text, base_prompt):
        llm = self.model
        prompt = None
        chain = None

        prompt = PromptTemplate(
            template = base_prompt,
            input_variables = {"context"}
        )
        
        chain = prompt | llm
        return chain.invoke({"context": text})

    def generate_rag_context(self, context, question, base_prompt):
        llm = self.model
        prompt = None
        chain = None

        prompt = PromptTemplate(
            template = base_prompt,
            input_variables = {"context", "question"}
        )
        
        chain = prompt | llm
        return chain.invoke({"context": context, "question": question}
            )

    def generate_prompt_only(self, base_prompt):
        llm = self.model

        safe_prompt = base_prompt.replace("{", "{{").replace("}", "}}")
        prompt = PromptTemplate(
            template=safe_prompt,
            input_variables=[]
        )
        chain = prompt | llm
        return chain.invoke({})