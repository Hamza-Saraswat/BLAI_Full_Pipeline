# SOURCE CACHE
# fetched via: web_extract
# accessed: 2026-11-25
# note: page text as fetched this session; em dashes (U+2014) replaced with -- per repo convention.

# url: https://github.com/open-webui/open-webui
# title: GitHub - open-webui/open-webui: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
# tier: tier 1 (primary, GitHub repo page; star/fork/contributor counts seen 2026-11-25)

[Skip to content](https://github.com/open-webui/open-webui#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/open-webui/open-webui) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/open-webui/open-webui) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/open-webui/open-webui) to refresh your session.Dismiss alert

{{ message }}

main

[**2** Branches](https://github.com/open-webui/open-webui/branches) [**183** Tags](https://github.com/open-webui/open-webui/tags)

[Go to Branches page](https://github.com/open-webui/open-webui/branches)[Go to Tags page](https://github.com/open-webui/open-webui/tags)

Go to file

Code

Open more actions menu

## Latest commit

[![tjbck](https://avatars.githubusercontent.com/u/25473318?v=4&size=40)](https://github.com/tjbck)[tjbck](https://github.com/open-webui/open-webui/commits?author=tjbck)

[Merge pull request](https://github.com/open-webui/open-webui/commit/926f826eaef6179c092a936eede6c7363e425975) [#34613](https://github.com/open-webui/open-webui/pull/34613) [from open-webui/dev](https://github.com/open-webui/open-webui/commit/926f826eaef6179c092a936eede6c7363e425975)

Open commit detailssuccess

2 hours agoNov 25, 2026

[926f826](https://github.com/open-webui/open-webui/commit/926f826eaef6179c092a936eede6c7363e425975) · 2 hours agoNov 25, 2026

## History

[21,286 Commits](https://github.com/open-webui/open-webui/commits/main/)

Open commit details

[View commit history for this file.](https://github.com/open-webui/open-webui/commits/main/) 21,286 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [.github](https://github.com/open-webui/open-webui/tree/main/.github ".github") | [.github](https://github.com/open-webui/open-webui/tree/main/.github ".github") | [ci: stop running the test suite automatically on release pull requests (](https://github.com/open-webui/open-webui/commit/27b82831a46ebe9bd191871d32e55d4921124d45 "ci: stop running the test suite automatically on release pull requests (#34037)  While a release pull request is open, every commit to dev restarted the full test suite and cancelled the run that was in progress, so runs rarely finished and they kept taking runners from the builds here. The suite is now started by hand from the tests repo against the commit we want checked. A run started there is not cancelled by new commits, so it finishes, and nothing starts a new one on every commit.") | 2 weeks agoNov 11, 2026 |
| [backend](https://github.com/open-webui/open-webui/tree/main/backend "backend") | [backend](https://github.com/open-webui/open-webui/tree/main/backend "backend") | [fix: attaching a file without pandoc sometimes shows a raw error inst…](https://github.com/open-webui/open-webui/commit/7e5634d2086be4e87e3c7921b1421933ee489a9a "fix: attaching a file without pandoc sometimes shows a raw error instead of \"Pandoc is not installed\" (#35065)  On a server without pandoc, attaching a file that needs it could show the raw library error, which tells the user to install pandoc themselves, instead of \"Pandoc is not installed on the server\". The raw error was saved first and replaced with the friendly message a moment later, and the chat often picked up the raw one in between. The friendly message is now saved right away, so the warning toast always shows it.  Fixes #35064") | 2 hours agoNov 25, 2026 |
| [crypto/encryption](https://github.com/open-webui/open-webui/tree/main/crypto/encryption "This path skips through empty directories") | [crypto/encryption](https://github.com/open-webui/open-webui/tree/main/crypto/encryption "This path skips through empty directories") | [refac](https://github.com/open-webui/open-webui/commit/7dc91de86c41866f4170602f074c39dbf1609377 "refac") | last monthOct 15, 2026 |
| [docs](https://github.com/open-webui/open-webui/tree/main/docs "docs") | [docs](https://github.com/open-webui/open-webui/tree/main/docs "docs") | [docs: CVE ID requests go through GitHub Security Advisories only (](https://github.com/open-webui/open-webui/commit/0fe01f276585c1904b5ec5d9a555a3e767712653 "docs: CVE ID requests go through GitHub Security Advisories only (#34992)  The security policy now says that CVE ID requests, like vulnerability reports, are accepted only through GitHub Security Advisories. The CVE program asked for this wording so requests do not reach other channels.") [#34992](https://github.com/open-webui/open-webui/pull/34992) | 12 hours agoNov 24, 2026 |
| [scripts](https://github.com/open-webui/open-webui/tree/main/scripts "scripts") | [scripts](https://github.com/open-webui/open-webui/tree/main/scripts "scripts") | [refac](https://github.com/open-webui/open-webui/commit/d99ec1c02cfb6f45caa858bc9b4ba34a8963084f "refac") | 3 weeks agoNov 1, 2026 |
| [src](https://github.com/open-webui/open-webui/tree/main/src "src") | [src](https://github.com/open-webui/open-webui/tree/main/src "src") | [chore: format](https://github.com/open-webui/open-webui/commit/bb51c01700757e04fb383e0fd5d35c7b5525e2a0 "chore: format") | 2 hours agoNov 25, 2026 |
| [static](https://github.com/open-webui/open-webui/tree/main/static "static") | [static](https://github.com/open-webui/open-webui/tree/main/static "static") | [refac](https://github.com/open-webui/open-webui/commit/5b75d3100a9a0ce0f2fd7f4be51f8dd291ece05f "refac") | 12 hours agoNov 24, 2026 |
| [test/test\_files/image\_gen](https://github.com/open-webui/open-webui/tree/main/test/test_files/image_gen "This path skips through empty directories") | [test/test\_files/image\_gen](https://github.com/open-webui/open-webui/tree/main/test/test_files/image_gen "This path skips through empty directories") | [feat: add image gen with automatic1111 to integration test](https://github.com/open-webui/open-webui/commit/a937f6504a6a4e692acdd7a33ee83f533c52783e "feat: add image gen with automatic1111 to integration test") | 2 years agoMay 20, 2024 |
| [.dockerignore](https://github.com/open-webui/open-webui/blob/main/.dockerignore ".dockerignore") | [.dockerignore](https://github.com/open-webui/open-webui/blob/main/.dockerignore ".dockerignore") | [refac](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1 "refac") | 2 months agoSep 6, 2026 |
| [.env.example](https://github.com/open-webui/open-webui/blob/main/.env.example ".env.example") | [.env.example](https://github.com/open-webui/open-webui/blob/main/.env.example ".env.example") | [refac](https://github.com/open-webui/open-webui/commit/57c955a0330a1dbf4f1387bdbd246231e4c31b0d "refac") | yesterdayNov 24, 2026 |
| [.eslintignore](https://github.com/open-webui/open-webui/blob/main/.eslintignore ".eslintignore") | [.eslintignore](https://github.com/open-webui/open-webui/blob/main/.eslintignore ".eslintignore") | [refac](https://github.com/open-webui/open-webui/commit/7dc91de86c41866f4170602f074c39dbf1609377 "refac") | last monthOct 15, 2026 |
| [.eslintrc.cjs](https://github.com/open-webui/open-webui/blob/main/.eslintrc.cjs ".eslintrc.cjs") | [.eslintrc.cjs](https://github.com/open-webui/open-webui/blob/main/.eslintrc.cjs ".eslintrc.cjs") | [feat: add basic cypress test as initial work towards e2e tests](https://github.com/open-webui/open-webui/commit/730befce45fdb42ef16909b645d57664102f09e3 "feat: add basic cypress test as initial work towards e2e tests") | 2 years agoApr 27, 2024 |
| [.gitattributes](https://github.com/open-webui/open-webui/blob/main/.gitattributes ".gitattributes") | [.gitattributes](https://github.com/open-webui/open-webui/blob/main/.gitattributes ".gitattributes") | [refac: standardize formatting in .gitattributes for consistency](https://github.com/open-webui/open-webui/commit/5fb5daf07fc86cf6809d5edc54089daa61f7fe9d "refac: standardize formatting in .gitattributes for consistency") | last yearJun 4, 2025 |
| [.gitignore](https://github.com/open-webui/open-webui/blob/main/.gitignore ".gitignore") | [.gitignore](https://github.com/open-webui/open-webui/blob/main/.gitignore ".gitignore") | [refac](https://github.com/open-webui/open-webui/commit/1810b2547e7b1ee10d06d42967848fc2e6e79ab3 "refac") | 3 days agoNov 22, 2026 |
| [.npmrc](https://github.com/open-webui/open-webui/blob/main/.npmrc ".npmrc") | [.npmrc](https://github.com/open-webui/open-webui/blob/main/.npmrc ".npmrc") | [chat feature added](https://github.com/open-webui/open-webui/commit/5e03670f1eedf42fd2bda5df6264c41f05da0219 "chat feature added") | 3 years agoOct 8, 2023 |
| [.pre-commit-config.yaml](https://github.com/open-webui/open-webui/blob/main/.pre-commit-config.yaml ".pre-commit-config.yaml") | [.pre-commit-config.yaml](https://github.com/open-webui/open-webui/blob/main/.pre-commit-config.yaml ".pre-commit-config.yaml") | [feat: add ruff linter & formatter (](https://github.com/open-webui/open-webui/commit/b73010bb366b18b1297b67de25e7e07e2a737534 "feat: add ruff linter & formatter (#22576)  * chore: add ruff linter with base config  * ci: add ruff pre-commit hook  * ci: add ruff github actions workflow  * ci: run ruff only on changed files") [#22576](https://github.com/open-webui/open-webui/pull/22576) [)](https://github.com/open-webui/open-webui/commit/b73010bb366b18b1297b67de25e7e07e2a737534 "feat: add ruff linter & formatter (#22576)  * chore: add ruff linter with base config  * ci: add ruff pre-commit hook  * ci: add ruff github actions workflow  * ci: run ruff only on changed files") | 8 months agoMar 15, 2026 |
| [.prettierignore](https://github.com/open-webui/open-webui/blob/main/.prettierignore ".prettierignore") | [.prettierignore](https://github.com/open-webui/open-webui/blob/main/.prettierignore ".prettierignore") | [refac](https://github.com/open-webui/open-webui/commit/7dc91de86c41866f4170602f074c39dbf1609377 "refac") | last monthOct 15, 2026 |
| [.prettierrc](https://github.com/open-webui/open-webui/blob/main/.prettierrc ".prettierrc") | [.prettierrc](https://github.com/open-webui/open-webui/blob/main/.prettierrc ".prettierrc") | [refac: update .gitattributes and .prettierrc for consistent line endings](https://github.com/open-webui/open-webui/commit/059327cd19fbc3a931432b91520610ad5bb4009e "refac: update .gitattributes and .prettierrc for consistent line endings") | last yearJun 4, 2025 |
| [CHANGELOG.md](https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md "CHANGELOG.md") | [CHANGELOG.md](https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md "CHANGELOG.md") | [doc: changelog](https://github.com/open-webui/open-webui/commit/46af28cfaf3912cefc512cbe8bf0256be2f08067 "doc: changelog") | 12 hours agoNov 24, 2026 |
| [CODE\_OF\_CONDUCT.md](https://github.com/open-webui/open-webui/blob/main/CODE_OF_CONDUCT.md "CODE_OF_CONDUCT.md") | [CODE\_OF\_CONDUCT.md](https://github.com/open-webui/open-webui/blob/main/CODE_OF_CONDUCT.md "CODE_OF_CONDUCT.md") | [refac](https://github.com/open-webui/open-webui/commit/3394a10b765c7b619c292b0ccf927dedde6e5f5f "refac") | 2 months agoSep 16, 2026 |
| [CONTRIBUTOR\_LICENSE\_AGREEMENT](https://github.com/open-webui/open-webui/blob/main/CONTRIBUTOR_LICENSE_AGREEMENT "CONTRIBUTOR_LICENSE_AGREEMENT") | [CONTRIBUTOR\_LICENSE\_AGREEMENT](https://github.com/open-webui/open-webui/blob/main/CONTRIBUTOR_LICENSE_AGREEMENT "CONTRIBUTOR_LICENSE_AGREEMENT") | [refac](https://github.com/open-webui/open-webui/commit/c71beb0a7df1a4e4a3ac7ace757fe67a73e4935a "refac") | 9 months agoFeb 28, 2026 |
| [Dockerfile](https://github.com/open-webui/open-webui/blob/main/Dockerfile "Dockerfile") | [Dockerfile](https://github.com/open-webui/open-webui/blob/main/Dockerfile "Dockerfile") | [feat: build the Docker image from locked, hash-verified dependencies (](https://github.com/open-webui/open-webui/commit/1c58242b4ffa89786276607da0e39108df838f3c "feat: build the Docker image from locked, hash-verified dependencies (#33981)  The image used to install only the directly pinned packages and resolved everything below them fresh from PyPI on every build, so the same commit could produce different images. The standard and slim images now install from lock files that pin every package with hashes, except PyTorch and its few own dependencies, which still come from the PyTorch index so the CPU and CUDA variants keep working. A new CI check fails when a requirements file changes without regenerating its lock, and the script that regenerates them sits next to the requirements.  Fixes #33979") [#…](https://github.com/open-webui/open-webui/pull/33981) | 2 weeks agoNov 9, 2026 |
| [LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE "LICENSE") | [LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE "LICENSE") | [refac: license](https://github.com/open-webui/open-webui/commit/26a645f9e64914799bafa343413d95bd295cf6b7 "refac: license  wording") | 7 months agoApr 14, 2026 |
| [LICENSE\_HISTORY](https://github.com/open-webui/open-webui/blob/main/LICENSE_HISTORY "LICENSE_HISTORY") | [LICENSE\_HISTORY](https://github.com/open-webui/open-webui/blob/main/LICENSE_HISTORY "LICENSE_HISTORY") | [refac](https://github.com/open-webui/open-webui/commit/43e11aa8072a395ee1c27ed000891c430e2894a0 "refac") | last yearJul 18, 2025 |
| [LICENSE\_NOTICE](https://github.com/open-webui/open-webui/blob/main/LICENSE_NOTICE "LICENSE_NOTICE") | [LICENSE\_NOTICE](https://github.com/open-webui/open-webui/blob/main/LICENSE_NOTICE "LICENSE_NOTICE") | [doc: readme](https://github.com/open-webui/open-webui/commit/6bc5d331a27c5106f492213510a763effa316faf "doc: readme") | last yearSep 20, 2025 |
| [Makefile](https://github.com/open-webui/open-webui/blob/main/Makefile "Makefile") | [Makefile](https://github.com/open-webui/open-webui/blob/main/Makefile "Makefile") | [Chose between "docker-compose" and "docker compose" in Makefile](https://github.com/open-webui/open-webui/commit/e1e66f708f595388b49af54f6765adf31b9a1d4d "Chose between \"docker-compose\" and \"docker compose\" in Makefile") | 2 years agoApr 19, 2024 |
| [README.ar.md](https://github.com/open-webui/open-webui/blob/main/README.ar.md "README.ar.md") | [README.ar.md](https://github.com/open-webui/open-webui/blob/main/README.ar.md "README.ar.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.bn.md](https://github.com/open-webui/open-webui/blob/main/README.bn.md "README.bn.md") | [README.bn.md](https://github.com/open-webui/open-webui/blob/main/README.bn.md "README.bn.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.br.md](https://github.com/open-webui/open-webui/blob/main/README.br.md "README.br.md") | [README.br.md](https://github.com/open-webui/open-webui/blob/main/README.br.md "README.br.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.bs.md](https://github.com/open-webui/open-webui/blob/main/README.bs.md "README.bs.md") | [README.bs.md](https://github.com/open-webui/open-webui/blob/main/README.bs.md "README.bs.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.da.md](https://github.com/open-webui/open-webui/blob/main/README.da.md "README.da.md") | [README.da.md](https://github.com/open-webui/open-webui/blob/main/README.da.md "README.da.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.de.md](https://github.com/open-webui/open-webui/blob/main/README.de.md "README.de.md") | [README.de.md](https://github.com/open-webui/open-webui/blob/main/README.de.md "README.de.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.es.md](https://github.com/open-webui/open-webui/blob/main/README.es.md "README.es.md") | [README.es.md](https://github.com/open-webui/open-webui/blob/main/README.es.md "README.es.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.fr.md](https://github.com/open-webui/open-webui/blob/main/README.fr.md "README.fr.md") | [README.fr.md](https://github.com/open-webui/open-webui/blob/main/README.fr.md "README.fr.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.gr.md](https://github.com/open-webui/open-webui/blob/main/README.gr.md "README.gr.md") | [README.gr.md](https://github.com/open-webui/open-webui/blob/main/README.gr.md "README.gr.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.it.md](https://github.com/open-webui/open-webui/blob/main/README.it.md "README.it.md") | [README.it.md](https://github.com/open-webui/open-webui/blob/main/README.it.md "README.it.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.ja.md](https://github.com/open-webui/open-webui/blob/main/README.ja.md "README.ja.md") | [README.ja.md](https://github.com/open-webui/open-webui/blob/main/README.ja.md "README.ja.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.ko.md](https://github.com/open-webui/open-webui/blob/main/README.ko.md "README.ko.md") | [README.ko.md](https://github.com/open-webui/open-webui/blob/main/README.ko.md "README.ko.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.md](https://github.com/open-webui/open-webui/blob/main/README.md "README.md") | [README.md](https://github.com/open-webui/open-webui/blob/main/README.md "README.md") | [refac](https://github.com/open-webui/open-webui/commit/b76e2f6a3f4918b5bfd816271b23e4abb13c2a34 "refac") | 12 hours agoNov 24, 2026 |
| [README.no.md](https://github.com/open-webui/open-webui/blob/main/README.no.md "README.no.md") | [README.no.md](https://github.com/open-webui/open-webui/blob/main/README.no.md "README.no.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.pl.md](https://github.com/open-webui/open-webui/blob/main/README.pl.md "README.pl.md") | [README.pl.md](https://github.com/open-webui/open-webui/blob/main/README.pl.md "README.pl.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.ru.md](https://github.com/open-webui/open-webui/blob/main/README.ru.md "README.ru.md") | [README.ru.md](https://github.com/open-webui/open-webui/blob/main/README.ru.md "README.ru.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.th.md](https://github.com/open-webui/open-webui/blob/main/README.th.md "README.th.md") | [README.th.md](https://github.com/open-webui/open-webui/blob/main/README.th.md "README.th.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.tr.md](https://github.com/open-webui/open-webui/blob/main/README.tr.md "README.tr.md") | [README.tr.md](https://github.com/open-webui/open-webui/blob/main/README.tr.md "README.tr.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.uk.md](https://github.com/open-webui/open-webui/blob/main/README.uk.md "README.uk.md") | [README.uk.md](https://github.com/open-webui/open-webui/blob/main/README.uk.md "README.uk.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.vi.md](https://github.com/open-webui/open-webui/blob/main/README.vi.md "README.vi.md") | [README.vi.md](https://github.com/open-webui/open-webui/blob/main/README.vi.md "README.vi.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.zh.md](https://github.com/open-webui/open-webui/blob/main/README.zh.md "README.zh.md") | [README.zh.md](https://github.com/open-webui/open-webui/blob/main/README.zh.md "README.zh.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [README.zht.md](https://github.com/open-webui/open-webui/blob/main/README.zht.md "README.zht.md") | [README.zht.md](https://github.com/open-webui/open-webui/blob/main/README.zht.md "README.zht.md") | [refac](https://github.com/open-webui/open-webui/commit/c6dde2a4e6392e6d9f48390808b052a45ee1a90d "refac") | 12 hours agoNov 24, 2026 |
| [TROUBLESHOOTING.md](https://github.com/open-webui/open-webui/blob/main/TROUBLESHOOTING.md "TROUBLESHOOTING.md") | [TROUBLESHOOTING.md](https://github.com/open-webui/open-webui/blob/main/TROUBLESHOOTING.md "TROUBLESHOOTING.md") | [fix: Fix typos](https://github.com/open-webui/open-webui/commit/12516c8a45cf478672d8d38721535144ec17b764 "fix: Fix typos") | 2 years agoOct 14, 2024 |
| [banner.png](https://github.com/open-webui/open-webui/blob/main/banner.png "banner.png") | [banner.png](https://github.com/open-webui/open-webui/blob/main/banner.png "banner.png") | [doc: banner](https://github.com/open-webui/open-webui/commit/67fd2ec759ef8701dadff19377f14e763335aa86 "doc: banner") | 11 months agoDec 21, 2025 |
| [contribution\_stats.py](https://github.com/open-webui/open-webui/blob/main/contribution_stats.py "contribution_stats.py") | [contribution\_stats.py](https://github.com/open-webui/open-webui/blob/main/contribution_stats.py "contribution_stats.py") | [refac](https://github.com/open-webui/open-webui/commit/de3317e26bb67a2a7ea015a183bbd1d369880ebd "refac") | 8 months agoMar 17, 2026 |
| [docker-cleanup.sh](https://github.com/open-webui/open-webui/blob/main/docker-cleanup.sh "docker-cleanup.sh") | [docker-cleanup.sh](https://github.com/open-webui/open-webui/blob/main/docker-cleanup.sh "docker-cleanup.sh") | [refac](https://github.com/open-webui/open-webui/commit/d99ec1c02cfb6f45caa858bc9b4ba34a8963084f "refac") | 3 weeks agoNov 1, 2026 |
| [docker-compose-launcher.sh](https://github.com/open-webui/open-webui/blob/main/docker-compose-launcher.sh "docker-compose-launcher.sh") | [docker-compose-launcher.sh](https://github.com/open-webui/open-webui/blob/main/docker-compose-launcher.sh "docker-compose-launcher.sh") | [refac](https://github.com/open-webui/open-webui/commit/d99ec1c02cfb6f45caa858bc9b4ba34a8963084f "refac") | 3 weeks agoNov 1, 2026 |
| [docker-compose.a1111-test.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.a1111-test.yaml "docker-compose.a1111-test.yaml") | [docker-compose.a1111-test.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.a1111-test.yaml "docker-compose.a1111-test.yaml") | [feat: add image gen with automatic1111 to integration test](https://github.com/open-webui/open-webui/commit/a937f6504a6a4e692acdd7a33ee83f533c52783e "feat: add image gen with automatic1111 to integration test") | 2 years agoMay 20, 2024 |
| [docker-compose.amdgpu.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.amdgpu.yaml "docker-compose.amdgpu.yaml") | [docker-compose.amdgpu.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.amdgpu.yaml "docker-compose.amdgpu.yaml") | [Add variables](https://github.com/open-webui/open-webui/commit/8db03f3ab28b2ae98173352dafc189d0b7cd9837 "Add variables") | 2 years agoApr 6, 2024 |
| [docker-compose.api.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.api.yaml "docker-compose.api.yaml") | [docker-compose.api.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.api.yaml "docker-compose.api.yaml") | [Removed version synatax as its no longer needed per Docker Docs](https://github.com/open-webui/open-webui/commit/93aea0a4d4d05ec841bacf446be971a397e66914 "Removed version synatax as its no longer needed per Docker Docs") | 2 years agoMay 9, 2024 |
| [docker-compose.data.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.data.yaml "docker-compose.data.yaml") | [docker-compose.data.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.data.yaml "docker-compose.data.yaml") | [Removed version synatax as its no longer needed per Docker Docs](https://github.com/open-webui/open-webui/commit/93aea0a4d4d05ec841bacf446be971a397e66914 "Removed version synatax as its no longer needed per Docker Docs") | 2 years agoMay 9, 2024 |
| [docker-compose.gpu.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.gpu.yaml "docker-compose.gpu.yaml") | [docker-compose.gpu.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.gpu.yaml "docker-compose.gpu.yaml") | [Removed version synatax as its no longer needed per Docker Docs](https://github.com/open-webui/open-webui/commit/93aea0a4d4d05ec841bacf446be971a397e66914 "Removed version synatax as its no longer needed per Docker Docs") | 2 years agoMay 9, 2024 |
| [docker-compose.otel.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.otel.yaml "docker-compose.otel.yaml") | [docker-compose.otel.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.otel.yaml "docker-compose.otel.yaml") | [fix: otel yaml](https://github.com/open-webui/open-webui/commit/626ad9c83d7dc0065604042eabb72f45ea3b4381 "fix: otel yaml") | last yearJul 24, 2025 |
| [docker-compose.playwright.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.playwright.yaml "docker-compose.playwright.yaml") | [docker-compose.playwright.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.playwright.yaml "docker-compose.playwright.yaml") | [chore: bump Python backend dependencies, drop unused peewee (](https://github.com/open-webui/open-webui/commit/b295a20b9df5f9e513d5da6b7ca1a404bf03db18 "chore: bump Python backend dependencies, drop unused peewee (#25786)  * chore: bump Python backend dependencies, drop unused peewee  Minor/patch + reviewed major bumps across requirements.txt, requirements-min.txt, pyproject.toml and uv.lock; playwright image bumped in docker-compose.playwright.yaml. peewee/peewee-migrate removed (zero imports).  Security-relevant: cryptography 46->48, authlib 1.6.10->1.7.2, PyJWT 2.11->2.13, requests 2.33.1->2.34.2, RestrictedPython 8.1->8.2, pillow 12.1.1->12.2.0. Reviewed majors: redis 7->8, pymilvus ->2.6.14, azure-search-documents 11->12, chardet 5->7, unstructured 0.18->0.22, pycrdt 0.12->0.13.  Testing: - Resolution: `uv lock` resolves the full bumped set with no conflicts; uv.lock   regenerated to match (peewee dropped, every pin including   azure-search-documents==12.0.0 resolves). - Per-dependency contract tests (external tests repo, unit/deps/): 105 files,   2205 passed / 6 skipped, ruff-clean. One file per dependency pins the symbols,   signatures and behaviour the backend actually uses, so an API removal/rename in   a bumped version fails loudly instead of at runtime. Offline/deterministic. - End-to-end embed->retrieve test driving transformers + sentence-transformers +   chromadb together through Open WebUI's real RAG path (cached model, in-memory   chroma, semantic retrieval asserted). - Install/startup/health resolution gate added to the dep-bump workflow and the   integration suite (uv/pip resolve + uvicorn /health + Playwright dev visibility). - Bugs surfaced while testing each got an isolated fix branch + regression test:   Mistral OCR aiohttp FilePayload (#25779), chroma has_collection (#25780),   aiocache per-user model-cache key (security), otel semconv deprecation,   pydub/audioop <3.13 note.  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>  * Bump python-multipart 0.0.22 -> 0.0.27 (CVE-2026-42561, CVE-2026-40347)  0.0.22 is affected by two DoS CVEs in the multipart parser that Starlette/FastAPI run for every multipart/form-data request, so any authenticated user hitting an upload endpoint can trigger them: - CVE-2026-42561: unbounded part-header count/size -> CPU exhaustion (fixed 0.0.27) - CVE-2026-40347: large multipart preamble/epilogue DoS (fixed 0.0.26)  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>  ---------  Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>") [#25786](https://github.com/open-webui/open-webui/pull/25786) [)](https://github.com/open-webui/open-webui/commit/b295a20b9df5f9e513d5da6b7ca1a404bf03db18 "chore: bump Python backend dependencies, drop unused peewee (#25786)  * chore: bump Python backend dependencies, drop unused peewee  Minor/patch + reviewed major bumps across requirements.txt, requirements-min.txt, pyproject.toml and uv.lock; playwright image bumped in docker-compose.playwright.yaml. peewee/peewee-migrate removed (zero imports).  Security-relevant: cryptography 46->48, authlib 1.6.10->1.7.2, PyJWT 2.11->2.13, requests 2.33.1->2.34.2, RestrictedPython 8.1->8.2, pillow 12.1.1->12.2.0. Reviewed majors: redis 7->8, pymilvus ->2.6.14, azure-search-documents 11->12, chardet 5->7, unstructured 0.18->0.22, pycrdt 0.12->0.13.  Testing: - Resolution: `uv lock` resolves the full bumped set with no conflicts; uv.lock   regenerated to match (peewee dropped, every pin including   azure-search-documents==12.0.0 resolves). - Per-dependency contract tests (external tests repo, unit/deps/): 105 files,   2205 passed / 6 skipped, ruff-clean. One file per dependency pins the symbols,   signatures and behaviour the backend actually uses, so an API removal/rename in   a bumped version fails loudly instead of at runtime. Offline/deterministic. - End-to-end embed->retrieve test driving transformers + sentence-transformers +   chromadb together through Open WebUI's real RAG path (cached model, in-memory   chroma, semantic retrieval asserted). - Install/startup/health resolution gate added to the dep-bump workflow and the   integration suite (uv/pip resolve + uvicorn /health + Playwright dev visibility). - Bugs surfaced while testing each got an isolated fix branch + regression test:   Mistral OCR aiohttp FilePayload (#25779), chroma has_collection (#25780),   aiocache per-user model-cache key (security), otel semconv deprecation,   pydub/audioop <3.13 note.  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>  * Bump python-multipart 0.0.22 -> 0.0.27 (CVE-2026-42561, CVE-2026-40347)  0.0.22 is affected by two DoS CVEs in the multipart parser that Starlette/FastAPI run for every multipart/form-data request, so any authenticated user hitting an upload endpoint can trigger them: - CVE-2026-42561: unbounded part-header count/size -> CPU exhaustion (fixed 0.0.27) - CVE-2026-40347: large multipart preamble/epilogue DoS (fixed 0.0.26)  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>  ---------  Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>") | 5 months agoJun 29, 2026 |
| [docker-compose.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.yaml "docker-compose.yaml") | [docker-compose.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.yaml "docker-compose.yaml") | [refac](https://github.com/open-webui/open-webui/commit/ca332db7eb8bbc8496a9fc771834bea257446e54 "refac") | last yearOct 20, 2025 |
| [docker-ollama.sh](https://github.com/open-webui/open-webui/blob/main/docker-ollama.sh "docker-ollama.sh") | [docker-ollama.sh](https://github.com/open-webui/open-webui/blob/main/docker-ollama.sh "docker-ollama.sh") | [refac](https://github.com/open-webui/open-webui/commit/d99ec1c02cfb6f45caa858bc9b4ba34a8963084f "refac") | 3 weeks agoNov 1, 2026 |
| [docker-run.sh](https://github.com/open-webui/open-webui/blob/main/docker-run.sh "docker-run.sh") | [docker-run.sh](https://github.com/open-webui/open-webui/blob/main/docker-run.sh "docker-run.sh") | [refac](https://github.com/open-webui/open-webui/commit/d99ec1c02cfb6f45caa858bc9b4ba34a8963084f "refac") | 3 weeks agoNov 1, 2026 |
| [docker-update-models.sh](https://github.com/open-webui/open-webui/blob/main/docker-update-models.sh "docker-update-models.sh") | [docker-update-models.sh](https://github.com/open-webui/open-webui/blob/main/docker-update-models.sh "docker-update-models.sh") | [refac](https://github.com/open-webui/open-webui/commit/d99ec1c02cfb6f45caa858bc9b4ba34a8963084f "refac") | 3 weeks agoNov 1, 2026 |
| [hatch\_build.py](https://github.com/open-webui/open-webui/blob/main/hatch_build.py "hatch_build.py") | [hatch\_build.py](https://github.com/open-webui/open-webui/blob/main/hatch_build.py "hatch_build.py") | [fix: Docker, frontend CI and pip builds fail when the ONNX runtime GP…](https://github.com/open-webui/open-webui/commit/d67c707027ade0b86813c85d19449c787a9fd6a4 "fix: Docker, frontend CI and pip builds fail when the ONNX runtime GPU download times out (#33917)  Installing the frontend dependencies makes the onnxruntime-node package download its GPU binaries from GitHub releases, and the whole install fails whenever that download times out. Neither the frontend build nor the Docker image uses those binaries (the image only ships the built frontend), so the Docker build, the frontend CI and building the Python package now skip that download with ONNXRUNTIME_NODE_INSTALL_CUDA=skip. The regular CPU binaries are part of the npm package and are not affected.") | 2 weeks agoNov 8, 2026 |
| [i18next-parser.config.ts](https://github.com/open-webui/open-webui/blob/main/i18next-parser.config.ts "i18next-parser.config.ts") | [i18next-parser.config.ts](https://github.com/open-webui/open-webui/blob/main/i18next-parser.config.ts "i18next-parser.config.ts") | [refac](https://github.com/open-webui/open-webui/commit/e7771ad00c3daa40238ec51abfbc883683d1876a "refac") | last monthOct 10, 2026 |
| [package-lock.json](https://github.com/open-webui/open-webui/blob/main/package-lock.json "package-lock.json") | [package-lock.json](https://github.com/open-webui/open-webui/blob/main/package-lock.json "package-lock.json") | [refac](https://github.com/open-webui/open-webui/commit/10af571e7113fa9bcfddfec3cc7cf93cc93dfbed "refac") | 13 hours agoNov 24, 2026 |
| [package.json](https://github.com/open-webui/open-webui/blob/main/package.json "package.json") | [package.json](https://github.com/open-webui/open-webui/blob/main/package.json "package.json") | [refac](https://github.com/open-webui/open-webui/commit/10af571e7113fa9bcfddfec3cc7cf93cc93dfbed "refac") | 13 hours agoNov 24, 2026 |
| [postcss.config.js](https://github.com/open-webui/open-webui/blob/main/postcss.config.js "postcss.config.js") | [postcss.config.js](https://github.com/open-webui/open-webui/blob/main/postcss.config.js "postcss.config.js") | [chore: format](https://github.com/open-webui/open-webui/commit/a79a6a5c347153656bafabcf8779aed548c341b6 "chore: format") | last yearFeb 18, 2025 |
| [pyproject.toml](https://github.com/open-webui/open-webui/blob/main/pyproject.toml "pyproject.toml") | [pyproject.toml](https://github.com/open-webui/open-webui/blob/main/pyproject.toml "pyproject.toml") | [chore: bump redis to 8.2.0 (](https://github.com/open-webui/open-webui/commit/6b1d890ffd556a0aa0d7e24b7a1b1b607f47b555 "chore: bump redis to 8.2.0 (#34835)  Moves the Redis client library from 8.0.1 to 8.2.0. When a Redis server or proxy rejects the newer handshake, connecting now falls back to the older protocol by default instead of failing. On Sentinel setups, the connections behind the socket locks and shared socket state are no longer reused after an interrupted read, and Sentinel lookups no longer retry the same Sentinel. No other package changes version.") [#34835](https://github.com/open-webui/open-webui/pull/34835) [)](https://github.com/open-webui/open-webui/commit/6b1d890ffd556a0aa0d7e24b7a1b1b607f47b555 "chore: bump redis to 8.2.0 (#34835)  Moves the Redis client library from 8.0.1 to 8.2.0. When a Redis server or proxy rejects the newer handshake, connecting now falls back to the older protocol by default instead of failing. On Sentinel setups, the connections behind the socket locks and shared socket state are no longer reused after an interrupted read, and Sentinel lookups no longer retry the same Sentinel. No other package changes version.") | 2 days agoNov 23, 2026 |
| [svelte.config.js](https://github.com/open-webui/open-webui/blob/main/svelte.config.js "svelte.config.js") | [svelte.config.js](https://github.com/open-webui/open-webui/blob/main/svelte.config.js "svelte.config.js") | [refac](https://github.com/open-webui/open-webui/commit/51f0e01258b92c77952d4534bb8ce8c618b2700c "refac") | last monthOct 5, 2026 |
| [tailwind.config.js](https://github.com/open-webui/open-webui/blob/main/tailwind.config.js "tailwind.config.js") | [tailwind.config.js](https://github.com/open-webui/open-webui/blob/main/tailwind.config.js "tailwind.config.js") | [refac](https://github.com/open-webui/open-webui/commit/2d27ef4ece915629002e0b789cdb19522983f6cc "refac  Co-Authored-By: Ingmar van Hulzen <13165062+ingmarvanhulzen@users.noreply.github.com>") | 9 months agoFeb 28, 2026 |
| [tsconfig.json](https://github.com/open-webui/open-webui/blob/main/tsconfig.json "tsconfig.json") | [tsconfig.json](https://github.com/open-webui/open-webui/blob/main/tsconfig.json "tsconfig.json") | [chat feature added](https://github.com/open-webui/open-webui/commit/5e03670f1eedf42fd2bda5df6264c41f05da0219 "chat feature added") | 3 years agoOct 8, 2023 |
| [uv.lock](https://github.com/open-webui/open-webui/blob/main/uv.lock "uv.lock") | [uv.lock](https://github.com/open-webui/open-webui/blob/main/uv.lock "uv.lock") | [chore: bump redis to 8.2.0 (](https://github.com/open-webui/open-webui/commit/6b1d890ffd556a0aa0d7e24b7a1b1b607f47b555 "chore: bump redis to 8.2.0 (#34835)  Moves the Redis client library from 8.0.1 to 8.2.0. When a Redis server or proxy rejects the newer handshake, connecting now falls back to the older protocol by default instead of failing. On Sentinel setups, the connections behind the socket locks and shared socket state are no longer reused after an interrupted read, and Sentinel lookups no longer retry the same Sentinel. No other package changes version.") [#34835](https://github.com/open-webui/open-webui/pull/34835) [)](https://github.com/open-webui/open-webui/commit/6b1d890ffd556a0aa0d7e24b7a1b1b607f47b555 "chore: bump redis to 8.2.0 (#34835)  Moves the Redis client library from 8.0.1 to 8.2.0. When a Redis server or proxy rejects the newer handshake, connecting now falls back to the older protocol by default instead of failing. On Sentinel setups, the connections behind the socket locks and shared socket state are no longer reused after an interrupted read, and Sentinel lookups no longer retry the same Sentinel. No other package changes version.") | 2 days agoNov 23, 2026 |
| [vite.config.ts](https://github.com/open-webui/open-webui/blob/main/vite.config.ts "vite.config.ts") | [vite.config.ts](https://github.com/open-webui/open-webui/blob/main/vite.config.ts "vite.config.ts") | [refac](https://github.com/open-webui/open-webui/commit/e46920dcc73d5e0edec0679d5323e19bf1c61410 "refac") | 2 weeks agoNov 11, 2026 |
| View all files |

## Repository files navigation

## Open WebUI

[Permalink: Open WebUI](https://github.com/open-webui/open-webui#open-webui)

Open WebUI is [**a home for AI**](https://docs.openwebui.com/): an extensible, easy-to-use, self-hosted platform built to run entirely offline. Connect local models through Ollama, use OpenAI-compatible APIs for local and cloud models, or add agents through [Agent Client Protocol (ACP)](https://docs.openwebui.com/features/open-terminal/agents).

[English](https://github.com/open-webui/open-webui/blob/main/README.md) \|
[简体中文](https://github.com/open-webui/open-webui/blob/main/README.zh.md) \|
[繁體中文](https://github.com/open-webui/open-webui/blob/main/README.zht.md) \|
[한국어](https://github.com/open-webui/open-webui/blob/main/README.ko.md) \|
[Deutsch](https://github.com/open-webui/open-webui/blob/main/README.de.md) \|
[Español](https://github.com/open-webui/open-webui/blob/main/README.es.md) \|
[Français](https://github.com/open-webui/open-webui/blob/main/README.fr.md) \|
[Italiano](https://github.com/open-webui/open-webui/blob/main/README.it.md) \|
[Dansk](https://github.com/open-webui/open-webui/blob/main/README.da.md) \|
[日本語](https://github.com/open-webui/open-webui/blob/main/README.ja.md) \|
[Polski](https://github.com/open-webui/open-webui/blob/main/README.pl.md) \|
[Русский](https://github.com/open-webui/open-webui/blob/main/README.ru.md) \|
[Bosanski](https://github.com/open-webui/open-webui/blob/main/README.bs.md) \|
[العربية](https://github.com/open-webui/open-webui/blob/main/README.ar.md) \|
[Norsk](https://github.com/open-webui/open-webui/blob/main/README.no.md) \|
[Português (Brasil)](https://github.com/open-webui/open-webui/blob/main/README.br.md) \|
[ไทย](https://github.com/open-webui/open-webui/blob/main/README.th.md) \|
[Türkçe](https://github.com/open-webui/open-webui/blob/main/README.tr.md) \|
[Українська](https://github.com/open-webui/open-webui/blob/main/README.uk.md) \|
[বাংলা](https://github.com/open-webui/open-webui/blob/main/README.bn.md) \|
[Ελληνικά](https://github.com/open-webui/open-webui/blob/main/README.gr.md) \|
[Tiếng Việt](https://github.com/open-webui/open-webui/blob/main/README.vi.md)

[![Open WebUI Demo](https://camo.githubusercontent.com/7424a3b98d6029c2865a30b849370e6540a06b6c73dbf9d5185014f396f809f2/68747470733a2f2f63646e2e6f70656e77656275692e636f6d2f6f70656e2d77656275692d64656d6f2e676966)](https://docs.openwebui.com/)[![Open WebUI Demo](https://camo.githubusercontent.com/7424a3b98d6029c2865a30b849370e6540a06b6c73dbf9d5185014f396f809f2/68747470733a2f2f63646e2e6f70656e77656275692e636f6d2f6f70656e2d77656275692d64656d6f2e676966)](https://docs.openwebui.com/)

![GitHub stars](https://camo.githubusercontent.com/b037b4e6687c774a59808d14c2c3836809dba1e6ec64175a7aacad171148d195/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6f70656e2d77656275692f6f70656e2d77656275693f7374796c653d736f6369616c)![GitHub forks](https://camo.githubusercontent.com/eaceba8b5f5f59c9775e3c966d2863670c06fb713c68c89c987d58370f091f22/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6f70656e2d77656275692f6f70656e2d77656275693f7374796c653d736f6369616c)![GitHub watchers](https://camo.githubusercontent.com/e3c7db7ecca3b2f7c6df49e38e72e3f5593f9193aa09b17a9912fb52e26e508d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f77617463686572732f6f70656e2d77656275692f6f70656e2d77656275693f7374796c653d736f6369616c)![GitHub repo size](https://camo.githubusercontent.com/ebf99de6a9214ebb05564cd6f63167150dfcc27f6ec5848fdf58f3e7d2e4142e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7265706f2d73697a652f6f70656e2d77656275692f6f70656e2d7765627569)![GitHub language count](https://camo.githubusercontent.com/826551a2293a05fa26bb4a627d2da4d689a442b89df13f34935d912f2aa9533f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c616e6775616765732f636f756e742f6f70656e2d77656275692f6f70656e2d7765627569)![GitHub top language](https://camo.githubusercontent.com/7b9f4c5e5a8bd72ff89f2f1ce5b6844876223b5c986ef3af2509dd8d634d4500/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c616e6775616765732f746f702f6f70656e2d77656275692f6f70656e2d7765627569)![GitHub last commit](https://camo.githubusercontent.com/83c11eb6b6f6a2b32fd9e895783642acb3d6580932fcce808bf635f79467e13d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f6f70656e2d77656275692f6f70656e2d77656275693f636f6c6f723d726564)[![Discord](https://camo.githubusercontent.com/18e257b185c6f26ccbf61c586af01650bd29d07ba4d2157cfc0b752e8f103371/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d4f70656e5f57656255492d626c75653f6c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/5rJgQTnV4s)[![](https://camo.githubusercontent.com/e7f49e613609b2b9d9cfc66c96b54bf2a0442632bac56e5eee7944dbed96f157/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d53706f6e736f72266d6573736167653d537570706f7274266c6f676f3d47697448756226636f6c6f723d253233666538653836)](https://github.com/sponsors/open-webui)

[Explore Open WebUI →](https://docs.openwebui.com/)

### Installation

[Permalink: Installation](https://github.com/open-webui/open-webui#installation)

#### Python

[Permalink: Python](https://github.com/open-webui/open-webui#python)

```
# With uv installed (macOS/Linux)
DATA_DIR=~/.open-webui uvx --python 3.12 open-webui@latest serve

# Or install and run with pip (Python 3.12)
pip install open-webui
open-webui serve
```

Then open [http://localhost:8080](http://localhost:8080/).

#### Docker

[Permalink: Docker](https://github.com/open-webui/open-webui#docker)

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Then open [http://localhost:3000](http://localhost:3000/).

| Image tag | Includes |
| --- | --- |
| `:main` | Standard image with local AI dependencies |
| `:slim` | Lightweight image using external services for embeddings, document extraction, and voice |
| `:cuda` | Open WebUI with CUDA acceleration |
| `:ollama` | Open WebUI bundled with Ollama |
| `:dev` | Latest development build |

Add these options to `docker run` before the image name as needed:

| Option | Purpose |
| --- | --- |
| `-e OLLAMA_BASE_URL=http://your-ollama-server:11434` | Connect to Ollama on another server |
| `-e OPENAI_API_KEY=your_secret_key` | Set your OpenAI API key |
| `-e HF_HUB_OFFLINE=1` | Disable Hugging Face model downloads for offline use |
| `--gpus all` | Enable Nvidia GPU access for `:cuda` or `:ollama`; requires the Nvidia Container Toolkit |

See the [Docker installation guide](https://docs.openwebui.com/getting-started/quick-start/) for setup instructions and configuration options.

#### Desktop App

[Permalink: Desktop App](https://github.com/open-webui/open-webui#desktop-app)

[Download the native desktop app](https://github.com/open-webui/desktop) for macOS, Windows, and Linux.

[Read the docs →](https://docs.openwebui.com/getting-started/)

### Ecosystem

[Permalink: Ecosystem](https://github.com/open-webui/open-webui#ecosystem)

- [Open Terminal](https://github.com/open-webui/open-terminal) / [Terminals (Enterprise)](https://github.com/open-webui/terminals): The action layer that turns Open WebUI into a full agent harness, with enterprise orchestration for per-user workspaces.
- [Knowledge Base Sync (oikb)](https://github.com/open-webui/oikb): Mirror folders, repos, buckets, and wikis into Open WebUI Knowledge Bases with incremental sync.
- [Open WebUI Computer](https://github.com/open-webui/computer): Your computer in any browser: files, editor, terminal, git, and optional AI agents, running on your real machine.

See the [ecosystem documentation](https://docs.openwebui.com/ecosystem/) for details.

### Troubleshooting and Updates

[Permalink: Troubleshooting and Updates](https://github.com/open-webui/open-webui#troubleshooting-and-updates)

See the [troubleshooting guide](https://docs.openwebui.com/troubleshooting/) for connection issues and the [updating guide](https://docs.openwebui.com/getting-started/updating) to update your installation.

### Documentation

[Permalink: Documentation](https://github.com/open-webui/open-webui#documentation)

See the [docs](https://docs.openwebui.com/) for configuration and usage, and the [roadmap](https://docs.openwebui.com/roadmap/) for planned work.

For Docker Compose, Kubernetes, and other setups, see the [installation docs](https://docs.openwebui.com/getting-started/).

### Support

[Permalink: Support](https://github.com/open-webui/open-webui#support)

[Open an issue](https://github.com/open-webui/open-webui/issues) or [start a discussion](https://github.com/open-webui/open-webui/discussions).

Find us on [Reddit](https://www.reddit.com/r/OpenWebUI/), [X](https://x.com/OpenWebUI), and [Discord](https://discord.gg/5rJgQTnV4s).

### Security

[Permalink: Security](https://github.com/open-webui/open-webui#security)

Report vulnerabilities privately through [GitHub security advisories](https://github.com/open-webui/open-webui/security). Security reports are accepted only through GitHub.

### Star History

[Permalink: Star History](https://github.com/open-webui/open-webui#star-history)

[![Star History Chart](https://camo.githubusercontent.com/3cf9ca8c724f27b82d69b32f3337bcb036eac12ebcfa03b3f045ffd1bea6b9fa/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6f70656e2d77656275692f6f70656e2d776562756926747970653d44617465)](https://star-history.com/#open-webui/open-webui&Date)

#### License

[Permalink: License](https://github.com/open-webui/open-webui#license)

Includes code under the Open WebUI License, which requires preserving the Open WebUI branding, and prior contributions under their original licenses. See [LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE) and [LICENSE\_HISTORY](https://github.com/open-webui/open-webui/blob/main/LICENSE_HISTORY) for terms and history.

[Enterprise](https://docs.openwebui.com/enterprise) · [Careers](https://careers.openwebui.com/) · [Sponsor](https://github.com/sponsors/open-webui)

Created by [Timothy Jaeryang Baek](https://github.com/tjbck).

## About

User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

[openwebui.com](https://openwebui.com/)

### Topics

[ai](https://github.com/topics/ai) [llm](https://github.com/topics/llm) [llm-ui](https://github.com/topics/llm-ui) [llm-webui](https://github.com/topics/llm-webui) [llms](https://github.com/topics/llms) [mcp](https://github.com/topics/mcp) [ollama](https://github.com/topics/ollama) [ollama-webui](https://github.com/topics/ollama-webui) [open-webui](https://github.com/topics/open-webui) [openai](https://github.com/topics/openai) [openapi](https://github.com/topics/openapi) [rag](https://github.com/topics/rag) [self-hosted](https://github.com/topics/self-hosted) [ui](https://github.com/topics/ui) [webui](https://github.com/topics/webui)

### Resources

[Readme](https://github.com/open-webui/open-webui#readme-ov-file)

[License](https://github.com/open-webui/open-webui#License-1-ov-file)

### Code of conduct

[Code of conduct](https://github.com/open-webui/open-webui#coc-ov-file)

### Security policy

[Security policy](https://github.com/open-webui/open-webui#security-ov-file)

[Activity](https://github.com/open-webui/open-webui/activity)

[Custom properties](https://github.com/open-webui/open-webui/custom-properties)

### Stars

**159.5k** stars

### Watchers

**687** watching

### Forks

[**23.1k** forks](https://github.com/open-webui/open-webui/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui&report=open-webui+%28user%29)

## [Releases](https://github.com/open-webui/open-webui/releases) 183 (183)

[v0.13.5Latest\\
\\
2 hours agoNov 25, 2026](https://github.com/open-webui/open-webui/releases/tag/v0.13.5)

[\+ 182 releases](https://github.com/open-webui/open-webui/releases)

## Sponsor this project

- [![@open-webui](https://avatars.githubusercontent.com/u/158137808?s=64&v=4)](https://github.com/open-webui) [**open-webui**](https://github.com/open-webui) Open WebUISponsor @open-webui

[Learn more about GitHub Sponsors](https://github.com/sponsors)

## [Used by](https://github.com/open-webui/open-webui/network/dependents) 280 (280)

[![@StankySpence](https://avatars.githubusercontent.com/u/224382215?s=64&v=4)![@developer3000S](https://avatars.githubusercontent.com/u/626752?s=64&v=4)![@templeoflum](https://avatars.githubusercontent.com/u/212080460?s=64&v=4)![@eturkes](https://avatars.githubusercontent.com/u/25193231?s=64&v=4)![@JasonWilder117](https://avatars.githubusercontent.com/u/132273347?s=64&v=4)\\
\+ 271](https://github.com/open-webui/open-webui/network/dependents)

## [Contributors](https://github.com/open-webui/open-webui/graphs/contributors) 888 (888)

- [![@tjbck](https://avatars.githubusercontent.com/u/25473318?s=64&v=4)](https://github.com/tjbck)
- [![@Classic298](https://avatars.githubusercontent.com/u/27028174?s=64&v=4)](https://github.com/Classic298)
- [![@silentoplayz](https://avatars.githubusercontent.com/u/50341825?s=64&v=4)](https://github.com/silentoplayz)
- [![@cheahjs](https://avatars.githubusercontent.com/u/818368?s=64&v=4)](https://github.com/cheahjs)
- [![@ShirasawaSama](https://avatars.githubusercontent.com/u/17093811?s=64&v=4)](https://github.com/ShirasawaSama)
- [![@dependabot[bot]](https://avatars.githubusercontent.com/in/29110?s=64&v=4)](https://github.com/apps/dependabot)
- [![@claude](https://avatars.githubusercontent.com/u/81847?s=64&v=4)](https://github.com/claude)
- [![@jannikstdl](https://avatars.githubusercontent.com/u/69747628?s=64&v=4)](https://github.com/jannikstdl)
- [![@michaelpoluektov](https://avatars.githubusercontent.com/u/78477503?s=64&v=4)](https://github.com/michaelpoluektov)
- [![@joaoback](https://avatars.githubusercontent.com/u/156559121?s=64&v=4)](https://github.com/joaoback)
- [![@rgaricano](https://avatars.githubusercontent.com/u/131402327?s=64&v=4)](https://github.com/rgaricano)
- [![@aleixdorca](https://avatars.githubusercontent.com/u/25510463?s=64&v=4)](https://github.com/aleixdorca)
- [![@dannyl1u](https://avatars.githubusercontent.com/u/45186464?s=64&v=4)](https://github.com/dannyl1u)
- [![@karllee830](https://avatars.githubusercontent.com/u/61072264?s=64&v=4)](https://github.com/karllee830)

[\+ 874 contributors](https://github.com/open-webui/open-webui/graphs/contributors)

## Languages

- [Svelte38.5%](https://github.com/open-webui/open-webui/search?l=svelte)
- [Python36.7%](https://github.com/open-webui/open-webui/search?l=python)
- [JavaScript15.7%](https://github.com/open-webui/open-webui/search?l=javascript)
- [TypeScript7%](https://github.com/open-webui/open-webui/search?l=typescript)
- [CSS1.6%](https://github.com/open-webui/open-webui/search?l=css)
- [Shell0.2%](https://github.com/open-webui/open-webui/search?l=shell)
- [Other0.3%](https://github.com/open-webui/open-webui/search?l=Other)

You can’t perform that action at this time.