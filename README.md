Получите github токен с правами админа.

Создайте файл .env в корне проекта:
```
USER='your github username'
TOKEN='your github token'
```

```bash
#Windows
git clone https://github.com/MixidFinder/EffMob-API.git
python -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
pytest

#Linux
git clone https://github.com/MixidFinder/EffMob-API.git
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
