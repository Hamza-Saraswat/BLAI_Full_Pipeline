<!-- url: https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/ -->
<!-- fetched via web_extract 2026-10-24, tier 2 (docs, NVIDIA technical blog, Jul 03 2023, Hongxiao Bai and Yun Li). -->

[Technical Blog](https://developer.nvidia.com/blog)

[Subscribe](https://developer.nvidia.com/email-signup)

[Related Resources](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/#main-content-end)

[Data Science](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/)

English中文

# Structured Sparsity in the NVIDIA Ampere Architecture and Applications in Search Engines

![Decorative image of structured sparsity](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/structured-sparsity-featured-1024x576.png)

Jul 03, 2023


By [Hongxiao Bai](https://developer.nvidia.com/blog/author/hongxiaob/ "Posts by Hongxiao Bai") and [Yun Li](https://developer.nvidia.com/blog/author/charlesyli/ "Posts by Yun Li")

+14

Like

[Discuss (0)](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/#entry-content-comments)

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F)
- [T](https://twitter.com/intent/tweet?text=Structured+Sparsity+in+the+NVIDIA+Ampere+Architecture+and+Applications+in+Search+Engines+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F&title=Structured+Sparsity+in+the+NVIDIA+Ampere+Architecture+and+Applications+in+Search+Engines+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F)

## AI-Generated Summary

- NVIDIA Ampere and Hopper architecture GPUs introduce fine-grained structured sparsity with a 2:4 pattern that enables sparse Tensor Cores to process only non-zero values for up to 2x compute throughput during inference.
- Training recipes including basic retraining, progressive sparsity that divides target sparsity into incremental steps, and sparse-QAT combining sparsity with int8 quantization and MiniLM knowledge distillation maintain or improve model accuracy while achieving 50% weight sparsity.
- Tencent MLPD applied progressive training techniques to achieve 1.3–1.8x acceleration in offline search services using structured sparsity and quantization.
- NVIDIA TensorRT 8.0 and later supports sparse convolution inference when weights have 2:4 sparsity and the sparsity flag is enabled in the builder configuration.
- For variable input sizes, cuSPARSELt can enhance TensorRT performance through custom plug-ins that initialize multiple sparse GEMM plans for different input dimensions.
- Search engine applications including relevance prediction, query performance prediction, recall tasks, and text-to-image generation demonstrate sparse models achieving comparable or higher accuracy than dense baselines with up to 4x inference speedup.

### Next Steps

- Watch the [Structured Sparsity in the NVIDIA Ampere Architecture and its Applications in Tencent WeChat Search](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s51299/) GTC session for deeper technical details.
- Download the latest [TensorRT](https://developer.nvidia.com/nvidia-tensorrt-download) to enable sparse weight inference in your deployment pipeline.
- Download the latest [cuSPARSELt](https://developer.nvidia.com/cusparselt-downloads) to build custom sparse GEMM plug-ins for variable input sizes.

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. [Learn more](https://www.nvidia.com/en-us/agreements/trustworthy-ai/terms/)

Deep learning is achieving significant success in various fields and areas, as it has revolutionized the way we analyze, understand, and manipulate data. There are many success stories in computer vision, natural language processing (NLP), medical diagnosis and health care, autonomous vehicles, recommendation systems, and climate and weather modeling.

In an era of ever-growing neural network models, the high demand for computational speed becomes a big challenge for hardware and software. Model pruning and low-precision inference are useful solutions.

Starting with the NVIDIA Ampere architecture and the introduction of the A100 Tensor Core GPU, NVIDIA GPUs have the fine-grained structured sparsity feature, which can be used to accelerate inference. For more information, see the [NVIDIA A100 Tensor Core GPU Architecture: Unprecedented Acceleration at Every Scale](https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf) whitepaper.

In this post, we introduce some training recipes for such sparse models to maintain accuracy, including the basic recipes, the progressive recipes, and the combination with int8 quantization. We also discuss how to do the inference with the structured sparsity in the NVIDIA Ampere architecture.

Tencent’s Machine Learning Platform department (MLPD) used the progressive training techniques to simplify training and achieve better accuracy. With the sparsity feature and some quantization techniques, they achieved 1.3–1.8x acceleration in Tencent’s offline services.

## Structured sparsity in the NVIDIA Ampere architecture [Scroll to Structured sparsity in the NVIDIA Ampere architecture section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#structured_sparsity_in_the_nvidia_ampere_architecture)

NVIDIA Ampere and NVIDIA Hopper architecture GPUs add the new feature of fine-grained structured sparsity, which can mainly be used to accelerate inference workloads. This feature is supported by sparse Tensor Cores, which require a 2:4 sparsity pattern. Among each group of four contiguous values, at least two must be zero, which is a 50% sparsity rate.

This pattern can have efficient memory access, good speedup, and can easily recover accuracy. After compression, only non-zero values and the associated index metadata are stored (Figure 1). The sparse Tensor Cores process only the non-zero values when doing matrix multiplication and theoretically, the compute throughput would be 2x compared to the equivalent dense matrix multiplication.

![Diagram shows a structured-sparse matrix with a 2:4 sparsity pattern. In four contiguous values, at least two values are zero. After compression, only non-zero values and the associated index metadata are stored.](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/2-4-structured-sparsity-pattern.png) _Figure 1. 2:4 structured sparsity pattern and compression_

Structured sparsity can mainly be applied on fully connected layers and convolution layers where 2:4 sparse weights are provided. If you prune the weights of these layers in advance, then these layers can be accelerated by structured sparsity.

## Training recipes [Scroll to Training recipes section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#training_recipes)

As directly pruning the weights decreases the model accuracy, you should do some training to recover the accuracy when using the structured sparsity. Here, we introduce some basic recipes and new progressive recipes.

### Basic recipes [Scroll to Basic recipes section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#basic_recipes)

The basic recipes maintain the model accuracy without any hyperparameter tuning. For more information, see [Accelerating Sparse Deep Neural Networks](https://arxiv.org/abs/2104.08378).

The workflow is easy to follow:

1. Train a model without sparsity.
2. Prune the model in a 2:4 sparse pattern for the FC and convolution layers.
3. Retrain the pruned model by following these rules:
1. Initialize the weights to the values from Step 2.
2. Use the same optimizer and hyperparameter (learning rate, schedule, number of epochs, and so on) as in Step 1.
3. Maintain the sparsity pattern computed in Step 2.

![Diagram shows that the basic training recipe is simply repeating the original dense training with the pruned weights and the masked optimizer.](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/basic-training-recipe.png) _Figure 2. Basic training recipe_

There are also some advanced recipes for complicated cases.

For example, apply sparse training in multiple stages. For some object detection models, if the dataset in the downstream task is large enough, you can just repeat the fine-tuning with sparsity. For models like BERT-SQuAD, the dataset is relatively small, and you must apply the sparsity to the pretraining phase for better accuracy.

Also, you can easily combine the sparsity training with int8 QAT by inserting the quant nodes before fine-tuning. All these training and fine-tuning methods are one-shot, as the final model is obtained after one sparse training process.

### Progressive training recipes [Scroll to Progressive training recipes section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#progressive_training_recipes)

One-shot sparse fine-tuning can cover most tasks and achieve speedup without accuracy loss. On the other hand, for some difficult tasks that are sensitive to weight changes, one-shot sparsity for all weights causes large information loss. It’s difficult to recover accuracy by only fine-tuning with small datasets, and sparse pretraining is also needed for these tasks.

Sparse pretraining requires more data and is more time-consuming. So, inspired by the pruning method for CNN, the progressive sparsity is introduced to apply sparsity only on fine-tuning phase for such tasks without too much accuracy loss. For more information, see [Learning Both Weights and Connections for Efficient Neural Networks](https://arxiv.org/pdf/1506.02626.pdf).

![Diagram compares one-shot sparsity and progressive sparsity to show that the latter divides the sparsity ratio into several steps for easy recovery.](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/idea-progressive-sparsity.png) _Figure 3. The idea of progressive sparsity_

The key idea of progressive sparsity is to divide the target sparsity ratio into several small steps.

𝑆𝑡⁢𝑎⁢𝑟⁢𝑔⁡𝑒⁢𝑡=𝑁∑𝑛−1𝑆𝑛

As shown in the equation and Figure 4, for a target sparsity ratio _S_, you divide it into _N_ steps, which facilitates the rapid recovery of information during the fine-tuning process. Based on our experiments, progressive sparsity can achieve higher accuracy than one-shot sparsity with the same fine-tuning epochs.

![Diagram shows three-step example case for progressive sparsity: prune 25% weights, fine-tune, and then prune 50% weights and finetune.](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/progressive-sparsity.png)_Figure 4. Progressive sparsity (50% sparsity in a 2:4 pattern）_

Taking 50% sparsity in a 2:4 pattern as a simple case, divide the sparsity ratio into two steps, and progressively sparse and fine-tune the weights in the network.

As shown in Figure 4, you first compute the mask of weights to achieve 25% sparsity, and then perform sparse fine-tuning to recover the accuracy. Finally, you recalculate the mask to 50% sparsity and fine-tuning the network to obtain a sparse model without loss of accuracy.

### Sparse-QAT: Combine sparsity with quantization and distillation [Scroll to Sparse-QAT: Combine sparsity with quantization and distillation section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#sparse-qat_combine_sparsity_with_quantization_and_distillation)

To obtain lighter models, you can further combine sparsity with quantization and distillation in a method called sparse-QAT.

#### Quantization (PTQ and QAT)

The following equation formulates a general quantization procedure. For a float32 value x, use 𝑄⁡\[𝑥\] to denote its quantized value with K-bit representation.

𝑄⁡\[𝑥\]=𝑠×𝑟⁢𝑜⁢𝑢⁢𝑛⁢𝑑⁡(𝑐⁢𝑙⁢𝑎⁢𝑚⁢𝑝⁡(𝑥𝑠,𝑙𝑚𝑖𝑛,𝑙𝑚𝑎𝑥))

In general, you first quantize the original parameters to a certain range and round them to integers. Then, you use the quantization scale to recover the original value. This motivates your first quantization method, calibration, also known as post-training quantization (PTQ).

In calibration, a critical thing is to set an appropriate quantization scale. If the scale is too large, it is less accurate for numbers within the range. On the contrary, if the scale is too small, it results in too many numbers outside the range of 𝑙𝑚𝑖𝑛 to 𝑙𝑚𝑎𝑥.

Therefore, to balance these two aspects, you first obtain the distribution of tensor values and then set the quantization scale to include 99.99% of the numbers. It has been proved in multiple works that this method is helpful in finding a good quantization scale during calibration.

However, although you have set a reasonable quantization scale for calibration, the accuracy still drops significantly for 8 bits. You then introduce quantization-aware training (QAT) to further improve the accuracy after calibration. The idea of QAT is to train a model with simulation quantization.

In the forward pass, you quantize the weights to int8 and dequantize them to float in the node to simulate quantization. In the backward pass, the gradients are used to update the model weights, which is called straight-through estimation (STE). The key idea is the following equation:

𝜕𝑓𝜕𝑥=𝜕𝑓𝜕𝑄⁡\[𝑥\]

Gradients of values in the threshold ranges are passed directly in the backward pass, and gradients of values outside the threshold ranges are clipped to 0.

#### Knowledge distillation

In addition to the previous methods, we introduced knowledge distillation (KD) to further ensure the accuracy of the sparse-QAT model. Take the original model as the teacher and the quantized sparse model as the student.

During the fine-tuning process, we adopted mini-distillation, which is a layer-wise distillation. With MiniLM, you only have to use the self-attention output of the last transformer layer to do the distillation. You can even achieve higher accuracy than the teacher model after Sparse-QAT. For more information, see [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](https://arxiv.org/abs/2002.10957).

#### Pipeline of Sparse-QAT

Figure 5 shows the pipeline of Sparse-QAT. You use sparsity, quantization, and KD together to get the final sparse-int8 model. There are three passes:

- **Sparsity pass:** Apply progressive sparsity to get a sparse tensor.
- **Quantization pass:** Use PTQ and QAT to get an int8 tensor.
- **Knowledge distillation pass:** Use MiniLM to guarantee the accuracy of the final sparse-int8 model.

![Workflow diagram shows that sparsity, quantization, and knowledge distillation are combined to get the final sparse-int8 model.](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/pipeline-sparse-qat.png)_Figure 5. Pipeline of sparse-QAT_

## Inference with NVIDIA Ampere architecture sparsity [Scroll to Inference with NVIDIA Ampere architecture sparsity section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#inference_with_nvidia_ampere_architecture_sparsity)

After the sparse model is trained, you can use TensorRT and cuSPARSELt to accelerate the inference with NVIDIA Ampere architecture structured sparsity.

### Inference with NVIDIA TensorRT [Scroll to Inference with NVIDIA TensorRT section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#inference_with_nvidia_tensorrt)

NVIDIA TensorRT supports sparse convolution as of version 8.0. GEMMs should be replaced with 1×1 convolutions to use the sparsity inference. Enabling sparsity in TensorRT is easy. Before importing into TensorRT, the weights of the model should have 2:4 sparsity. If `trtexec` is used to build the engine, set the `–sparsity=enable` flag. If you are writing codes or scripts to build the engine, set the build config as follows:

For C++: `config->setFlag(BuilderFlag::kSPARSE_WEIGHTS)`

For Python: `config.set_flag(trt.BuilderFlag.SPARSE_WEIGHTS)`

### Use NVIDIA cuSPARSELt to enhance TensorRT [Scroll to Use NVIDIA cuSPARSELt to enhance TensorRT section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#use_nvidia_cusparselt_to_enhance_tensorrt)

For some use cases, the input sizes may vary and TensorRT may not provide the best performance. You can use NVIDIA cuSPARSELt to further accelerate these cases.

The solution is to write TensoRT plug-ins with cuSPARSELt. Initialize multiple descriptors and plans of cuSPARSELt sparse GEMM for different input sizes and choose an appropriate plan for each input.

Assuming that you implement the `SpmmPluginDynamic` plug-in, it inherits from `nvinfer1::IPluginV2DynamicExt` and you use a private struct to store the plans.

|     |
| --- |
| `struct``cusparseLtContext {`<br>```cusparseLtHandle_t handle;`<br>```std::vector<cusparseLtMatmulPlan_t> plans;`<br>```std::vector<cusparseLtMatDescriptor_t> matAs, matBs, matCs;`<br>```std::vector<cusparseLtMatmulDescriptor_t> matmuls;`<br>```std::vector<cusparseLtMatmulAlgSelection_t> alg_sels;`<br>`}` |

A TensorRT plug-in should implement the `configurePlugin` method, which sets up the plug-in according to the input and output types and sizes. You initialize the cuSPARSELt-related structures in this method.

There is a constraint that the input size of cuSPARSELt should be a multiple of 4, 8, or 16 depending on the data type. For this post, we set it to a multiple of 16. For more information about the constraints, see [cusparseLtDenseDescriptorInit](https://docs.nvidia.com/cuda/cusparselt/functions.html#cusparseltdensedescriptorinit).

|     |
| --- |
| `for``(``int``i = 0; i < size_num; ++i) {`<br>```m = 16 * (i + 1);`<br>```int``alignment = 16;`<br>```CHECK_CUSPARSE(cusparseLtStructuredDescriptorInit(`<br>```&handle, &matBs[i], n, k, k, alignment, type, CUSPARSE_ORDER_ROW,`<br>```CUSPARSELT_SPARSITY_50_PERCENT))`<br>```CHECK_CUSPARSE(cusparseLtDenseDescriptorInit(`<br>```&handle, &matAs[i], m, k, k, alignment, type, CUSPARSE_ORDER_ROW))`<br>```CHECK_CUSPARSE(cusparseLtDenseDescriptorInit(`<br>```&handle, &matCs[i], m, n, n, alignment, type, CUSPARSE_ORDER_ROW))`<br>```CHECK_CUSPARSE(cusparseLtMatmulDescriptorInit(`<br>```&handle, &matmuls[i], CUSPARSE_OPERATION_NON_TRANSPOSE,`<br>```CUSPARSE_OPERATION_TRANSPOSE, &matAs[i], &matBs[i], &matCs[i], &matCs[i], compute_type))`<br>```CHECK_CUSPARSE(cusparseLtMatmulAlgSelectionInit(`<br>```&handle, &alg_sels[i], &matmuls[i], CUSPARSELT_MATMUL_ALG_DEFAULT))`<br>```int``split_k = 1;`<br>```CHECK_CUSPARSE(cusparseLtMatmulAlgSetAttribute(`<br>```&handle, &alg_sels[i], CUSPARSELT_MATMUL_SPLIT_K, &split_k,``sizeof``(split_k)))`<br>```int``alg_id = 0;`<br>```CHECK_CUSPARSE(cusparseLtMatmulAlgSetAttribute(`<br>```&handle, &alg_sels[i], CUSPARSELT_MATMUL_ALG_CONFIG_ID, &alg_id,``sizeof``(alg_id)))`<br>```size_t ws{0};`<br>```CHECK_CUSPARSE(cusparseLtMatmulPlanInit(&handle, &plans[i], &matmuls[i], &alg_sels[i],`<br>```ws))`<br>```CHECK_CUSPARSE(`<br>```cusparseLtMatmulGetWorkspace(&handle, &plans[i], &ws))`<br>```workspace_size = std::max(workspace_size, ws);`<br>`}` |

In the `enqueue` function, you can select the proper plan to do the `matmul` operation:

|     |
| --- |
| `int``m = inputDesc->dims.d[0];`<br>`int``idx = (m + 15) / 16 - 1;`<br>`float``alpha = 1.0f;`<br>`float``beta = 0.0f;`<br>`auto input = static_cast<``const``float``*>(inputs[0]);`<br>`auto output = static_cast<``float``*>(outputs[0]);`<br>`cusparseStatus_t status = cusparseLtMatmul(`<br>```&handle, &plans[idx], &alpha, input,`<br>```weight_compressed, &beta, output, output, workSpace, &stream, 1);` |

## Some applications in search engines [Scroll to Some applications in search engines section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#some_applications_in_search_engines)

In this section, we show four applications that take advantage of sparsity in search engines:

- **Search relevance prediction** aims to evaluate the relevance between the input text and the videos in the database.
- **Query performance prediction** is used for the document recall delivery strategy.
- A **recall task** for recalling the most relevant texts.
- The **text-to-image task** automatically generates corresponding pictures according to the input prompt.

### Search relevance cases [Scroll to Search relevance cases section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#search_relevance_cases)

The results of these cases are evaluated with positive negative rate (PNR) or accuracy (Acc).

In relevance case 1, we ran Sparse-QAT and obtained a sparse-int8 model with higher PNR than the online int8 model in two important evaluation indices.

|     |     |     |
| --- | --- | --- |
| **Model** | **Evaluation** **Index A** | **Evaluation** **Index B** |
| float32 | 4.0138 | 3.1384 |
| int8 (online) | 3.9454 | 2.9120 |
| Sparse-int8 | 4.0406 | 2.9591 |

_Table 1. Relevance case 1 in a search engine (PNR)_

In relevance case 2, the sparse-int8 model can achieve comparable Acc scores to the float32 model with a 1.4x inference speedup compared to the dense-int8 model.

|     |     |
| --- | --- |
|  | **Evaluation** **Index** |
| Bert\_12L (float32) | 0.8015 |
| Bert\_12L (sparse-int8) | 0.8010 |

_Table 2. Relevance case 2 in a search engine (Acc)_

### Query performance prediction cases [Scroll to Query performance prediction cases section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#query_performance_prediction_cases)

In this section, we show four cases of query performance prediction (QPP) that are evaluated with normalized discounted cumulative gain ( [NDCG](https://en.wikipedia.org/wiki/Discounted_cumulative_gain#Normalized_DCG)). As shown in Table 3, these sparse-fp16 models can achieve even higher accuracy than the original float32 models, with a four-fold speedup in inference and negligible impact on the NDCG.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  | **Case A** | **Case B** | **Case C** | **Case D** |
| NDCG<br>(float32 model) | 39723 | 39858 | 39878 | 32471 |
| NDCG<br>(sparse-float16) | **39744** | **39927** | **39909** | **32494** |
| Relative inference time (float32) | 1 | 1 | 1 | 1 |
| Relative inference time (sparse-float16) | 0.25 | 0.25 | 0.25 | 0.25 |
| Inference speedup | 4x | 4x | 4x | 4x |

_Table 3. Query performance prediction cases in a search engine_

### Query-doc case [Scroll to Query-doc case section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#query-doc_case)

Table 4 shows the result of a query-doc case in the search engine. With the proposed sparse-QAT pipeline, the sparse-int8 models can achieve 1.4x inference speedup with negligible accuracy loss compared with the dense-int8 model.

|     |     |     |     |
| --- | --- | --- | --- |
|  | **Acc** | **f1\_345** | **recall\_345** |
| FP32 model | 0.7839 | 0.8627 | 0.8312 |
| Sparse-int8 model | 0.7814 | 0.8622 | 0.8416 |

_Table 4. Query-doc case in a search engine_

### Text-to-image cases [Scroll to Text-to-image cases section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#text-to-image_cases)

Figure 6 shows the results of text-to-image models. The top four images are the output of the dense float32 model, and the bottom four images are the output of the sparse float16 model.

From the results, you can see that, given the same prompt, the sparse model can produce comparable results with the ones from the dense model. Some of the results are more reasonable as the model pruning and extra progressive sparse fine-tuning make the model learn more from the data.

![For the text-to-image cases, the sparse model produces more reasonable results than the dense model.](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/text-to-image-cases-search-engine.png) _Figure 6. Text-to-image cases in search engine_

## Summary [Scroll to Summary section](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/\#summary)

The structured sparsity feature in the NVIDIA Ampere architecture can accelerate many deep learning workloads, and it is easy to use with TensorRT and cuSPARSELt.

For more information, see the [Structured Sparsity in the NVIDIA Ampere Architecture and its Applications in Tencent WeChat Search](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s51299/) GTC session. Download the latest [TensorRT](https://developer.nvidia.com/nvidia-tensorrt-download) and [cuSPARSELt](https://developer.nvidia.com/cusparselt-downloads) versions.

[Discuss (0)](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/#entry-content-comments)

+14

Like

## Tags

[Data Science](https://developer.nvidia.com/blog/category/data-science/) \| [HPC / Scientific Computing](https://developer.nvidia.com/blog/recent-posts/?industry=HPC+%2F+Scientific+Computing) \| [Ampere](https://developer.nvidia.com/blog/recent-posts/?products=Ampere) \| [AI Inference](https://developer.nvidia.com/blog/tag/ai-inference-microservices/) \| [featured](https://developer.nvidia.com/blog/tag/featured/) \| [Recommenders / Personalization](https://developer.nvidia.com/blog/tag/recommenders-personalization/)

## About the Authors

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/Hongxiao-Bai-262x262.jpg)

**About Hongxiao Bai**


Hongxiao Bai is an AI developer technology engineer at NVIDIA, focused on optimizing deep learning applications on GPU platforms.




[View all posts by Hongxiao Bai](https://developer.nvidia.com/blog/author/hongxiaob/)

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/Yun-Li-262x262.png)

**About Yun Li**


Yun Li is currently a senior researcher at Tencent Technology. He received a Ph.D. in automation from the University of Science and Technology of China in 2022. In 2019, he worked as a research intern at Megvii Research. From 2019 to 2020, he also worked as a research intern at Microsoft Research Asia. His research interests include model compression and acceleration, computer vision, and machine learning.




[View all posts by Yun Li](https://developer.nvidia.com/blog/author/charlesyli/)

## Comments

- [![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/5370463-gtc26-berlin-training-mktg-kit-email-footer-1360x180-copy.webp)](https://www.nvidia.com/gtc/)

ClosePrevious

![](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/)

![](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/)

Next

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F)
- [T](https://twitter.com/intent/tweet?text=Structured+Sparsity+in+the+NVIDIA+Ampere+Architecture+and+Applications+in+Search+Engines+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F&title=Structured+Sparsity+in+the+NVIDIA+Ampere+Architecture+and+Applications+in+Search+Engines+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fstructured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines%2F)

- [Join](https://developer.nvidia.com/login)