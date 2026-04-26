---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:10003
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: Where is the tracking number for the card?
  sentences:
  - How long will it be to get this new card?
  - How long does it take for a cash withdrawal to show?
  - What are your exchange rates calculated from?
- source_sentence: Why is there an extra €1 fee in my statement?
  sentences:
  - There must have been a mistake, why was I charged an extra pound?
  - How many different currencies can I hold money in?
  - How long does it take for me to get my new card?
- source_sentence: I got a card, how do I get it in the app?
  sentences:
  - I am inquiring about a $1 charge on my statement.
  - I tried to get some with-drawls but the machine didn't work. The transaction still
    seems in progress.Seems like  something is wrong,I don't want to be charged for
    Transaction i did not make.
  - I found my card in my jacket this morning, so can I reactivate it?
- source_sentence: I checked on google and the exchange rate you are using is really
    bad. Can you update it?
  sentences:
  - Why is the exchange rate on my card payment different than I expected?
  - Is there a way I can check on the card on route to me?
  - Why has my card been charged an extra pound?
- source_sentence: Hello, I tried to take out some money out of the ATM, but it's
    still showing that it's pending? I really don't want to be charged for this.
  sentences:
  - Why would a cash withdrawal be pending?
  - I tried to get cash out of the ATM but it is taking too long
  - When will a cash withdrawal show up?
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for retrieval.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 384, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    "Hello, I tried to take out some money out of the ATM, but it's still showing that it's pending? I really don't want to be charged for this.",
    'Why would a cash withdrawal be pending?',
    'When will a cash withdrawal show up?',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.8255, 0.7270],
#         [0.8255, 1.0000, 0.8705],
#         [0.7270, 0.8705, 1.0000]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 10,003 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                            | positive                                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            |
  | details | <ul><li>min: 6 tokens</li><li>mean: 15.94 tokens</li><li>max: 79 tokens</li></ul> | <ul><li>min: 6 tokens</li><li>mean: 15.86 tokens</li><li>max: 71 tokens</li></ul> |
* Samples:
  | anchor                                                                    | positive                                                            |
  |:--------------------------------------------------------------------------|:--------------------------------------------------------------------|
  | <code>I am still waiting on my card?</code>                               | <code>What is the expected delivery date for my card?</code>        |
  | <code>What can I do if my card still hasn't arrived after 2 weeks?</code> | <code>What do I do if I still have not received my new card?</code> |
  | <code>I have been waiting over a week. Is the card still coming?</code>   | <code>What's the expected wait time to recieve my new card?</code>  |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 128
- `num_train_epochs`: 5
- `learning_rate`: 0.0002

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 128
- `num_train_epochs`: 5
- `max_steps`: -1
- `learning_rate`: 0.0002
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1.0
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: trackio
- `per_device_eval_batch_size`: 8
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `warmup_ratio`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 0.1266 | 10   | 3.0809        |
| 0.2532 | 20   | 2.9761        |
| 0.3797 | 30   | 2.8140        |
| 0.5063 | 40   | 2.7844        |
| 0.6329 | 50   | 2.5473        |
| 0.7595 | 60   | 2.5995        |
| 0.8861 | 70   | 2.5746        |
| 1.0127 | 80   | 2.4344        |
| 1.1392 | 90   | 2.5207        |
| 1.2658 | 100  | 2.4604        |
| 1.3924 | 110  | 2.4899        |
| 1.5190 | 120  | 2.4685        |
| 1.6456 | 130  | 2.3968        |
| 1.7722 | 140  | 2.4601        |
| 1.8987 | 150  | 2.3518        |
| 2.0253 | 160  | 2.1367        |
| 2.1519 | 170  | 2.3204        |
| 2.2785 | 180  | 2.3703        |
| 2.4051 | 190  | 2.3722        |
| 2.5316 | 200  | 2.3087        |
| 2.6582 | 210  | 2.3304        |
| 2.7848 | 220  | 2.3148        |
| 2.9114 | 230  | 2.3766        |
| 3.0380 | 240  | 2.1824        |
| 3.1646 | 250  | 2.3583        |
| 3.2911 | 260  | 2.2873        |
| 3.4177 | 270  | 2.3099        |
| 3.5443 | 280  | 2.3408        |
| 3.6709 | 290  | 2.2785        |
| 3.7975 | 300  | 2.2392        |
| 3.9241 | 310  | 2.2713        |
| 4.0506 | 320  | 2.0884        |
| 4.1772 | 330  | 2.2726        |
| 4.3038 | 340  | 2.2751        |
| 4.4304 | 350  | 2.2535        |
| 4.5570 | 360  | 2.2943        |
| 4.6835 | 370  | 2.2899        |
| 4.8101 | 380  | 2.2763        |
| 4.9367 | 390  | 2.2821        |


### Training Time
- **Training**: 38.8 seconds

### Framework Versions
- Python: 3.12.7
- Sentence Transformers: 5.4.1
- Transformers: 5.5.4
- PyTorch: 2.5.1+cu121
- Accelerate: 1.13.0
- Datasets: 4.8.4
- Tokenizers: 0.22.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->