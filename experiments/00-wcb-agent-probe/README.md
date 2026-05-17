# 00 — WCB Agent API probe

第一个 experiment：用 WCB Agent Secret API Key 拉自己的课表 / 任务。  
也是 Agent Wallet 类问题的微缩演练 —— "Agent 拿了我的密钥能干什么"。

## 准备

1. WCB profile → Agent Secret API Key → 生成新 key（命名如 `claude-learning-agent`）
2. 在 Windows 用户级环境变量里加：

```
WCB_AGENT_SECRET_API_KEY=<你的 key>
```

> 不要写进 `.env` 提交、不要贴 prompt 截图、不要写 README。

## 运行

```bash
python pull-schedule.py
```

输出未来 3 周的 events + 当前 learner tasks 数量。

## 已知能力（learner key）

✅ 可调：
- `users.getProfile` / `users.getMyPermissions`
- `program.getById`（用 `idOrSlug` 字段，不是 `slug`）
- `events.listForLearner`
- `tasks.listForLearner` / `tasks.myTaskHistory` / `tasks.submitEvidence`
- `opportunities.list` / `opportunities.myApplications`

❌ 不开放（FORBIDDEN）：
- `program.list` / `program.listMine` / `program.getApplication`
- `tracks.listForProgram` / `tracks.mySelection` / `tracks.setMySelection`
- `announcements.listForLearner`
- `leaderboard.credits` / `tasks.myTotalPoints`
- 所有 `admin.*`

## 学习触点

这个 experiment 已经踩中 Bridge 章节几个关键问题：
- **Agent Identity**：key 继承 user 权限，learner key 能读 ≠ 能写选 Track
- **Agent Wallet** 的预演：权限边界由服务端定，不由 prompt 定
- **Audit**：所有调用都会留痕（`users.getAuditLogs`）

记 W1 复盘时回看这里。
