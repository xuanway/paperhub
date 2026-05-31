#!/usr/bin/env bash
# 快速创建新论文笔记
# 用法：bash scripts/new_paper.sh <会议> <分类> <文件名> [论文标题]
#
# 示例：
#   bash scripts/new_paper.sh ICLR2025 llm_reasoning attention_is_all_you_need "Attention Is All You Need"
#   bash scripts/new_paper.sh CVPR2025 image_generation sdxl "SDXL: Improving Latent Diffusion Models"

set -e

CONF="${1}"
TRACK="${2}"
SLUG="${3}"
TITLE="${4:-${SLUG}}"

if [[ -z "$CONF" || -z "$TRACK" || -z "$SLUG" ]]; then
  echo "用法: bash scripts/new_paper.sh <会议> <分类目录> <文件名(不含.md)> [论文标题]"
  echo ""
  echo "现有会议目录:"
  ls docs/ | grep -v "index.md\|stylesheets\|assets"
  exit 1
fi

DIR="docs/${CONF}/${TRACK}"
FILE="${DIR}/${SLUG}.md"

mkdir -p "$DIR"

# 如果分类 index.md 不存在，自动创建
if [[ ! -f "${DIR}/index.md" ]]; then
  cat > "${DIR}/index.md" << INDEXEOF
# ${TRACK}

本分类收录 ${CONF} 中关于 ${TRACK} 的论文解读。
INDEXEOF
  echo "✅ 创建分类索引: ${DIR}/index.md"
fi

# 如果论文文件已存在，退出
if [[ -f "$FILE" ]]; then
  echo "⚠️  文件已存在: $FILE"
  exit 1
fi

cat > "$FILE" << EOF
---
title: "${TITLE}"
description: ""
tags:
  - "${CONF}"
  - "${TRACK}"
---

# ${TITLE}

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">一句话描述论文核心贡献。</p>
<p class="paper-seo-summary__tags">${CONF} · ${TRACK}</p>
</div>

**论文链接**：[arXiv ]()
**代码**：
**机构**：

---

## 一句话总结

> 用一句话说清楚这篇论文解决了什么问题、用了什么方法、达到了什么效果。

## 背景与动机

- **问题**：
- **现有方案的不足**：
- **本文思路**：

## 方法详解

### 核心思想

### 关键模块

## 实验结果

| 数据集 | Metric | 本文 | 对比基线 |
|--------|--------|------|----------|
|        |        |      |          |

## 核心亮点

1.
2.
3.

## 局限性

-
EOF

echo ""
echo "✅ 已创建: $FILE"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 请在 mkdocs.yml 的 nav 部分添加以下条目："
echo ""
echo "      - ${TITLE}: ${CONF}/${TRACK}/${SLUG}.md"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "完成后运行: git add . && git commit -m 'add: ${TITLE}' && git push"
