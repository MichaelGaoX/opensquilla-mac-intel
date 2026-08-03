# OpenSquilla — macOS Intel (x86_64) 桌面构建

<p align="center">
  <img src="assets/opensquilla-long-logo.png" alt="OpenSquilla logo" width="500">
</p>

<p align="center">
  <b>为 macOS Intel 设备提供官方桌面安装包</b><br>
  自动同步上游 <a href="https://github.com/opensquilla/opensquilla">opensquilla/opensquilla</a>，每 3 小时检查新版本
</p>

<p align="center">
  <a href="https://github.com/opensquilla/opensquilla">⬆️ 上游仓库</a> ·
  <a href="https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2">🔍 代码对比</a> ·
  <a href="https://github.com/MichaelGaoX/opensquilla-mac-intel/releases">📦 Intel 下载</a>
</p>

---

## 这是什么

[OpenSquilla](https://github.com/opensquilla/opensquilla) 是一个 token 高效的 AI
Agent 运行时。上游官方只发布 macOS Apple Silicon 安装包。

本仓库在上游代码基础上，自动构建 **macOS Intel (x86_64)** 桌面安装包，供 Intel Mac
用户使用。

## 与上游的区别

| 改动 | 说明 |
|---|---|
| `onnxruntime <= 1.23.0` | 1.23.1+ 移除了 macOS x86_64 wheel，锁定最后一个支持 Intel 的版本 |
| `wheelhouse-release.yml` | 只构建 macOS Intel DMG/ZIP，移除 arm64 / Windows / wheel 构建 |
| `sync-upstream.yml` | 每 3 小时自动检查上游新 tag，同步后自动构建 Intel 安装包 |

> 🔍 [查看完整代码对比](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2)

## 下载

前往 [Releases](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases) 下载最新版本：

- `OpenSquilla-{version}-mac-x64.dmg` — macOS Intel 桌面安装包
- `OpenSquilla-{version}-mac-x64.zip` — macOS Intel 压缩包

## 使用

安装、配置、文档全部参考上游仓库：

→ **[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

## 自动化

- **sync-upstream.yml** — 每 3 小时检查上游新 tag，自动同步代码并触发 Intel 构建
- **手动触发** — Actions → Sync Upstream & Build Intel → Run workflow

## 许可

本项目沿用上游的 [Apache-2.0](LICENSE) 许可。

[上游仓库](https://github.com/opensquilla/opensquilla) ·
[代码对比](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2) ·
[下载](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases)