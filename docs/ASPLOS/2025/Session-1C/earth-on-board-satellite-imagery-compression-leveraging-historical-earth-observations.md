---
title: "Earth+: On-Board Satellite Imagery Compression Leveraging Historical Earth Observations"
description: "ASPLOS 2025 · Session 1C · Earth+：利用历史地球观测数据的星上卫星图像压缩"
tags:
  - "ASPLOS2025"
  - "Session 1C"
  - "Edge Computing"
---

# Earth+: On-Board Satellite Imagery Compression Leveraging Historical Earth Observations

**中文标题：** Earth+：利用历史地球观测数据的星上卫星图像压缩

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Kuntai Du (University of Chicago), Yihua Cheng (University of Chicago), Peder Olsen (Microsoft Research), Shadi Noghabi (Microsoft Research), Junchen Jiang (University of Chicago)

**单位：** University of Chicago；Microsoft Research

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707222) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Due to limited downlink (satellite-to-ground) capacity, over 90% of the images captured by the earth-observation satellites are not downloaded to the ground. To overcome the downlink limitation, we present Earth+, a new on-board satellite imagery compression system that identifies and downloads only changed areas in each image compared to latest on-board reference images of the same location. The key of Earth+ is that it obtains latest on-board reference images by letting the ground stations upload images recently captured by all satellites in the constellation. To our best knowledge, Earth+ is the first system that leverages images across an entire satellite constellation to enable more images to be downloaded to the ground (by better satellite imagery compression). Our evaluation shows that to download images of the same area, Earth+ can reduce the downlink usage by 3.3× compared to state-of-the-art on-board image compression techniques without sacrificing imagery quality or using more resources (downlink, computation or storage).

## 中文摘要

由于下行链路（星地之间）容量有限，对地观测卫星所拍摄的图像中有超过 90% 无法下传至地面。为克服下行链路限制，我们提出 Earth+，一种新型星上卫星图像压缩系统，它通过将每幅图像与同一位置最新的星上参考图像进行比对，仅识别并下传发生变化区域。Earth+ 的关键在于，它让地面站上传星座中所有卫星近期拍摄的图像，从而获得最新的星上参考图像。据我们所知，Earth+ 是首个利用整个卫星星座的图像来实现更多图像下传（通过更好的卫星图像压缩）的系统。我们的评估表明，在下载同一区域图像时，与最先进的星上图像压缩技术相比，Earth+ 可在不牺牲图像质量、也不消耗更多资源（下行链路、计算或存储）的前提下，将下行链路用量降低 3.3 倍。

## 英文关键词

satellite imagery compression, reference image, downlink optimization, earth observation satellites

## 中文关键词

卫星图像压缩；参考图像；下行链路优化；对地观测卫星

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707222)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1C](index.md) · [返回 ASPLOS 2025](../index.md)
