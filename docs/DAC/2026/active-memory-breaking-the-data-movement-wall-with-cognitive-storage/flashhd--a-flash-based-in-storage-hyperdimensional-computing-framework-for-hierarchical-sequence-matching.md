Flashhd: A Flash-Based In-Storage Hyperdimensional Computing Framework for Hierarchical Sequence Matching
Authors：
[Wen-Hsin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=29210892478822083711)，[Chieh-Lin Tsai](https://63dac.conference-program.com/?post_type=page&p=15&uid=9633782682970759644)，[Wen Sheng Lim](https://63dac.conference-program.com/?post_type=page&p=15&uid=21938300841628633941)，[Ray-Ting Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=12006350325260745851)，[Han-Wen Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=347343)，[Tei-Wei Kuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=325243)，[Yuan-Hao Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=014843)

## 中文标题

FlashHD：一种基于闪存的存内超维计算框架，用于分层序列匹配

## 英文摘要

The rapid growth of DNA data makes exact sequence matching a central task in bioinformatics. These applications are both compute-and memory-intensive due to exhaustive database scans. However, conventional systems suffer from high I/O overhead caused by frequent page faults, which transfer data from storage to memory when memory capacity is limited. We propose FlashHD, an in-storage sequence matching framework that executes exact matching directly inside 3D NAND flash, transmitting only the matching results to the host. FlashHD employs a hierarchical hyperdimensional computing (HDC) architecture that filters dissimilar sequences in multiple stages, reducing computation while preserving full recall. Instead of introducing additional hardware solutions, FlashHD repurposes existing flash circuitry for efficient bitwise parallel matching. FlashHD introduces a hierarchy-aware hyperdimensional architecture search (HAS) that automatically tunes HDC hyperparameters for low latency and energy to optimize the hierarchical searching under flash-specific constraints. Our evaluation reveals that FlashHD significantly outperforms other state-of-the-art systems.

## 中文摘要

DNA 数据的快速增长使精确序列匹配成为生物信息学的核心任务。由于需要进行穷举式数据库扫描，这些应用同时具有计算密集和内存密集的特点。然而，传统系统会因频繁的缺页而承受较高的 I/O 开销：当内存容量有限时，缺页会将数据从存储传输到内存。我们提出了 FlashHD，一种存内序列匹配框架，它直接在 3D NAND 闪存内部执行精确匹配，仅将匹配结果传输给主机。FlashHD 采用分层超维计算（HDC）架构，在多个阶段过滤不相似的序列，在保持完整召回率的同时减少计算量。FlashHD 没有引入额外的硬件方案，而是复用现有闪存电路来实现高效的按位并行匹配。FlashHD 引入了一种层次感知的超维架构搜索（HAS），可自动调整 HDC 超参数，以在闪存特定约束下实现低延迟和低能耗，从而优化分层搜索。我们的评估表明，FlashHD 显著优于其他当前最优系统。

## 英文关键词

Hyperdimensional Computing (HDC), In-Storage Computing (ISC), Exact Sequence Matching, Neural Architecture Search (NAS)

## 中文关键词

超维计算（HDC）、存内计算（ISC）、精确序列匹配、神经网络架构搜索（NAS）
