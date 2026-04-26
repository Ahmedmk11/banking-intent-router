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
# tensor([[1.0000, 0.8488, 0.7128],
#         [0.8488, 1.0000, 0.8464],
#         [0.7128, 0.8464, 1.0000]])
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

- `per_device_train_batch_size`: 64
- `num_train_epochs`: 10
- `learning_rate`: 0.0001

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 64
- `num_train_epochs`: 10
- `max_steps`: -1
- `learning_rate`: 0.0001
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
<details><summary>Click to expand</summary>

| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 0.0637 | 10   | 2.4474        |
| 0.1274 | 20   | 2.2941        |
| 0.1911 | 30   | 2.3623        |
| 0.2548 | 40   | 2.2093        |
| 0.3185 | 50   | 2.2453        |
| 0.3822 | 60   | 2.1724        |
| 0.4459 | 70   | 2.2115        |
| 0.5096 | 80   | 2.1670        |
| 0.5732 | 90   | 2.0043        |
| 0.6369 | 100  | 1.9749        |
| 0.7006 | 110  | 1.9543        |
| 0.7643 | 120  | 2.0094        |
| 0.8280 | 130  | 2.0047        |
| 0.8917 | 140  | 1.9279        |
| 0.9554 | 150  | 1.9211        |
| 1.0191 | 160  | 1.8694        |
| 1.0828 | 170  | 1.8837        |
| 1.1465 | 180  | 1.9586        |
| 1.2102 | 190  | 1.8628        |
| 1.2739 | 200  | 1.9092        |
| 1.3376 | 210  | 1.8931        |
| 1.4013 | 220  | 1.8500        |
| 1.4650 | 230  | 1.8387        |
| 1.5287 | 240  | 1.9530        |
| 1.5924 | 250  | 1.8382        |
| 1.6561 | 260  | 1.7666        |
| 1.7197 | 270  | 1.8605        |
| 1.7834 | 280  | 1.8172        |
| 1.8471 | 290  | 1.7851        |
| 1.9108 | 300  | 1.7143        |
| 1.9745 | 310  | 1.9010        |
| 2.0382 | 320  | 1.4878        |
| 2.1019 | 330  | 1.6957        |
| 2.1656 | 340  | 1.6937        |
| 2.2293 | 350  | 1.8782        |
| 2.2930 | 360  | 1.6928        |
| 2.3567 | 370  | 1.7657        |
| 2.4204 | 380  | 1.8328        |
| 2.4841 | 390  | 1.6761        |
| 2.5478 | 400  | 1.7759        |
| 2.6115 | 410  | 1.7747        |
| 2.6752 | 420  | 1.7636        |
| 2.7389 | 430  | 1.6002        |
| 2.8025 | 440  | 1.8647        |
| 2.8662 | 450  | 1.8352        |
| 2.9299 | 460  | 1.7562        |
| 2.9936 | 470  | 1.7964        |
| 3.0573 | 480  | 1.6026        |
| 3.1210 | 490  | 1.7243        |
| 3.1847 | 500  | 1.7628        |
| 3.2484 | 510  | 1.7989        |
| 3.3121 | 520  | 1.6409        |
| 3.3758 | 530  | 1.7573        |
| 3.4395 | 540  | 1.7468        |
| 3.5032 | 550  | 1.7715        |
| 3.5669 | 560  | 1.6965        |
| 3.6306 | 570  | 1.6452        |
| 3.6943 | 580  | 1.6852        |
| 3.7580 | 590  | 1.6353        |
| 3.8217 | 600  | 1.6663        |
| 3.8854 | 610  | 1.7511        |
| 3.9490 | 620  | 1.6423        |
| 4.0127 | 630  | 1.5643        |
| 4.0764 | 640  | 1.5472        |
| 4.1401 | 650  | 1.6297        |
| 4.2038 | 660  | 1.7447        |
| 4.2675 | 670  | 1.7028        |
| 4.3312 | 680  | 1.6724        |
| 4.3949 | 690  | 1.6805        |
| 4.4586 | 700  | 1.6054        |
| 4.5223 | 710  | 1.6745        |
| 4.5860 | 720  | 1.6539        |
| 4.6497 | 730  | 1.7941        |
| 4.7134 | 740  | 1.5544        |
| 4.7771 | 750  | 1.7323        |
| 4.8408 | 760  | 1.8078        |
| 4.9045 | 770  | 1.5367        |
| 4.9682 | 780  | 1.6771        |
| 5.0318 | 790  | 1.5922        |
| 5.0955 | 800  | 1.6865        |
| 5.1592 | 810  | 1.6715        |
| 5.2229 | 820  | 1.6413        |
| 5.2866 | 830  | 1.6329        |
| 5.3503 | 840  | 1.6005        |
| 5.4140 | 850  | 1.6712        |
| 5.4777 | 860  | 1.6288        |
| 5.5414 | 870  | 1.4987        |
| 5.6051 | 880  | 1.7021        |
| 5.6688 | 890  | 1.6762        |
| 5.7325 | 900  | 1.6776        |
| 5.7962 | 910  | 1.5675        |
| 5.8599 | 920  | 1.6444        |
| 5.9236 | 930  | 1.5833        |
| 5.9873 | 940  | 1.5487        |
| 6.0510 | 950  | 1.6100        |
| 6.1146 | 960  | 1.5858        |
| 6.1783 | 970  | 1.5544        |
| 6.2420 | 980  | 1.5960        |
| 6.3057 | 990  | 1.6599        |
| 6.3694 | 1000 | 1.6380        |
| 6.4331 | 1010 | 1.6121        |
| 6.4968 | 1020 | 1.6510        |
| 6.5605 | 1030 | 1.6178        |
| 6.6242 | 1040 | 1.5630        |
| 6.6879 | 1050 | 1.5892        |
| 6.7516 | 1060 | 1.5821        |
| 6.8153 | 1070 | 1.5064        |
| 6.8790 | 1080 | 1.6991        |
| 6.9427 | 1090 | 1.6048        |
| 7.0064 | 1100 | 1.4956        |
| 7.0701 | 1110 | 1.6092        |
| 7.1338 | 1120 | 1.6063        |
| 7.1975 | 1130 | 1.5969        |
| 7.2611 | 1140 | 1.6192        |
| 7.3248 | 1150 | 1.6008        |
| 7.3885 | 1160 | 1.5602        |
| 7.4522 | 1170 | 1.5644        |
| 7.5159 | 1180 | 1.5802        |
| 7.5796 | 1190 | 1.5769        |
| 7.6433 | 1200 | 1.5602        |
| 7.7070 | 1210 | 1.5550        |
| 7.7707 | 1220 | 1.5860        |
| 7.8344 | 1230 | 1.5869        |
| 7.8981 | 1240 | 1.5610        |
| 7.9618 | 1250 | 1.5494        |
| 8.0255 | 1260 | 1.5242        |
| 8.0892 | 1270 | 1.5916        |
| 8.1529 | 1280 | 1.6734        |
| 8.2166 | 1290 | 1.6912        |
| 8.2803 | 1300 | 1.5668        |
| 8.3439 | 1310 | 1.6137        |
| 8.4076 | 1320 | 1.5688        |
| 8.4713 | 1330 | 1.5685        |
| 8.5350 | 1340 | 1.4918        |
| 8.5987 | 1350 | 1.6187        |
| 8.6624 | 1360 | 1.5118        |
| 8.7261 | 1370 | 1.6192        |
| 8.7898 | 1380 | 1.5204        |
| 8.8535 | 1390 | 1.5461        |
| 8.9172 | 1400 | 1.5357        |
| 8.9809 | 1410 | 1.6156        |
| 9.0446 | 1420 | 1.5686        |
| 9.1083 | 1430 | 1.5871        |
| 9.1720 | 1440 | 1.5260        |
| 9.2357 | 1450 | 1.5992        |
| 9.2994 | 1460 | 1.5879        |
| 9.3631 | 1470 | 1.5769        |
| 9.4268 | 1480 | 1.5652        |
| 9.4904 | 1490 | 1.5205        |
| 9.5541 | 1500 | 1.4290        |
| 9.6178 | 1510 | 1.6722        |
| 9.6815 | 1520 | 1.5488        |
| 9.7452 | 1530 | 1.6163        |
| 9.8089 | 1540 | 1.5593        |
| 9.8726 | 1550 | 1.6994        |
| 9.9363 | 1560 | 1.6335        |
| 10.0   | 1570 | 1.4793        |

</details>

### Training Time
- **Training**: 1.3 minutes

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