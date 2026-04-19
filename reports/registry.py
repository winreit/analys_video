from typing import Type
from reports.base_report import BaseReport
from reports.clickbait_report import ClickbaitReport

REPORT_REGISTRY = {
    'clickbait': ClickbaitReport,
}


def get_report_class(report_name: str) -> Type[BaseReport]:
    """Возвращает класс отчёта по его имени."""
    report_class = REPORT_REGISTRY.get(report_name)
    if report_class is None:
        raise ValueError(f"Неизвестный тип отчета: {report_name}")
    return report_class