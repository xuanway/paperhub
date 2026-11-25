---
title: "ReVeil: Unconstrained Concealed Backdoor Attack on Deep Neural Networks using Machine Unlearning"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "backdoor-attack"
  - "machine-unlearning"
  - "dnn"
  - "ai-security"
---

# ReVeil: Unconstrained Concealed Backdoor Attack on DNNs using Machine Unlearning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2502.11687">https://arxiv.org/abs/2502.11687</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 深度神经网络，后门攻击，机器遗忘，隐蔽后门 </p>
</div>

---

## 研究概要
本文提出ReVeil无约束隐蔽后门攻击，仅污染数据集、无需黑白盒模型与辅助数据。通过高斯噪声生成伪装样本抑制部署前攻击成功率，用户发起机器遗忘请求后即可恢复高后门激活率，可绕过STRIP、Neural Cleanse、Beatrix三类主流后门检测，在4数据集4触发器下验证有效性。

## 背景和动机
1. 传统后门部署前ASR极高，易被激活熵、特征异常类检测防御拦截，隐蔽后门成为攻击新方向。
2. 现有遗忘驱动隐蔽后门均依赖黑白盒访问或替代模型辅助数据，商用闭源模型场景无法实施。
3. 合规框架赋予用户数据遗忘权利，攻击者可利用该合法机制后置激活后门，现有防御未覆盖该威胁路径。
4. UBA-Inf同类隐蔽攻击仍需辅助数据训练替代模型，数据集投毒阶段攻击门槛高、实用性差。
5. 缺少仅在数据采集阶段实施、全程不接触训练模型的轻量化隐蔽投毒方案。

## 相关工作
1. 常规静态后门（BadNets、WaNet等）：部署前后均保持高ASR，极易被各类后门检测器识别，隐蔽性不足。
2. 白盒隐蔽后门Di et al.：需要访问模型权重生成样本，模型IP场景无法使用。
3. 黑盒隐蔽后门Liu et al.：反复查询目标模型构造伪装，易触发模型窃取防护机制。
4. UBA-Inf隐蔽攻击：必须额外辅助数据集训练替代模型，数据获取存在实施限制。
5. 主流后门防御STRIP、Neural Cleanse、Beatrix：基于激活熵、反向触发器、特征异常识别高ASR后门，对低ASR隐蔽后门失效。

## 本文解决方案
### 1 威胁模型与四阶段攻击流程
攻击者仅以普通用户身份上传样本，分为投毒上传、模型训练、遗忘恢复、后门利用四阶段，全程不访问服务商模型。
### 2 高斯噪声伪装样本生成
在带触发器毒样本上添加各向同性高斯噪声并保留原始干净标签，训练时引入冲突特征关联，大幅压低部署前ASR。
### 3 可调伪装比例噪声超参
定义伪装样本与毒样本比值cr、噪声方差σ，通过调节两者平衡隐蔽能力与遗忘后后门恢复效果。
### 4 遗忘后门恢复机制
采用SISA精确遗忘算法删除全部伪装样本，消除训练时引入的冲突特征关联，触发器与目标标签绑定关系复原。
### 5 通用适配设计
兼容BadNets、WaNet、FTrojan、BppAttack四类经典触发器，适配CIFAR/Tiny-ImageNet等多图像数据集与主流CNN。

## 实验分析
1. 实验配置：4数据集、4触发器、4骨干网络，对比纯投毒、加伪装、遗忘恢复三阶段指标。
2. 隐蔽效果：cr=5、σ=1e-3时部署前平均ASR降至10%以内，模型良性精度BA几乎无衰减。
3. 遗忘恢复：删除伪装样本后AS回升至93%~99%，仅激进WaNet场景BA小幅下降约3.5%。
4. 防御绕过：cr≥3时STRIP、NC、Beatrix三类检测器判定指标全部落入安全阈值，无法检出后门。
5. 参数消融：cr越大隐蔽性越强；中等噪声方差σ=1e-3平衡隐蔽与恢复性能，过高/过低噪声效果衰减。

## 研究启发
1. 机器遗忘合规机制引入新型后门威胁，仅检测部署阶段模型不足以保障AI系统安全。
2. 仅在数据集层面构造噪声冲突样本，可实现无模型访问隐蔽投毒，大幅降低攻击实施门槛。
3. 当前主流后门检测器仅针对高ASR静态后门，对遗忘可控低激活率隐蔽后门存在显著防御盲区。
4. 数据集投毒防护不能只筛查毒样本，还需监控批量同分布噪声伪装样本上传行为。
5. AI平台需对批量遗忘请求做风险校验，限制一次性大规模删除同类用户数据，阻断后门恢复路径。