* Как запустить в дебаггере?
  * https://fastapi.tiangolo.com/tutorial/debugging/#run-your-code-with-your-debugger
  * просто как отладка файла Python
  * важно, чтобы в main.py был uvicorn.run()
  
* Рекомендация перед работой - после создания venv внутри виртуальной среды обновить 
  * pip python -m pip install --upgrade pip
  
* Обновить requirements.txt можно командой: pip freeze > requirements.txt
  
* Создание vevn: 
    1. python -m venv venv
    2. venv\Scripts\activate
    ИЛИ через vs code:
        1. Ctrl+Shift+P
        2. env
        3. https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment
* Создание FastAPI прилы:
  * ``pip install fastapi uvicorn``
  * Пояснение:
    * fastapi - движок
    * uvicorn - сервер
* Запустить прилу:
  * python main.py
  * Сервис доступен по адресу http://127.0.0.1:8000
  * После этого сваггер будет доступен по адресу http://127.0.0.1:8000/docs

* Линтер flake8 и black formatter:
  * Сейчас нужно устанавливать Flake8 из маркета расширений и включать/или выключать для каждой рабочей области, а как настроить под себя я хз
  * Поэтому использую black formatter с настройками форматирования при сохранении файла (для рабочей области опять же)

* Для подключения базы:
  * pip install sqlalchemy databases pyodbc (для mssql)
  * 
  * 