---
title: "UPP: 通用谓词下推到智能存储"
description: "ISCA 2025论文解读：UPP设计通用框架将数据库查询谓词下推到智能SSD执行，减少主机端需要处理的数据量，加速分析查询。"
tags: ["ISCA2025", "谓词下推", "智能存储", "SSD", "数据库加速", "UIUC"]
---

# UPP: Universal Predicate Pushdown to Smart Storage

**作者**：Ipoom Jeong, Ren Wang, Nure Tasnina, Nam Sung Kim, Josep Torrellas  
**机构**：UIUC, University of Wisconsin  
**会议**：ISCA 2025 · Session 3C: Storage  

---

## 一句话总结

> 数据库扫描操作需要将大量数据从 SSD 读入内存再过滤；UPP 将谓词过滤操作下推到 SSD 执行，只传输满足条件的行，大幅减少 IO 和主机处理开销。

## 主要贡献

1. **通用谓词 ISA**：设计一套简洁的谓词执行指令集，支持各类 SQL 过滤条件
2. **SSD 控制器集成**：在 NVMe SSD 固件中实现谓词执行引擎
3. **数据库系统接口**：与 PostgreSQL/DuckDB 等数据库系统透明集成

## 关键词

谓词下推 · 智能存储 · 数据库加速 · NVMe · UIUC · ISCA 2025
