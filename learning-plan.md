# 学习计划 — AI × Web3 School Cohort 0

起点：AI 熟悉 / Web3 有基础 / 编程基础脚本。  
目标：6 周内拼出一个 **AI Agent + 钱包 + 链上工具调用 + 可验证记录** 的最小可演示原型，作为黑客松雏形。

## 路径选择：Bridge-first

跳过 AI 基础线性课，直接进 Bridge 章节，用 Web3 基础按需补课。判断依据：

- AI 那一侧（LLM / Prompt / Context / RAG / Agent）已是日常工具，再读一遍收益低
- 真正的盲区在「Agent 怎么安全调链上」，而不是「Agent 是什么」
- 黑客松导向需要尽早动手，概念课只能压缩成索引

## 6 周里程碑

| 周 | 主题 | 目标产出 |
| --- | --- | --- |
| W1 | 环境 + Web3 复盘 | gh / wallet / RPC / testnet ETH 就位；读完 Wallet + Smart Contract + Account Abstraction，写 1 篇 handbook-feedback |
| W2 | Web3 Tool Use | 用 Agent 调通一次 RPC（读余额/读交易），写 `experiments/01-rpc-readonly/` |
| W3 | Agent Wallet | 跑通一次 Smart Account + Session Key 的最小 demo，记录权限边界 |
| W4 | Agent Workflow | 把 W2+W3 串成一个「Agent 帮我读链 + 限额签名」的小流程，加 human-in-the-loop |
| W5 | AI Security + Verifiable AI | 加 Prompt Injection 防护、审计日志；选 1 个验证手段（签名 / TEE / zk 概念） |
| W6 | 黑客松原型 | 锁定一个 track（Agentic Commerce / Wallet-Permission / AI Security），打磨 demo + README + 视频 |

## 每周节奏

- 周一：读 Handbook 当周 2–3 个节点，更新 `learning-plan.md` 当周细化
- 周二—周五：每天 1 个 task，写 `daily/YYYY-MM-DD.md`
- 周六：跑通本周 experiment，写 `experiments/<编号>-<主题>/README.md`
- 周日：复盘 + handbook-feedback + 决定下周是否调整路径

## 当前 Track 候选（W6 之前不锁死）

1. **Wallet / Permission** — 最贴近现有兴趣，UX 切入点最多
2. **Agentic Commerce** — Agent 发现服务 + 支付 + 凭证，故事最完整
3. **AI Security** — 防 Prompt Injection 的 Agent，门槛适中

## 不做清单

- 不深入 Solidity 合约开发（外包给 AI 生成 + 审）
- 不做 L1/L2 共识、密码学底层证明
- 不做纯前端 dApp 美化
