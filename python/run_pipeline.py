from pathlib import Path
import subprocess,sys
B=Path(__file__).resolve().parent
for f in ['01_clean.py','02_abc.py','03_basket.py','04_layout.py']:subprocess.run([sys.executable,str(B/f)],check=True)
print('Pipeline completed.')
