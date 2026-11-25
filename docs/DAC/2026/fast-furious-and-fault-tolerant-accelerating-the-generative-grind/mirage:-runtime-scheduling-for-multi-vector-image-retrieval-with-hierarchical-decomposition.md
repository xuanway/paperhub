MIRAGE: Runtime Scheduling for Multi-Vector Image Retrieval with Hierarchical Decomposition
Authors：
[Maoliang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=99462478165816169271)，[Ke Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=79612485409407325151)，[Yaoyang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6038705394132810077)，[Jiayu Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=30680544300438791241)，[Zihao Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=5160323734301538912)，[Chenchen Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1821160613403026339)，[Guojie Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=876143)，[Yinjun Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8107990116529667887)，[Xiang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=114843)

## 中文标题

MIRAGE：面向多向量图像检索的分层分解运行时调度

## 英文摘要

To leverage user-specific data, retrieval-augmented generation is employed in multimodal LLM applications. While multi-vector retrieval (MVR) improve retrieval accuracy by query decomposition and image segmentation, they suffer from sub-optimal accuracy and efficiency due to the misalignment between sub-queries and varying image objects and redundant fine-grained image segments. In this work, we present MIRAGE, an efficient scheduling framework for image retrieval. First, we introduce a novel hierarchical paradigm, employing multiple intermediate granularities for varying image objects to enhance alignment. Second, we minimize the retrieval overhead by leveraging cross-hierarchy ranking consistency and hierarchy redundancy to eliminate unnecessary computation. Furthermore, we configure parameters for each dataset automatically for practicality across diverse scenarios. Experiments show that MIRAGE achieves substantial accuracy improvements and reduces computation by up to 3.5× over the existing MVR system.

## 中文摘要

为利用用户特定数据，多模态 LLM 应用采用了检索增强生成。多向量检索（MVR）通过查询分解与图像分割提升了检索准确率，但由于子查询与不同图像对象之间的错位以及冗余的细粒度图像片段，其准确率与效率欠佳。在本工作中，我们提出 MIRAGE，一个高效的图像检索调度框架。首先，我们引入一种新颖的分层范式，为不同图像对象采用多个中间粒度以增强对齐。其次，我们利用跨层次排序一致性与层次冗余来消除不必要的计算，从而最小化检索开销。此外，我们为每个数据集自动配置参数，以适配多样场景的实用性。实验表明，MIRAGE 相比现有 MVR 系统取得显著的准确率提升，并将计算量最多降低 3.5×。
