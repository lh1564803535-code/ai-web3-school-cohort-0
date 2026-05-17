# ai-web3-school-cohort-0

Personal **build log + experiments** for **AI × Web3 School** Cohort 0（2026-05-18 → 06-14）。

> 注意：这个 repo 不是打卡 repo。打卡走 ICL fork（`lh1564803535-code/AI-Web3-School` 的 `notes/lh1564803535-code.md`）。本 repo 写详细 build log + 代码 + 黑客松证据，是长期资产。

- Handbook：https://aiweb3.school/zh/handbook/
- WCB 课程：https://web3career.build/zh/programs/AI-Web3-School
- WCB Learning：https://web3career.build/zh/programs/AI-Web3-School#tab=learning
- ICL 打卡 repo：https://github.com/lh1564803535-code/AI-Web3-School
- Learning Agent Prompt：https://aiweb3.school/learning-agent.zh.txt

## 目录结构

| 目录 | 用途 |
| --- | --- |
| `profile.md` | 学员画像，Agent 每次启动先读 |
| `learning-plan.md` | 6 周学习路径与里程碑 |
| `daily/` | 每日学习笔记 `YYYY-MM-DD.md`，含计划/产出/打卡草稿 |
| `tasks/` | WCB 任务对应的笔记与提交说明 |
| `experiments/` | 自己跑通的最小 demo（脚本、prompt、合约调用片段） |
| `handbook-feedback/` | Handbook 阅读中发现的问题、错别字、概念建议 |
| `hackathon/` | 黑客松想法、组队记录、原型草稿 |
| `submissions/` | 正式提交的作品归档（链接 + 截图 + 说明） |
| `templates/` | 日报、任务笔记模板 |

## 隐私红线（public repo）

不写：助记词、私钥、API key、未公开联系方式、内部会议链接、他人个人数据、任何 secret。  
WCB Agent secret 只放本地环境变量 `WCB_AGENT_SECRET_API_KEY`，不进 commit、不进 prompt 截图、不进 README。

## 工作节奏（build-first）

**目标是 4 周内拼一个能 demo 的 AI × Web3 原型，不是写 4 周听课笔记。**  
每天 `daily/YYYY-MM-DD.md` 是 **build log**：写了几行代码、卡在哪、demo 进度。听课心得是次要副产品，没产出就如实写空转。详见 `learning-plan.md` 与 `CLAUDE.md`。

**打卡走 ICL fork**：本仓库写详细 build log，ICL fork 的 `notes/lh1564803535-code.md` 写当天精炼摘要，push 即打卡（平台 30 秒轮询）。两边内容不冗余。
