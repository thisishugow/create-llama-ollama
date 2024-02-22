import os, sys
from dotenv import load_dotenv

load_dotenv()




if __name__ == '__main__':
    conf_fp: os.PathLike|None = sys.argv[1] if len(sys.argv)>1 else None
    if conf_fp:
        os.environ['CREATE_LLAMA_APP_CONF'] = conf_fp
        print(f"Read config from { os.environ['CREATE_LLAMA_APP_CONF']}")
    else: 
        print('Use default settings from constants.py')

    import app
    from app.engine.generate import generate_datasource
    generate_datasource()