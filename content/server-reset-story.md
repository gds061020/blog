Title: 服务器换盘历险记：从数据丢失到 Git 备份
Date: 2026-02-18
Category: 运维笔记
Tags: 服务器, Git, 教训

## 晴天霹雳
昨天收到服务商通知，服务器要换硬盘。当时没在意，结果今天登录——**数据全没了**！博客没了，区块链代码也没了。

## 重建之路
硬着头皮从头再来：
1. **SSH 连接**：IP 变了，端口也变了，重新配置 `~/.ssh/config`。
2. **安装环境**：nginx、Python、Pelican 重新装一遍。
3. **虚拟环境**：遇到 `externally-managed-environment` 错误，学会了用 `venv`。
4. **博客恢复**：凭记忆重写了两篇文章，虽然累，但加深了理解。
5. **换主题**：换上了 Elegant，博客焕然一新。

## 血的教训：一定要备份！
这次之后，我学会了用 Git 把博客和代码都推送到 GitHub：

- 博客仓库：[gds061020/blog](https://github.com/gds061020/blog)
- 区块链仓库：[gds061020/blockchain](https://github.com/gds061020/blockchain)

以后每次修改，只需 `git add` → `git commit` → `git push`，再也不怕数据丢失。

## 结语
这次经历虽然折腾，但收获巨大。以后看到这篇博客，会提醒自己：**备份！备份！备份！**