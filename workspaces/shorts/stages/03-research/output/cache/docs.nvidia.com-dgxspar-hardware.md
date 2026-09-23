https://docs.nvidia.com/dgx/dgx-spark/hardware.html
Accessed: 2026-09-23

# Hardware Overview - DGX Spark User Guide (docs.nvidia.com)

## System Overview

The DGX Spark features:

- NVIDIA Grace Blackwell architecture with integrated GPU and CPU
- 20-core Arm processor with high-performance cores
- 128 GB unified system memory
- Compact desktop form factor
- Advanced connectivity including Wi-Fi 7, 10 GbE, and ConnectX-7
- Support for AI models up to 200 billion parameters (or 405B for dual-Spark configuration)

### Component Descriptions

| Component | Specification |
| --- | --- |
| GPU | NVIDIA Blackwell Architecture with 5th Generation Tensor Cores, 4th Generation RT Cores |
| CPU | 20-core Arm processor (10 Cortex-X925 + 10 Cortex-A725) |
| Memory | 128 GB LPDDR5x unified system memory, 256-bit interface, 4266 MHz, 273 GB/s bandwidth |
| Storage | 1 TB or 4 TB NVMe M.2 with self-encryption |
| Network | 1x RJ-45 (10 GbE), ConnectX-7 Smart NIC, Wi-Fi 7, Bluetooth 5.4 |
| Connectivity | 4x USB Type-C, 1x HDMI 2.1a, HDMI multichannel audio |
| Video Processing | 1x NVENC, 1x NVDEC |

## Performance Specifications

### Compute Performance

- **AI Compute**: Up to 1,000 TOPS (trillion operations per second) inference and up to 1 PFLOP (petaFLOP) at FP4 precision with sparsity
- **CUDA Cores**: 6,144
- **Copy Engines**: 2 (enables simultaneous data transfers to and from GPU memory, improving throughput for AI workloads)
- **CPU Performance**: 20 cores (10 Cortex-X925 + 10 Cortex-A725)
- **Memory Bandwidth**: 273 GB/s
- **Memory Channels**: 16 channels (256 bit) LPDDR5X 8533

### AI/ML Capabilities

- **Model Support**: AI models up to 200 billion parameters
- **Tensor Performance**: 5th Generation Tensor Cores with FP4 support
- **Framework Support**: PyTorch, TRT-LLM, and other AI frameworks
- **Use Cases**: Inference, deployment, and fine-tuning of large language models

## Power and Thermal Management

- **Power Supply**: 240W external power supply (included)
  - GB10 SOC Thermal Design Power (TDP) is 140W
  - 100W is available for other system components (ConnectX-7, Wi-Fi, SSD, USB-C, etc.)
