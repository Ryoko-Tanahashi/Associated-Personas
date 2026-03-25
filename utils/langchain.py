from langchain_core.prompts import PromptTemplate

class Langchain:
    """
    モデルの設定とプロンプトを受け取って、OpenAIのコンテキストを生成するクラス
    """

    def __init__(self, llm_model) -> None:
        """
        初期化

        Args:
        llm_model: 使用する言語モデル
        """
        self.model = llm_model

    def generate_context(self, text, base_prompt):
        """
        OpenAIのコンテキストを生成する

        Args:
            system_message (str): システムメッセージ
            text (str): ユーザーの入力テキスト
            prompt (str): プロンプト

        Returns:
            str: OpenAI APIからの応答内容
        """
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
        """
        OpenAIのコンテキストを生成する

        Args:
            context (str): コンテキスト
            question (str): 質問
            base_prompt (str): プロンプト

        Returns:
            str: OpenAI APIからの応答内容
        """
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
        # 変数が無く、テンプレートに生の '{' '}' が含まれる場合はエスケープして渡す
        safe_prompt = base_prompt.replace("{", "{{").replace("}", "}}")
        prompt = PromptTemplate(
            template=safe_prompt,
            input_variables=[]  # 変数なし
        )
        chain = prompt | llm
        return chain.invoke({})