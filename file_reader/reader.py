import csv
from typing import List, Dict, Any


def read_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    all_data = []

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['ctr'] = float(row['ctr'])
                    row['retention_rate'] = float(row['retention_rate'])
                    row['views'] = int(row['views'])
                    row['likes'] = int(row['likes'])
                    row['avg_watch_time'] = float(row['avg_watch_time'])
                    all_data.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        except Exception as e:
            raise Exception(f"Ошибка при чтении файла {file_path}: {str(e)}")

    return all_data