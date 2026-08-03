# OpenSquilla — macOS Intel (x86_64) Desktop Builds

<p align="center">
  <img src="assets/opensquilla-long-logo.png" alt="OpenSquilla logo" width="500">
</p>

<p align="center">
  <b>Official desktop installers for macOS Intel devices</b><br>
  Auto-synced from upstream <a href="https://github.com/opensquilla/opensquilla">opensquilla/opensquilla</a>, checked every 3 hours for new versions
</p>

<p align="center">
  <a href="https://github.com/opensquilla/opensquilla">⬆️ Upstream</a> ·
  <a href="https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2">🔍 Compare</a> ·
  <a href="https://github.com/MichaelGaoX/opensquilla-mac-intel/releases">📦 Intel Downloads</a>
</p>

<p align="center">
  <a href="README.md">中文</a> ·
  <b>English</b> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.es.md">Español</a>
</p>

---

## What is this

[OpenSquilla](https://github.com/opensquilla/opensquilla) is a token-efficient AI
Agent runtime. The upstream project only publishes macOS Apple Silicon installers.

This repository builds **macOS Intel (x86_64)** desktop installers on top of the
upstream code, for Intel Mac users.

## Differences from upstream

| Change | Description |
|---|---|
| `onnxruntime <= 1.23.0` | 1.23.1+ dropped macOS x86_64 wheels; pinned to last Intel-compatible version |
| `wheelhouse-release.yml` | Only builds macOS Intel DMG/ZIP; removed arm64 / Windows / wheel builds |
| `sync-upstream.yml` | Auto-checks upstream for new tags every 3 hours, syncs and triggers Intel build |

> 🔍 [View full code comparison](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2)

## Download

Go to [Releases](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases) for the latest version:

- `OpenSquilla-{version}-mac-x64.dmg` — macOS Intel desktop installer
- `OpenSquilla-{version}-mac-x64.zip` — macOS Intel archive

## Usage

For installation, configuration, and documentation, refer to the upstream repository:

→ **[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

## Automation

- **sync-upstream.yml** — Checks upstream for new tags every 3 hours, syncs code and triggers Intel build
- **Manual trigger** — Actions → Sync Upstream & Build Intel → Run workflow

## License

This project inherits the upstream [Apache-2.0](LICENSE) license.

[Upstream](https://github.com/opensquilla/opensquilla) ·
[Compare](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2) ·
[Downloads](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases)