from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseReport(ABC):
    """Абстрактный базовый класс для всех отчётов."""

    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data

    @abstractmethod
    def generate(self) -> List[Dict[str, Any]]:
        """Генерирует данные для отчёта."""
        pass

    def display(self, result: List[Dict[str, Any]]) -> None:
        """Выводит отчёт в консоль."""
        if not result:
            print("Нет данных для отображения.")
            return

        try:
            from tabulate import tabulate
            print(tabulate(result, headers="keys", tablefmt="grid"))
        except ImportError:
            print("title,ctr,retention_rate")
            for row in result:
                print(f"{row['title']},{row['ctr']},{row['retention_rate']}")