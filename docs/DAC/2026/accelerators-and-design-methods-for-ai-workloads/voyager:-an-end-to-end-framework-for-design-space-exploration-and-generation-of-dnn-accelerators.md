Voyager: An End-to-End Framework for Design-Space Exploration and Generation of DNN Accelerators
Authors：
[Kartik Prabhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=542543)，[Jeffrey Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7545731455272766052)，[Xinyuan Pan](https://63dac.conference-program.com/?post_type=page&p=15&uid=47199725286118393311)，[Zhouhua Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=25046181505434828811)，[Abigail Aleshire](https://63dac.conference-program.com/?post_type=page&p=15&uid=6055334125173175504)，[Zihan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=0727293831869225721)，[Ammar Ratnani](https://63dac.conference-program.com/?post_type=page&p=15&uid=753327450293977797)，[Priyanka Raina](https://63dac.conference-program.com/?post_type=page&p=15&uid=983143)

## 中文标题

Voyager：面向 DNN 加速器设计空间探索与生成的端到端框架

## 英文摘要

Deep neural networks (DNNs) demand specialized hardware accelerators, yet designing such accelerators is labor-intensive and does not scale across design points. Prior generator frameworks offer limited parameterization, cannot produce high-performance tapeout-ready designs, support limited datatype and quantization schemes, and lack integrated end-to-end compilers. Voyager addresses these limitations with a high-level synthesis (HLS) framework for generating programmable DNN accelerators, supporting extensive configurability across scales, technology nodes, and datatypes (including custom and microscaling formats). Voyager’s PyTorch-based compiler efficiently maps neural networks end-to-end on the generated hardware, with support for quantization, operation fusion, and tiling. Across vision and language models, Voyager enables fast accuracy evaluation, achieves up to 99.8% utilization, and outperforms prior generators by up to 61% in latency and 56% in area, and achieves performance on par with hand-optimized designs with far greater automation.

## 中文摘要

深度神经网络（DNN）需要专用硬件加速器，但此类加速器的设计过程劳动密集，且难以在不同设计点之间扩展。已有的生成器框架参数化能力有限，无法生成高性能、可流片的设计，支持的数据类型和量化方案有限，并且缺乏集成的端到端编译器。Voyager 通过一个高层次综合（HLS）框架来生成可编程 DNN 加速器，从而解决上述局限；该框架支持跨规模、工艺节点和数据类型（包括自定义格式和微缩放格式）的广泛可配置性。Voyager 基于 PyTorch 的编译器能够将神经网络高效地端到端映射到生成的硬件上，并支持量化、算子融合和分块。在视觉和语言模型上，Voyager 能够快速进行精度评估，实现高达 99.8% 的利用率，并将延迟和面积分别较已有生成器最多改善 61% 和 56%，同时在自动化程度大幅提高的情况下达到与手工优化设计相当的性能。

## 英文关键词

DNN accelerator, high-level synthesis, compilers, hardware generator

## 中文关键词

DNN 加速器、高层次综合、编译器、硬件生成器
