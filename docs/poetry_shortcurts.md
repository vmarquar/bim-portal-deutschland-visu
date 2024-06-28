### Poetry Shortcuts and Commands

### Installation
- install pyenv to be able to switch between python versions
- add pyenv zsh commands
- deactivate conda base activation for every command line session
- install python interpreter `pyenv install 3.10`
- activate python version as global python version `pyenv global 3.10`
- install poetry into each python interpreter version if needed  `pip install poetry`

### Most Common Poetry Commands
0. Setup .venv inside current folder `poetry config virtualenvs.in-project true`
1. Create new Project `poetry new my-project-name`
2. Activate .venv `poetry shell`, to deactive `exit or deactivate`
3. Add new modules to the .venv `poetry add ifcopenshell`
4. Run your script inside poetry `poetry run python your_script.py`
5. Run your tests inside the venv using poetry `poetry run pytest`
6. Get info about the current .venv `poetry env info` or just `poetry env info --path` to obtain the python interpreter path
7. Add .venv to the VS Code Workspace `Shift + CMD + P: > Select interpreter` + add the interpreter path from Step 5