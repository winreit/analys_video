import argparse
from file_reader.reader import read_csv_files
from reports.registry import get_report_class


def main():
    parser = argparse.ArgumentParser(description='Анализ метрик YouTube видео')
    parser.add_argument('--files', nargs='+', required=True,
                        help='Пути к CSV файлам с данными')
    parser.add_argument('--report', required=True,
                        help='Название отчета (clickbait)')

    args = parser.parse_args()

    try:
        data = read_csv_files(args.files)
        report_class = get_report_class(args.report)
        report = report_class(data)
        result = report.generate()
        report.display(result)

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        exit(1)


if __name__ == '__main__':
    main()