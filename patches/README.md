# 自定义补丁

此目录存放你对上游代码的自定义修改补丁。

## 使用方法

1. 本地拉取上游代码并修改
2. 生成补丁文件：
   ```bash
   git diff upstream/main > patches/custom.patch
   ```
3. 提交并推送补丁文件：
   ```bash
   git add patches/
   git commit -m "update custom patches for v0.5.3"
   git push origin main
   ```

## 自动化

`sync-upstream.yml` 会在每次同步上游时自动应用 `patches/*.patch`。
如果补丁冲突，同步会失败并报错，需要你手动更新补丁文件。

## 示例

- `patches/desktop-update-darwin-x64.patch` — 客户端自动更新通道改为 macOS Intel 单平台：
  - `update-channel.ts`：平台收敛为 `darwin-x64`，GitHub 发现/下载源指向本 fork；资产要求改为 `mac-x64`（dmg/zip/latest-mac.yml/SHA256SUMS）
  - `main.ts`：`desktopUpdatePlatform()` 只认 `darwin` + `x64`
  - `update-feed-resolver.ts`：`GITHUB_UPDATE_OWNER/REPO` 指向本 fork
  - `package.json`：repository / publish 指向本 fork
  - 同步更新 `test-update-resolver.mjs`、`test-packaged-update-banner.mjs` 断言

> 注意：若上游改动这些文件导致补丁冲突，`sync-upstream.yml` 会报错并停止，需要手动更新本补丁。
