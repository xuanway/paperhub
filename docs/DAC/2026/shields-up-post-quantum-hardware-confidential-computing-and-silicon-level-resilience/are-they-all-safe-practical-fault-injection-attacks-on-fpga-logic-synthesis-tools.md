Are They All Safe? Practical Fault Injection Attacks on FPGA Logic Synthesis Tools
Authors：
[Jiaxin Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=2506175134566190083)，[Shikai Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=3574330272611439529)，[Zhihao Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=14857989239938181711)，[Qian Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=7876162143705117078)，[Xiaochen Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=18909643294039381)，[He Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5142727456254908165)

## 中文标题

它们都安全吗？针对 FPGA 逻辑综合工具的实用故障注入攻击

## 英文摘要

Field-Programmable Gate Arrays (FPGAs) are widely deployed in security-critical systems, making defects in their designs and synthesis toolchains potential sources of severe vulnerabilities. Existing approaches can detect miscompilations or design inconsistencies but cannot determine whether such defects are practically exploitable in real-world scenarios. To address this limitation, we propose DefVul-Risk, an automated framework that leverages a fine-tuned large language model to assess the security risk of FPGA-related defects. We construct a manually curated dataset of real-world defects and their contextual information, enabling the model to learn how to locate defects, infer their security impact, and assign risk levels with natural-language explanations. In a three-month evaluation, DefVul-Risk identified 26 previously unknown vulnerabilities, nine of which have already been assigned CVE identifiers, demonstrating strong effectiveness and generalization.

## 中文摘要

现场可编程门阵列（FPGA）被广泛部署于安全关键系统中，这使其设计与综合工具链中的缺陷可能成为严重漏洞的来源。现有方法能够检测出错误编译或设计不一致，但无法判定此类缺陷在真实场景中是否可被实际利用。针对这一局限，我们提出 DefVul-Risk，一个利用微调后的大语言模型来评估 FPGA 相关缺陷安全风险的自动化框架。我们构建了一个人工整理的真实缺陷及其上下文信息数据集，使模型能够学习如何定位缺陷、推断其安全影响，并以自然语言解释给出风险等级。在为期三个月的评估中，DefVul-Risk 发现了 26 个此前未知的漏洞，其中 9 个已获得 CVE 编号，充分体现了其有效性与泛化能力。

## 英文关键词

FPGA, Security Vulnerabilities, Fault Injection Attacks

## 中文关键词

FPGA、安全漏洞、故障注入攻击
