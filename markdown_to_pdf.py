import sys
from pathlib import Path
from markdown_pdf import MarkdownPdf, Section


def main():
    if len(sys.argv) != 2:
        print("Использование: python main.py <файл.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1])

    if not md_path.is_file():
        print(f"Ошибка: файл '{md_path}' не найден.")
        sys.exit(1)

    if md_path.suffix.lower() != '.md':
        print("Предупреждение: файл не имеет расширения .md, но продолжаем...")

    # Считываем содержимое
    try:
        content = md_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        sys.exit(1)

    # Генерируем PDF
    pdf = MarkdownPdf(toc_level=2, optimize=True)
    pdf.add_section(Section(content, toc=False))

    # Меняем расширение на .pdf
    pdf_path = md_path.with_suffix('.pdf')

    try:
        pdf.save(pdf_path)
        print(f"✅ Сохранено: {pdf_path}")
    except Exception as e:
        print(f"Ошибка сохранения PDF: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()