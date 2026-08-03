# OpenSquilla — macOS Intel (x86_64) デスクトップビルド

<p align="center">
  <img src="assets/opensquilla-long-logo.png" alt="OpenSquilla logo" width="500">
</p>

<p align="center">
  <b>macOS Intel デバイス向けデスクトップインストーラー</b><br>
  上流 <a href="https://github.com/opensquilla/opensquilla">opensquilla/opensquilla</a> から自動同期、3時間ごとに新バージョンを確認
</p>

<p align="center">
  <a href="https://github.com/opensquilla/opensquilla">⬆️ 上流リポジトリ</a> ·
  <a href="https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2">🔍 コード比較</a> ·
  <a href="https://github.com/MichaelGaoX/opensquilla-mac-intel/releases">📦 Intel ダウンロード</a>
</p>

<p align="center">
  <a href="README.md">中文</a> ·
  <a href="README.en.md">English</a> ·
  <b>日本語</b> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.es.md">Español</a>
</p>

---

## これについて

[OpenSquilla](https://github.com/opensquilla/opensquilla) はトークン効率の高い
AIエージェントランタイムです。上流プロジェクトは macOS Apple Silicon
インストーラーのみ公開しています。

本リポジトリは上流コードをベースに **macOS Intel (x86_64)** デスクトップ
インストーラーを自動ビルドし、Intel Mac ユーザーに提供します。

## 上流との違い

| 変更 | 説明 |
|---|---|
| `onnxruntime <= 1.23.0` | 1.23.1+ は macOS x86_64 wheel を削除、最後の Intel 対応バージョンに固定 |
| `wheelhouse-release.yml` | macOS Intel DMG/ZIP のみビルド、arm64 / Windows / wheel ビルドを削除 |
| `sync-upstream.yml` | 3時間ごとに上流の新規タグを確認、同期後に Intel ビルドを自動実行 |

> 🔍 [完全なコード比較を見る](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2)

## ダウンロード

[Releases](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases) から最新版をダウンロード：

- `OpenSquilla-{version}-mac-x64.dmg` — macOS Intel デスクトップインストーラー
- `OpenSquilla-{version}-mac-x64.zip` — macOS Intel アーカイブ

## 使い方

インストール・設定・ドキュメントは上流リポジトリを参照：

→ **[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

## 自動化

- **sync-upstream.yml** — 3時間ごとに上流の新規タグを確認、コードを同期して Intel ビルドを実行
- **手動実行** — Actions → Sync Upstream & Build Intel → Run workflow

## ライセンス

本プロジェクトは上流の [Apache-2.0](LICENSE) ライセンスを継承します。

[上流リポジトリ](https://github.com/opensquilla/opensquilla) ·
[コード比較](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2) ·
[ダウンロード](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases)