import sys
from qdrant_client import QdrantClient
from llama_index.llms.ollama import Ollama
from llama_index import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.vector_stores import QdrantVectorStore
from llama_index.storage import StorageContext
from llama_index.memory import ChatMemoryBuffer
from ..utils.logger import get_logger
from ..utils.exception import exception_handler, CustomException

logger = get_logger(__name__)

class TechSupportAssistant:
    @exception_handler
    def __init__(self):
        self._qdrant_url = "http://localhost:6333"
        self._client = QdrantClient(url=self._qdrant_url, prefer_grpc=False)
        self._llm = Ollama(model="mistral", request_timeout=120.0)
        self._service_context = ServiceContext.from_defaults(llm=self._llm, embed_model="local")
        self._index = None
        self._create_kb()
        self._create_chat_engine()
        logger.info("TechSupportAssistant initialized")

    @exception_handler
    def _create_chat_engine(self):
        memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
        self._chat_engine = self._index.as_chat_engine(
            chat_mode="context",
            memory=memory,
            system_prompt=self._prompt,
        )
        logger.info("Chat engine created")

    @exception_handler
    def _create_kb(self):
        try:
            reader = SimpleDirectoryReader(
                input_files=[r"./data/tech_support_manual.txt"]
            )
            documents = reader.load_data()
            vector_store = QdrantVectorStore(client=self._client, collection_name="tech_support_db")
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            self._index = VectorStoreIndex.from_documents(
                documents, service_context=self._service_context, storage_context=storage_context
            )
            logger.info("Knowledge base created successfully")
        except Exception as e:
            logger.error(f"Error while creating knowledge base: {str(e)}")
            raise CustomException("Failed to create knowledge base", sys.exc_info())

    @exception_handler
    def interact_with_llm(self, user_query):
        logger.info(f"Processing user query: {user_query[:50]}...")
        response = self._chat_engine.chat(user_query)
        logger.info(f"Generated response: {response.response[:50]}...")
        return response.response

    @property
    def _prompt(self):
        return """
        You are an AI Technical Support Assistant.
        Provide clear, concise answers to technical queries.
        If you're unsure, admit it and suggest contacting human support.
        Keep responses brief and focused on solving the user's problem.
        """