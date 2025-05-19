import flet as ft
import os
from CLI_and_testing_MIPT_project.feature_directory_analysis import analyze_directory
from CLI_and_testing_MIPT_project.feature_renaming import rename_photos
from CLI_and_testing_MIPT_project.feature_copying_files import copy_photos

def main(page: ft.Page):
    page.title = "Photo Manager"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 800
    page.window_height = 600
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    results_container = ft.Container(
        content=ft.Column(scroll=ft.ScrollMode.AUTO),
        border=ft.border.all(1, ft.colors.OUTLINE),
        border_radius=10,
        padding=10,
        expand=True
    )

    def pick_directory(e: ft.FilePickerResultEvent):
        if e.path:
            directory_path.value = e.path
            page.update()

    def pick_source_directory(e: ft.FilePickerResultEvent):
        if e.path:
            source_path.value = e.path
            page.update()

    def pick_target_directory(e: ft.FilePickerResultEvent):
        if e.path:
            target_path.value = e.path
            page.update()

    directory_picker = ft.FilePicker(
        on_result=pick_directory
    )
    source_picker = ft.FilePicker(
        on_result=pick_source_directory
    )
    target_picker = ft.FilePicker(
        on_result=pick_target_directory
    )
    page.overlay.extend([directory_picker, source_picker, target_picker])

    directory_path = ft.TextField(
        label="Путь к директории",
        read_only=True,
        expand=True,
        tooltip="Путь к выбранной директории"
    )
    source_path = ft.TextField(
        label="Исходная директория",
        read_only=True,
        expand=True,
        tooltip="Путь к исходной директории"
    )
    target_path = ft.TextField(
        label="Целевая директория",
        read_only=True,
        expand=True,
        tooltip="Путь к целевой директории"
    )

    def analyze_clicked(e):
        if not directory_path.value:
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Пожалуйста, выберите директорию")))
            return

        try:
            results = analyze_directory(directory_path.value)
            total_size = sum(size for _, size in results)
            
            results_container.content.controls.clear()
            results_container.content.controls.append(
                ft.Text("Результаты анализа:", size=20, weight=ft.FontWeight.BOLD)
            )
            
            for file, size in sorted(results, key=lambda x: x[1], reverse=True):
                results_container.content.controls.append(
                    ft.Text(f"{file}: {size} бит")
                )
            
            results_container.content.controls.append(
                ft.Text(f"\nОбщий размер директории: {total_size} бит")
            )
            results_container.content.controls.append(
                ft.Text(f"Количество файлов: {len(results)}")
            )
            
            page.update()
        except Exception as e:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Ошибка: {str(e)}")))

    def rename_clicked(e):
        if not directory_path.value:
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Пожалуйста, выберите директорию")))
            return

        try:
            rename_photos(directory_path.value)
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Файлы успешно переименованы")))
        except Exception as e:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Ошибка: {str(e)}")))

    def copy_clicked(e):
        if not source_path.value or not target_path.value:
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Пожалуйста, выберите обе директории")))
            return

        try:
            copy_photos(source_path.value, target_path.value)
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Фотографии успешно скопированы")))
        except Exception as e:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Ошибка: {str(e)}")))

    page.add(
        ft.Text("Photo Manager", size=30, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        
        ft.Container(
            content=ft.Column([
                ft.Text("Анализ директории", size=20, weight=ft.FontWeight.BOLD),
                ft.Row([
                    directory_path,
                    ft.IconButton(
                        icon=ft.icons.FOLDER_OPEN,
                        tooltip="Выбрать директорию",
                        on_click=lambda _: directory_picker.get_directory_path()
                    ),
                ]),
                ft.ElevatedButton(
                    "Анализировать",
                    icon=ft.icons.ANALYTICS,
                    on_click=analyze_clicked
                ),
            ]),
            padding=10,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=10,
            margin=ft.margin.only(bottom=20)
        ),
        
        ft.Container(
            content=ft.Column([
                ft.Text("Переименование файлов", size=20, weight=ft.FontWeight.BOLD),
                ft.Row([
                    directory_path,
                    ft.IconButton(
                        icon=ft.icons.FOLDER_OPEN,
                        tooltip="Выбрать директорию",
                        on_click=lambda _: directory_picker.get_directory_path()
                    ),
                ]),
                ft.ElevatedButton(
                    "Переименовать",
                    icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE,
                    on_click=rename_clicked
                ),
            ]),
            padding=10,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=10,
            margin=ft.margin.only(bottom=20)
        ),
        
        ft.Container(
            content=ft.Column([
                ft.Text("Копирование фотографий", size=20, weight=ft.FontWeight.BOLD),
                ft.Row([
                    source_path,
                    ft.IconButton(
                        icon=ft.icons.FOLDER_OPEN,
                        tooltip="Выбрать исходную директорию",
                        on_click=lambda _: source_picker.get_directory_path()
                    ),
                ]),
                ft.Row([
                    target_path,
                    ft.IconButton(
                        icon=ft.icons.FOLDER_OPEN,
                        tooltip="Выбрать целевую директорию",
                        on_click=lambda _: target_picker.get_directory_path()
                    ),
                ]),
                ft.ElevatedButton(
                    "Копировать",
                    icon=ft.icons.COPY,
                    on_click=copy_clicked
                ),
            ]),
            padding=10,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=10,
            margin=ft.margin.only(bottom=20)
        ),
        
        ft.Text("Результаты:", size=20, weight=ft.FontWeight.BOLD),
        results_container,
    )

ft.app(target=main) 