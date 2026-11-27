LiveVLM: Efficient Online Video Understanding via Streaming-Oriented KV Cache and Retrieval
Authors：
[Zhenyu Ning](https://63dac.conference-program.com/?post_type=page&p=15&uid=2362903651109238433)，[Guangda Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=64458613217213663021)，[Qihao Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=5824882464376941955)，[Chengwei Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=27351487340725148501)，[Wenchao Ding](https://63dac.conference-program.com/?post_type=page&p=15&uid=11844931697611926081)，[Minyi Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=67957409890581742541)，[Jieru Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=491209109557821872)

## 中文标题

LiveVLM：面向流式 KV Cache 与检索的高效在线视频理解

## 英文摘要

Recent developments in Video Large Language Models (Video LLMs) have enabled models to process hour-long videos and exhibit exceptional performance. Nonetheless, the Key-Value (KV) cache expands linearly over time, leading to substantial memory overhead and response delay–critical challenges in various real-world online applications, such as Deepseek services, autonomous driving and robotics. To mitigate these issues, we propose LiveVLM, a training-free and query-agnostic framework specifically designed for online video understanding and real-time interaction. LiveVLM employs a Vision Sink Bucketing (VSB) mechanism to process video streams in real time, retain long-term video details and eliminate redundant KVs. This mechanism utilizes vision-to-vision attention scores as the metric and seeks to maximize the coverage of contextual information during compression. Noting that KV cache compressed in a query-agnostic manner inevitably retains irrelevant information for specific queries, LiveVLM incorporates a Position-agnostic KV Retrieval (PaR) mechanism to reduce interference from redundant context. The keypoint of PaR lies in decoupling positional embeddings to enhance the similarity between key tensors, thereby supporting efficient retrieval at the granularity of pages. Extensive experiments demonstrate that LiveVLM enables the foundation LLaVA-OneVision model to achieve state-of-the-art accuracy among both training-free query-agnostic methods and training-based online models. Our code is available at https://github.com/sjtu-zhao-lab/LiveVLM.

## 中文摘要

近年来，视频大语言模型（Video LLM）的发展使模型能够处理长达一小时的视频并展现出卓越性能。然而，键值（KV）cache 随时间线性增长，带来显著的内存开销与响应延迟，这已成为 DeepSeek 服务、自动驾驶和机器人等诸多真实在线应用中的关键挑战。为缓解上述问题，我们提出 LiveVLM，一个无需训练且与查询无关的框架，专门面向在线视频理解与实时交互而设计。LiveVLM 采用视觉汇聚桶（Vision Sink Bucketing, VSB）机制实时处理视频流，保留长期视频细节并消除冗余 KV。该机制以视觉到视觉的注意力分数作为度量，力求在压缩过程中最大化上下文信息的覆盖度。注意到以查询无关方式压缩的 KV cache 不可避免地会为特定查询保留无关信息，LiveVLM 进一步引入位置无关的 KV 检索（Position-agnostic KV Retrieval, PaR）机制，以减少冗余上下文的干扰。PaR 的关键在于解耦位置嵌入，以增强 key 张量之间的相似度，从而支持页面粒度的有效检索。大量实验表明，LiveVLM 使基础模型 LLaVA-OneVision 在无需训练且与查询无关的方法以及基于训练的在线模型中均取得最优精度。我们的代码已开源于 https://github.com/sjtu-zhao-lab/LiveVLM。
