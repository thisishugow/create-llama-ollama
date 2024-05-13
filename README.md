This is a [LlamaIndex](https://www.llamaindex.ai/) project using [FastAPI](https://fastapi.tiangolo.com/) bootstrapped with [`create-llama`](https://github.com/run-llama/LlamaIndexTS/tree/main/packages/create-llama).

## Getting Started
### Quickstart
#### Option 1) Clone project and setup by yourself
```bash
git clone https://github.com/thisishugow/create-llama-ollama.git
cd create-llama-ollama
poetry install
```
Install Ollama([Guide](https://ollama.com)). 
```bash
# After Ollama is installed.
ollama pull llama3
ollama serve &
```

Start the app:
```bash
poetry install
poetry run ./backend/main.py -c config.json # you can make your configuration. 
```
Then visit [http://localhost:8080](http://localhost:8080) with your browser to see the result.

#### Optional 2) Docker container

```bash
docker run --name my-offline-llama -p 8080:8080 thisisyuwang/create-llama-ollama:latest

```
> ⚠️ WARNING: It will take minutes to download LLM at the first time.   

Then visit [http://localhost:8080](http://localhost:8080) with your browser to see the result.



### For Development
Startup the backend as described in the [backend README](./backend/README.md).

Second, run the development server of the frontend as described in the [frontend README](./frontend/README.md).

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

First, setup the environment:

```
poetry install
poetry shell
```

By default, we use the OpenAI LLM (though you can customize, see `app/context.py`). As a result you need to specify an `OPENAI_API_KEY` in an .env file in this directory.

Example `.env` file:

```
OPENAI_API_KEY=<openai_api_key>
```

Second, generate the embeddings of the documents in the `./data` directory (if this folder exists - otherwise, skip this step):

```
python app/engine/generate.py
```

Third, run the development server:

```
python main.py
```

Then call the API endpoint `/api/chat` to see the result:

```
curl --location 'localhost:8000/api/chat' \
--header 'Content-Type: application/json' \
--data '{ "messages": [{ "role": "user", "content": "Hello" }] }'
```

You can start editing the API by modifying `app/api/routers/chat.py`. The endpoint auto-updates as you save the file.

Open [http://localhost:8000/docs](http://localhost:8000/docs) with your browser to see the Swagger UI of the API.

The API allows CORS for all origins to simplify development. You can change this behavior by setting the `ENVIRONMENT` environment variable to `prod`:

```
ENVIRONMENT=prod uvicorn main:app
```

## Learn More

To learn more about LlamaIndex, take a look at the following resources:

- [LlamaIndex Documentation](https://docs.llamaindex.ai) - learn about LlamaIndex.
- [LlamaIndexTS Documentation](https://ts.llamaindex.ai) - learn about LlamaIndex (Typescript features).

You can check out [the LlamaIndex GitHub repository](https://github.com/run-llama/llama_index) - your feedback and contributions are welcome!
