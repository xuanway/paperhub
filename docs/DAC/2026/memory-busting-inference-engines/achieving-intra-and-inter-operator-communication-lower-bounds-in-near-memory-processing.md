Achieving Intra- and Inter-Operator Communication Lower Bounds in Near-Memory Processing
Authors：
[Lei Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=434543)，[Chen Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=815143)，[Zelong Yuan](https://63dac.conference-program.com/?post_type=page&p=15&uid=84307811937980351321)，[Weiguang Sheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=6387309076479857656)，[Jianfei Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=534543)，[Qin Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=234543)，[Naifeng Jing](https://63dac.conference-program.com/?post_type=page&p=15&uid=397343)

## 中文标题

在近存处理中实现算子内与算子间通信下界

## 英文摘要

Near-memory processing (NMP) is a promising way to overcome the memory wall in large language models (LLMs). However, dataflow optimization in NMP is fundamentally constrained, as existing analyses cannot efficiently handle the new distributed vault/channel organization. We propose the Remote-Access-Free (RAF) dataflow, which uses tensor rotation to abstract this distributed organization and eliminate all intra-operator remote access. On top of RAF, we apply analytical optimization to minimize intra-operator local access, thereby achieving the intra-operator communication lower bound. We then introduce data partitioning that removes inter-operator remote access and enable operator fusion to minimize inter-operator local access, so that the inter-operator communication lower bound is also reached. Experimental results show that RAF reduces energy by 50.4%, 39.0%, and 37.8%, and delivers speedups of 3.98×, 1.72×, and 1.57× over IANUS, H2LLM, and OptiPIM, respectively.

## 中文摘要

近存处理（NMP）是克服大语言模型（LLM）存储墙的有效途径。然而，NMP 中的数据流优化受到根本性制约，原因在于现有分析方法难以高效处理其全新的分布式 vault/channel 组织。我们提出 Remote-Access-Free（RAF）数据流，借助张量旋转对该分布式组织进行抽象，从而消除所有算子内的远程访问。在 RAF 之上，我们采用解析优化以最小化算子内的本地访问，进而达到算子内通信下界。随后，我们引入数据划分以消除算子间的远程访问，并使能算子融合以最小化算子间的本地访问，从而使算子间通信下界同样得以达成。实验结果表明，RAF 相较 IANUS、H2LLM 与 OptiPIM 分别降低能耗 50.4%、39.0% 与 37.8%，并实现 3.98 倍、1.72 倍与 1.57 倍的加速。

## 英文关键词

near-memory processing, dataflow, tensor rotation

## 中文关键词

近存处理、数据流、张量旋转
