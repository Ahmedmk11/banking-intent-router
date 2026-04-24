from datasets import load_from_disk

train_dataset = load_from_disk("src/data/data/train")
eval_dataset = load_from_disk("src/data/data/eval")

train_dataset = train_dataset.select_columns(['anchor', 'positive', 'negative'])
eval_dataset = eval_dataset.select_columns(['anchor', 'positive', 'negative'])

from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer, SentenceTransformerTrainingArguments
from sentence_transformers.sentence_transformer.losses import TripletLoss
from peft import LoraConfig, get_peft_model

model = SentenceTransformer("all-MiniLM-L6-v2", device="cuda")

lora_config = LoraConfig(
    r=8,
    target_modules=["query", "value"],
    task_type=None,
    lora_alpha=16,
    lora_dropout=0.05,
    inference_mode=False,
)

peft_model = get_peft_model(model[0].auto_model, lora_config)

# trainable params: 73,728 || all params: 22,786,944 || trainable%: 0.3236

model[0].auto_model = peft_model

loss = TripletLoss(model)

args = SentenceTransformerTrainingArguments(
    output_dir="src/training/checkpoints",
    num_train_epochs=3,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    learning_rate=2e-4,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

trainer = SentenceTransformerTrainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    loss=loss,
)

trainer.train()

model.save_pretrained("src/training/model")
