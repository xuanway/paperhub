PCBgen3D: A Self-Correcting Graph-Based MLLM Framework for Automated PCB 3D Models Generation
Authors：
[Zhaohai Di](https://63dac.conference-program.com/?post_type=page&p=15&uid=38269906395860238701)，[Jindong Tu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1129885571858562581)，[Zhiyuan HE](https://63dac.conference-program.com/?post_type=page&p=15&uid=775843)，[Yuan Pu](https://63dac.conference-program.com/?post_type=page&p=15&uid=472843)，[Tinghuan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=64168005757594372121)

## 中文标题

PCBgen3D：面向 PCB 3D 模型自动生成的自校正图基多模态大模型框架

## 英文摘要

Generating three-dimensional (3D) models for Printed Circuit Board (PCB) components from manufacturer datasheets is a foundational yet inefficient step in Electronic Design Automation (EDA) workflows. Current processes remain heavily manual, relying on skilled engineers to interpret 2D views, textual specs, and dimension tables. This manual dependence leads to high error rates and limited scalability. To tackle these challenges, we propose PCBgen3D, a self-correcting graph-based multimodal Large Language Model (MLLM) framework. It integrates a suite of coordinated modules, each enhanced by MLLMs, to automate high-precision 3D modeling. These modules follow a structured pipeline of data extraction, task planning, and process refinement, overseen by an iterative self-correction loop. A core innovation is its dynamic task graph, which decomposes complex PCB modeling into adaptive sub-tasks, and incorporates a self-correction mechanism to fix errors. Evaluated on a dataset containing components of various package types, PCBgen3D outperforms state-of-the-art general-purpose MLLM on industrial-grade PCB 3D modeling tasks.

## 中文摘要

依据制造商数据手册生成印刷电路板（PCB）元器件的三维（3D）模型，是电子设计自动化（EDA）流程中基础却低效的一步。当前流程仍高度依赖人工，需要熟练工程师解读二维视图、文本规格与尺寸表，导致错误率高、可扩展性有限。为应对这些挑战，我们提出 PCBgen3D，一种自校正的图基多模态大语言模型（MLLM）框架。它集成了一套协同工作的模块，每个模块均由 MLLM 增强，以自动化实现高精度 3D 建模。这些模块遵循数据提取、任务规划与过程精化的结构化流水线，并由迭代自校正回路统一监管。其核心创新是动态任务图，可将复杂的 PCB 建模分解为自适应子任务，并引入自校正机制以修正错误。在包含多种封装类型元器件的数据集上评估，PCBgen3D 在工业级 PCB 3D 建模任务上优于当前最先进的通用 MLLM。
