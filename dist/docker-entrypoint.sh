#!/usr/bin/env bash
cd /app/backend
ollama serve &
ollama pull llama3
python3 main.py -c config.json