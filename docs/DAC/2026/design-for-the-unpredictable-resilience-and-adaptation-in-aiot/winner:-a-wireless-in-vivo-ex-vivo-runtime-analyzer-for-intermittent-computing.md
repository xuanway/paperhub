WINNER: A Wireless In-Vivo/ex-Vivo Runtime Analyzer for Intermittent Computing
Authors：
[Justin Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=365863146123072291)，[Arman Roohi](https://63dac.conference-program.com/?post_type=page&p=15&uid=642843)，[Nader Sehatbakhsh](https://63dac.conference-program.com/?post_type=page&p=15&uid=64032790672848841841)

## 中文标题

WINNER：面向间歇计算的无线体内/体外运行时分析器

## 英文摘要

Intermittent computing systems suffer from limited observability and lack effective runtime analysis mechanisms. Unlike conventional systems, they are vulnerable to a distinct class of failures known as intermittence bugs, which emerge from their fragmented non-linear execution model caused by frequent power out-ages. Traditional debugging tools are ill-suited for this context, as they assume persistent power and continuous connectivity. To address these challenges, we present a new remote runtime analyzer called WINNER. It is a lightweight task management that records fine-grained execution traces—such as interrupts, memory/register states—into non-volatile memory during regular operation (in-vivo), and exposes them only during debug sessions (ex-vivo) triggered automatically by a user-defined property violation, such as exceeding repeated task execution. Building on this, WINNER introduces a new software-based communication paradigm that leverages controllable electromagnetic emanations (side-channel) for frequent but low-rate uplink communication, enabling software-controlled ultra-low-energy data transmission (up to 4x lower than BLE). We evaluate our solution across six applications and five platforms, demonstrating its effectiveness in detecting various bugs. The introduced overhead is minimal, with a runtime increase of less than 1% and an average binary size increase of 6%. Our tool is open-sourced.

## 中文摘要

间歇计算系统受限于可观测性不足，缺乏有效的运行时分析机制。与传统系统不同，它们易受一类称为间歇性缺陷的独特故障影响，这类故障源于频繁断电所导致的碎片化非线性执行模型。传统调试工具不适用于这种场景，因为它们假定电源持续供电且连接持续可用。为应对这些挑战，我们提出一种新的远程运行时分析器，称为 WINNER。它是一种轻量级任务管理机制，在正常运行（体内）期间将细粒度执行轨迹——如中断、内存/寄存器状态——记录到非易失性存储器中，并且仅在由用户定义的属性违规（例如重复任务执行次数超限）自动触发的调试会话（体外）期间将其暴露出来。在此基础上，WINNER 引入一种新的基于软件的通信范式，利用可控的电磁辐射（侧信道）进行频繁但低速率的上行通信，实现软件控制的超低能耗数据传输（比 BLE 低最多 4 倍）。我们在六个应用和五个平台上评估了我们的方案，证明了其在检测各类缺陷方面的有效性。所引入的开销极小，运行时增加不到 1%，二进制文件平均增大 6%。我们的工具已开源。

## 英文关键词

Intermittent computing, runtime monitoring, side-channels

## 中文关键词

间歇计算、运行时监测、侧信道
