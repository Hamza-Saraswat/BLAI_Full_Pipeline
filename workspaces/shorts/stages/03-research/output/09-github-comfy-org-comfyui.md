# Source: https://github.com/Comfy-Org/ComfyUI
# Fetched: 2026-11-11 via hermes web_extract

[Skip to content](https://github.com/Comfy-Org/ComfyUI#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/Comfy-Org/ComfyUI) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/Comfy-Org/ComfyUI) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/Comfy-Org/ComfyUI) to refresh your session.Dismiss alert

{{ message }}

master

[**645** Branches](https://github.com/Comfy-Org/ComfyUI/branches) [**223** Tags](https://github.com/Comfy-Org/ComfyUI/tags)

[Go to Branches page](https://github.com/Comfy-Org/ComfyUI/branches)[Go to Tags page](https://github.com/Comfy-Org/ComfyUI/tags)

Go to file

Code

Open more actions menu

## Latest commit

[![jtydhr88](https://avatars.githubusercontent.com/u/860985?v=4&size=40)](https://github.com/jtydhr88)[jtydhr88](https://github.com/Comfy-Org/ComfyUI/commits?author=jtydhr88)

[Conform Concatenate Video clips to the first clip's frame rate and au…](https://github.com/Comfy-Org/ComfyUI/commit/4d64a8bc072b81c9b47321789b4d83fb7348ae2a)

Open commit detailssuccess

23 minutes agoNov 11, 2026

[4d64a8b](https://github.com/Comfy-Org/ComfyUI/commit/4d64a8bc072b81c9b47321789b4d83fb7348ae2a) · 23 minutes agoNov 11, 2026

## History

[6,316 Commits](https://github.com/Comfy-Org/ComfyUI/commits/master/)

Open commit details

[View commit history for this file.](https://github.com/Comfy-Org/ComfyUI/commits/master/) 6,316 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [.ci](https://github.com/Comfy-Org/ComfyUI/tree/master/.ci ".ci") | [.ci](https://github.com/Comfy-Org/ComfyUI/tree/master/.ci ".ci") | [Move portable fast fp16 script to ./advanced (](https://github.com/Comfy-Org/ComfyUI/commit/af02df4811fb7b0f55e2faf65692334e085160dc "Move portable fast fp16 script to ./advanced (#17570)") [#17570](https://github.com/Comfy-Org/ComfyUI/pull/17570) [)](https://github.com/Comfy-Org/ComfyUI/commit/af02df4811fb7b0f55e2faf65692334e085160dc "Move portable fast fp16 script to ./advanced (#17570)") | 4 days agoNov 6, 2026 |
| [.github](https://github.com/Comfy-Org/ComfyUI/tree/master/.github ".github") | [.github](https://github.com/Comfy-Org/ComfyUI/tree/master/.github ".github") | [Update api-node.md (](https://github.com/Comfy-Org/ComfyUI/commit/51285bff5bdc618f5dbe821377bbcdc5f3e94ea7 "Update api-node.md (#17569)") [#17569](https://github.com/Comfy-Org/ComfyUI/pull/17569) [)](https://github.com/Comfy-Org/ComfyUI/commit/51285bff5bdc618f5dbe821377bbcdc5f3e94ea7 "Update api-node.md (#17569)") | 5 days agoNov 6, 2026 |
| [alembic\_db](https://github.com/Comfy-Org/ComfyUI/tree/master/alembic_db "alembic_db") | [alembic\_db](https://github.com/Comfy-Org/ComfyUI/tree/master/alembic_db "alembic_db") | [fix(assets): date scanned assets by their file's mtime (](https://github.com/Comfy-Org/ComfyUI/commit/0df64eb242b7c5759c3e86afd5d1846d923b1033 "fix(assets): date scanned assets by their file's mtime (#16810)  * fix(assets): date scanned assets by their file's mtime  The scanner stamped every file it found with the scan time, so a library catalogued on its first scan listed newest-first in reverse walk order. Records the scanner creates now take the file's mtime (capped at now) as created_at. Migration 0009 redates existing scanned records the same way, only ever moving a record earlier. Generated outputs and uploads keep their registration time.  * test(assets): pass created_at through the seeder's create_record stub  * docs(assets): state what the mtime cap guarantees  * test(assets): bound the cursor walk, probe just outside the migration window; note why 0009 inlines its conversion  * fix(assets): cap a future mtime at the file's ctime too  * fix(assets): use the ctime only for a future mtime  * test(assets): check the ctime's now cap directly; say what the ctime is per platform  * test(assets): drop an unused import  * test(assets): a future mtime with a pre-1970 ctime is dated now  * fix(assets): fall back to now when the ctime is before 1970") [#16810](https://github.com/Comfy-Org/ComfyUI/pull/16810) [)](https://github.com/Comfy-Org/ComfyUI/commit/0df64eb242b7c5759c3e86afd5d1846d923b1033 "fix(assets): date scanned assets by their file's mtime (#16810)  * fix(assets): date scanned assets by their file's mtime  The scanner stamped every file it found with the scan time, so a library catalogued on its first scan listed newest-first in reverse walk order. Records the scanner creates now take the file's mtime (capped at now) as created_at. Migration 0009 redates existing scanned records the same way, only ever moving a record earlier. Generated outputs and uploads keep their registration time.  * test(assets): pass created_at through the seeder's create_record stub  * docs(assets): state what the mtime cap guarantees  * test(assets): bound the cursor walk, probe just outside the migration window; note why 0009 inlines its conversion  * fix(assets): cap a future mtime at the file's ctime too  * fix(assets): use the ctime only for a future mtime  * test(assets): check the ctime's now cap directly; say what the ctime is per platform  * test(assets): drop an unused import  * test(assets): a future mtime with a pre-1970 ctime is dated now  * fix(assets): fall back to now when the ctime is before 1970") | last monthOct 10, 2026 |
| [api\_server](https://github.com/Comfy-Org/ComfyUI/tree/master/api_server "api_server") | [api\_server](https://github.com/Comfy-Org/ComfyUI/tree/master/api_server "api_server") | [fix: append directory type annotation to internal files endpoint resp…](https://github.com/Comfy-Org/ComfyUI/commit/138571da955d85935baa09371ac2b67ea8b7a8ca "fix: append directory type annotation to internal files endpoint response (#13078) (#13305)") | 7 months agoApr 19, 2026 |
| [app](https://github.com/Comfy-Org/ComfyUI/tree/master/app "app") | [app](https://github.com/Comfy-Org/ComfyUI/tree/master/app "app") | [Fix potential database issue. (](https://github.com/Comfy-Org/ComfyUI/commit/01ca52b912cb9d7853abd4b32994d7833a9ecb32 "Fix potential database issue. (#17602)") [#17602](https://github.com/Comfy-Org/ComfyUI/pull/17602) [)](https://github.com/Comfy-Org/ComfyUI/commit/01ca52b912cb9d7853abd4b32994d7833a9ecb32 "Fix potential database issue. (#17602)") | 3 days agoNov 8, 2026 |
| [blueprints](https://github.com/Comfy-Org/ComfyUI/tree/master/blueprints "blueprints") | [blueprints](https://github.com/Comfy-Org/ComfyUI/tree/master/blueprints "blueprints") | [Add Marigold V2 and YuE2 blueprints (](https://github.com/Comfy-Org/ComfyUI/commit/683421b679f85e0f0fe00fc875640dfcd01103e9 "Add Marigold V2 and YuE2 blueprints (#16318)") [#16318](https://github.com/Comfy-Org/ComfyUI/pull/16318) [)](https://github.com/Comfy-Org/ComfyUI/commit/683421b679f85e0f0fe00fc875640dfcd01103e9 "Add Marigold V2 and YuE2 blueprints (#16318)") | 2 months agoSep 14, 2026 |
| [comfy](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy "comfy") | [comfy](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy "comfy") | [feat: Support MiniMax-H3-image (CORE-708) (](https://github.com/Comfy-Org/ComfyUI/commit/ede4e5fe8d15445c6fcd6828d70b202c22f9502c "feat: Support MiniMax-H3-image (CORE-708) (#17655)") [#17655](https://github.com/Comfy-Org/ComfyUI/pull/17655) [)](https://github.com/Comfy-Org/ComfyUI/commit/ede4e5fe8d15445c6fcd6828d70b202c22f9502c "feat: Support MiniMax-H3-image (CORE-708) (#17655)") | 14 hours agoNov 10, 2026 |
| [comfy\_api](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_api "comfy_api") | [comfy\_api](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_api "comfy_api") | [Conform Concatenate Video clips to the first clip's frame rate and au…](https://github.com/Comfy-Org/ComfyUI/commit/4d64a8bc072b81c9b47321789b4d83fb7348ae2a "Conform Concatenate Video clips to the first clip's frame rate and audio (FRONT-3775) (#17621)") | 23 minutes agoNov 11, 2026 |
| [comfy\_api\_nodes](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_api_nodes "comfy_api_nodes") | [comfy\_api\_nodes](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_api_nodes "comfy_api_nodes") | [\[Partner Nodes\] feat(MiniMax): add MiniMax H3 Image node (](https://github.com/Comfy-Org/ComfyUI/commit/d9238b25d23e0354b0169c8197b63eca7b46443f "[Partner Nodes] feat(MiniMax): add MiniMax H3 Image node (#17661)  Signed-off-by: bigcat88 <bigcat88@icloud.com>") [#17661](https://github.com/Comfy-Org/ComfyUI/pull/17661) [)](https://github.com/Comfy-Org/ComfyUI/commit/d9238b25d23e0354b0169c8197b63eca7b46443f "[Partner Nodes] feat(MiniMax): add MiniMax H3 Image node (#17661)  Signed-off-by: bigcat88 <bigcat88@icloud.com>") | 10 hours agoNov 10, 2026 |
| [comfy\_config](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_config "comfy_config") | [comfy\_config](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_config "comfy_config") | [Add new fields to the config types (](https://github.com/Comfy-Org/ComfyUI/commit/5b12b55e32aa2aa8fd47d545265a974d3b01ac7c "Add new fields to the config types (#8507)") [#8507](https://github.com/Comfy-Org/ComfyUI/pull/8507) [)](https://github.com/Comfy-Org/ComfyUI/commit/5b12b55e32aa2aa8fd47d545265a974d3b01ac7c "Add new fields to the config types (#8507)") | last yearJun 18, 2025 |
| [comfy\_execution](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_execution "comfy_execution") | [comfy\_execution](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_execution "comfy_execution") | [Return execution\_meta in the job detail (](https://github.com/Comfy-Org/ComfyUI/commit/0698f6d7c24ce1790c5e48f42eff3023d92cd4f3 "Return execution_meta in the job detail (#17397)  * test: job detail returns each node's execution meta  * Return execution_meta in the job detail  GET /api/jobs/{job_id} documents execution_meta but never filled it. The history record already stores each node's meta, including the display_node an expanded node is shown on. Return it so a client that reloads a finished job's outputs (for example after a websocket reconnect) can send each output to the node the live executed message would have used.  * test: a cached output keeps its own node's execution meta  Two identical previews share an output cache entry. The second one replays the entry with the first node's meta, so the job detail points its output at the wrong node.  * Record the current node's meta for a cached output  emit_cached_output stored the meta of whichever node wrote the cache entry. Pass the current node's meta from both callers instead.  * Pass the node meta to emit_cached_output instead of the display id  Both callers now always pass the current node's meta, so the optional parameter and the separate display id go away; the executed message reads display_node from the meta. The test fixture's real_node_id now matches get_real_node_id (the top-level node).  * test: an expanded node's execution meta names the node that expanded it  ---------  Co-authored-by: guill <jacob.e.segal@gmail.com>") [#17397](https://github.com/Comfy-Org/ComfyUI/pull/17397) [)](https://github.com/Comfy-Org/ComfyUI/commit/0698f6d7c24ce1790c5e48f42eff3023d92cd4f3 "Return execution_meta in the job detail (#17397)  * test: job detail returns each node's execution meta  * Return execution_meta in the job detail  GET /api/jobs/{job_id} documents execution_meta but never filled it. The history record already stores each node's meta, including the display_node an expanded node is shown on. Return it so a client that reloads a finished job's outputs (for example after a websocket reconnect) can send each output to the node the live executed message would have used.  * test: a cached output keeps its own node's execution meta  Two identical previews share an output cache entry. The second one replays the entry with the first node's meta, so the job detail points its output at the wrong node.  * Record the current node's meta for a cached output  emit_cached_output stored the meta of whichever node wrote the cache entry. Pass the current node's meta from both callers instead.  * Pass the node meta to emit_cached_output instead of the display id  Both callers now always pass the current node's meta, so the optional parameter and the separate display id go away; the executed message reads display_node from the meta. The test fixture's real_node_id now matches get_real_node_id (the top-level node).  * test: an expanded node's execution meta names the node that expanded it  ---------  Co-authored-by: guill <jacob.e.segal@gmail.com>") | last weekNov 1, 2026 |
| [comfy\_extras](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_extras "comfy_extras") | [comfy\_extras](https://github.com/Comfy-Org/ComfyUI/tree/master/comfy_extras "comfy_extras") | [Fix for some workflows not working properly. (](https://github.com/Comfy-Org/ComfyUI/commit/0228a9d73cd7c2daf8f61fe13d56b12efe307171 "Fix for some workflows not working properly. (#17675)") [#17675](https://github.com/Comfy-Org/ComfyUI/pull/17675) [)](https://github.com/Comfy-Org/ComfyUI/commit/0228a9d73cd7c2daf8f61fe13d56b12efe307171 "Fix for some workflows not working properly. (#17675)") | 7 hours agoNov 10, 2026 |
| [custom\_nodes](https://github.com/Comfy-Org/ComfyUI/tree/master/custom_nodes "custom_nodes") | [custom\_nodes](https://github.com/Comfy-Org/ComfyUI/tree/master/custom_nodes "custom_nodes") | [Update nodes categories and display names (CORE-89) (](https://github.com/Comfy-Org/ComfyUI/commit/594de378fe1d2e32128338f5cc57864ee1d9d96f "Update nodes categories and display names (CORE-89) (#13786)") [#13786](https://github.com/Comfy-Org/ComfyUI/pull/13786) [)](https://github.com/Comfy-Org/ComfyUI/commit/594de378fe1d2e32128338f5cc57864ee1d9d96f "Update nodes categories and display names (CORE-89) (#13786)") | 6 months agoMay 8, 2026 |
| [input](https://github.com/Comfy-Org/ComfyUI/tree/master/input "input") | [input](https://github.com/Comfy-Org/ComfyUI/tree/master/input "input") | [LoadLatent and SaveLatent should behave like the LoadImage and SaveIm…](https://github.com/Comfy-Org/ComfyUI/commit/faf899ad5ae32f770f0dae6a9df457e81d2b5c38 "LoadLatent and SaveLatent should behave like the LoadImage and SaveImage.") | 3 years agoMay 18, 2023 |
| [middleware](https://github.com/Comfy-Org/ComfyUI/tree/master/middleware "middleware") | [middleware](https://github.com/Comfy-Org/ComfyUI/tree/master/middleware "middleware") | [fix: use no-store cache headers to prevent stale frontend chunks (](https://github.com/Comfy-Org/ComfyUI/commit/e0982a7174a9cacb0c3cd3fb6bd1f8e06d9aaf51 "fix: use no-store cache headers to prevent stale frontend chunks (#12911)  After a frontend update (e.g. nightly build), browsers could load outdated cached index.html and JS/CSS chunks, causing dynamically imported modules to fail with MIME type errors and vite:preloadError.  Hard refresh (Ctrl+Shift+R) was insufficient to fix the issue because Cache-Control: no-cache still allows the browser to cache and revalidate via ETags. aiohttp's FileResponse auto-generates ETags based on file mtime+size, which may not change after pip reinstall, so the browser gets 304 Not Modified and serves stale content.  Clearing ALL site data in DevTools did fix it, confirming the HTTP cache was the root cause.  The fix changes: - index.html: no-cache -> no-store, must-revalidate - JS/CSS/JSON entry points: no-cache -> no-store  no-store instructs browsers to never cache these responses, ensuring every page load fetches the current index.html with correct chunk references. This is a small tradeoff (~5KB re-download per page load) for guaranteed correctness after updates.") [#12911](https://github.com/Comfy-Org/ComfyUI/pull/12911) | 8 months agoMar 14, 2026 |
| [models](https://github.com/Comfy-Org/ComfyUI/tree/master/models "models") | [models](https://github.com/Comfy-Org/ComfyUI/tree/master/models "models") | [Update MediaPipe nodes to standardize with existing code base (CORE-2…](https://github.com/Comfy-Org/ComfyUI/commit/7b7c5fed7ce978b05da27b13e26ef340d284b60e "Update MediaPipe nodes to standardize with existing code base (CORE-242) (#14025)") | 6 months agoMay 21, 2026 |
| [output](https://github.com/Comfy-Org/ComfyUI/tree/master/output "output") | [output](https://github.com/Comfy-Org/ComfyUI/tree/master/output "output") | [Initial commit.](https://github.com/Comfy-Org/ComfyUI/commit/220afe33101a3874cf40e9cc221d27f8a8b1fae1 "Initial commit.") | 4 years agoJan 17, 2023 |
| [script\_examples](https://github.com/Comfy-Org/ComfyUI/tree/master/script_examples "script_examples") | [script\_examples](https://github.com/Comfy-Org/ComfyUI/tree/master/script_examples "script_examples") | [Update comment in api example. (](https://github.com/Comfy-Org/ComfyUI/commit/4368d8f87f580f526e8b2bc43bf0ac88e2b67033 "Update comment in api example. (#9708)") [#9708](https://github.com/Comfy-Org/ComfyUI/pull/9708) [)](https://github.com/Comfy-Org/ComfyUI/commit/4368d8f87f580f526e8b2bc43bf0ac88e2b67033 "Update comment in api example. (#9708)") | last yearSep 3, 2025 |
| [tests-unit](https://github.com/Comfy-Org/ComfyUI/tree/master/tests-unit "tests-unit") | [tests-unit](https://github.com/Comfy-Org/ComfyUI/tree/master/tests-unit "tests-unit") | [Conform Concatenate Video clips to the first clip's frame rate and au…](https://github.com/Comfy-Org/ComfyUI/commit/4d64a8bc072b81c9b47321789b4d83fb7348ae2a "Conform Concatenate Video clips to the first clip's frame rate and audio (FRONT-3775) (#17621)") | 23 minutes agoNov 11, 2026 |
| [tests](https://github.com/Comfy-Org/ComfyUI/tree/master/tests "tests") | [tests](https://github.com/Comfy-Org/ComfyUI/tree/master/tests "tests") | [Return execution\_meta in the job detail (](https://github.com/Comfy-Org/ComfyUI/commit/0698f6d7c24ce1790c5e48f42eff3023d92cd4f3 "Return execution_meta in the job detail (#17397)  * test: job detail returns each node's execution meta  * Return execution_meta in the job detail  GET /api/jobs/{job_id} documents execution_meta but never filled it. The history record already stores each node's meta, including the display_node an expanded node is shown on. Return it so a client that reloads a finished job's outputs (for example after a websocket reconnect) can send each output to the node the live executed message would have used.  * test: a cached output keeps its own node's execution meta  Two identical previews share an output cache entry. The second one replays the entry with the first node's meta, so the job detail points its output at the wrong node.  * Record the current node's meta for a cached output  emit_cached_output stored the meta of whichever node wrote the cache entry. Pass the current node's meta from both callers instead.  * Pass the node meta to emit_cached_output instead of the display id  Both callers now always pass the current node's meta, so the optional parameter and the separate display id go away; the executed message reads display_node from the meta. The test fixture's real_node_id now matches get_real_node_id (the top-level node).  * test: an expanded node's execution meta names the node that expanded it  ---------  Co-authored-by: guill <jacob.e.segal@gmail.com>") [#17397](https://github.com/Comfy-Org/ComfyUI/pull/17397) [)](https://github.com/Comfy-Org/ComfyUI/commit/0698f6d7c24ce1790c5e48f42eff3023d92cd4f3 "Return execution_meta in the job detail (#17397)  * test: job detail returns each node's execution meta  * Return execution_meta in the job detail  GET /api/jobs/{job_id} documents execution_meta but never filled it. The history record already stores each node's meta, including the display_node an expanded node is shown on. Return it so a client that reloads a finished job's outputs (for example after a websocket reconnect) can send each output to the node the live executed message would have used.  * test: a cached output keeps its own node's execution meta  Two identical previews share an output cache entry. The second one replays the entry with the first node's meta, so the job detail points its output at the wrong node.  * Record the current node's meta for a cached output  emit_cached_output stored the meta of whichever node wrote the cache entry. Pass the current node's meta from both callers instead.  * Pass the node meta to emit_cached_output instead of the display id  Both callers now always pass the current node's meta, so the optional parameter and the separate display id go away; the executed message reads display_node from the meta. The test fixture's real_node_id now matches get_real_node_id (the top-level node).  * test: an expanded node's execution meta names the node that expanded it  ---------  Co-authored-by: guill <jacob.e.segal@gmail.com>") | last weekNov 1, 2026 |
| [utils](https://github.com/Comfy-Org/ComfyUI/tree/master/utils "utils") | [utils](https://github.com/Comfy-Org/ComfyUI/tree/master/utils "utils") | [feat(assets): previews for EXR assets, written by SaveImageAdvanced f…](https://github.com/Comfy-Org/ComfyUI/commit/12081cf9b8cb2c8128e32f689aabc8ac4688fde7 "feat(assets): previews for EXR assets, written by SaveImageAdvanced for outputs (#16898)") | last monthOct 13, 2026 |
| [.coderabbit.yaml](https://github.com/Comfy-Org/ComfyUI/blob/master/.coderabbit.yaml ".coderabbit.yaml") | [.coderabbit.yaml](https://github.com/Comfy-Org/ComfyUI/blob/master/.coderabbit.yaml ".coderabbit.yaml") | [Keep linked repository findings focused (](https://github.com/Comfy-Org/ComfyUI/commit/81100cd83612317fa0cc9edbbcab1b7e2efca986 "Keep linked repository findings focused (#16920)") [#16920](https://github.com/Comfy-Org/ComfyUI/pull/16920) [)](https://github.com/Comfy-Org/ComfyUI/commit/81100cd83612317fa0cc9edbbcab1b7e2efca986 "Keep linked repository findings focused (#16920)") | last monthOct 11, 2026 |

[... middle omitted -- see footer ...]


The default installation includes a fast latent preview method that's low-resolution. To enable higher-quality previews with [TAESD](https://github.com/madebyollin/taesd), download the [taesd\_decoder.pth, taesdxl\_decoder.pth, taesd3\_decoder.pth and taef1\_decoder.pth](https://github.com/madebyollin/taesd/) and place them in the `models/vae_approx` folder. Once they're installed, restart ComfyUI and launch it with `--preview-method taesd` to enable high-quality previews.

## How to use TLS/SSL?

[Permalink: How to use TLS/SSL?](https://github.com/Comfy-Org/ComfyUI#how-to-use-tlsssl)

Generate a self-signed certificate (not appropriate for shared/production use) and key by running the command: `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"`

Use `--tls-keyfile key.pem --tls-certfile cert.pem` to enable TLS/SSL, the app will now be accessible with `https://...` instead of `http://...`.

> Note: Windows users can use [alexisrolland/docker-openssl](https://github.com/alexisrolland/docker-openssl) or one of the [3rd party binary distributions](https://wiki.openssl.org/index.php/Binaries) to run the command example above.
>
> If you use a container, note that the volume mount `-v` can be a relative path so `... -v ".\:/openssl-certs" ...` would create the key & cert files in the current directory of your command prompt or powershell terminal.

## Support and dev channel

[Permalink: Support and dev channel](https://github.com/Comfy-Org/ComfyUI#support-and-dev-channel)

[Discord](https://comfy.org/discord): Try the #help or #feedback channels.

[Matrix space: #comfyui\_space:matrix.org](https://app.element.io/#/room/%23comfyui_space%3Amatrix.org) (it's like discord but open source).

See also: [https://www.comfy.org/](https://www.comfy.org/)

> _psst -- we're hiring!_ Help build ComfyUI: [comfy.org/careers](https://www.comfy.org/careers)

## Frontend Development

[Permalink: Frontend Development](https://github.com/Comfy-Org/ComfyUI#frontend-development)

As of August 15, 2024, we have transitioned to a new frontend, which is now hosted in a separate repository: [ComfyUI Frontend](https://github.com/Comfy-Org/ComfyUI_frontend). The compiled JS files (from TS/Vue) are published to [pypi](https://pypi.org/project/comfyui-frontend-package) and installed as a dependency in ComfyUI.

### Reporting Issues and Requesting Features

[Permalink: Reporting Issues and Requesting Features](https://github.com/Comfy-Org/ComfyUI#reporting-issues-and-requesting-features)

For any bugs, issues, or feature requests related to the frontend, please use the [ComfyUI Frontend repository](https://github.com/Comfy-Org/ComfyUI_frontend). This will help us manage and address frontend-specific concerns more efficiently.

### Using the Latest Frontend

[Permalink: Using the Latest Frontend](https://github.com/Comfy-Org/ComfyUI#using-the-latest-frontend)

The new frontend is now the default for ComfyUI. However, please note:

1. The frontend in the main ComfyUI repository is updated fortnightly.
2. Daily releases are available in the separate frontend repository.

To use the most up-to-date frontend version:

1. For the latest daily release, launch ComfyUI with this command line argument:



```
   --front-end-version Comfy-Org/ComfyUI_frontend@latest
```

2. For a specific version, replace `latest` with the desired version number:



```
   --front-end-version Comfy-Org/ComfyUI_frontend@1.2.2
```


This approach allows you to easily switch between the stable fortnightly release and the cutting-edge daily updates, or even specific versions for testing purposes.

# QA

[Permalink: QA](https://github.com/Comfy-Org/ComfyUI#qa)

### Which GPU should I buy for this?

[Permalink: Which GPU should I buy for this?](https://github.com/Comfy-Org/ComfyUI#which-gpu-should-i-buy-for-this)

[See this page for some recommendations](https://github.com/comfyanonymous/ComfyUI/wiki/Which-GPU-should-I-buy-for-ComfyUI)

## About

The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. The fastest local inference engine in the world.

[www.comfy.org/](https://www.comfy.org/)

### Topics

[ai](https://github.com/topics/ai) [comfy](https://github.com/topics/comfy) [comfyui](https://github.com/topics/comfyui) [python](https://github.com/topics/python) [pytorch](https://github.com/topics/pytorch) [stable-diffusion](https://github.com/topics/stable-diffusion)

### Resources

[Readme](https://github.com/Comfy-Org/ComfyUI#readme-ov-file)

[GPL-3.0 license](https://github.com/Comfy-Org/ComfyUI#GPL-3.0-1-ov-file)

### Contributing

[Contributing](https://github.com/Comfy-Org/ComfyUI#contributing-ov-file)

### Security policy

[Security policy](https://github.com/Comfy-Org/ComfyUI#security-ov-file)

[Activity](https://github.com/Comfy-Org/ComfyUI/activity)

[Custom properties](https://github.com/Comfy-Org/ComfyUI/custom-properties)

### Stars

**146.2k** stars

### Watchers

**840** watching

### Forks

[**17.4k** forks](https://github.com/Comfy-Org/ComfyUI/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FComfy-Org%2FComfyUI&report=Comfy-Org+%28user%29)

## [Releases](https://github.com/Comfy-Org/ComfyUI/releases) 166 (166)

[v0.45.0Latest\\
\\
8 hours agoNov 10, 2026](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.45.0)

[\+ 165 releases](https://github.com/Comfy-Org/ComfyUI/releases)

## [Contributors](https://github.com/Comfy-Org/ComfyUI/graphs/contributors) 366 (366)

- [![@comfyanonymous](https://avatars.githubusercontent.com/u/121283862?s=64&v=4)](https://github.com/comfyanonymous)
- [![@bigcat88](https://avatars.githubusercontent.com/u/13381981?s=64&v=4)](https://github.com/bigcat88)
- [![@pythongosssss](https://avatars.githubusercontent.com/u/125205205?s=64&v=4)](https://github.com/pythongosssss)
- [![@comfyui-wiki](https://avatars.githubusercontent.com/u/192523189?s=64&v=4)](https://github.com/comfyui-wiki)
- [![@rattus128](https://avatars.githubusercontent.com/u/46076784?s=64&v=4)](https://github.com/rattus128)
- [![@kijai](https://avatars.githubusercontent.com/u/40791699?s=64&v=4)](https://github.com/kijai)
- [![@christian-byrne](https://avatars.githubusercontent.com/u/72887196?s=64&v=4)](https://github.com/christian-byrne)
- [![@Kosinkadink](https://avatars.githubusercontent.com/u/7365912?s=64&v=4)](https://github.com/Kosinkadink)
- [![@huchenlei](https://avatars.githubusercontent.com/u/20929282?s=64&v=4)](https://github.com/huchenlei)
- [![@jtydhr88](https://avatars.githubusercontent.com/u/860985?s=64&v=4)](https://github.com/jtydhr88)
- [![@alexisrolland](https://avatars.githubusercontent.com/u/13064696?s=64&v=4)](https://github.com/alexisrolland)
- [![@ltdrdata](https://avatars.githubusercontent.com/u/128333288?s=64&v=4)](https://github.com/ltdrdata)
- [![@guill](https://avatars.githubusercontent.com/u/3157454?s=64&v=4)](https://github.com/guill)
- [![@comfy-pr-bot](https://avatars.githubusercontent.com/u/172744619?s=64&v=4)](https://github.com/comfy-pr-bot)

[\+ 352 contributors](https://github.com/Comfy-Org/ComfyUI/graphs/contributors)

## Languages

- [Python99.8%](https://github.com/Comfy-Org/ComfyUI/search?l=python)
- [Other0.2%](https://github.com/Comfy-Org/ComfyUI/search?l=Other)

You can’t perform that action at this time.

──────── [TRUNCATED] ────────
Showing 21,858 chars (head) + 7,466 chars (tail) of 89,706 total clean characters.
Full text saved to: /home/buildlocalai/.hermes/cache/web/github.com-32faae7066.md
To read the omitted middle: read_file path="/home/buildlocalai/.hermes/cache/web/github.com-32faae7066.md" offset=65 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
