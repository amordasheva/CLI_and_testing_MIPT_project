import argparse
import sys
from feature_directory_analysis import analyze_directory
from feature_renaming import rename_photos
from feature_copying_files import copy_photos

def create_parser():
    parser = argparse.ArgumentParser(
        description="Photo Manager — утилита для работы с фотографиями",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
    
    # Анализ директории
    analyze_parser = subparsers.add_parser("analyze", help="Анализ размера файлов в директории")
    analyze_parser.add_argument("directory", help="Путь к директории для анализа")
    
    # Переименование файлов
    rename_parser = subparsers.add_parser("rename", help="Переименование файлов по дате создания и размеру")
    rename_parser.add_argument("directory", help="Путь к директории с файлами")
    
    # Копирование файлов
    copy_parser = subparsers.add_parser("copy", help="Копирование .jpg файлов из одной директории в другую")
    copy_parser.add_argument("source", help="Путь к исходной директории")
    copy_parser.add_argument("target", help="Путь к целевой директории")
    
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.command == "analyze":
            results = analyze_directory(args.directory)
            total_size = sum(size for _, size in results)
            
            for file, size in sorted(results, key=lambda x: x[1], reverse=True):
                print(f"{file}: {size} бит")
            print(f"\nОбщий размер директории: {total_size} бит")
            print(f"Количество файлов: {len(results)}")
            
        elif args.command == "rename":
            rename_photos(args.directory)
            print("Файлы переименованы")
            
        elif args.command == "copy":
            copy_photos(args.source, args.target)
            print("Фотографии скопированы")

    except Exception as e:
        print(f"Ошибка: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()