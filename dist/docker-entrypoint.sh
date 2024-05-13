#!/usr/bin/env bash
cd /app
ollama serve &
ollama pull llama3
python3 main.py -c config.json