from datasets import load_from_disk

ds = load_from_disk("src/data/triplet_dataset")
ds = ds.select_columns(['text', 'domain'])

import os
import numpy as np
from sentence_transformers import SentenceTransformer

model_path = "src/training/model"
model = SentenceTransformer(model_path, device="cuda")

os.makedirs("src/training/centroids", exist_ok=True)

for domain in ds.unique("domain"):
    print("================================")
    print(f"Computing: {domain}")

    domain_ds = ds.filter(lambda x: x["domain"] == domain)
    texts = domain_ds["text"]

    embeddings = model.encode(texts, convert_to_tensor=True)
    centroid = embeddings.mean(dim=0)
    print(f"Centroid for domain {domain}: {centroid}")

    save_path = f"src/training/centroids/{domain}_centroid.npy"
    np.save(save_path, centroid.cpu().numpy())

    print("================================")
