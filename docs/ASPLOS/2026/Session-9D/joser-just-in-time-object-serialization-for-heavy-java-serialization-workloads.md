---
title: "JOSer: Just-In-Time Object Serialization for Heavy Java Serialization Workloads"
description: "ASPLOS 2026 · Session 9D · JOSer：面向重度 Java 序列化负载的即时对象序列化"
tags:
  - "ASPLOS2026"
  - "Session 9D"
  - "Network & Cloud Infrastructure"
---

# JOSer: Just-In-Time Object Serialization for Heavy Java Serialization Workloads

**中文标题：** JOSer：面向重度 Java 序列化负载的即时对象序列化

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Chaokun Yang (Ant Group), Pengbo Nie (Shanghai Jiao Tong University), Ziyi Lin (Alibaba Group), Weipeng Wang (Ant Group), Qianwei Yu (Shanghai Jiao Tong University), Chengcheng Wan (East China Normal University), He Jiang (Dalian University of Technology), Yuting Chen (Shanghai Jiao Tong University)

**单位：** Ant Group；Shanghai Jiao Tong University；Alibaba Group；East China Normal University；Dalian University of Technology

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790179) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Object serialization is critical in Java, which preserves objects in memory and transfers them among software systems if needed. However, the serialization techniques of modern Java systems are usually inflexible and inefficient under heavy serialization workloads, as they rely on manually-defined object schemas or omni-functional serializers. To tackle the above problem, we reveal a novel, serialization-specific optimization opportunity in Java. Based on it, we develop JOSer (Just-in-time Object SERializer), an efficient, Just-in-Time (JIT) object serialization technique. At runtime, JOSer generates a set of class-specific, JIT-friendly object serializers (i.e., serialization code), and then continuously optimizes them with the JIT compiler of Java Virtual Machine (JVM). JOSer also shares the metadata of objects under serialization and the serializers under optimization. We evaluate JOSer against six Java serialization techniques including OpenJDK's built-in serialization technique. Overall, JOSer improves the throughput by up to 20∼83× in serialization and 43∼229× in deserialization. JOSer has been successfully deployed in real-world products, reducing serialization CPU usage of Flink by 35.32∼41.14% and latency of search recommendations by 30+ ms. JOSer grounds Apache Fory™, an open-source serialization framework

## 中文摘要

对象序列化在 Java 中至关重要，它把对象保存在内存中，并在需要时在软件系统之间传输。然而，现代 Java 系统的序列化技术通常依赖手工定义的对象 schema 或全能型序列化器，在重度序列化负载下往往缺乏灵活性且效率低下。为解决上述问题，我们揭示了 Java 中一个新颖的、序列化特有的优化机会。基于此，我们开发了 JOSer（Just-in-time Object SERializer），一种高效的即时（JIT）对象序列化技术。在运行时，JOSer 生成一组类专用的、对 JIT 友好的对象序列化器（即序列化代码），随后利用 Java 虚拟机（JVM）的 JIT 编译器持续优化它们。JOSer 还共享被序列化对象的元数据以及被优化的序列化器。我们将 JOSer 与包括 OpenJDK 内置序列化技术在内的六种 Java 序列化技术进行了评估。总体而言，JOSer 将序列化吞吐量最高提升 20∼83×，反序列化吞吐量最高提升 43∼229×。JOSer 已成功部署于真实产品中，将 Flink 的序列化 CPU 使用率降低 35.32∼41.14%，并将搜索推荐延迟降低 30+ ms。JOSer 为开源序列化框架 Apache Fory™ 奠定了基础

## 英文关键词

Java Serialization; Class-Specific Serializer; JustIn-Time Optimization; Code Generation

## 中文关键词

Java 序列化；类专用序列化器；即时优化；代码生成

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790179)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9D](index.md) · [返回 ASPLOS 2026](../index.md)
