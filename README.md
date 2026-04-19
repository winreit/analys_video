1. Создайте виртуальное окружение и активируйте его:
  
   Для macOS/Linux
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```
   Для Windows
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```
   
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запуск проекта:
   ```bash
   python main.py --files csv_files/stats1.csv csv_files/stats2.csv --report clickbait
   ```

4. Запуск тестов:
   ```bash
   pytest tests/ -v   
   ```

   Скриншоты с примерами запуска тестов и запуска приложения в директории 'screenshots'
