https://forums.developer.nvidia.com/t/ubuntu-26-04-drivers-610-cuda-toolkit-13-3-zfs-on-gx10/373655
Accessed: 2026-09-23

# Ubuntu 26.04 + drivers 610 + cuda-toolkit 13.3 + ZFS on GX10 - DGX Spark / GB10 - NVIDIA Developer Forums

## post by vasimv on Jun 17

Finally managed to get fully working setup with Ubuntu 26.04 (clean of that DGX OS's bloatware) with newest drivers/cuda and ZFS. Why ZFS? Because it has checksums and configurable disk cache size. Compression is not fully useless too (4% on my GGUFs collection), snapshots may help if you like to play roulette with different versions.

So far, tested with llama.cpp, speed is about same as DGX OS+595 drivers+13.3 cuda. Will test with vllm later.

Had to play with reinstalling 24.04 and 26.04 for two days to fix problem with additional 15W power consumption (it was connectx7, of course). Here is my steps: [full DIY install steps: backup DGX OS drive; install ubuntu 26.04 desktop ARM with drivers and third-party software; ZFS without encryption; install cuda-keyring from developer.download.nvidia.com/compute/cuda/repos/ubuntu2604/sbsa; apt install linux-nvidia-hwe-24.04-edge; apt install cuda-toolkit-13-3 cuda-13-3 libnccl2 libnccl-dev; apt install nvtop nvidia-container-toolkit; apt install nvidia-open cuda; install dgx-spark-mlnx-hotplug_26.01-1_all.deb from repo.download.nvidia.com/baseos/ubuntu/noble/arm64; update-initramfs -u]

The system will be configured with 2GB max disk cache. After this you should able to clone llama.cpp and compile it.

## post by elsaco on Jun 17
[messages collapsed in extraction]

## post by vasimv on Jun 25
# NVIDIA GB10: Ubuntu 24.04 + NVIDIA 580 vs Ubuntu 26.04 + NVIDIA 610 in clpeak (https://github.com/krrishnarraj/clpeak)
[benchmark comparison heading; details collapsed in extraction]

## Related topics visible on the page

- "595.58.03 Certified Linux-aarch64 (ARM64) Display Driver and CUDA 13.2 - when for DGX Spark GB10" (26 replies, activity 19h ago) -- https://forums.developer.nvidia.com/t/595-58-03-certified-linux-aarch64-arm64-display-driver-and-cuda-13-2-when-for-dgx-spark-gb10/364688
- "Has anyone tried an alternative Linux distro?" (64 replies)
- "I am EXTREMely disappointed with the current state of DGX Spark" (91 replies, 29.4k views)
- "DGX Spark: 13 -> 49 tok/s with Qwen3.5-35B -- Native SM121 Kernel Build Guide"
