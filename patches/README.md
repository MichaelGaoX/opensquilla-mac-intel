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

当前尚无自定义补丁。如需添加，创建 `patches/custom.patch` 文件即可。
