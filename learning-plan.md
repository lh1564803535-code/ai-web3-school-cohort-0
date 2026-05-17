# 学习计划 — AI × Web3 School Cohort 0

起点：AI 熟悉 / Web3 有基础（DeFi 用户，未写合约）/ 编程基础脚本。  
**目标：4 周内拼出一个能演示的 AI Agent × Web3 原型。** 不是写 4 周的听课笔记。

## 周期

2026-05-18 → 2026-06-14（4 周 bootcamp）。课表见 `wcb-schedule.md`。

## 路径选择：Build-first，不是 class-first

开营仪式（2026-05-17 晚）后判断：课程内容偏轻，重点必须落在自建项目。

- 听课不是产出，**代码和 demo 才是**
- Handbook 已通读，作为索引按需翻
- 每周必出一个能跑通的 experiment，不能只交"今天读了 X"

听课优先级：
- 🔥 必到（与 build 直接相关）：Hermes 从 0 到 1（05-19）、ERC-8004 / 8183（05-23）
- ✅ 推荐：AI 时代基础架构（05-18）、AI 下乡计划（05-21）
- ⚪ 跳过 / 回放 1.5x：Co-Learning 时段、Z.AI、Web3 运行原理（基础已会）

## 候选项目：Wallet Lens Agent

> 一句话：**输入任意地址，Agent 读链上活动，返回人话报告 + 风险标签。**

W1 出最小版本后正式锁定。判优逻辑：
- 切口在卡兹克最强的"AI + UX"，不需要写 Solidity
- 每周长一层，每层映射 Bridge 一个章节
- 黑客松直接能投 Wallet/Permission 或 Open Track
- 每一步都能拍 30 秒 demo 视频

| 周 | 加什么能力 | Bridge 章节映射 | 能演示什么 |
| --- | --- | --- | --- |
| **W1** 05-18 → 05-24 | 只读 RPC：拉地址最近 N 笔 tx，LLM 总结 5 行人话 | Chain-aware Context + Web3 Tool Use | "把任意地址扔进去，30 秒看懂这钱包在干什么" |
| **W2** 05-25 → 05-31 | Smart Account + Session Key，Agent 在限额内代签 | Agent Wallet + Account Abstraction | "Agent 帮我自动 claim airdrop，但只能花 $5 gas，超了打回" |
| **W3** 06-01 → 06-07 | 规则引擎 + human-in-the-loop + 审计日志 | Agent Workflow + AI Security | "可疑操作 Agent 必须问我，所有动作链上可查" |
| **W4** 06-08 → 06-14 | 包装成可演示产品 + 30s 视频 + README | Verifiable AI（签名留痕） | 提交 hackathon |

如果 W1 跑通后发现这条路不对，第二候选：**防 Prompt Injection 的 Agent**（AI Security track）。

## 每周节奏

- 周一：明确本周 deliverable（一段代码 + README）
- 周二—周五：动手，每天写 build log（不是听课心得）
- 周六：跑通 + 录 30s demo 视频
- 周日：复盘 + 1 条 handbook-feedback + 下周路径微调

## 不做清单

- 不深入 Solidity 合约开发（外包给 AI 生成 + 审）
- 不做 L1/L2 共识、密码学底层证明
- 不做纯前端 dApp 美化
- **不为了打卡而打卡**：没产出就如实写"今日空转"，不凑字数

## WCB 平台联动

- 课表自动拉：`python experiments/00-wcb-agent-probe/pull-schedule.py`
- 任务提交：`tasks.submitEvidence`（W1 实测后写文档）
- 选 Track / 报名活动：去网页操作（API 不开放给 learner key）
