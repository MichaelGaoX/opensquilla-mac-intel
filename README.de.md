# OpenSquilla — macOS Intel (x86_64) Desktop-Builds

<p align="center">
  <img src="assets/opensquilla-long-logo.png" alt="OpenSquilla logo" width="500">
</p>

<p align="center">
  <b>Offizielle Desktop-Installationsprogramme für macOS Intel-Geräte</b><br>
  Automatisch synchronisiert von <a href="https://github.com/opensquilla/opensquilla">opensquilla/opensquilla</a>, alle 3 Stunden auf neue Versionen geprüft
</p>

<p align="center">
  <a href="https://github.com/opensquilla/opensquilla">⬆️ Upstream-Repository</a> ·
  <a href="https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2">🔍 Code-Vergleich</a> ·
  <a href="https://github.com/MichaelGaoX/opensquilla-mac-intel/releases">📦 Intel-Downloads</a>
</p>

<p align="center">
  <a href="README.md">中文</a> ·
  <a href="README.en.md">English</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.fr.md">Français</a> ·
  <b>Deutsch</b> ·
  <a href="README.es.md">Español</a>
</p>

---

## Was ist das

[OpenSquilla](https://github.com/opensquilla/opensquilla) ist eine token-effiziente
AI-Agent-Laufzeitumgebung. Das Upstream-Projekt veröffentlicht nur macOS Apple
Silicon-Installationsprogramme.

Dieses Repository erstellt **macOS Intel (x86_64)** Desktop-Installationsprogramme
auf Basis des Upstream-Codes für Intel Mac-Benutzer.

## Unterschiede zum Upstream

| Änderung | Beschreibung |
|---|---|
| `onnxruntime <= 1.23.0` | 1.23.1+ hat macOS x86_64 Wheels entfernt; auf die letzte Intel-kompatible Version fixiert |
| `wheelhouse-release.yml` | Baut nur macOS Intel DMG/ZIP; arm64 / Windows / Wheel-Builds entfernt |
| `sync-upstream.yml` | Prüft alle 3 Stunden auf neue Upstream-Tags, synchronisiert und startet den Intel-Build |

> 🔍 [Vollständigen Code-Vergleich anzeigen](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2)

## Download

Gehen Sie zu [Releases](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases) für die neueste Version:

- `OpenSquilla-{version}-mac-x64.dmg` — macOS Intel Desktop-Installationsprogramm
- `OpenSquilla-{version}-mac-x64.zip` — macOS Intel-Archiv

## Verwendung

Für Installation, Konfiguration und Dokumentation verweisen wir auf das Upstream-Repository:

→ **[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

## Automatisierung

- **sync-upstream.yml** — Prüft alle 3 Stunden auf neue Upstream-Tags, synchronisiert den Code und startet den Intel-Build
- **Manueller Start** — Actions → Sync Upstream & Build Intel → Run workflow

## Lizenz

Dieses Projekt übernimmt die Upstream-[Apache-2.0](LICENSE)-Lizenz.

[Upstream-Repository](https://github.com/opensquilla/opensquilla) ·
[Code-Vergleich](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2) ·
[Downloads](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases)