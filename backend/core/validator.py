from pathlib import Path

def validate_dir():
    #create a directory if it doesn't exists
    Path('./img/').mkdir(parents=True, exist_ok=True)
