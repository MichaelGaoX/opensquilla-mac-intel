# OpenSquilla — Builds de bureau macOS Intel (x86_64)

<p align="center">
  <img src="assets/opensquilla-long-logo.png" alt="OpenSquilla logo" width="500">
</p>

<p align="center">
  <b>Installateurs de bureau officiels pour les appareils macOS Intel</b><br>
  Synchronisé automatiquement depuis <a href="https://github.com/opensquilla/opensquilla">opensquilla/opensquilla</a>, vérifié toutes les 3 heures
</p>

<p align="center">
  <a href="https://github.com/opensquilla/opensquilla">⬆️ Dépôt amont</a> ·
  <a href="https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2">🔍 Comparaison</a> ·
  <a href="https://github.com/MichaelGaoX/opensquilla-mac-intel/releases">📦 Téléchargements Intel</a>
</p>

<p align="center">
  <a href="README.md">中文</a> ·
  <a href="README.en.md">English</a> ·
  <a href="README.ja.md">日本語</a> ·
  <b>Français</b> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.es.md">Español</a>
</p>

---

## Qu'est-ce que c'est

[OpenSquilla](https://github.com/opensquilla/opensquilla) est un runtime d'agent
IA économe en tokens. Le projet amont ne publie que des installateurs macOS
Apple Silicon.

Ce dépôt construit des installateurs de bureau **macOS Intel (x86_64)** à partir
du code amont, pour les utilisateurs de Mac Intel.

## Différences avec l'amont

| Modification | Description |
|---|---|
| `onnxruntime <= 1.23.0` | La version 1.23.1+ a supprimé les wheels macOS x86_64 ; fixé à la dernière version compatible Intel |
| `wheelhouse-release.yml` | Construit uniquement les DMG/ZIP macOS Intel ; supprimé les builds arm64 / Windows / wheel |
| `sync-upstream.yml` | Vérifie les nouveaux tags amont toutes les 3 heures, synchronise et lance le build Intel |

> 🔍 [Voir la comparaison complète du code](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2)

## Téléchargement

Allez dans [Releases](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases) pour la dernière version :

- `OpenSquilla-{version}-mac-x64.dmg` — Installateur de bureau macOS Intel
- `OpenSquilla-{version}-mac-x64.zip` — Archive macOS Intel

## Utilisation

Pour l'installation, la configuration et la documentation, référez-vous au dépôt amont :

→ **[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

## Automatisation

- **sync-upstream.yml** — Vérifie les nouveaux tags amont toutes les 3 heures, synchronise le code et lance le build Intel
- **Déclenchement manuel** — Actions → Sync Upstream & Build Intel → Run workflow

## Licence

Ce projet hérite de la licence [Apache-2.0](LICENSE) amont.

[Dépôt amont](https://github.com/opensquilla/opensquilla) ·
[Comparaison](https://github.com/opensquilla/opensquilla/compare/v0.5.2...MichaelGaoX:opensquilla-mac-intel:v0.5.2) ·
[Téléchargements](https://github.com/MichaelGaoX/opensquilla-mac-intel/releases)