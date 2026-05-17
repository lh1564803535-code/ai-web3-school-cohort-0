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

WCB 平台和 GitHub repo 是**两份独立内容**，不靠 URL 联动。WCB 当天打卡用，GitHub 长期 build log + 黑客松证据。

**Agent 负责**：
- 拉课表（`python experiments/00-wcb-agent-probe/pull-schedule.py`）
- 预填当天 daily note 顶部（build 目标、课程清单）
- 接收卡兹克给的图片 → 落 `daily/assets/YYYY-MM-DD-<slug>.png`
- 把对话里的"做了 X / 卡在 Y"整理进 daily note 中段
- 整理"打卡正文段"（3-6 行，能直接复制到 WCB）
- `git add . && git commit && git push`

**卡兹克负责**：
- 在对话里告诉 Agent：今天写了什么代码、卡在哪、哪些图要附
- 复制 Agent 整理的"打卡正文段"到 WCB UI，手动贴图，提交
- 提交后回一句"打过了"

**W1 末（2026-05-24 周日）复盘**：
- 流程跑通几次？哪些环节冗余？是否升级到双轨 / 脚本化 / `tasks.submitEvidence` API。

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
