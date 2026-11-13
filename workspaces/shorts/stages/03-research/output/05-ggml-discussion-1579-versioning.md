[Skip to content](https://github.com/ggml-org/ggml/discussions/1579#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/ggml-org/ggml/discussions/1579) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/ggml-org/ggml/discussions/1579) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/ggml-org/ggml/discussions/1579) to refresh your session.Dismiss alert

{{ message }}

# dist : releases and versioning of `ggml-org` projects  \#1579

[ggerganov](https://github.com/ggerganov)

started this conversation in
[General](https://github.com/ggml-org/ggml/discussions/categories/general)

[dist : releases and versioning of \`ggml-org\` projects](https://github.com/ggml-org/ggml/discussions/1579#top)#1579

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=40&v=4)\\
ggerganov](https://github.com/ggerganov)

on Aug 7Aug 7, 2026·
14 comments
·
47 replies


[Return to top](https://github.com/ggml-org/ggml/discussions/1579#top)

Discussion options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

## [![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)\ ggerganov](https://github.com/ggerganov) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussion-10568280)   Maintainer

|     |
| --- |
| # Overview<br>Below is a summary of the release process of the [ggml-org](https://github.com/ggml-org) projects. The document should be useful for downstream project to decide how to build and distribute them.<br># Projects<br>## [ggml-org/ggml](https://github.com/ggml-org/ggml)<br>- Core library used by the rest of the projects<br>  <br>- Release builds use semantic versioning: `vX.Y.Z`<br>  - Git tags: `vX.Y.Z`<br>- Release list: [v0](https://github.com/ggml-org/ggml/releases?q=tag:v0)<br>  <br>  <br>  ### Downstreams<br>  <br>  - Homebrew: `ggml` [package](https://formulae.brew.sh/formula/ggml), [formula](https://github.com/Homebrew/homebrew-core/blob/main/Formula/g/ggml.rb)<br>  - Debian:<br>    - `ggml` [package](https://packages.debian.org/source/sid/ggml), [packaging repository](https://salsa.debian.org/deeplearning-team/ggml)<br>    - `ggml-cuda` [package](https://packages.debian.org/source/sid/ggml-cuda) (separate build because of non-free CUDA dependencies)<br>## [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)<br>- Includes an internal copy of `ggml` that may deviate from the official released version<br>  <br>- The internal copy is used for [nightly development builds](https://github.com/ggml-org/llama.cpp/releases) from the `master` branch<br>  <br>- The nightly builds use commit number `[NUM]` for version:<br>  - Git tags: `b[NUM]`<br>  - Build with CMake option `-DLLAMA_BUILD_IS_DEV=ON`<br>- Official release builds use semantic versioning: `vX.Y.Z`<br>  - Git tags: `vX.Y.Z`<br>  - Build with CMake option `-DLLAMA_BUILD_IS_DEV=OFF`<br>  - The release tags are created on the condition that the internal `ggml` copy is identical to the released `ggml` copy. This guarantees that a downstream building from the release tags and linking to a system-wide `ggml` will be compatible.<br>- Release list: [v0](https://github.com/ggml-org/llama.cpp/releases?q=tag:v0)<br>  <br>  <br>  ### Downstreams<br>  <br>  - ggml-org: `llama.app` [webpage](https://llama.app/), [packaging repository](https://github.com/ggml-org/llama-install.sh)<br>    - Does not link to a system-level `ggml` (i.e. packs the internal `ggml` copy)<br>    - Publishes the nightly builds instead of the official releases (TODO: switch to official releases?)<br>  - Homebrew: `llama.cpp` [package](https://formulae.brew.sh/formula/llama.cpp), [formula](https://github.com/Homebrew/homebrew-core/blob/main/Formula/l/llama.cpp.rb)<br>    - Depends on the `ggml` package and links to the installed system-wide `ggml`<br>  - Debian: `llama.cpp` [package](https://packages.debian.org/source/sid/llama.cpp), [packaging repository](https://salsa.debian.org/deeplearning-team/llama.cpp)<br>    - Depends on the `ggml` and `ggml-cuda` packages and links to the installed system-wide `ggml`<br>  - Winget: `llama.cpp` [workflow](https://github.com/ggml-org/llama.cpp/blob/master/.github/workflows/winget.yml), [manifests](https://github.com/microsoft/winget-pkgs/tree/master/manifests/g/ggml/llamacpp)<br>    - Does not link to a system-level `ggml` (i.e. packs the internal `ggml` copy)<br>    - Publishes the nightly builds instead of the official releases (TODO: switch to official releases?)<br>## [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)<br>- Includes an internal copy of `ggml` that may deviate from the official released version<br>  <br>- There are no nightly builds - only official releases<br>  <br>- Official release builds use semantic versioning:<br>  - Git tags: `vX.Y.Z`<br>  - Build with CMake option `-DWHISPER_BUILD_IS_DEV=OFF`<br>- The release tags are created on the condition that the internal `ggml` copy is identical to the released `ggml` copy. This guarantees that a downstream building from the release tags and linking to a system-wide `ggml` will be compatible.<br>  <br>- Release list: [v1](https://github.com/ggml-org/whisper.cpp/releases?q=tag:v1)<br>  <br>  <br>  ### Downstreams<br>  <br>  - Homebrew: `whisper-cpp` [package](https://formulae.brew.sh/formula/whisper-cpp), [formula](https://github.com/Homebrew/homebrew-core/blob/main/Formula/w/whisper-cpp.rb)<br>    - TODO: rename to `whisper.cpp`?<br>  - Debian: `whisper.cpp` [package](https://packages.debian.org/source/sid/whisper.cpp), [packaging repository](https://salsa.debian.org/deeplearning-team/whisper.cpp)<br>## [ggml-org/llama.cpp/gguf-py](https://github.com/ggml-org/llama.cpp/tree/master/gguf-py)<br>- Release builds use semantic versioning: `vX.Y.Z`<br>  <br>  <br>  - Git tags: `gguf-vX.Y.Z`<br>### Downstreams<br>  - pip: `gguf` [package](https://pypi.org/project/gguf/), [workflow](https://github.com/ggml-org/llama.cpp/blob/master/.github/workflows/gguf-publish.yml)<br>## [ggml-org/llama.vim](https://github.com/ggml-org/llama.vim)<br>- Uses semantic versioning: `vX.Y.Z`<br>* * *<br># TODOs<br>- [x]  Update homebrew `llama.cpp` formula to build from release tag<br>- [x]  Add auto-generated summaries for the releases (new models, API changes, etc.) |

1You must be logged in to vote

👍1

All reactions

- 👍1

## Replies:   14 comments  ·  47 replies

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)\ ggerganov](https://github.com/ggerganov) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17930978)   Maintainer  Author

|     |
| --- |
| FYI @ggml-org/ci [@ckastner](https://github.com/ckastner) [@p-linnane](https://github.com/p-linnane) |

1You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/1629204?s=64&v=4)\ CISC](https://github.com/CISC) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17931146)   Collaborator

|     |
| --- |
| May be worth mentioning `gguf-py` here as well? |

1You must be logged in to vote

👍1

All reactions

- 👍1

3 replies


[![@ckastner](https://avatars.githubusercontent.com/u/15859947?s=60&v=4)](https://github.com/ckastner)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ckastner](https://github.com/ckastner) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17931442)

|     |
| --- |
| Also llama.vim? |

All reactions

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17931568)   Maintainer  Author

|     |
| --- |
| Added, though I'm not sure how to spec it at the moment. |

All reactions

[![@ddeteljAI](https://avatars.githubusercontent.com/u/288738912?s=60&v=4)](https://github.com/ddeteljAI)

### This comment was marked as off-topic.

[Sign in to view](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fggml-org%2Fggml%2Fdiscussions%2F1579)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/15859947?s=64&v=4)\ ckastner](https://github.com/ckastner) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17931642)

|     |
| --- |
| This is very useful, thanks!<br>Super-happy to see semantic versioning for llama.cpp coming. That will also enable maintaining a SOVER. And that will allow us in Debian to ship it as a library in public search paths, because we can now guarantee backwards-compatibility (breaking can be communicated and maintained via SOVER bumps).<br>For llama.cpp and whisper.cpp release builds, it would be great if they could somehow specify the minimum ggml version they need, something like `find_package(ggml 0.18 REQUIRED)`, so that packaging tools can make use of this.<br>Debian links:<br>- ggml [package](https://packages.debian.org/source/sid/ggml), [packaging repository](https://salsa.debian.org/deeplearning-team/ggml)<br>- ggml-cuda [package](https://packages.debian.org/source/sid/ggml-cuda) (separate build because of non-free CUDA dependencies)<br>- llama.cpp [package](https://packages.debian.org/source/sid/llama.cpp), [packaging repository](https://salsa.debian.org/deeplearning-team/llama.cpp)<br>- whisper.cpp [package](https://packages.debian.org/source/sid/whisper.cpp), [packaging repository](https://salsa.debian.org/deeplearning-team/whisper.cpp)<br>- llama.vim [package](https://packages.debian.org/source/sid/llama.vim), [packaging repository](https://salsa.debian.org/deeplearning-team/llama.vim)<br>We also have HIP and CUDA builds using AMD's/NVIDIA's repositories, for bleeding edge hardware and toolkit support. I'd add that in an increment, though.<br>Below just FYI:<br>In Debian, we currently tend to update llama.cpp in tandem with new ggml release, since that was the point where both were expected to be ~"in sync":<br>- If ggml had a minor x.y bump, something key was added, and we increase llama.cpp's dependency on ggml version accordingly<br>- If ggml had a patch x.y.z bump, we assume a bugfix, and increase llama.cpp's dependency on ggml version only if a build shows it's needed<br>- We always verify this in practice, with various rebuilds and test runs<br>With this new release strategy, things are much more deterministic and plannable. |

1You must be logged in to vote

👍1

All reactions

- 👍1

2 replies


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17931689)   Maintainer  Author

|     |
| --- |
| > For llama.cpp and whisper.cpp release builds, it would be great if they could somehow specify the minimum ggml version they need, something like find\_package(ggml 0.18 REQUIRED), so that packaging tools can make use of this.<br>Right now this can be deduced from the included internal copy of `ggml`. For example, for `llama.cpp`: [https://github.com/ggml-org/llama.cpp/blob/master/ggml/CMakeLists.txt#L1-L10](https://github.com/ggml-org/llama.cpp/blob/master/ggml/CMakeLists.txt#L1-L10)<br>But maybe this is too inconvenient for the package managers? We'll look into the `find_package` suggestion. |

👍3

All reactions

- 👍3

[![@ckastner](https://avatars.githubusercontent.com/u/15859947?s=60&v=4)](https://github.com/ckastner)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ckastner](https://github.com/ckastner) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17931812)

|     |
| --- |
| `find_package` is just a bit more obvious as the build should already fail at the configuration stage, with a useful error message. And this works even outside of managed packages. |

👍2

All reactions

- 👍2

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/7702203?s=64&v=4)\ ngxson](https://github.com/ngxson) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17931875)   Collaborator

|     |
| --- |
| I think the semantic version for llama.cpp makes perfect sense. Two things I want to bring to the discussion:<br>First: it will probably be better to have a list of requirements to bump major/minor/patch, to avoid forever sticking with something like `0.1.1234`<br>I'm suggesting a initial version of the list for further discussions:<br>- Patch number bump when:<br>  - small bug fixes<br>  - vendor updates<br>- Minor bump when:<br>  - new model support<br>  - perf improvements<br>- Major bump when:<br>  - major changes in pubic API (i.e. new array of API is added, deprecated old one)<br>  - features added to server (which also changes the public REST API)<br>Second: we can setup a specific pipeline that tests the release against common models before releasing it<br>- To decide: what is the list of models? Maybe last N well known / most downloaded on HF, plus a fixed list of hand-picked models<br>- We may not have enough hw capacity to test on all backend, probably starts with CUDA & Metal for now? |

1You must be logged in to vote

👍2

All reactions

- 👍2

13 replies


Show 8 previous replies

[![@ngxson](https://avatars.githubusercontent.com/u/7702203?s=60&v=4)](https://github.com/ngxson)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [ngxson](https://github.com/ngxson) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17938352)   Collaborator

|     |
| --- |
| > Interesting. At first glance, the 1.0.0 and 2.0.0 just look like additions to the REST API, that doesn't really breaking anything though, right? The 4.0.0 bump was because the `/metrics` endpoint got new fields, not sure about that.<br>Right, in general we rarely have breaking changes for server API, only addition (with backward compat), so it's true that the past 100 commit doesn't bump major number at all.<br>However, that would still mean at least ~50 minor bumps for a time span of 5 days. And if (for example) we choose to release once per week, that would mean (almost) always one minor bump per week, almost no patch bump (unless in the rare case of force triggering the release workflow).<br>So assuming 1 release per week, the releases will look almost like this:<br>```<br>0.1.0 --> first week<br>0.2.0 --> second week<br>0.3.0 --> third week<br>0.3.1 --> "force" release because 0.3.0 is broken<br>... (rarely a patch bump)<br>0.123.0 --> 123-th week after semver was adopted<br>```<br>That got me thinking about home assistant's [calver](https://developers.home-assistant.io/docs/versioning/) scheme:<br>```<br>2026.1.0<br>2026.2.0<br>2026.2.1  --> "force" release for bug fixes<br>...<br>2026.8.0  --> latest<br>``` |

All reactions

[![@ngxson](https://avatars.githubusercontent.com/u/7702203?s=60&v=4)](https://github.com/ngxson)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ngxson](https://github.com/ngxson) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17938454)   Collaborator

|     |
| --- |
| If we choose to release every N commits instead of every week, the homebrew releases is a nice place to measure the speed: [https://github.com/Homebrew/homebrew-core/pulls?q=sort:updated-desc+is:pr+llama.cpp+in:title](https://github.com/Homebrew/homebrew-core/pulls?q=sort:updated-desc+is:pr+llama.cpp+in:title)<br>Things that I observed about this approach:<br>- We are merging about 10-20 commits per day, so if N less than 20 then it will be more frequent than nightly (which we don't want)<br>- Minor version bump almost always happen for a span of 10-20 commits, we rarely have 10-20 patches (bug fixes) in a row |

All reactions

[![@ckastner](https://avatars.githubusercontent.com/u/15859947?s=60&v=4)](https://github.com/ckastner)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ckastner](https://github.com/ckastner) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17938863)

|     |
| --- |
| > And if (for example) we choose to release once per week, that would mean (almost) always one minor bump per week, almost no patch bump (unless in the rare case of force triggering the release workflow).<br>One minor bump per week wouldn't really shock me that much, TBH. I wouldn't do more frequent than that, because at some point one just lands back at the nightlies. Perhaps "weekly" is even too strict, something like ~weekly, but shorter if some release needs it, or longer if stuff isn't ready yet.<br>The calver scheme you linked also looks nice. One can't really tell breaking changes from it, but for the library there is the SOVER to signal that independently, and for the tools -- well, maybe they don't need that signal? |

All reactions

[![@ngxson](https://avatars.githubusercontent.com/u/7702203?s=60&v=4)](https://github.com/ngxson)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [ngxson](https://github.com/ngxson) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17939182)   Collaborator

|     |
| --- |
| Agree, I think weekly release the as good as we can guaranteed for now. So these point are pretty much aligned for now:<br>- Most releases will be minor bump<br>- The release frequency is not strictly fixed, we can force-release. For example, some cases that I can think of:<br>  - If a model support is added, it's likely mean a new release --> likely be a minor bump<br>  - If the release is broken somehow --> likely be a patch bump<br>- Occasionally major release on these changes:<br>  - Breaking changes in ABI. Note that we usually try to have function calls backward-compat, meaning new libllama calls don't mean breaking change; however adding a new enum value will still be a breaking change<br>  - Do we cover `llama-ext.h` header? or only the `llama.h`?<br>  - For server API: only breaking change to **inference endpoints** (completions, embeddings) are considered major bump. Breaking changes to other things: router API, tools, CORS proxy are patches<br>  - Changes to components like llama-cli, llama-ui, llama-quantize are always (but not strictly) minor bump<br>I'll try to run another simulation tomorrow |

👍2

All reactions

- 👍2

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Aug 10Aug 10, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17961261)   Maintainer  Author

|     |
| --- |
| > Do we cover llama-ext.h header? or only the llama.h?<br>The purpose of the `llama-ext.h` is to be able to experiment with some API changes without affecting the official API of the library and therefore without affecting the minor and major versions. The `llama-ext.h` is not public so we can change it without announcing this with a version bumps. |

👍1

All reactions

- 👍1

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/515930?s=64&v=4)\ mbaudier](https://github.com/mbaudier) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17934239)

|     |
| --- |
| Will this versioning policy also cover mtmd?<br>More generally, is it planned that `libmtmd` would be maintained as a library, like `libllama`? (vs. in `tools/` as is currently the case)<br>Or will it be merged into `libllama` at some point? |

1You must be logged in to vote

All reactions

5 replies


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17934657)   Maintainer  Author

|     |
| --- |
| I wish one day we will merge it in `libllama`, but it might take a while. For now it seems much simpler to remain separate. Though we probably should treat its API the same way as `libllama`'s API and reflect changes in the semantic version accordingly. [@ngxson](https://github.com/ngxson) WDYT? |

All reactions

[![@ngxson](https://avatars.githubusercontent.com/u/7702203?s=60&v=4)](https://github.com/ngxson)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ngxson](https://github.com/ngxson) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17937179)   Collaborator

|     |
| --- |
| Good point. I don't have a good idea for now, but I'm considering about this:<br>Since our goal is to merge libmtmd and libllama into one package, it might be important to always keep the libmtmd version less than libllama until we merge them together.<br>One idea I'm thinking about: libmtmd will have versioning with major = 0 for now, and I will only bump the minor+patch. Then when we merge it to libllama, the major version will be increase to match libllama (in other words: if we bump mtmd major number right now, when we merge it, we will end up with mtmd's major > llama's major, which will be a messy situation) |

All reactions

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Aug 10Aug 10, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17960868)   Maintainer  Author

|     |
| --- |
| I meant that we can have a single semantic version that tracks both `libllama` and `libmtmd`. So basically as if the `llama.h` and `mtmd.h` were part of the same API. Changes in either API results in version update. |

👍1

All reactions

- 👍1

[![@danbev](https://avatars.githubusercontent.com/u/432351?s=60&v=4)](https://github.com/danbev)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [danbev](https://github.com/danbev) [on Aug 10Aug 10, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17961525)   Maintainer

|     |
| --- |
| I've opened [ggml-org/llama.cpp#26839](https://github.com/ggml-org/llama.cpp/pull/26839) and libmtmd in which both use the same semantic version. |

👍2

All reactions

- 👍2

[![@mbaudier](https://avatars.githubusercontent.com/u/515930?s=60&v=4)](https://github.com/mbaudier)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [mbaudier](https://github.com/mbaudier) [on Aug 10Aug 10, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17961684)

|     |
| --- |
| As a consumer (vs. as a packager) of the libraries only, that is, developing directly on top of `libllama` and `libmtmd`, this is indeed one same API. The separation currently makes sense because `libmtmd` is, as stated in the doc, slightly less stable than `libllama`, and that makes it easier to track the dependencies (simply check the headers). +1 for using the same semantic version, as it will be easier for everyone to manage. |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)\ ggerganov](https://github.com/ggerganov) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17934785)   Maintainer  Author

|     |
| --- |
| Next week will try to implement some automation with [@danbev](https://github.com/danbev) according to the spec above to start semver tagging of `llama.cpp` and utilizing `find_package` for discovering the correct `ggml` version. Until then we can iterate on the spec and discuss. |

1You must be logged in to vote

👍2

All reactions

- 👍2

3 replies


[![@danbev](https://avatars.githubusercontent.com/u/432351?s=60&v=4)](https://github.com/danbev)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [danbev](https://github.com/danbev) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17934992)   Maintainer

|     |
| --- |
| I've made a start on find\_package which can be found here [#1582](https://github.com/ggml-org/ggml/pull/1582) |

All reactions

[![@danbev](https://avatars.githubusercontent.com/u/432351?s=60&v=4)](https://github.com/danbev)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [danbev](https://github.com/danbev) [on Aug 10Aug 10, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17962181)   Maintainer

|     |
| --- |
| [@ggerganov](https://github.com/ggerganov) Regarding the release branches mentioned above. I was thinking of using the current build flow but with the addition of verifying that the ggml version in llama.cpp matches the released version for llama.cpp release builds, and do this in a github action. Basically not having a separate release branch is what I'm suggesting/asking, but perhaps I'm overlooking some additional benefit of using a separate release branch? |

All reactions

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Aug 10Aug 10, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17962570)   Maintainer  Author

|     |
| --- |
| Yes, I also realized that we don't need the `release` branches. I will update the spec accordingly to simplify. |

👍1

All reactions

- 👍1

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/105994585?s=64&v=4)\ p-linnane](https://github.com/p-linnane) [on Aug 7Aug 7, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-17936483)

|     |
| --- |
| For Homebrew we perform regression tests of dependents when updating formulae. If a new version of `ggml` was released that `llama.cpp` didn't work with, CI would fail. Likewise, as seen in our latest bump, if a version of `llama.cpp` was released that didn't work with the current `ggml`, CI would fail. |

1You must be logged in to vote

👍1

All reactions

- 👍1

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/432351?s=64&v=4)\ danbev](https://github.com/danbev) [on Aug 18Aug 18, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18061218)   Maintainer

|     |
| --- |
| [@ggerganov](https://github.com/ggerganov) Do you think we are in a good enough shape with the llama.cpp changes that I should start looking at whisper.cpp and introduce the same/similar changes. I'm mainly thinking about the ggml check, as it would be possible to keep the current release build that happens upon tag creation/push if we wanted to. But perhaps it would be better to make this consistent with llama.cpp and introduce the same changes? |

1You must be logged in to vote

All reactions

10 replies


Show 5 previous replies

[![@mbaudier](https://avatars.githubusercontent.com/u/515930?s=60&v=4)](https://github.com/mbaudier)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [mbaudier](https://github.com/mbaudier) [on Aug 19Aug 19, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18076656)

|     |
| --- |
| [@danbev](https://github.com/danbev) I had a look at talk-llama's `CMakeLists.txt` in your branch. From what I understand, a given llama.cpp tag is fetched and built, allowing then to use `libllama` as a private library. (This is essentially what I do too when developing the [JJML](https://github.com/argeo/argeo-jjml) Java bindings, with ggml, llama.cpp, and whisper.cpp as git submodules)<br>What I can already tell you is that, from a Debian packaging perspective, we will want to use the packaged `libllama`. So, it would be very useful if we could from the start have something like `WHISPER_USE_SYSTEM_LLAMA` (similar to `WHISPER_USE_SYSTEM_GMML`, or `LLAMA_USE_SYSTEM_GGML` in llama.cpp) which would completely bypass the git fetch and the llama.cpp build. If this variable is set, `libllama` would simply be referenced as a public library in `target_link_libraries()`.<br>If you could make these changes, I would then test the packaging in a fork of the [official Debian packages](https://salsa.debian.org/deeplearning-team/whisper.cpp) and we could make sure that we have clean Debian packages from day one. |

👍1

All reactions

- 👍1

[![@danbev](https://avatars.githubusercontent.com/u/432351?s=60&v=4)](https://github.com/danbev)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [danbev](https://github.com/danbev) [on Aug 19Aug 19, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18079051)   Maintainer

|     |
| --- |
| [@mbaudier](https://github.com/mbaudier) I've taken a stab at this and added a new commit to [ggml-org/whisper.cpp#3996](https://github.com/ggml-org/whisper.cpp/pull/3996). Could you take a look and give this a try and see if this is what you had in mind? |

All reactions

[![@mbaudier](https://avatars.githubusercontent.com/u/515930?s=60&v=4)](https://github.com/mbaudier)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [mbaudier](https://github.com/mbaudier) [on Aug 19Aug 19, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18080656)

|     |
| --- |
| [@danbev](https://github.com/danbev) I built your branch manually on Debian sid/unstable, and it looks good.<br>```<br>sudo apt install libggml-dev libllama-dev libsdl2-dev<br>cmake -B build/ \<br> -DWHISPER_SDL2=ON \<br> -DWHISPER_USE_SYSTEM_LLAMA=ON \<br> -DCMAKE_PREFIX_PATH=/usr/lib/x86_64-linux-gnu/llama/cmake-private<br>cmake --build build/ -j $(nproc)<br>```<br>The executable is properly linked to the deployed `libllama`:<br>```<br>  ldd build/bin/whisper-talk-llama<br>    ...<br>    libllama.so.0 => /usr/lib/x86_64-linux-gnu/llama/libllama.so.0 (0x00007f10a4a00000)<br>    ...<br>    libggml.so.0 => /usr/lib/x86_64-linux-gnu/libggml.so.0 (0x00007f10a4db3000)<br>    libggml-base.so.0 => /usr/lib/x86_64-linux-gnu/libggml-base.so.0 (0x00007f10a486c000)<br>    ...<br>```<br>Once we have llama.cpp packages with the new versioning scheme, `CMAKE_PREFIX_PATH` won't be needed any more, and `libllama` will be available directly in `/usr/lib/<arch>-linux-gnu` (like `libggml` and `libwhisper`). The includes and CMake configs will also be in the standard locations expected by default.<br>As soon as we have finalised these new llama.cpp packages, we will enable building and distributing `whisper-talk-llama` in the whisper.cpp packages. So, from my perspective, this is good to merge. Thanks a lot! |

All reactions

[![@danbev](https://avatars.githubusercontent.com/u/432351?s=60&v=4)](https://github.com/danbev)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [danbev](https://github.com/danbev) [on Aug 19Aug 19, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18080761)   Maintainer

|     |
| --- |
| [@mbaudier](https://github.com/mbaudier) Awesome! Thanks for testing and verifying this! |

All reactions

[![@mbaudier](https://avatars.githubusercontent.com/u/515930?s=60&v=4)](https://github.com/mbaudier)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [mbaudier](https://github.com/mbaudier) [on Aug 24Aug 24, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18133571)

|     |
| --- |
| [@danbev](https://github.com/danbev) whisper.cpp v1.9.3 is now available in Debian sid/unstable and provides `whisper-talk-llama`, which uses the packaged llama.cpp deployed on the system. This closes the related [Debian enhancement request](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1137510). |

🎉1

All reactions

- 🎉1

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)\ ggerganov](https://github.com/ggerganov) [on Aug 18Aug 18, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18064730)   Maintainer  Author

|     |
| --- |
| Semantic version in `llama.cpp` is pretty much ready: [https://github.com/ggml-org/llama.cpp/releases/tag/v0.1.2](https://github.com/ggml-org/llama.cpp/releases/tag/v0.1.2)<br>Marked as "pre-release" for now, until we do a few quick release rounds in the next few days to make sure everything is good. After that, we'll remove the "pre-release" flag and will aim for a slow-paced, steady release cycle. |

4You must be logged in to vote

🎉4❤️6🚀5

All reactions

- 🎉4
- ❤️6
- 🚀5

3 replies


[![@danbev](https://avatars.githubusercontent.com/u/432351?s=60&v=4)](https://github.com/danbev)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [danbev](https://github.com/danbev) [on Aug 20Aug 20, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18092733)   Maintainer

|     |
| --- |
| We have done the same/similar now for whisper.cpp: [https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.3](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.3) |

👍1

All reactions

- 👍1

[![@danbev](https://avatars.githubusercontent.com/u/432351?s=60&v=4)](https://github.com/danbev)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [danbev](https://github.com/danbev) [on Aug 24Aug 24, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18131370)   Maintainer

|     |
| --- |
| And now also for llama.vim: [https://github.com/ggml-org/llama.vim/releases](https://github.com/ggml-org/llama.vim/releases) |

👍2

All reactions

- 👍2

[![@ckastner](https://avatars.githubusercontent.com/u/15859947?s=60&v=4)](https://github.com/ckastner)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ckastner](https://github.com/ckastner) [on Aug 24Aug 24, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18131899)

|     |
| --- |
| Perfect, thanks!<br>I wonder, will llama.vim also need some way to communicate a minimum version of the llama.cpp it needs? Even if it's just a .txt or whatever. Or is that generally not an issue? |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/432351?s=64&v=4)\ danbev](https://github.com/danbev) [on Aug 20Aug 20, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18094107)   Maintainer

|     |
| --- |
| Regarding llama.vim, I think we could simply start tagging using semantic versioning and that would allow plugin managers to be able to specify a semver tag instead of today where I think the only choice is to follow the master branch, or a specific commit. |

1You must be logged in to vote

👍1

All reactions

- 👍1

1 reply


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Aug 20Aug 20, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18094463)   Maintainer  Author

|     |
| --- |
| Yes, we can do that. |

👍2

All reactions

- 👍2

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/15859947?s=64&v=4)\ ckastner](https://github.com/ckastner) [on Aug 20Aug 20, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18097212)

|     |
| --- |
| When cutting releases, could we also have the web assets for that release as `vX.Y.Z` in the HF [bucket](https://huggingface.co/buckets/ggml-org/llama-ui)? |

0You must be logged in to vote

All reactions

6 replies


Show 1 previous reply

[![@ckastner](https://avatars.githubusercontent.com/u/15859947?s=60&v=4)](https://github.com/ckastner)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ckastner](https://github.com/ckastner) [on Aug 21Aug 21, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18103542)

|     |
| --- |
| > However, we are thinking about dropping the HF bucket distribution of the WebUI because we already distribute the UI with the Github releases: [ggml-org/llama.cpp#27316](https://github.com/ggml-org/llama.cpp/issues/27316). Any concerns?<br>Oh, I missed that. That is fine, I'll switch to that.<br>Context: we can't ship the WebUI directly with the Debian package because of a technicality: by Policy, all assets need to be rebuildable from source from within Debian, and some of the npm dependencies aren't packaged yet.<br>So the workaround our package offers is to simply download the UI at package install/update time. We have a second worarkound in progress (a standalone package in the `contrib` section).<br>> I think they are already there currently as part of the corresponding nightly build?<br>I wonder: can the corresponding build number be made available as part of the tarballs? The nightly tarballs happen to have the number in the directory name, but nothing in the 0.1.2 tarball suggests b10485.<br>Just thinking aloud here. If (big IF) there is an easy way, this could be generally useful, for example by initializing `BUILD_NUMBER` to something other than 0, in the tarballs. |

All reactions

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [ggerganov](https://github.com/ggerganov) [on Aug 21Aug 21, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18103576)   Maintainer  Author

|     |
| --- |
| Would it work if we also attach the UI asset from the corresponding nightly build along with the source-code tarball in the release page: [https://github.com/ggml-org/llama.cpp/releases/tag/v0.1.2](https://github.com/ggml-org/llama.cpp/releases/tag/v0.1.2) |

All reactions

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [ggerganov](https://github.com/ggerganov) [on Aug 21Aug 21, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18103658)   Maintainer  Author

|     |
| --- |
| I just manually updated the `v0.1.2` pre-release by attaching the UI asset to clarify what I mean.<br>Alternatively, we can include just a simple text file `nightly.tag` or `nightly-tag.txt` and it can contain the corresponding tag - in this case: `b10485`. From there, one could download the asset. |

All reactions

[![@ckastner](https://avatars.githubusercontent.com/u/15859947?s=60&v=4)](https://github.com/ckastner)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ckastner](https://github.com/ckastner) [on Aug 21Aug 21, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18104309)

|     |
| --- |
| Yes, both would work. Thanks!<br>I think having `nightly.tag[.txt]` is more generally useful, we'd grab it and feed `LLAMA_BUILD_NUMBER` for example.<br>Also shipping the UI assets is convenient, but also duplication. I'm not sure the extra convenience (saving 1-2 curl calls) is worth the effort. |

👍1

All reactions

- 👍1

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Aug 21Aug 21, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18104390)   Maintainer  Author

|     |
| --- |
| Ok, going with the `nightly-tag.txt` then. |

👍1

All reactions

- 👍1

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)\ ggerganov](https://github.com/ggerganov) [on Aug 21Aug 21, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18109683)   Maintainer  Author

|     |
| --- |
| I think this doc is now complete. Any feedback for improvements is welcome. I've added a few TODOs to the OP for later. |

1You must be logged in to vote

👍2

All reactions

- 👍2

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/22483295?s=64&v=4)\ AHeinlein](https://github.com/AHeinlein) [on Sep 5Sep 5, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18306708)

|     |
| --- |
| Is it intentional or by accident that the point release assets contain neither prebuilt binaries nor the UI package? I see that the build process is trying to download the UI files at build time - I don't like that because I usually build in isolated environments. It also means that v0.4.0 built now may differ from 0.4.0 built next week or next month - the build script tries to download a version "b0" first from HF, which doesn't exist, and then the latest version which I guess is subject to change. If possible please provide UI files with the point releases or include them in the source package. |

1You must be logged in to vote

All reactions

1 reply


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Sep 10Sep 10, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18382336)   Maintainer  Author

|     |
| --- |
| > Is it intentional or by accident that the point release assets contain neither prebuilt binaries nor the UI package?<br>Yes, the point releases are just a semantic version tag. Each such release also points to a respective nightly build. For example [https://github.com/ggml-org/llama.cpp/releases/tag/v0.4.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.4.0) points to nightly build [https://github.com/ggml-org/llama.cpp/releases/tag/b10809](https://github.com/ggml-org/llama.cpp/releases/tag/b10809). This nightly build has all the corresponding assets.<br>> I see that the build process is trying to download the UI files at build time - I don't like that because I usually build in isolated environments.<br>This can be disabled with `LLAMA_BUILD_UI=OFF` cmake option.<br>> It also means that v0.4.0 built now may differ from 0.4.0 built next week or next month - the build script tries to download a version "b0" first from HF, which doesn't exist, and then the latest version which I guess is subject to change.<br>That should not be the case - the `bXXXX` UI builds always exist for the point releases.<br>> If possible please provide UI files with the point releases or include them in the source package.<br>They are already provided by following the included nightly tag. |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/ggml/discussions/1579).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/310686526?s=64&v=4)\ jameschristopherfrederick18-star](https://github.com/jameschristopherfrederick18-star) [on Oct 2Oct 3, 2026](https://github.com/ggml-org/ggml/discussions/1579\#discussioncomment-18725341)

|     |
| --- |
| This helps alot |

1You must be logged in to vote

👍1

All reactions

- 👍1

0 replies


[Sign up for free](https://github.com/join?source=comment-repo) **to join this conversation on GitHub**.
Already have an account?
[Sign in to comment](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fggml-org%2Fggml%2Fdiscussions%2F1579)

Category


[💬\\
\\
General](https://github.com/ggml-org/ggml/discussions/categories/general)

Labels


None yet


10 participants


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=48&v=4)](https://github.com/ggerganov)[![@danbev](https://avatars.githubusercontent.com/u/432351?s=48&v=4)](https://github.com/danbev)[![@mbaudier](https://avatars.githubusercontent.com/u/515930?s=48&v=4)](https://github.com/mbaudier)[![@CISC](https://avatars.githubusercontent.com/u/1629204?s=48&v=4)](https://github.com/CISC)[![@ngxson](https://avatars.githubusercontent.com/u/7702203?s=48&v=4)](https://github.com/ngxson)[![@ckastner](https://avatars.githubusercontent.com/u/15859947?s=48&v=4)](https://github.com/ckastner)[![@AHeinlein](https://avatars.githubusercontent.com/u/22483295?s=48&v=4)](https://github.com/AHeinlein)[![@p-linnane](https://avatars.githubusercontent.com/u/105994585?s=48&v=4)](https://github.com/p-linnane)[![@ddeteljAI](https://avatars.githubusercontent.com/u/288738912?s=48&v=4)](https://github.com/ddeteljAI)[![@jameschristopherfrederick18-star](https://avatars.githubusercontent.com/u/310686526?s=48&v=4)](https://github.com/jameschristopherfrederick18-star)

Heading

Bold

Italic

Quote

Code

Link

* * *

Numbered list

Unordered list

Task list

* * *

Attach files

Mention

Reference

# Select a reply

Loading

[Create a new saved reply](https://github.com/ggml-org/ggml/discussions/1579)

👍1 reacted with thumbs up emoji👎1 reacted with thumbs down emoji😄1 reacted with laugh emoji🎉1 reacted with hooray emoji😕1 reacted with confused emoji❤️1 reacted with heart emoji🚀1 reacted with rocket emoji👀1 reacted with eyes emoji

You can’t perform that action at this time.