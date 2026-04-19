import pytest
import tempfile
import os

from file_reader.reader import read_csv_files


def test_read_csv_files_success():
    """Тест успешного чтения CSV файлов."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as f:
        f.write("title,ctr,retention_rate,views,likes,avg_watch_time\n")
        f.write("Test video,18.2,35,45200,1240,4.2\n")
        temp_path = f.name

    try:
        data = read_csv_files([temp_path])
        assert len(data) == 1
        assert data[0]['title'] == "Test video"
        assert data[0]['ctr'] == 18.2
        assert data[0]['retention_rate'] == 35.0
        assert data[0]['views'] == 45200
        assert data[0]['likes'] == 1240
        assert data[0]['avg_watch_time'] == 4.2
    finally:
        os.unlink(temp_path)


def test_read_csv_files_not_found():
    """Тест обработки ошибки при отсутствии файла."""
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        read_csv_files(["nonexistent.csv"])


def test_read_csv_files_multiple():
    """Тест чтения нескольких файлов."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as f1:
        f1.write("title,ctr,retention_rate,views,likes,avg_watch_time\n")
        f1.write("Video 1,10.0,50,1000,100,5.0\n")
        path1 = f1.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as f2:
        f2.write("title,ctr,retention_rate,views,likes,avg_watch_time\n")
        f2.write("Video 2,20.0,30,2000,200,3.0\n")
        path2 = f2.name

    try:
        data = read_csv_files([path1, path2])
        assert len(data) == 2
        assert data[0]['title'] == "Video 1"
        assert data[1]['title'] == "Video 2"
    finally:
        os.unlink(path1)
        os.unlink(path2)