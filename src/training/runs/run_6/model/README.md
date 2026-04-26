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
# tensor([[1.0000, 0.8833, 0.8062],
#         [0.8833, 1.0000, 0.8609],
#         [0.8062, 0.8609, 1.0000]])
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
| 0.0637  | 10   | 2.4309        |
| 0.1274  | 20   | 2.2408        |
| 0.1911  | 30   | 2.2563        |
| 0.2548  | 40   | 2.0813        |
| 0.3185  | 50   | 2.0715        |
| 0.3822  | 60   | 1.9974        |
| 0.4459  | 70   | 2.0087        |
| 0.5096  | 80   | 2.0055        |
| 0.5732  | 90   | 1.8451        |
| 0.6369  | 100  | 1.8383        |
| 0.7006  | 110  | 1.8236        |
| 0.7643  | 120  | 1.8564        |
| 0.8280  | 130  | 1.8778        |
| 0.8917  | 140  | 1.8303        |
| 0.9554  | 150  | 1.8136        |
| 1.0191  | 160  | 1.7568        |
| 1.0828  | 170  | 1.7366        |
| 1.1465  | 180  | 1.8446        |
| 1.2102  | 190  | 1.7189        |
| 1.2739  | 200  | 1.7840        |
| 1.3376  | 210  | 1.7764        |
| 1.4013  | 220  | 1.7113        |
| 1.4650  | 230  | 1.7294        |
| 1.5287  | 240  | 1.8348        |
| 1.5924  | 250  | 1.7053        |
| 1.6561  | 260  | 1.6520        |
| 1.7197  | 270  | 1.7302        |
| 1.7834  | 280  | 1.6731        |
| 1.8471  | 290  | 1.6663        |
| 1.9108  | 300  | 1.5951        |
| 1.9745  | 310  | 1.7529        |
| 2.0382  | 320  | 1.3617        |
| 2.1019  | 330  | 1.5722        |
| 2.1656  | 340  | 1.5433        |
| 2.2293  | 350  | 1.7026        |
| 2.2930  | 360  | 1.5477        |
| 2.3567  | 370  | 1.6200        |
| 2.4204  | 380  | 1.6683        |
| 2.4841  | 390  | 1.5272        |
| 2.5478  | 400  | 1.6190        |
| 2.6115  | 410  | 1.6048        |
| 2.6752  | 420  | 1.6089        |
| 2.7389  | 430  | 1.4287        |
| 2.8025  | 440  | 1.6768        |
| 2.8662  | 450  | 1.6465        |
| 2.9299  | 460  | 1.5654        |
| 2.9936  | 470  | 1.6192        |
| 3.0573  | 480  | 1.4416        |
| 3.1210  | 490  | 1.5149        |
| 3.1847  | 500  | 1.5541        |
| 3.2484  | 510  | 1.5721        |
| 3.3121  | 520  | 1.4668        |
| 3.3758  | 530  | 1.5774        |
| 3.4395  | 540  | 1.5299        |
| 3.5032  | 550  | 1.5872        |
| 3.5669  | 560  | 1.4996        |
| 3.6306  | 570  | 1.4672        |
| 3.6943  | 580  | 1.4769        |
| 3.7580  | 590  | 1.4847        |
| 3.8217  | 600  | 1.4413        |
| 3.8854  | 610  | 1.5330        |
| 3.9490  | 620  | 1.4394        |
| 4.0127  | 630  | 1.3651        |
| 4.0764  | 640  | 1.3659        |
| 4.1401  | 650  | 1.4058        |
| 4.2038  | 660  | 1.5062        |
| 4.2675  | 670  | 1.4674        |
| 4.3312  | 680  | 1.4588        |
| 4.3949  | 690  | 1.4669        |
| 4.4586  | 700  | 1.3714        |
| 4.5223  | 710  | 1.4809        |
| 4.5860  | 720  | 1.4214        |
| 4.6497  | 730  | 1.5497        |
| 4.7134  | 740  | 1.3286        |
| 4.7771  | 750  | 1.5089        |
| 4.8408  | 760  | 1.5751        |
| 4.9045  | 770  | 1.3092        |
| 4.9682  | 780  | 1.4484        |
| 5.0318  | 790  | 1.3456        |
| 5.0955  | 800  | 1.4596        |
| 5.1592  | 810  | 1.4228        |
| 5.2229  | 820  | 1.3962        |
| 5.2866  | 830  | 1.3982        |
| 5.3503  | 840  | 1.3724        |
| 5.4140  | 850  | 1.4117        |
| 5.4777  | 860  | 1.3614        |
| 5.5414  | 870  | 1.2636        |
| 5.6051  | 880  | 1.4513        |
| 5.6688  | 890  | 1.4225        |
| 5.7325  | 900  | 1.4266        |
| 5.7962  | 910  | 1.3248        |
| 5.8599  | 920  | 1.3810        |
| 5.9236  | 930  | 1.3767        |
| 5.9873  | 940  | 1.3304        |
| 6.0510  | 950  | 1.3094        |
| 6.1146  | 960  | 1.3353        |
| 6.1783  | 970  | 1.3148        |
| 6.2420  | 980  | 1.3905        |
| 6.3057  | 990  | 1.4082        |
| 6.3694  | 1000 | 1.3760        |
| 6.4331  | 1010 | 1.3446        |
| 6.4968  | 1020 | 1.3845        |
| 6.5605  | 1030 | 1.3686        |
| 6.6242  | 1040 | 1.3207        |
| 6.6879  | 1050 | 1.3276        |
| 6.7516  | 1060 | 1.3427        |
| 6.8153  | 1070 | 1.2886        |
| 6.8790  | 1080 | 1.4345        |
| 6.9427  | 1090 | 1.3514        |
| 7.0064  | 1100 | 1.2440        |
| 7.0701  | 1110 | 1.3416        |
| 7.1338  | 1120 | 1.3140        |
| 7.1975  | 1130 | 1.3410        |
| 7.2611  | 1140 | 1.3428        |
| 7.3248  | 1150 | 1.3379        |
| 7.3885  | 1160 | 1.3093        |
| 7.4522  | 1170 | 1.3202        |
| 7.5159  | 1180 | 1.3200        |
| 7.5796  | 1190 | 1.2915        |
| 7.6433  | 1200 | 1.3189        |
| 7.7070  | 1210 | 1.2755        |
| 7.7707  | 1220 | 1.3147        |
| 7.8344  | 1230 | 1.2770        |
| 7.8981  | 1240 | 1.3064        |
| 7.9618  | 1250 | 1.2572        |
| 8.0255  | 1260 | 1.2459        |
| 8.0892  | 1270 | 1.3202        |
| 8.1529  | 1280 | 1.3489        |
| 8.2166  | 1290 | 1.3726        |
| 8.2803  | 1300 | 1.2839        |
| 8.3439  | 1310 | 1.3293        |
| 8.4076  | 1320 | 1.2870        |
| 8.4713  | 1330 | 1.2850        |
| 8.5350  | 1340 | 1.2154        |
| 8.5987  | 1350 | 1.3489        |
| 8.6624  | 1360 | 1.2582        |
| 8.7261  | 1370 | 1.3450        |
| 8.7898  | 1380 | 1.2107        |
| 8.8535  | 1390 | 1.2573        |
| 8.9172  | 1400 | 1.2548        |
| 8.9809  | 1410 | 1.3629        |
| 9.0446  | 1420 | 1.2708        |
| 9.1083  | 1430 | 1.2799        |
| 9.1720  | 1440 | 1.2590        |
| 9.2357  | 1450 | 1.2839        |
| 9.2994  | 1460 | 1.3170        |
| 9.3631  | 1470 | 1.2766        |
| 9.4268  | 1480 | 1.2747        |
| 9.4904  | 1490 | 1.2352        |
| 9.5541  | 1500 | 1.1444        |
| 9.6178  | 1510 | 1.3590        |
| 9.6815  | 1520 | 1.2448        |
| 9.7452  | 1530 | 1.3101        |
| 9.8089  | 1540 | 1.2784        |
| 9.8726  | 1550 | 1.4005        |
| 9.9363  | 1560 | 1.3014        |
| 10.0    | 1570 | 1.1765        |
| 10.0637 | 1580 | 1.2205        |
| 10.1274 | 1590 | 1.2494        |
| 10.1911 | 1600 | 1.1976        |
| 10.2548 | 1610 | 1.3442        |
| 10.3185 | 1620 | 1.3138        |
| 10.3822 | 1630 | 1.3425        |
| 10.4459 | 1640 | 1.2068        |
| 10.5096 | 1650 | 1.2575        |
| 10.5732 | 1660 | 1.3123        |
| 10.6369 | 1670 | 1.3546        |
| 10.7006 | 1680 | 1.2535        |
| 10.7643 | 1690 | 1.2058        |
| 10.8280 | 1700 | 1.2096        |
| 10.8917 | 1710 | 1.2491        |
| 10.9554 | 1720 | 1.2330        |
| 11.0191 | 1730 | 1.1726        |
| 11.0828 | 1740 | 1.2850        |
| 11.1465 | 1750 | 1.3302        |
| 11.2102 | 1760 | 1.2586        |
| 11.2739 | 1770 | 1.1969        |
| 11.3376 | 1780 | 1.2697        |
| 11.4013 | 1790 | 1.3193        |
| 11.4650 | 1800 | 1.2146        |
| 11.5287 | 1810 | 1.2413        |
| 11.5924 | 1820 | 1.2233        |
| 11.6561 | 1830 | 1.2772        |
| 11.7197 | 1840 | 1.2572        |
| 11.7834 | 1850 | 1.2589        |
| 11.8471 | 1860 | 1.0892        |
| 11.9108 | 1870 | 1.1565        |
| 11.9745 | 1880 | 1.2559        |
| 12.0382 | 1890 | 1.2126        |
| 12.1019 | 1900 | 1.1451        |
| 12.1656 | 1910 | 1.2358        |
| 12.2293 | 1920 | 1.2813        |
| 12.2930 | 1930 | 1.2882        |
| 12.3567 | 1940 | 1.3161        |
| 12.4204 | 1950 | 1.1657        |
| 12.4841 | 1960 | 1.1953        |
| 12.5478 | 1970 | 1.2375        |
| 12.6115 | 1980 | 1.2368        |
| 12.6752 | 1990 | 1.1703        |
| 12.7389 | 2000 | 1.2744        |
| 12.8025 | 2010 | 1.1974        |
| 12.8662 | 2020 | 1.1818        |
| 12.9299 | 2030 | 1.3116        |
| 12.9936 | 2040 | 1.2222        |
| 13.0573 | 2050 | 1.1808        |
| 13.1210 | 2060 | 1.2582        |
| 13.1847 | 2070 | 1.2027        |
| 13.2484 | 2080 | 1.2615        |
| 13.3121 | 2090 | 1.1807        |
| 13.3758 | 2100 | 1.2037        |
| 13.4395 | 2110 | 1.2142        |
| 13.5032 | 2120 | 1.2717        |
| 13.5669 | 2130 | 1.1781        |
| 13.6306 | 2140 | 1.1723        |
| 13.6943 | 2150 | 1.2619        |
| 13.7580 | 2160 | 1.2319        |
| 13.8217 | 2170 | 1.1567        |
| 13.8854 | 2180 | 1.1672        |
| 13.9490 | 2190 | 1.1989        |
| 14.0127 | 2200 | 1.2178        |
| 14.0764 | 2210 | 1.1777        |
| 14.1401 | 2220 | 1.2084        |
| 14.2038 | 2230 | 1.1116        |
| 14.2675 | 2240 | 1.1856        |
| 14.3312 | 2250 | 1.1973        |
| 14.3949 | 2260 | 1.1780        |
| 14.4586 | 2270 | 1.1807        |
| 14.5223 | 2280 | 1.1717        |
| 14.5860 | 2290 | 1.2742        |
| 14.6497 | 2300 | 1.2095        |
| 14.7134 | 2310 | 1.2149        |
| 14.7771 | 2320 | 1.2314        |
| 14.8408 | 2330 | 1.2534        |
| 14.9045 | 2340 | 1.2323        |
| 14.9682 | 2350 | 1.2417        |

</details>

### Training Time
- **Training**: 1.8 minutes

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