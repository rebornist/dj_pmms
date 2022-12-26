# 프로젝트 관리 프로그램 작성

## Settings

1. ctrl + shift + p > Open Settings (UI) > 작업영역 > 텍스트편집기 > Code Actions On Save
2. pipenv install flake8 --dev
3. pipenv install black --dev --pre
```py
 {
    "editor.defaultFormatter": "batisteo.vscode-django",
    "editor.formatOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.enabled": true,
    "python.formatting.provider": "black",
    "python.linting.banditArgs": ["--max-line-length=88"]
}
```
4. 현지시간 세팅
```py
from datetime import datetime

datetime.utcnow()
# UTC 기준 naive datetime : datetime.datetime(2021, 2, 20, 7, 54, 29, 275492)

datetime.now()
# 실행 환경 시간대 기준 naive datetime : datetime.datetime(2021, 2, 20, 16, 56, 32, 939155)

...


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

...
```
5. python manage.py createsuperuser