# Hermes Agent 预习笔记（明晚 05-19 20:00 课程预备）

> 目的：明晚课程之前先有基础理解，听课时能带着问题听，不被 onboarding 占满注意力。

## 是什么

Hermes Agent — **Nous Research** 出品的开源 AI agent。

核心卖点：
- **持久记忆**（persistent memory）：跨会话记得做过什么、学过什么
- **自动生成 skill**：从经历里"长出"可复用的技能，不靠人手写 prompt
- **多平台触达**：能在不同 surface（CLI / IM / web）找到你
- **自托管**：跑在你自己服务器上，数据不出本地

## 关键资源

- 官网：https://hermes-agent.nousresearch.com/
- GitHub：https://github.com/nousresearch/hermes-agent
- 中文介绍：https://hermes-agent.org/

## 听课带着的问题

1. **持久记忆怎么实现** — 是 RAG over conversation log？是 fine-tune？还是结构化 skill DB？
2. **skill 自动生成的边界** — 什么样的"经历"会被沉淀成 skill？防止 skill 爆炸怎么做？
3. **vs Claude Code skill 体系** — Claude Code 的 skill 是 markdown + 元数据，触发靠描述匹配。Hermes 怎么做触发？
4. **Web3 接口** — 这是 AI × Web3 课，Hermes 怎么连钱包、签名、链上工具？是 MCP server，还是内置？
5. **secret 管理** — 长期跑的 agent 怎么保管 RPC key、wallet、API key？

## 课后立刻做

- clone repo，跑 hello world
- 写到 `experiments/01-hermes-hello/`：本地跑通的最小路径 + 5 个问题的实证答案
- 一条 handbook-feedback：Handbook 里 "Agent" / "Frameworks" 章节有没有讲 Hermes 这种 self-improving 模式？没讲就提案

## 已有储备（可直接对比）

- Claude Code skill 体系（已经在用）
- Claude Agent SDK（自定义 agent 经验）
- task-observer 那套观察→沉淀机制（自己的 meta-skill）
