[Skip to content](https://github.com/ggml-org/llama.cpp/releases/tag/b12360#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/releases/tag/b12360) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/releases/tag/b12360) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/releases/tag/b12360) to refresh your session.Dismiss alert

{{ message }}

# b12360

Pre-release

Pre-release

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/releases/tag/b12360).

## No results found

[View all tags](https://github.com/ggml-org/llama.cpp/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

1 hour ago
13 Nov 10:02


[b12360](https://github.com/ggml-org/llama.cpp/tree/b12360)

[`2d8a325`](https://github.com/ggml-org/llama.cpp/commit/2d8a32502909ca065c41c4cf5f2fb1c427c047fc)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Nov 13, 2026, 04:15 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


CUDA: split the PAD\_REFLECT\_1D grid to stay within the HIP grid limit ( [#32179](https://github.com/ggml-org/llama.cpp/pull/32179))

The kernel launches one block per row and 256-wide tile, so the

{2, 16777217} test case asks for 16777217 blocks of 256 threads. HIP

refuses a grid dimension above 2^32 threads and the ROCm jobs fail

with "invalid configuration argument".

The host now launches the grid in chunks of at most UINT32\_MAX / 256

blocks and passes the chunk offset to the kernel. Real sizes fit in a

single chunk and keep their timings.

**Website:**

- [https://llama.app](https://llama.app/)

**Attestations:**

- [https://github.com/ggml-org/llama.cpp/attestations/67114504](https://github.com/ggml-org/llama.cpp/attestations/67114504)

**macOS/iOS:**

- [macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-macos-arm64.tar.gz)
- macOS Apple Silicon (arm64, KleidiAI enabled) [DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780)
- [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-macos-x64.tar.gz)
- [iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-xcframework.zip)

**Linux:**

- [Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-x64.tar.gz)
- [Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-arm64.tar.gz)
- [Ubuntu 24.04 s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-s390x.tar.gz)
- [Ubuntu 26.04 s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-26.04-s390x.tar.gz)
- [Ubuntu 26.04 s390x (zDNN)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-zdnn-s390x.tar.gz)
- [Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-vulkan-x64.tar.gz)
- [Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-vulkan-arm64.tar.gz)
- [Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-cuda-12.8-x64.tar.gz) \- [CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-b12360-bin-ubuntu-cuda-12.8-x64.tar.gz)
- [Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-cuda-13.5-x64.tar.gz) \- [CUDA 13.5 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-b12360-bin-ubuntu-cuda-13.5-x64.tar.gz)
- [Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-cuda-13.5-arm64.tar.gz) \- [CUDA 13.5 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-b12360-bin-ubuntu-cuda-13.5-arm64.tar.gz)
- [Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-rocm-10.0-x64.tar.gz)
- [Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-openvino-2026.4.1-x64.tar.gz)
- [Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-sycl-fp32-x64.tar.gz)
- [Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-sycl-fp16-x64.tar.gz)
- [Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-linux-arm64-snapdragon.tar.gz) \- [setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

- [Android arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-android-arm64.tar.gz)
- [Android arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-android-arm64-snapdragon.tar.gz) \- [setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/README.md)

**Windows:**

- [Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cpu-x64.zip)
- [Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cpu-arm64.zip)
- [Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-opencl-adreno-arm64.zip)
- [Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cuda-12.4-x64.zip) \- [CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-bin-win-cuda-12.4-x64.zip)
- [Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cuda-13.5-x64.zip) \- [CUDA 13.5 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-bin-win-cuda-13.5-x64.zip)
- [Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cuda-13.5-arm64.zip) \- [CUDA 13.5 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-bin-win-cuda-13.5-arm64.zip)
- [Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-vulkan-x64.zip)
- [Windows arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-vulkan-arm64.zip)
- [Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-openvino-2026.4.1-x64.zip)
- [Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-sycl-x64.zip)
- [Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-rocm-10.0-x64.zip)

**openEuler:**

- [DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)
- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

- [UI](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-ui.tar.gz)

Assets40

- [cudart-llama-b12360-bin-ubuntu-cuda-12.8-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-b12360-bin-ubuntu-cuda-12.8-x64.tar.gz)



sha256:be7ec0dba5eac064460b34c02e4010deb14eb8bfba95ae9b508ae4c0a1983b5f



567 MB1 hour ago2026-11-13T10:02:30Z

- [cudart-llama-b12360-bin-ubuntu-cuda-13.5-arm64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-b12360-bin-ubuntu-cuda-13.5-arm64.tar.gz)



sha256:9e85247f3f47280d48b3ce8cbafc5e59d7eaa16375a95b811f80ae90932f92e2



534 MB1 hour ago2026-11-13T10:02:46Z

- [cudart-llama-b12360-bin-ubuntu-cuda-13.5-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-b12360-bin-ubuntu-cuda-13.5-x64.tar.gz)



sha256:066423c40e87fcaa01dd1631ca48376be7b04123da1b732117cd74b004046de4



424 MB1 hour ago2026-11-13T10:03:03Z

- [cudart-llama-bin-win-cuda-12.4-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-bin-win-cuda-12.4-x64.zip)



sha256:8c79a9b226de4b3cacfd1f83d24f962d0773be79f1e7b75c6af4ded7e32ae1d6



373 MB1 hour ago2026-11-13T10:03:17Z

- [cudart-llama-bin-win-cuda-13.5-arm64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-bin-win-cuda-13.5-arm64.zip)



sha256:f89e7b2457f627d052dd99f42205ddfd01964454809754cdc649cffc74320dca



266 MB1 hour ago2026-11-13T10:03:28Z

- [cudart-llama-bin-win-cuda-13.5-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/cudart-llama-bin-win-cuda-13.5-x64.zip)



sha256:c2bf4cc202bfbaaa7a0b75f5082457c3811326947bb216059b72839d844e9cba



407 MB1 hour ago2026-11-13T10:03:41Z

- [llama-b12360-bin-android-arm64-snapdragon.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-android-arm64-snapdragon.tar.gz)



sha256:a7ca584b39472c4cb64f4877172fcc6b013e46550ce37b1db23842c03e33950a



62.6 MB1 hour ago2026-11-13T10:03:53Z

- [llama-b12360-bin-android-arm64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-android-arm64.tar.gz)



sha256:2c52705bf6eb5b296c7ac46e5d794988aa086a6470ec7b16524da4a3c7acacdb



75.2 MB1 hour ago2026-11-13T10:03:55Z

- [llama-b12360-bin-linux-arm64-snapdragon.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-linux-arm64-snapdragon.tar.gz)



sha256:0ce0a3a010760e5e6ffc10da651ce68a0439a00381ef707d23977aa2fc30a88f



24.7 MB1 hour ago2026-11-13T10:03:58Z

- [llama-b12360-bin-macos-arm64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-macos-arm64.tar.gz)



sha256:e815561e9621c606388d4538101d56fcf317cdec6ce8f2bbd1bf14f0df29925e



16.1 MB1 hour ago2026-11-13T10:04:00Z

- [llama-b12360-bin-macos-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-macos-x64.tar.gz)



sha256:ed329ff7f4048dbfbc401909926a6c6f49114fc7cb7860ed9c7976fadcc11a34



12.1 MB1 hour ago2026-11-13T10:04:01Z

- [llama-b12360-bin-ubuntu-26.04-s390x.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-26.04-s390x.tar.gz)



sha256:fb35b859b8a9808d8916e3669d903df21f03a1e1157ec7413ddd3d4929095cc9



15.2 MB1 hour ago2026-11-13T10:04:02Z

- [llama-b12360-bin-ubuntu-arm64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-arm64.tar.gz)



sha256:a8e2783d74e3e77c4f5e31fbe88e6365c98dffbeb203a1031737121764b62a2a



18.1 MB1 hour ago2026-11-13T10:04:04Z

- [llama-b12360-bin-ubuntu-cuda-12.8-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-cuda-12.8-x64.tar.gz)



sha256:1874218dad4a58b5187e01a65de1cdb68218d93a510bca59a976ccb47fafed85



190 MB1 hour ago2026-11-13T10:04:05Z

- [llama-b12360-bin-ubuntu-cuda-13.5-arm64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-cuda-13.5-arm64.tar.gz)



sha256:77bfa8d0966c7d7490b3dd52e7c4255613738d960c278f6b719b0c344121c305



165 MB1 hour ago2026-11-13T10:04:12Z

- [llama-b12360-bin-ubuntu-cuda-13.5-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-cuda-13.5-x64.tar.gz)



sha256:e566d6e13019798ecea3a81c7d33783099b89d94dd4e72dfc379af5fde0566ad



170 MB1 hour ago2026-11-13T10:04:18Z

- [llama-b12360-bin-ubuntu-openvino-2026.4.1-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-openvino-2026.4.1-x64.tar.gz)



sha256:3532dce9d26829cee9aedaaeb6a1752c3c10086f6610ece19ffaf729043d00d2



117 MB1 hour ago2026-11-13T10:04:24Z

- [llama-b12360-bin-ubuntu-rocm-10.0-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-rocm-10.0-x64.tar.gz)



sha256:fc3ddf64f9a5f7697754d156f36ac9efc419d7f571f7f07b3048f66bbc18d187



258 MB1 hour ago2026-11-13T10:04:32Z

- [llama-b12360-bin-ubuntu-s390x.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-s390x.tar.gz)



sha256:61ffac3673a78ba2c6e9aa705979f2b04e0cc5a170b334f9af0e0d279503f7d6



17.3 MB1 hour ago2026-11-13T10:04:40Z

- [llama-b12360-bin-ubuntu-sycl-fp16-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-sycl-fp16-x64.tar.gz)



sha256:742708b5cc414ba3528e9ef11d14dee2b35a72d53f8c4c57e06127ab6ec510ea



64 MB1 hour ago2026-11-13T10:04:42Z

- [llama-b12360-bin-ubuntu-sycl-fp32-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-sycl-fp32-x64.tar.gz)



sha256:50faadda199405e71a8b9c2f46fb6a24222c70cb670965436645b95bff69d919



63.9 MB1 hour ago2026-11-13T10:04:46Z

- [llama-b12360-bin-ubuntu-vulkan-arm64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-vulkan-arm64.tar.gz)



sha256:e475abf45095ebf3db483c0bfe1a7e258881dee5c1efc8ec767158653bce459c



28.1 MB1 hour ago2026-11-13T10:04:49Z

- [llama-b12360-bin-ubuntu-vulkan-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-vulkan-x64.tar.gz)



sha256:2133682fba36e101ec1059ee646287bd1768916d3d0479fa4d6135f40f02e309



34.5 MB1 hour ago2026-11-13T10:04:51Z

- [llama-b12360-bin-ubuntu-x64.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-x64.tar.gz)



sha256:b60dc211e4ba206bb04bbc9eb06294364c43d0aab8fc308c44a361477466ba4c



22.2 MB1 hour ago2026-11-13T10:04:52Z

- [llama-b12360-bin-ubuntu-zdnn-s390x.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-ubuntu-zdnn-s390x.tar.gz)



sha256:c91c1036aab8496ac457fdc5ecafe021dd417367ba06baa7a7f5e5daa1d3eb4e



13.4 MB1 hour ago2026-11-13T10:04:54Z

- [llama-b12360-bin-win-cpu-arm64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cpu-arm64.zip)



sha256:269794d34c6d8f5c827f4558442ee28ae07b03a5daf64da8ce112ea477bef4fc



12.8 MB1 hour ago2026-11-13T10:04:55Z

- [llama-b12360-bin-win-cpu-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cpu-x64.zip)



sha256:eae1726047e0eaa707b1302929d196c999b96c2f243b21aea6e93bcebacc4e17



23.9 MB1 hour ago2026-11-13T10:04:56Z

- [llama-b12360-bin-win-cuda-12.4-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cuda-12.4-x64.zip)



sha256:70c0a244acf39f2f3fd8975a8447884e03fd35f499bf7dc284113845e894c382



304 MB1 hour ago2026-11-13T10:04:58Z

- [llama-b12360-bin-win-cuda-13.5-arm64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cuda-13.5-arm64.zip)



sha256:2a795aaecb4a7c4a6a1725175d5de5e72c3dd8f68bd11eb1d91c3520b9c6f6ff



159 MB1 hour ago2026-11-13T10:05:09Z

- [llama-b12360-bin-win-cuda-13.5-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-cuda-13.5-x64.zip)



sha256:aa6a78dea72b14335249175da1765fef63ae30e9d9920e8457a2783dce8654a9



171 MB1 hour ago2026-11-13T10:05:14Z

- [llama-b12360-bin-win-opencl-adreno-arm64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-opencl-adreno-arm64.zip)



sha256:2fdb95352bce5fd650b897e941604dd6edb1e554d3bc882d344813ed99c171be



13.8 MB1 hour ago2026-11-13T10:05:20Z

- [llama-b12360-bin-win-openvino-2026.4.1-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-openvino-2026.4.1-x64.zip)



sha256:55a8ff2b1727ecc5f978695769066ee9960e73a668434cb76822803df1fb6301



100 MB1 hour ago2026-11-13T10:05:22Z

- [llama-b12360-bin-win-rocm-10.0-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-rocm-10.0-x64.zip)



sha256:67e52106b5c8585936d48ac4cf9e92c0bdc01784e70da287d044d6d835ca0d56



267 MB1 hour ago2026-11-13T10:05:28Z

- [llama-b12360-bin-win-sycl-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-sycl-x64.zip)



sha256:92d0269b6d190df364d3fef3eb0361b1f32d76c38bb99b628a0b84e3e3375635



164 MB1 hour ago2026-11-13T10:05:37Z

- [llama-b12360-bin-win-vulkan-arm64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-vulkan-arm64.zip)



sha256:e126f9990ae79a1c039d3d4c67bed55c1abbbc5d392a551e3385b36035f9255f



24.8 MB1 hour ago2026-11-13T10:05:43Z

- [llama-b12360-bin-win-vulkan-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-bin-win-vulkan-x64.zip)



sha256:42a6f9df608b99c1c83fcaf77284a516e3f167b32a4690f4e4e364c377547055



36.3 MB1 hour ago2026-11-13T10:05:44Z

- [llama-b12360-ui.tar.gz](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-ui.tar.gz)



sha256:93d45261b52345aded907d4b32087627bea37499150f149f0e1db1b4a2a0d0b5



3.23 MB1 hour ago2026-11-13T10:05:46Z

- [llama-b12360-xcframework.zip](https://github.com/ggml-org/llama.cpp/releases/download/b12360/llama-b12360-xcframework.zip)



sha256:bf45668c4f916117faea4d1f6b3adf75f31c08fa53b8b8269c4d92358c9c7b30



62.1 MB1 hour ago2026-11-13T10:05:47Z

- [Source code (zip)](https://github.com/ggml-org/llama.cpp/archive/refs/tags/b12360.zip)

2 hours ago2026-11-13T09:15:25Z

- [Source code (tar.gz)](https://github.com/ggml-org/llama.cpp/archive/refs/tags/b12360.tar.gz)

2 hours ago2026-11-13T09:15:25Z


All reactions

You can’t perform that action at this time.