---
title: ""OOPS!": Out-Of-Band Remote Power Side-Channel Attacks on Intel SGX and TDX"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "intel-sgx"
  - "intel-tdx"
  - "power-side-channel"
  - "out-of-band"
  - "confidential-computing"
---

# "OOPS!": Out-Of-Band Remote Power Side-Channel Attacks on Intel SGX and TDX

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://kislay536.github.io/assets/pdf/oob_dac.pdf">https://kislay536.github.io/assets/pdf/oob_dac.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 电源侧信道，英特尔软件保护扩展，英特尔信任域扩展 </p>
</div>

---

## 研究概要
本文提出OOPS跨带远程功耗侧信道攻击，针对开启RAPL过滤防护的Intel Sapphire Rapids服务器。逆向PECI协议RdPkgConfig指令，发现PCS能量读数不受噪声过滤；设计PMC同步通道，分别从SGX窃取2048位RSA密钥、从TDX恢复AESNI密钥，证明BMC带外管理接口是新型TEE泄露面。

## 背景和动机
1. 现有Platypus等攻击利用RAPL MSR读取内核功耗，Intel推出RAPL噪声过滤机制，业界认为该防护可阻断此类远程功耗攻击。
2. 现有侧信道研究仅聚焦CPU内核带内MSR接口，忽略服务器BMC带外(OOB)管理通道的遥测数据泄露风险。
3. PECI协议PCS包级功耗读取通道未纳入RAPL过滤管控，厂商安全范围仅覆盖带内寄存器，未评估带外接口威胁。
4. 带外BMC采集与飞地执行难以时序对齐，缺少无硬件修改的同步机制，限制带外侧信道攻击落地。
5. SGX、TDX两类可信执行环境未做PCS功耗隔离，包级能量数据可跨可信边界泄露密码运算特征。

## 相关工作
1. 带内功耗侧信道：Platypus、Hertzbleed等利用RAPL MSR读取内核功耗，依赖未过滤寄存器，开启RAPL防护后失效。
2. TEE微架构攻击：Spectre类瞬态攻击、缓存侧信道，均基于内核执行痕迹，不涉及服务器BMC带外接口。
3. BMC/PECI安全研究：仅研究故障注入、温度泄露，未挖掘PCS功耗遥测带来密钥窃取能力。
4. SGX/TDX防护方案：针对缓存、分支预测、内核MSR加固，未覆盖带外PECI功耗读取通道漏洞。
5. 远程CPA密钥恢复：全部依赖内核采集的功耗轨迹，无基于带外管理遥测的攻击方案。

## 本文解决方案
### 1 PECI协议逆向，识别未过滤PCS读取指令
逆向OpenBMC中PECI通信结构，区分RdIAMSR（同步内核MSR、受RAPL过滤）与RdPkgConfig（读取PCS包级能耗、无噪声干扰）；确定索引3、参数0xff可获取1ms高精度功耗数据。
### 2 基于禁用PMC的带内-带外同步通道
利用默认失效IA32_PMC0性能寄存器构建单向同步信号：带内程序改写PMC最低位，BMC持续轮询感知，精准对齐密码运算起止与功耗采样窗口。
### 3 SGX RSA密钥提取攻击
基于单步/零步进假设，采集RdPkgConfig功耗轨迹，区分平方/乘运算功耗差异，通过滑动窗口指数分析恢复2048位RSA私钥。
### 4 TDX AESNI无假设CPA攻击
无需单步调试，采集多轮AES加密PCS功耗，基于汉明重量功耗模型做相关性分析，拟合轮密钥字节，完整恢复128位AES密钥。
### 5 威胁边界验证
证实PCS为包级全局统计数据，不受SGX核心隔离、TDX MSR虚拟化保护，厂商现有TEE安全模型存在边界遗漏。

## 实验分析
1. 实验平台：Intel Xeon Platinum 8481C（Sapphire Rapids），OpenBMC基板管理控制器，RAPL过滤功能开启。
2. 通道对比：RdIAMSR与PCS功耗相关性仅0.04，PCS无噪声叠加，数据方差远低于过滤后的RAPL读数。
3. SGX RSA结果：采集一万条功耗样本，5小时恢复97.4%的2048位RSA密钥，剩余比特可格归约补齐。
4. TDX AES结果：百万条轨迹下猜测熵持续下降，成功还原13字节AES轮密钥，剩余3字节熵极低可穷举。
5. 厂商反馈：Intel确认该OOB通道不在SGX/TDX原生安全防护范围内，未纳入现有TEE威胁模型。

## 研究启发
1. TEE安全评估不能仅局限CPU内核带内接口，服务器BMC、PECI等带外管理通道存在独立侧信道攻击面。
2 单一部件防护（RAPL过滤）存在安全盲区，需统一管控内核与包级所有功耗遥测读取接口。
3. 芯片包级全局功耗统计不受逻辑隔离保护，SGX/TDX仅隔离核心执行上下文，无法阻断整机能耗特征泄露。
4. BMC作为TCB外组件，其遥测采集权限会形成跨可信边界隐蔽泄露通路，云服务器安全审计必须纳入带外固件。
5. 可信硬件威胁模型需扩展至整机管理子系统，不能仅局限处理器内核与指令集防护机制。
