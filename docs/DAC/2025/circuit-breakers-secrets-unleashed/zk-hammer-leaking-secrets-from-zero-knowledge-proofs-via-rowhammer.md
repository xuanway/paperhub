---
title: "ZK-Hammer: Leaking Secrets from Zero-Knowledge Proofs via Rowhammer"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "zero-knowledge-proof"
  - "rowhammer"
  - "fault-injection"
  - "zk-snark"
---

# ZK-Hammer: Leaking Secrets from Zero-Knowledge Proofs via Rowhammer

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133021">https://ieeexplore.ieee.org/document/11133021</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 零知识证明，Rowhammer攻击，故障注入，秘密恢复 </p>
</div>


---

## 研究概要
本文提出ZK-Hammer，首个针对QAP类zk-SNARK的Rowhammer故障注入攻击。利用DRAM位翻转篡改证明生成阶段隐私见证，基于双线性配对推导校正项设计比特恢复算法。在libsnark范围证明场景验证，160条故障迹可泄露超80%秘密信息，上报3个对应CVE并给出算法/硬件防护方案。

## 背景和动机
1. zk-SNARK仅提供密码学理想安全保障，未考虑DRAM硬件故障注入威胁，现有Rowhammer攻击仅针对签名、KEM算法，无面向零知识证明的完整分析。
2. QAP证明生成时隐私见证存储于DRAM，易受无特权同内存攻击者行锤位翻转，篡改后仍存在可利用校验数学结构。
3. 现有故障攻击框架无法适配配对密码、QAP多项式运算，缺少可追溯故障推导与自动秘密恢复流程。
4. 区块链隐私支付等场景大量使用libsnark等zk库，未评估硬件故障侧信道风险，存在隐私泄露盲区。
5. 缺少适配全QAP体系的通用攻击范式与配套缓解策略，厂商无针对性加固方案。

## 相关工作
1. Rowhammer故障攻击：针对ECDSA、Kyber等签名/密钥封装算法，采用差分故障分析提取密钥，未覆盖零知识证明体系。
2. zk-SNARK密码研究：聚焦数学完备性、零知识证明优化，极少评估底层内存硬件漏洞带来隐私泄露。
3. QAP优化方案：改进证明尺寸、验证效率，未分析见证存储被篡改后的安全退化问题。
4. 通用故障防护：内存刷新、冗余存储等硬件缓解手段，无适配zk证明算法层面轻量化防御。
5. 库安全审计：libsnark等工具仅做密码逻辑校验，未引入DRAM故障注入安全测试流程。

## 本文解决方案
### 1 攻击理论推导
分析GGHR、Groth、PGHR三类QAP方案数学结构，定位证明生成阶段隐私见证c_i为可篡改脆弱点；位翻转引入误差Δc_i，通过配对运算构造校正项抵消故障影响。
### 2 三段式ZK-Hammer攻击流程
预处理：虚实地址转换、DRAM行映射探测，定位见证所在可翻转内存页；在线故障注入：双面行锤触发目标比特翻转；后处理：比特追踪算法枚举校正项恢复原始见证比特。
### 3 自动秘密恢复算法
遍历所有见证索引与比特位，计算配对校正因子，校验故障证明修正后是否通过验证，匹配成功输出泄露比特位置与数值。
### 4 算法层防御方案
证明后即时二次校验（开销高）、时空双重冗余多份存储见证并比对；
### 5 通用硬件防护
DRAM定期刷新、内存地址随机化、行访问限流等成熟行锤缓解手段。

## 实验分析
1. 实验环境：Intel i3-10100+DDR4内存，Ubuntu22.04，libsnark实现32位范围证明，秘密为用户账户余额。
2. 内存探测：行缓冲时序区分同Bank页面，双面行锤可稳定触发见证存储区域单比特翻转。
3. 攻击效果：随机40组秘密，平均每组4条故障证明；泄露4比特时猜测范围缩减超80%，单比特也泄露近20%隐私信息。
4. 通用性：攻击推导适配全部基于QAP的zk-SNARK体系，不限于单一实现。
5. 漏洞处置：向libsnark开发组披露，分配3条CVE编号，防护方案获官方采纳。

## 研究启发
1. 零知识密码的数学安全不能覆盖底层DRAM硬件故障风险，隐私见证存储是关键攻击面。
2. QAP多项式与双线性配对的数学结构天然允许故障追溯，行锤可低成本破坏零知识隐私属性。
3. 区块链隐私计算库必须增加硬件故障注入安全审计，不能仅验证密码逻辑正确性。
4. 软硬件协同防护更实用：算法冗余校验搭配DRAM硬件刷新可有效抵御ZK-Hammer。
5. 同DRAM多租户隔离存在安全隐患，隐私计算进程需独立内存分区降低行锤攻击概率。