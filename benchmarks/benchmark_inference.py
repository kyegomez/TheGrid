#!/usr/bin/env python3

import argparse
import multiprocessing as mp
from time import perf_counter

import numpy as np
import torch
from hivemind.utils.logging import get_logger
from transformers import AutoTokenizer

from grid import AutoDistributedModelForCausalLM
from grid.constants import DTYPE_MAP, PUBLIC_INITIAL_PEERS

logger = get_logger()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="Agora/bloom")
    parser.add_argument("--initial_peers", type=str, nargs="+", default=PUBLIC_INITIAL_PEERS)
    parser.add_argument("--torch_dtype", type=str, default="bfloat16")
    parser.add_argument("--n_processes", type=str, default=1)
    parser.add_argument("--seq_len", type=int, default=2048)
    parser.add_argument("--warmup_steps", type=int, default=1)
    args = parser.parse_args()

    if args.n_processes == "n_gpus":
        args.n_processes = torch.cuda.device_count()
    else:
        args.n_processes = int(args.n_processes)

    processes = [mp.Process(target=benchmark_inference, args=(i, args)) for i in range(args.n_processes)]
    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()


@torch.inference_mode()
def benchmark_inference(process_idx, args):
    tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=False)
    # Using use_fast=False since LlamaTokenizerFast takes a long time to start, and we decode 1 token at a time anyway

    model = AutoDistributedModelForCausalLM.from_pretrained(
        args.model, initial_peers=args.initial_peers, torch_dtype=DTYPE_MAP[args.torch_dtype]
    )
    logger.info(f"Created model: {process_idx=} {model.device=}")

    result = ""
    step_times = []
    with model.transformer.h.inference_session(max_length=args.seq_len) as sess:
        for step in range(args.seq_len):
            start_time = perf_counter()

            outputs = model.generate(max_new_tokens=1, session=sess)
            result += tokenizer.decode(outputs[0])

            if step >= args.warmup_steps:
                step_times.append(perf_counter() - start_time)
                speed = 1 / np.mean(step_times)
                logger.info(f"{process_idx=} {step=} {speed=:.2f}")

    logger.info(f"Final result: {process_idx=} {speed=:.2f}")


if __name__ == "__main__":
    main()
