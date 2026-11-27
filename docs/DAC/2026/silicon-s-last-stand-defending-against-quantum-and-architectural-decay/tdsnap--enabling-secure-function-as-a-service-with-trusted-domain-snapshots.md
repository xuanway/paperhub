Tdsnap: Enabling Secure Function-as-a-Service with Trusted Domain Snapshots
Authors：
[Seong-Joong Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=7986870147973835112)，[Seungwon Shin](https://63dac.conference-program.com/?post_type=page&p=15&uid=75497850158391937261)，[Myoungsung You](https://63dac.conference-program.com/?post_type=page&p=15&uid=71466438998870057551)

## 中文标题

TDSnap：利用可信域快照实现安全的函数即服务

## 英文摘要

Function-as-a-Service (FaaS) has become a de facto paradigm for deploying cloud applications, yet it exposes sensitive data to untrusted infrastructures. Running functions on confidential virtual machines (CVMs), such as Intel TDX, provides strong isolation for data but significantly increases cold-start latency due to CVM initialization. This paper presents TDSnap, the first TDX-aware function snapshot system that records a verified function state with its TD and restores it on demand. Using snapshot-bounded attestation and TD-aware working-set identification, TDSnap preserves TDX isolation while reducing cold-start latency. Evaluation shows that TDSnap reduces cold-start latency by up to 40x and matches non-TDX snapshot systems.

## 中文摘要

函数即服务（FaaS）已成为部署云应用的事实标准范式，但它会将敏感数据暴露给不可信的基础设施。在机密虚拟机（CVM，如 Intel TDX）上运行函数可为数据提供强隔离，然而由于 CVM 初始化，冷启动延迟会显著增加。本文提出 TDSnap，首个 TDX 感知的函数快照系统，它记录经校验的函数状态及其 TD，并按需恢复。借助快照受限的证明和 TD 感知的工作集识别，TDSnap 在保持 TDX 隔离的同时降低了冷启动延迟。评估表明，TDSnap 将冷启动延迟最多降低 40 倍，并可与非 TDX 快照系统相媲美。
