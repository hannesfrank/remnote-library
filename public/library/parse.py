import json
from pathlib import Path
from glob import glob

public = Path('public')
screenshots = glob(str(public / 'library/*.png'))
data = {}

for s in screenshots:
    p = Path(s)
    name = p.stem
    data[name] = {
        'name': name,
        'categories': [],
        'stars': 42,
        'installed': False,
        
        'thumb': p.relative_to(public).as_posix(),
    }
with open('data.json', 'w') as f:
    json.dump(data, f)