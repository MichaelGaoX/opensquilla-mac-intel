# OpenSquilla — Builds de escritorio macOS Intel (x86_64)

<p align="center">
  <img src="assets/opensquilla-long-logo.png" alt="OpenSquilla logo" width="500">
</p>

<p align="center">
  <b>Instaladores de escritorio oficiales para dispositivos macOS Intel</b><br>
  Sincronizado automáticamente desde <a href="https://github.com/opensquilla/opensquilla">opensquilla/opensquilla</a>, verificado cada 3 horas
</p>

<p align="center">
  <a href="https://github.com/opensquilla/opensquilla">⬆️ Repositorio upstream</a> ·
  <a href="https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2">🔍 Comparación</a> ·
  <a href="https://github.com/MichaelGaoX/opensquilla-mac-intel/releases">📦 Descargas Intel</a>
</p>

<p align="center">
  <a href="README.md">中文</a> ·
  <a href="README.en.md">English</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <b>Español</b>
</p>

---

## ¿Qué es esto

[OpenSquilla](https://github.com/opensquilla/opensquilla) es un runtime de agente
IA eficiente en tokens. El proyecto upstream solo publica instaladores para
macOS Apple Silicon.

Este repositorio construye instaladores de escritorio **macOS Intel (x86_64)** a
partir del código upstream, para usuarios de Mac Intel.

## Diferencias con el upstream

| Cambio | Descripción |
|---|---|
| `onnxruntime <= 1.23.0` | La versión 1.23.1+ eliminó los wheels de macOS x86_64; fijado a la última versión compatible con Intel |
| `wheelhouse-release.yml` | Solo construye DMG/ZIP de macOS Intel; eliminados los builds de arm64 / Windows / wheel |
| `sync-upstream.yml` | Verifica nuevos tags del upstream cada 3 horas, sincroniza y lanza el build de Intel |

> 🔍 [Ver comparación completa de código](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2)

## Descarga

Vaya a [Releases](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases) para la última versión:

- `OpenSquilla-{version}-mac-x64.dmg` — Instalador de escritorio macOS Intel
- `OpenSquilla-{version}-mac-x64.zip` — Archivo macOS Intel

## Uso

Para instalación, configuración y documentación, consulte el repositorio upstream:

→ **[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

## Automatización

- **sync-upstream.yml** — Verifica nuevos tags del upstream cada 3 horas, sincroniza el código y lanza el build de Intel
- **Ejecución manual** — Actions → Sync Upstream & Build Intel → Run workflow

## Licencia

Este proyecto hereda la licencia [Apache-2.0](LICENSE) del upstream.

[Repositorio upstream](https://github.com/opensquilla/opensquilla) ·
[Comparación](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2) ·
[Descargas](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases)