import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:  %(message)s:')

proj_name = 'Wine_Quality'

list_of_files = [
    f'src/{proj_name}/__init__.py',
    f'src/{proj_name}/components/__init__.py',
    f'src/{proj_name}/utils/__init__.py',
    f'src/{proj_name}/utils/common.py',
    f'src/{proj_name}/config/__init__.y',
    f'src/{proj_name}/config/configuration.py',
    f'src/{proj_name}/pipeline/__init__.py',
    f'src/{proj_name}/entity/__init__.py',
    f'src/{proj_name}/entity/config_entity.py',
    f'src/{proj_name}/constant/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'    
]

for fpath in  list_of_files:
    filepath = Path(fpath)
    filedir, fname = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {fname}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'creating empty file: {filepath}')
        
    else:
        logging.info(f'{fname} already exists!')