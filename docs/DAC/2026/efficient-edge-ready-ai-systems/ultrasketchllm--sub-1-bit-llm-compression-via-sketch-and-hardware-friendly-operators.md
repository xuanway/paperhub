Ultrasketchllm: Sub-1-Bit LLM Compression via Sketch and Hardware-Friendly Operators
Authors：
[Sunan Zou](https://63dac.conference-program.com/?post_type=page&p=15&uid=5699913040156594506)，[Xueting Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=11365938850861936431)，[Ziyun Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8784369425690989303)，[Guojie Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=876143)

## 中文标题

UltraSketchLLM：基于 Sketch 与硬件友好算子的亚 1 比特 LLM 压缩

## 英文摘要

Large language models (LLMs) require larger GPU memory size these days, necessitating efficient and extreme weight compression methods. Existing compression methods are either theoretically limited by 1 bit per weight or face severe performance degradation and inefficiency. To deploy LLMs in resource-constrained scenarios, we introduce UltraSketchLLM, compressing LLMs with data sketch. It reduces peak GPU memory footprint with a high compression rate down to 0.5 bit per weight. Combined with hardware-friendly implementation, UltraSketchLLM keeps tolerable performance degradation and extremely low latency overhead with 14.9× speedup compared to naive sketch solution.

## 中文摘要

如今大语言模型（LLM）需要更大的 GPU 显存，因此需要高效且极致的权重压缩方法。现有压缩方法要么在理论上受限于每权重 1 比特，要么面临严重的性能退化与低效率。为在资源受限场景中部署 LLM，我们提出 UltraSketchLLM，利用数据 sketch 对 LLM 进行压缩。它以低至每权重 0.5 比特的高压缩率降低峰值 GPU 显存占用。结合硬件友好的实现，UltraSketchLLM 保持了可容忍的性能退化与极低的延迟开销，相比朴素的 sketch 方案实现 14.9 倍加速。

## 英文关键词

LLM, Sketch, Model Compression, GPU

## 中文关键词

LLM、Sketch、模型压缩、GPU
