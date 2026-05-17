# CLAUDE.md — ai-web3-school-cohort-0

> 项目级规则。下位补充全局 `~/.claude/CLAUDE.md`，不覆盖。

## 这是什么项目

卡兹克在 AI × Web3 School Cohort 0（2026-05-18 → 06-14, 4 周）的 **proof-of-work workspace**。public repo，用于沉淀 build log、experiments、handbook feedback。**不是听课笔记本**。

仓库：https://github.com/lh1564803535-code/ai-web3-school-cohort-0

## 核心原则：build-first，不是 class-first

开营当晚已确认课程内容偏轻，**重点不在课堂，在动手做出能演示的东西**。每周必须出一个可跑通的 experiment，不能只输出阅读笔记。

判断每个动作时反问：
- 这一步代码 / demo 增量是什么？
- 不写就不算今天有进度

听课只在两种情况值得现场：① 跟当周 build 直接相关；② 是稀缺的实战经验分享。其他一律回放 1.5x。

## 隐私红线（public repo）

绝不进文件 / commit / prompt 截图：
- WCB Agent Secret API Key（变量名 `WCB_AGENT_SECRET_API_KEY`）
- 助记词 / 私钥 / RPC URL 里的 API key 部分
- Telegram / 微信 / 邮件等未公开联系方式
- **图片类**：`daily/assets/` 是 public，**禁止**放聊天记录截图、私聊、密钥窗口、含真实身份证 / 银行卡 / 邮箱地址的页面截图

## 每日打卡流程（W1 试运行版）

**打卡的真实形态**（2026-05-17 晚发现）：WCB 平台不收 UI 贴图。打卡 = 给 ICL fork repo 的 `notes/lh1564803535-code.md` 追加一段 markdown 然后 push，平台每 30 秒拉一次检测更新。

涉及两个 repo，分工明确：

| Repo | 路径 | 角色 |
| --- | --- | --- |
| `lh1564803535-code/AI-Web3-School`（ICL fork） | 待 clone 到 `~/AI-Web3-School` | **打卡载体**。只编辑 `notes/lh1564803535-code.md`，每天追加一段。push 即提交 |
| `lh1564803535-code/ai-web3-school-cohort-0`（本仓库） | `~/ai-web3-school-cohort-0` | **build log + 黑客松证据**。代码、experiments、handbook-feedback、详细日记 |

两边内容不冗余：本仓库写"今天写了什么代码 / 卡在哪 / 截图 / 反思"，ICL notes 写"今日精炼版（3-8 行 + 关键截图）"。

**Agent 负责**：
- 拉课表（`python experiments/00-wcb-agent-probe/pull-schedule.py`）
- 预填本仓库当天 daily note 顶部
- 接收卡兹克给的图片 → 落 `daily/assets/YYYY-MM-DD-<slug>.png`
- 把对话整理进 daily note 中段
- 整理"ICL 打卡段"（3-8 行 markdown + 图片引用）
- 同时 push 两个 repo：本仓库（详细）+ ICL fork（精炼打卡段追加到 `notes/lh1564803535-code.md`）

**卡兹克负责**：
- 在对话里告诉 Agent：今天写了什么、卡在哪、哪些图要附
- 不需要再去 WCB UI 操作，push 到 ICL fork 就是打卡
- 30-60 秒后自己刷新 WCB 日历看是否变绿，回一句"绿了"或"没绿"

**W1 末（2026-05-24 周日）复盘**：
- ICL push 是否每次都被平台识别
- 截图嵌入是否有效（GitHub 渲染图片是公开 raw URL）
- 是否需要 Chrome 扩展辅助校验状态色

实际操作：
- secret 一律走 Windows 用户级环境变量（`setx KEY VALUE`）
- 代码里只用 `os.environ.get(...)`，没拿到就报错退出，不要默认值
- `.gitignore` 已封死 `.env` / `*.key` / `secrets/` 等
- commit 前过一遍 `git diff` 检查是否带出了 token 字符串

## WCB Agent API 使用约定

- 端点：`https://web3career.build/api/agent/call`（POST）+ `/api/agent/catalog`（GET）
- 鉴权：`Authorization: Bearer $WCB_AGENT_SECRET_API_KEY`，**必须带 `User-Agent` header**（默认 Python urllib UA 会被 403）
- learner key 能力清单见 `experiments/00-wcb-agent-probe/README.md`，**踩过的坑都写在那**
- 写入操作（如 `tasks.submitEvidence`）：先 dry-run 打印 payload → 卡兹克目视确认 → 再真发
- 关键 ID（如 programId）写到 `experiments/00-wcb-agent-probe/pull-schedule.py` 顶部常量，不散落

## 4 周 build 目标（待第一次 experiment 后锁死）

候选项目：**Wallet Lens Agent** —— 输入地址，Agent 读链 → LLM 总结 → 风险标签。
理由：每周长一层，每层映射一个 Bridge 章节，黑客松能投。

W1 出 `experiments/01-wallet-lens/` 跑通"读地址 + 5 行总结"后再正式锁。

## 文件归属

| 路径 | 受众 | 写什么 / 不写什么 |
| --- | --- | --- |
| `README.md` | 第一次看仓库的人 | 项目是什么、怎么读这个仓库、隐私红线 |
| `profile.md` | Agent 启动时读 | 学员画像、目标、节奏偏好 |
| `learning-plan.md` | 卡兹克 + Agent | 4 周 build 路径，每周 deliverable 而非阅读量 |
| `wcb-schedule.md` | 卡兹克 | 课表（自动生成，不手动维护） |
| `daily/YYYY-MM-DD.md` | 卡兹克自己复盘 | **build log**：今天写了几行代码、卡在哪、demo 进度。听课心得是次要副产品 |
| `experiments/<编号>-<主题>/` | 黑客松评委 + 自己回看 | 跑得通的最小代码 + README + 视频/截图 |
| `handbook-feedback/` | LXDAO / ETHPanda | 错别字、概念盲点、结构建议，开源 PR 候选 |
| `submissions/` | WCB 平台 | 正式提交件归档（链接 + 摘要） |
| `tasks/` | 留白 | WCB 任务系统下发后再填，目前空 |
| `hackathon/` | 留白 | W3-W4 才用 |

## 不进项目的事

- 全局 CLAUDE.md 已经讲过的（决策三法、第一性原理、工具默认）不复述，引用即可
- 公众号写作 / Obsidian 脑爆 / task-observer 这些归属在 `~/Documents/Obsidian Vault/脑爆/`，跟这个项目无关，**不要把内容生产逻辑掺进来**

## 同步约定

- 日常 commit 用英文、动词起手、≤72 字符
- 涉及 build 进度推进必 push（让仓库可作为黑客松证据）
- 每周日复盘后给 `learning-plan.md` 一次 minor 更新，反映实际偏移
