<div align="center">
    <!-- <img src="https://i.imgur.com/7eR7Pan.png" width="400"><br> -->
    <h1> The Grid: Democratizing Superintelligence</div>
    Fine-tuning and inference <a href="https://github.com/kyegomez/thegrid#benchmarks">up to 10x faster</a> than offloading<br><br>
    <a href="https://pypi.org/project/grid/"><img src="https://img.shields.io/pypi/v/grid.svg?color=green"></a><br>
</div>

![Agora banner](agora-banner-water.png)

Generate text with distributed [LLaMA 2](https://ai.meta.com/llama/) ([70B](https://huggingface.co/meta-llama/Llama-2-70b-hf), [70B-Chat](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf)), [LLaMA-65B](https://github.com/facebookresearch/llama/blob/llama_v1/MODEL_CARD.md), [Guanaco-65B](https://huggingface.co/timdettmers/guanaco-65b) or [BLOOM-176B](https://huggingface.co/Agora/bloom) and fine‑tune them for your own tasks &mdash; right from your desktop computer or Google Colab:

```python
from transformers import AutoTokenizer
from grid import AutoDistributedModelForCausalLM

model_name = "enoch/llama-65b-hf"
# You can also use "meta-llama/Llama-2-70b-hf", "meta-llama/Llama-2-70b-chat-hf",
# "Agora/bloom", or "Agora/bloomz"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)
# Embeddings & prompts are on your device, transformer blocks are distributed across the Internet

inputs = tokenizer("A cat sat", return_tensors="pt")["input_ids"]
outputs = model.generate(inputs, max_new_tokens=5)
print(tokenizer.decode(outputs[0]))  # A cat sat on a mat...
```

<p align="center">
    🚀 &nbsp;<b><a href="https://colab.research.google.com/drive/1uCphNY7gfAUkdDrTx21dZZwCOUDCMPw8?usp=sharing">Try now in Colab</a></b>
</p>

🦙 **Want to run LLaMA 2?** Request access to its weights at the ♾️ [Meta AI website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and 🤗 [Model Hub](https://huggingface.co/meta-llama/Llama-2-70b-hf), then run `huggingface-cli login` in the terminal before loading the model. Or just try it in our [chatbot app](https://chat.grid.dev).

📋 **Terms of use.** Make sure you follow the model license (see the ones for [LLaMA 2](https://bit.ly/llama2-license), [LLaMA](https://bit.ly/llama-license) and [BLOOM](https://bit.ly/bloom-license)).

🔏 **Privacy.** Your data will be processed by other people in the public swarm. Learn more about privacy [here](https://github.com/Agora-workshop/grid/wiki/Security,-privacy,-and-AI-safety). For sensitive data, you can set up a [private swarm](https://github.com/Agora-workshop/grid/wiki/Launch-your-own-swarm) among people you trust.

### Connect your GPU and increase Grid capacity

Grid is a community-run system &mdash; we rely on people sharing their GPUs. You can check out available servers on our [swarm monitor](https://health.grid.dev) and connect your GPU to help serving one of the models!

🐍 **Linux + Anaconda.** Run these commands:

```bash
conda install pytorch pytorch-cuda=11.7 -c pytorch -c nvidia
pip install git+https://github.com/Agora-workshop/grid
python -m grid.cli.run_server enoch/llama-65b-hf --adapters timdettmers/guanaco-65b
```

🪟 **Windows + WSL.** Follow the guide on our [Wiki](https://github.com/Agora-workshop/grid/wiki/Run-Grid-server-on-Windows).

🐋 **Any OS + Docker.** Run our [Docker](https://www.docker.com) image:

```bash
sudo docker run -p 31330:31330 --ipc host --gpus all --volume grid-cache:/cache --rm learningathome/grid:main \
    python -m grid.cli.run_server --port 31330 enoch/llama-65b-hf --adapters timdettmers/guanaco-65b
```

These commands host a part of LLaMA-65B with optional [Guanaco](https://huggingface.co/timdettmers/guanaco-65b) adapters on your machine. You can also host `meta-llama/Llama-2-70b-hf`, `meta-llama/Llama-2-70b-chat-hf`, `Agora/bloom`, `Agora/bloomz`, and other compatible models from 🤗 [Model Hub](https://huggingface.co/models), or [add support](https://github.com/Agora-workshop/grid/wiki/Run-a-custom-model-with-Grid) for new model architectures.

🦙 **Want to host LLaMA 2?** Request access to its weights at the ♾️ [Meta AI website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and 🤗 [Model Hub](https://huggingface.co/meta-llama/Llama-2-70b-hf), generate an 🔑 [access token](https://huggingface.co/settings/tokens), then use this command for `grid.cli.run_server`:

```bash
python -m grid.cli.run_server meta-llama/Llama-2-70b-chat-hf --token YOUR_TOKEN_HERE
```

💬 **FAQ.** Check out our [Wiki](https://github.com/Agora-workshop/grid/wiki/FAQ:-Frequently-asked-questions#running-a-server) to learn how to use multple GPUs, restart the server on reboot, etc. If you have any issues or feedback, ping us in [our Discord](https://discord.gg/D9MwApKgWa)!

🔒 **Security.** Hosting a server does not allow others to run custom code on your computer. Learn more [here](https://github.com/Agora-workshop/grid/wiki/Security,-privacy,-and-AI-safety).

🏆 **Thank you!** Once you load and host 10+ blocks, we can show your name or link on the [swarm monitor](https://health.grid.dev) as a way to say thanks. You can specify them with `--public_name YOUR_NAME`.

### Check out tutorials, examples, and more

Basic tutorials:

- Getting started: [tutorial](https://colab.research.google.com/drive/1uCphNY7gfAUkdDrTx21dZZwCOUDCMPw8?usp=sharing)
- Prompt-tune LLaMA-65B for text semantic classification: [tutorial](https://colab.research.google.com/github/Agora-workshop/grid/blob/main/examples/prompt-tuning-sst2.ipynb)
- Prompt-tune BLOOM to create a personified chatbot: [tutorial](https://colab.research.google.com/github/Agora-workshop/grid/blob/main/examples/prompt-tuning-personachat.ipynb)

Useful tools and advanced guides:

- [Chatbot web app](https://chat.grid.dev) (connects to Grid via an HTTP/WebSocket endpoint): [source code](https://github.com/borzunov/chat.grid.dev)
- [Monitor](https://health.grid.dev) for the public swarm: [source code](https://github.com/borzunov/health.grid.dev)
- Launch your own swarm: [guide](https://github.com/Agora-workshop/grid/wiki/Launch-your-own-swarm)
- Run a custom foundation model: [guide](https://github.com/Agora-workshop/grid/wiki/Run-a-custom-model-with-Grid)

Learning more:

- Frequently asked questions: [FAQ](https://github.com/Agora-workshop/grid/wiki/FAQ:-Frequently-asked-questions)
- In-depth system description: [paper](https://arxiv.org/abs/2209.01188)

## How does it work?

- Grid runs large language models like [LLaMA](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md) and [BLOOM](https://huggingface.co/Agora/bloom) **collaboratively** — you load a small part of the model, then team up with people serving the other parts to run inference or fine-tuning.
- Single-batch inference runs at up to 6 steps/sec for LLaMA 2 (70B) and &approx; 1 step/sec for BLOOM-176B. This is [up to 10x faster](https://github.com/Agora-workshop/grid#benchmarks) than offloading, enough for [chatbots](https://chat.grid.dev) and other interactive apps. Parallel inference reaches hundreds of tokens/sec.
- Beyond classic language model APIs — you can employ any fine-tuning and sampling methods, execute custom paths through the model, or see its hidden states. You get the comforts of an API with the flexibility of PyTorch.

<p align="center">
    <img src="https://i.imgur.com/RTYF3yW.png" width="800">
</p>

<p align="center">
    📚 &nbsp;<b><a href="https://github.com/Agora-workshop/grid/wiki/FAQ:-Frequently-asked-questions">See FAQ</a></b>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    📜 &nbsp;<b><a href="https://arxiv.org/pdf/2209.01188.pdf">Read paper</a></b>
</p>

## Installation

Here's how to install Grid with [Anaconda](https://www.anaconda.com/products/distribution) on Linux:

```bash
conda install pytorch pytorch-cuda=11.7 -c pytorch -c nvidia
pip install git+https://github.com/Agora-workshop/grid
```

If you don't use Anaconda, you can install PyTorch in [any other way](https://pytorch.org/get-started/locally/). If you want to run models with 8-bit weights, please install PyTorch with CUDA 11.x or newer for compatility with [bitsandbytes](https://github.com/timDettmers/bitsandbytes).

See the instructions for macOS and Windows, the full requirements, and troubleshooting advice in our [FAQ](https://github.com/Agora-workshop/grid/wiki/FAQ:-Frequently-asked-questions#running-a-client).

## Benchmarks

The benchmarks below are for BLOOM-176B:

<table align="center">
  <tr>
    <th colspan="2">Network</th>
    <th colspan="2">Single-batch inference<br>(steps/s)</th>
    <th colspan="2">Parallel forward<br>(tokens/s)</th>
  </tr>
  <tr>
    <th rowspan="2">Bandwidth</th>
    <th rowspan="2">Round-trip<br>latency</th>
    <th colspan="2">Sequence length</th>
    <th colspan="2">Batch size</th>
  </tr>
  <tr align="center">
    <td>128</td>
    <td>2048</td>
    <td>1</td>
    <td>64</td>
  </tr>
  <tr>
    <th colspan="6">Offloading, max. possible speed on 1x A100 <sup>1</sup></th>
  </tr>
  <tr align="center">
    <td>256 Gbit/s</td>
    <td></td>
    <td>0.18</td>
    <td>0.18</td>
    <td>2.7</td>
    <td>170.3</td>
  </tr>
  <tr align="center">
    <td>128 Gbit/s</td>
    <td></td>
    <td>0.09</td>
    <td>0.09</td>
    <td>2.4</td>
    <td>152.8</td>
  </tr>
  <tr>
    <th colspan="6">Grid on 14 heterogeneous servers across Europe and North America <sup>2</sup></th>
  </tr>
  <tr align="center">
    <td colspan="2">Real world</td>
    <td>0.83</td>
    <td>0.79</td>
    <td>32.6</td>
    <td>179.4</td>
  </tr>
  <tr>
    <th colspan="6">Grid on 3 servers, with one A100 each <sup>3</sup></th>
  </tr>
  <tr align="center">
    <td>1 Gbit/s</td>
    <td>&lt; 5 ms</td>
    <td>1.71</td>
    <td>1.54</td>
    <td>70.0</td>
    <td>253.6</td>
  </tr>
  <tr align="center">
    <td>100 Mbit/s</td>
    <td>&lt; 5 ms</td>
    <td>1.66</td>
    <td>1.49</td>
    <td>56.4</td>
    <td>182.0</td>
  </tr>
  <tr align="center">
    <td>100 Mbit/s</td>
    <td>100 ms</td>
    <td>1.23</td>
    <td>1.11</td>
    <td>19.7</td>
    <td>112.2</td>
  </tr>
</table>

<sup>1</sup> **An upper bound for offloading performance.** We base our offloading numbers on the best possible hardware setup for offloading: CPU RAM offloading via PCIe 4.0 with 16 PCIe lanes per GPU and PCIe switches for pairs of GPUs. We assume zero latency for the upper bound estimation. In 8-bit, the model uses 1 GB of memory per billion parameters. PCIe 4.0 with 16 lanes has a throughput of 256 Gbit/s, so offloading 176B parameters takes 5.5 seconds. The throughput is twice as slow (128 Gbit/s) if we have two GPUs behind the same PCIe switch.

<sup>2</sup> **A real-world distributed setting** with 14 servers holding 2× RTX 3060, 4× 2080Ti, 2× 3090, 2× A4000, and 4× A5000 GPUs. These are personal servers and servers from university labs, spread across Europe and North America and connected to the Internet at speeds of 100–1000 Mbit/s. 4 servers operate from under firewalls.

<sup>3</sup> **An optimistic setup** that requires least communication. The client nodes have 8 CPU cores and no GPU.

We provide more evaluations and discuss these results in more detail in **Section 3.3** of our [paper](https://arxiv.org/pdf/2209.01188.pdf).

## 🛠️ Contributing

Please see our [FAQ](https://github.com/Agora-workshop/grid/wiki/FAQ:-Frequently-asked-questions#contributing) on contributing.


--------------------------------------------------------------------------------

<p align="center">
    This project is a part of the <a href="https://Agora.huggingface.co/">Agora</a> research workshop.
</p>
<p align="center">
    <img src="https://grid.dev/Agora.png" width="150">
</p>
