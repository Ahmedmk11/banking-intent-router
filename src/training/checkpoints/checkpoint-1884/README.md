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
# tensor([[1.0000, 0.9234, 0.8747],
#         [0.9234, 1.0000, 0.9178],
#         [0.8747, 0.9178, 1.0000]])
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
- `num_train_epochs`: 15
- `learning_rate`: 0.0002

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 64
- `num_train_epochs`: 15
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
<details><summary>Click to expand</summary>

| Epoch   | Step | Training Loss |
|:-------:|:----:|:-------------:|
| 0.0637  | 10   | 2.3689        |
| 0.1274  | 20   | 2.1006        |
| 0.1911  | 30   | 2.0475        |
| 0.2548  | 40   | 1.9021        |
| 0.3185  | 50   | 1.8296        |
| 0.3822  | 60   | 1.8061        |
| 0.4459  | 70   | 1.7558        |
| 0.5096  | 80   | 1.7208        |
| 0.5732  | 90   | 1.6189        |
| 0.6369  | 100  | 1.5860        |
| 0.7006  | 110  | 1.5847        |
| 0.7643  | 120  | 1.5666        |
| 0.8280  | 130  | 1.5747        |
| 0.8917  | 140  | 1.5531        |
| 0.9554  | 150  | 1.5090        |
| 1.0191  | 160  | 1.4035        |
| 1.0828  | 170  | 1.3680        |
| 1.1465  | 180  | 1.4901        |
| 1.2102  | 190  | 1.3773        |
| 1.2739  | 200  | 1.4365        |
| 1.3376  | 210  | 1.4004        |
| 1.4013  | 220  | 1.3462        |
| 1.4650  | 230  | 1.3505        |
| 1.5287  | 240  | 1.4066        |
| 1.5924  | 250  | 1.2977        |
| 1.6561  | 260  | 1.2652        |
| 1.7197  | 270  | 1.3524        |
| 1.7834  | 280  | 1.3016        |
| 1.8471  | 290  | 1.3240        |
| 1.9108  | 300  | 1.2123        |
| 1.9745  | 310  | 1.3249        |
| 2.0382  | 320  | 1.0137        |
| 2.1019  | 330  | 1.1446        |
| 2.1656  | 340  | 1.1202        |
| 2.2293  | 350  | 1.2736        |
| 2.2930  | 360  | 1.1697        |
| 2.3567  | 370  | 1.1973        |
| 2.4204  | 380  | 1.2149        |
| 2.4841  | 390  | 1.1462        |
| 2.5478  | 400  | 1.1689        |
| 2.6115  | 410  | 1.1579        |
| 2.6752  | 420  | 1.1553        |
| 2.7389  | 430  | 1.0615        |
| 2.8025  | 440  | 1.2660        |
| 2.8662  | 450  | 1.2175        |
| 2.9299  | 460  | 1.1380        |
| 2.9936  | 470  | 1.2244        |
| 3.0573  | 480  | 1.0078        |
| 3.1210  | 490  | 1.1066        |
| 3.1847  | 500  | 1.0621        |
| 3.2484  | 510  | 1.1699        |
| 3.3121  | 520  | 1.0587        |
| 3.3758  | 530  | 1.1041        |
| 3.4395  | 540  | 1.0716        |
| 3.5032  | 550  | 1.1399        |
| 3.5669  | 560  | 1.1073        |
| 3.6306  | 570  | 1.0555        |
| 3.6943  | 580  | 1.1091        |
| 3.7580  | 590  | 1.0730        |
| 3.8217  | 600  | 1.0176        |
| 3.8854  | 610  | 1.1127        |
| 3.9490  | 620  | 1.0575        |
| 4.0127  | 630  | 0.9905        |
| 4.0764  | 640  | 0.9852        |
| 4.1401  | 650  | 0.9808        |
| 4.2038  | 660  | 1.0759        |
| 4.2675  | 670  | 1.0310        |
| 4.3312  | 680  | 1.0323        |
| 4.3949  | 690  | 1.0591        |
| 4.4586  | 700  | 0.9481        |
| 4.5223  | 710  | 1.0518        |
| 4.5860  | 720  | 0.9834        |
| 4.6497  | 730  | 1.1139        |
| 4.7134  | 740  | 0.9409        |
| 4.7771  | 750  | 1.0907        |
| 4.8408  | 760  | 1.1039        |
| 4.9045  | 770  | 0.8823        |
| 4.9682  | 780  | 1.0225        |
| 5.0318  | 790  | 0.9104        |
| 5.0955  | 800  | 0.9802        |
| 5.1592  | 810  | 0.9986        |
| 5.2229  | 820  | 0.9258        |
| 5.2866  | 830  | 0.9534        |
| 5.3503  | 840  | 0.9214        |
| 5.4140  | 850  | 0.9471        |
| 5.4777  | 860  | 0.9624        |
| 5.5414  | 870  | 0.8888        |
| 5.6051  | 880  | 1.0042        |
| 5.6688  | 890  | 0.9851        |
| 5.7325  | 900  | 1.0291        |
| 5.7962  | 910  | 0.9279        |
| 5.8599  | 920  | 0.9173        |
| 5.9236  | 930  | 0.9822        |
| 5.9873  | 940  | 0.9178        |
| 6.0510  | 950  | 0.8713        |
| 6.1146  | 960  | 0.9277        |
| 6.1783  | 970  | 0.9189        |
| 6.2420  | 980  | 0.9395        |
| 6.3057  | 990  | 0.9540        |
| 6.3694  | 1000 | 0.9779        |
| 6.4331  | 1010 | 0.9282        |
| 6.4968  | 1020 | 0.9135        |
| 6.5605  | 1030 | 0.9388        |
| 6.6242  | 1040 | 0.9136        |
| 6.6879  | 1050 | 0.8982        |
| 6.7516  | 1060 | 0.9025        |
| 6.8153  | 1070 | 0.9269        |
| 6.8790  | 1080 | 0.9797        |
| 6.9427  | 1090 | 0.9347        |
| 7.0064  | 1100 | 0.8387        |
| 7.0701  | 1110 | 0.8866        |
| 7.1338  | 1120 | 0.8674        |
| 7.1975  | 1130 | 0.9067        |
| 7.2611  | 1140 | 0.9084        |
| 7.3248  | 1150 | 0.9185        |
| 7.3885  | 1160 | 0.8868        |
| 7.4522  | 1170 | 0.9073        |
| 7.5159  | 1180 | 0.8605        |
| 7.5796  | 1190 | 0.8314        |
| 7.6433  | 1200 | 0.8648        |
| 7.7070  | 1210 | 0.8472        |
| 7.7707  | 1220 | 0.8554        |
| 7.8344  | 1230 | 0.8709        |
| 7.8981  | 1240 | 0.8927        |
| 7.9618  | 1250 | 0.8382        |
| 8.0255  | 1260 | 0.8217        |
| 8.0892  | 1270 | 0.8743        |
| 8.1529  | 1280 | 0.8922        |
| 8.2166  | 1290 | 0.8884        |
| 8.2803  | 1300 | 0.8371        |
| 8.3439  | 1310 | 0.9051        |
| 8.4076  | 1320 | 0.8505        |
| 8.4713  | 1330 | 0.8403        |
| 8.5350  | 1340 | 0.8309        |
| 8.5987  | 1350 | 0.8584        |
| 8.6624  | 1360 | 0.8797        |
| 8.7261  | 1370 | 0.8937        |
| 8.7898  | 1380 | 0.8300        |
| 8.8535  | 1390 | 0.8080        |
| 8.9172  | 1400 | 0.8370        |
| 8.9809  | 1410 | 0.9309        |
| 9.0446  | 1420 | 0.8240        |
| 9.1083  | 1430 | 0.8497        |
| 9.1720  | 1440 | 0.8234        |
| 9.2357  | 1450 | 0.8269        |
| 9.2994  | 1460 | 0.8654        |
| 9.3631  | 1470 | 0.8302        |
| 9.4268  | 1480 | 0.8102        |
| 9.4904  | 1490 | 0.8320        |
| 9.5541  | 1500 | 0.7896        |
| 9.6178  | 1510 | 0.9188        |
| 9.6815  | 1520 | 0.7977        |
| 9.7452  | 1530 | 0.8645        |
| 9.8089  | 1540 | 0.8464        |
| 9.8726  | 1550 | 0.8959        |
| 9.9363  | 1560 | 0.8642        |
| 10.0    | 1570 | 0.8077        |
| 10.0637 | 1580 | 0.8313        |
| 10.1274 | 1590 | 0.8057        |
| 10.1911 | 1600 | 0.7766        |
| 10.2548 | 1610 | 0.8218        |
| 10.3185 | 1620 | 0.8348        |
| 10.3822 | 1630 | 0.8991        |
| 10.4459 | 1640 | 0.8288        |
| 10.5096 | 1650 | 0.8344        |
| 10.5732 | 1660 | 0.8558        |
| 10.6369 | 1670 | 0.8922        |
| 10.7006 | 1680 | 0.8549        |
| 10.7643 | 1690 | 0.7838        |
| 10.8280 | 1700 | 0.7861        |
| 10.8917 | 1710 | 0.7840        |
| 10.9554 | 1720 | 0.8219        |
| 11.0191 | 1730 | 0.7976        |
| 11.0828 | 1740 | 0.7867        |
| 11.1465 | 1750 | 0.8400        |
| 11.2102 | 1760 | 0.8223        |
| 11.2739 | 1770 | 0.7711        |
| 11.3376 | 1780 | 0.8185        |
| 11.4013 | 1790 | 0.8211        |
| 11.4650 | 1800 | 0.7547        |
| 11.5287 | 1810 | 0.8228        |
| 11.5924 | 1820 | 0.7597        |
| 11.6561 | 1830 | 0.8256        |
| 11.7197 | 1840 | 0.8418        |
| 11.7834 | 1850 | 0.8111        |
| 11.8471 | 1860 | 0.7109        |
| 11.9108 | 1870 | 0.7617        |
| 11.9745 | 1880 | 0.7997        |

</details>

### Training Time
- **Training**: 1.9 minutes

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