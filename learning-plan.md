# 学习计划 — AI × Web3 School Cohort 0

起点：AI 熟悉 / Web3 有基础（DeFi 用户，未写合约）/ 编程基础脚本。  
目标：4 周内拼出一个 **AI Agent + 钱包 + 链上工具调用 + 可验证记录** 的最小可演示原型，作为黑客松雏形。

## 周期

**2026-05-18 → 2026-06-14（4 周，不是 6 周）**。已对齐 WCB Cohort 实际课表，详见 `wcb-schedule.md`。

## 路径选择：Bridge-first

跳过 AI 基础线性课，直接进 Bridge 章节，用 Web3 基础按需补课。判断依据：

- AI 那一侧（LLM / Prompt / Context / RAG / Agent）已是日常工具，再读一遍收益低
- 真正的盲区在「Agent 怎么安全调链上」，而不是「Agent 是什么」
- 4 周直奔黑客松，概念课只能压缩成索引

## 4 周里程碑（对齐 WCB 课表）

| 周 | WCB 主题节点 | 我的产出目标 |
| --- | --- | --- |
| **W1** 05-18 → 05-24 | 开营 / Hermes 从 0 到 1 / Web3 基础 / Week 1 例会 / ERC-8004 | ① 跟完 Hermes 课，跑通一次 Agent 调链上数据；② 选定 Track；③ 第 1 条 handbook-feedback；④ `experiments/01-rpc-readonly/` |
| **W2** 05-25 → 05-31 | （待 WCB 公布主题，预计 Wallet / Account Abstraction） | ① Smart Account + Session Key 最小 demo；② 写清"Agent 拿到什么权限"清单；③ `experiments/02-agent-wallet/` |
| **W3** 06-01 → 06-07 | （预计 Workflow / Tool Use 整合） | ① 串联 W1+W2 成一个「Agent 读链 + 限额签名 + 人审」流程；② 加 Prompt Injection 基础防护；③ `experiments/03-agent-workflow/` |
| **W4** 06-08 → 06-14 | （预计 hackathon 周 / 收官） | ① 锁 Track；② 打磨 demo + README + 30s 视频；③ 提交到 `submissions/` 并同步 WCB 平台 |

## 每日节奏

- 晚上：跟 WCB 课程或自学 → 记 `daily/YYYY-MM-DD.md` → 提交打卡
- 周中：交一个 task / experiment 的小产出
- 周日（W1/W2/W3 末）：复盘 + handbook-feedback + 下周路径微调

## 当前 Track 候选（最迟 W2 周一锁死）

1. **Wallet / Permission** — 最贴近兴趣，UX 切入点最多
2. **Agentic Commerce** — Agent 发现服务 + 支付 + 凭证，故事最完整
3. **AI Security** — 防 Prompt Injection 的 Agent，门槛适中

W1 末根据 Hermes 课实际体验决定。

## 不做清单

- 不深入 Solidity 合约开发（外包给 AI 生成 + 审）
- 不做 L1/L2 共识、密码学底层证明
- 不做纯前端 dApp 美化

## WCB 平台联动

- 课表自动拉：`experiments/00-wcb-agent-probe/`（用 `WCB_AGENT_SECRET_API_KEY` 环境变量）
- 任务提交：`tasks.submitEvidence`（W1 实测后写文档）
- 选 Track / 报名活动等不开放给 learner key 的，去网页操作
