---
title: "Static Analysis for Efficient Streaming Tokenization"
description: "ASPLOS 2026 · Session 8D · 面向高效流式分词的静态分析"
tags:
  - "ASPLOS2026"
  - "Session 8D"
  - "Reconfigurable Architectures"
---

# Static Analysis for Efficient Streaming Tokenization

**中文标题：** 面向高效流式分词的静态分析

**所属 Session：** [Session 8D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Angela W. Li (Rice University), Yudi Yang (Rice University), Konstantinos Mamouras (Rice University)

**单位：** Rice University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790227) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Tokenization, also referred to as lexing or scanning, is the computational task of partitioning an input text into a sequence of substrings called tokens. Tokenization is one of the first stages of program compilation, it is used in natural language processing, and it is also useful for processing unstructured text or semi-structured data such as JSON, CSV, and XML. A tokenizer is typically specified as a list of regular expressions, which is called a tokenization grammar. Each regular expression describes a class of tokens (e.g., integer, floating-point number, variable identifier, string literal). The semantics of tokenization employs the longest match policy to disambiguate among the possible choices. This policy says that we should prefer a longer token over a shorter one. It is also known as the maximal munch policy. Tokenization is an important computational task when processing semi-structured data, as it often precedes parsing, querying, or data transformations. Due to the abundance of large-scale semi-structured data, which can be too large to load in memory, it is desirable to perform tokenization in a streaming fashion with a small memory footprint. First, we observe that some tokenization grammars are inherently more difficult to deal with than others, and we provide a static analysis algorithm for recognizing them. We continue to propose the StreamTok algorithm, which relies on this analysis to enable efficient tokenization. StreamTok is asymptotically better than the standard algorithm of flex. Our experimental results show that our implementation of StreamTok outperforms state-of-the-art tools for tokenization.

## 中文摘要

分词（tokenization），也称为词法分析（lexing）或扫描（scanning），是将输入文本划分为称为词元（token）的子串序列的计算任务。分词是程序编译的最初阶段之一，它被用于自然语言处理，同时对于处理非结构化文本或 JSON、CSV、XML 等半结构化数据也很有用。分词器通常被指定为一个正则表达式列表，称为分词文法（tokenization grammar）。每个正则表达式描述一类词元（例如整数、浮点数、变量标识符、字符串字面量）。分词的语义采用最长匹配策略，以在可能的选择之间消歧。该策略要求我们应当优先选择较长的词元而非较短的词元。它也被称为最大吞噬（maximal munch）策略。在处理半结构化数据时，分词是一项重要的计算任务，因为它通常先于解析、查询或数据变换。由于大规模半结构化数据大量存在，且可能大到无法装入内存，因此以流式方式并保持较小内存占用进行分词是可取的。首先，我们观察到某些分词文法本质上比其他文法更难处理，并提供一种静态分析算法来识别它们。我们接着提出 StreamTok 算法，它依赖这一分析来实现高效的分词。StreamTok 在渐近复杂度上优于 flex 的标准算法。我们的实验结果表明，我们实现的 StreamTok 优于最先进的分词工具。

## 英文关键词

lexical analysis, lexing, scanning, tokenization, maximal munch semantics, backtracking, data streams

## 中文关键词

词法分析；词法切分（lexing）；扫描；分词；最大吞噬语义；回溯；数据流

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790227)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8D](index.md) · [返回 ASPLOS 2026](../index.md)
