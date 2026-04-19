import pytest

from reports.clickbait_report import ClickbaitReport
from reports.registry import get_report_class, REPORT_REGISTRY


@pytest.fixture
def sample_data():
    return [
        {
            'title': 'Clickbait video',
            'ctr': 25.0,
            'retention_rate': 30.0,
            'views': 1000,
            'likes': 100,
            'avg_watch_time': 3.0
        },
        {
            'title': 'Normal video',
            'ctr': 10.0,
            'retention_rate': 60.0,
            'views': 2000,
            'likes': 200,
            'avg_watch_time': 6.0
        },
        {
            'title': 'Another clickbait',
            'ctr': 30.0,
            'retention_rate': 20.0,
            'views': 3000,
            'likes': 300,
            'avg_watch_time': 2.0
        },
        {
            'title': 'High CTR but good retention',
            'ctr': 20.0,
            'retention_rate': 50.0,
            'views': 1500,
            'likes': 150,
            'avg_watch_time': 5.0
        },
        {
            'title': 'Low retention but normal CTR',
            'ctr': 10.0,
            'retention_rate': 30.0,
            'views': 1200,
            'likes': 120,
            'avg_watch_time': 3.0
        }
    ]


def test_clickbait_report_generate(sample_data):
    """Тест генерации кликбейт отчёта."""
    report = ClickbaitReport(sample_data)
    result = report.generate()

    assert len(result) == 2
    assert result[0]['title'] == 'Another clickbait'
    assert result[0]['ctr'] == 30.0
    assert result[1]['title'] == 'Clickbait video'
    assert result[1]['ctr'] == 25.0


def test_clickbait_report_empty():
    """Тест пустого отчёта."""
    data = [
        {
            'title': 'Normal video',
            'ctr': 10.0,
            'retention_rate': 60.0,
            'views': 1000,
            'likes': 100,
            'avg_watch_time': 6.0
        }
    ]
    report = ClickbaitReport(data)
    result = report.generate()
    assert len(result) == 0


def test_get_report_class():
    """Тест получения класса отчёта по имени."""
    assert get_report_class('clickbait') == ClickbaitReport

    with pytest.raises(ValueError, match="Неизвестный тип отчета"):
        get_report_class('nonexistent')


def test_report_registry():
    """Тест наличия отчёта в реестре."""
    assert 'clickbait' in REPORT_REGISTRY
    assert REPORT_REGISTRY['clickbait'] == ClickbaitReport