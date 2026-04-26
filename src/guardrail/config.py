from typing import List
from nemoguardrails.embeddings.providers.base import EmbeddingModel
from nemoguardrails import LLMRails

class BankingEmbeddingModel(EmbeddingModel):
    engine_name = "banking_embeddings"

    def __init__(self, embedding_model: str, **kwargs):
        from sentence_transformers import SentenceTransformer
        from peft import PeftModel
        
        finetuned_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        base_transformer = finetuned_model[0].auto_model
        peft = PeftModel.from_pretrained(base_transformer, embedding_model)
        merged = peft.merge_and_unload()
        finetuned_model[0].auto_model = merged
        self.model = finetuned_model

    def encode(self, documents: List[str]) -> List[List[float]]:
        embeddings = self.model.encode(
            documents,
            normalize_embeddings=True,
            convert_to_numpy=True
        )
        return embeddings.tolist()

    async def encode_async(self, documents: List[str]) -> List[List[float]]:
        return self.encode(documents)


def init(app: LLMRails):
    print("Registering banking embeddings provider...")
    app.register_embedding_provider(BankingEmbeddingModel, "banking_embeddings")
    print("Done.")