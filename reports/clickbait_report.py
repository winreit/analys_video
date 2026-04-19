from typing import List, Dict, Any
from reports.base_report import BaseReport


class ClickbaitReport(BaseReport):
    """Отчёт о кликбейтных видео.

    Кликбейтные видео — те, у которых CTR > 15% и удержание < 40%.
    """

    CTR_THRESHOLD = 15.0
    RETENTION_THRESHOLD = 40.0

    def generate(self) -> List[Dict[str, Any]]:
        """Генерирует список кликбейтных видео, отсортированный по убыванию CTR."""
        clickbait_videos = []

        for video in self.data:
            if video['ctr'] > self.CTR_THRESHOLD and video['retention_rate'] < self.RETENTION_THRESHOLD:
                clickbait_videos.append({
                    'title': video['title'],
                    'ctr': video['ctr'],
                    'retention_rate': video['retention_rate']
                })

        # Сортировка по убыванию CTR
        clickbait_videos.sort(key=lambda x: x['ctr'], reverse=True)

        return clickbait_videos