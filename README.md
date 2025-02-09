# Photo Manager

Консольная утилита для управления фотографиями. Позволяет анализировать размеры файлов, переименовывать фотографии по дате создания и копировать фотографии между директориями.

## Действия

1. Клонируйте репозиторий:

```python
git clone https://github.com/amordasheva/CLI_and_testing_MIPT_project
cd CLI_and_testing_MIPT_project
```

2. Используйте приложение:

### Анализ директории

Команда "analyze" показывает размер каждого файла в указанной директории и общую статистику.

```python
cli.py analyze /path/to/directory
```

### Переименование фотографий

Команда "rename" переименовывает файлы в формат "Photo_date_ДД_ММ_ГГГГ_size_РАЗМЕР.расширение"

```python
cli.py rename /path/to/photos
```

### Копирование фотографий

Команда "copy" копирует все .jpg файлы из исходной директории в целевую.

```python
cli.py copy /path/to/source /path/to/target
```

## Справка по командам

Для получения справки по доступным командам:

```python
cli.py --help
```

Для получения справки по конкретной команде:

```python
python cli.py analyze --help
python cli.py rename --help
python cli.py copy --help
```
