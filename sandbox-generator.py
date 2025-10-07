#!/usr/bin/env python3
"""
Sandbox Generator - создаёт интерактивные HTML sandboxes из JSON конфигов

Использование:
    python sandbox-generator.py config.json output.html
    python sandbox-generator.py --batch configs/ output_dir/

Формат JSON конфига:
{
    "title": "Variables & Types: Исправь тип",
    "lesson": "python_core_01",
    "code": "name = \"John\"\\nage = \"25\"  # Исправь!\\n\\nassert type(age) == int",
    "expected_fixes": [
        {"pattern": "age = 25", "test": "type(age) == int"}
    ],
    "hints": ["Возраст должен быть число, не строка"],
    "success_message": "Отлично! Теперь age — это число!"
}
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any

TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: transparent;
            padding: 0;
            overflow: hidden;
        }}

        .sandbox-container {{
            background: #1e1e1e;
            border-radius: 8px;
            overflow: hidden;
            height: 600px;
            display: flex;
            flex-direction: column;
        }}

        .sandbox-header {{
            background: #2d2d2d;
            padding: 10px 15px;
            padding-right: 80px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-shrink: 0;
        }}

        .sandbox-title {{
            font-weight: bold;
            font-size: 14px;
        }}

        .run-button {{
            background: #4caf50;
            color: white;
            border: none;
            padding: 7px 12px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 13px;
            font-weight: bold;
            transition: background 0.3s;
        }}

        .run-button:hover {{
            background: #45a049;
        }}

        .split-container {{
            display: flex;
            flex: 1;
            overflow: hidden;
            position: relative;
        }}

        .editor-panel {{
            width: 55%;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        .resizer {{
            width: 5px;
            background: #444;
            cursor: col-resize;
            flex-shrink: 0;
            transition: background 0.2s;
        }}

        .resizer:hover {{
            background: #4caf50;
        }}

        .resizer.resizing {{
            background: #4caf50;
        }}

        .output-panel {{
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        .panel-header {{
            background: #252525;
            color: #888;
            padding: 6px 12px;
            font-size: 11px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 1px solid #444;
        }}

        #editor {{
            flex: 1;
        }}

        #output {{
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 12px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            overflow-y: auto;
            white-space: pre-wrap;
            flex: 1;
        }}

        .output-success {{ color: #4caf50; }}
        .output-error {{ color: #f44336; }}
        .output-info {{ color: #2196F3; }}
    </style>
</head>
<body>
    <div class="sandbox-container">
        <div class="sandbox-header">
            <span class="sandbox-title">🐍 {title}</span>
            <button class="run-button" onclick="runCode()">▶️ Запустить</button>
        </div>
        <div class="split-container" id="splitContainer">
            <div class="editor-panel" id="editorPanel">
                <div class="panel-header">📝 Код</div>
                <div id="editor"></div>
            </div>
            <div class="resizer" id="resizer"></div>
            <div class="output-panel">
                <div class="panel-header">📊 Результат</div>
                <div id="output"><span class="output-info">💡 Нажми "▶️ Запустить" чтобы увидеть результат</span></div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs/loader.js"></script>
    <script>
        let editor;

        const defaultCode = `{code}`;

        const expectedFixes = {expected_fixes_json};
        const hints = {hints_json};
        const successMessage = "{success_message}";

        require.config({{ paths: {{ vs: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs' }} }});

        require(['vs/editor/editor.main'], function() {{
            editor = monaco.editor.create(document.getElementById('editor'), {{
                value: defaultCode,
                language: 'python',
                theme: 'vs-dark',
                fontSize: 13,
                minimap: {{ enabled: false }},
                scrollBeyondLastLine: false,
                automaticLayout: true,
                lineNumbers: 'on'
            }});
        }});

        // Resizable logic
        const resizer = document.getElementById('resizer');
        const editorPanel = document.getElementById('editorPanel');
        const splitContainer = document.getElementById('splitContainer');

        let isResizing = false;

        resizer.addEventListener('mousedown', (e) => {{
            isResizing = true;
            resizer.classList.add('resizing');
            document.body.style.cursor = 'col-resize';
            document.body.style.userSelect = 'none';
        }});

        document.addEventListener('mousemove', (e) => {{
            if (!isResizing) return;

            const containerRect = splitContainer.getBoundingClientRect();
            const newWidth = ((e.clientX - containerRect.left) / containerRect.width) * 100;

            if (newWidth > 20 && newWidth < 80) {{
                editorPanel.style.width = newWidth + '%';
            }}
        }});

        document.addEventListener('mouseup', () => {{
            if (isResizing) {{
                isResizing = false;
                resizer.classList.remove('resizing');
                document.body.style.cursor = '';
                document.body.style.userSelect = '';
            }}
        }});

        function runCode() {{
            const output = document.getElementById('output');
            const code = editor.getValue();

            output.innerHTML = '<span class="output-info">🚀 Проверяем код...</span>\\n\\n';

            setTimeout(() => {{
                let result = '';
                let allPassed = true;

                // Check each expected fix
                expectedFixes.forEach((fix, index) => {{
                    const testPassed = code.includes(fix.pattern);

                    if (testPassed) {{
                        result += `<span class="output-success">✅ Тест ${{index + 1}} PASSED</span>\\n`;
                    }} else {{
                        result += `<span class="output-error">❌ Тест ${{index + 1}} FAILED</span>\\n`;
                        if (hints[index]) {{
                            result += `<span class="output-info">   💡 Подсказка: ${{hints[index]}}</span>\\n`;
                        }}
                        allPassed = false;
                    }}
                }});

                result += '\\n<span class="output-info">━━━━━━━━━━━━━━━━━━━━━━</span>\\n';

                if (allPassed) {{
                    result += `<span class="output-success">🎉 ${{successMessage}}</span>`;
                }} else {{
                    const passed = expectedFixes.filter((fix) => code.includes(fix.pattern)).length;
                    result += `<span class="output-info">✅ ${{passed}}/${{expectedFixes.length}} passed</span>`;
                }}

                output.innerHTML = result;
            }}, 300);
        }}
    </script>
</body>
</html>
"""


def generate_sandbox(config: Dict[str, Any], output_path: Path) -> None:
    """Генерирует HTML sandbox из JSON конфига"""

    # Escape code for JavaScript string
    code = config['code'].replace('`', '\\`').replace('\\n', '\n')

    # Convert expected fixes and hints to JSON
    expected_fixes_json = json.dumps(config.get('expected_fixes', []))
    hints_json = json.dumps(config.get('hints', []))

    # Generate HTML
    html = TEMPLATE.format(
        title=config.get('title', 'Pytest Sandbox'),
        code=code,
        expected_fixes_json=expected_fixes_json,
        hints_json=hints_json,
        success_message=config.get('success_message', 'Отлично! Все тесты прошли!')
    )

    # Write to file
    output_path.write_text(html, encoding='utf-8')
    print(f"✅ Создан sandbox: {output_path}")


def generate_batch(config_dir: Path, output_dir: Path) -> None:
    """Генерирует все sandboxes из папки с конфигами"""

    output_dir.mkdir(parents=True, exist_ok=True)

    config_files = sorted(config_dir.glob('*.json'))

    if not config_files:
        print(f"❌ Не найдено JSON файлов в {config_dir}")
        return

    print(f"📦 Найдено {len(config_files)} конфигов")

    for config_file in config_files:
        try:
            config = json.loads(config_file.read_text(encoding='utf-8'))
            output_file = output_dir / f"{config_file.stem}.html"
            generate_sandbox(config, output_file)
        except Exception as e:
            print(f"❌ Ошибка в {config_file}: {e}")

    print(f"\n✅ Готово! Создано {len(config_files)} sandboxes в {output_dir}")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        print("\nПримеры:")
        print("  python sandbox-generator.py config.json output.html")
        print("  python sandbox-generator.py --batch configs/ sandboxes/")
        sys.exit(1)

    if sys.argv[1] == '--batch':
        config_dir = Path(sys.argv[2])
        output_dir = Path(sys.argv[3]) if len(sys.argv) > 3 else Path('sandboxes')
        generate_batch(config_dir, output_dir)
    else:
        config_path = Path(sys.argv[1])
        output_path = Path(sys.argv[2])

        if not config_path.exists():
            print(f"❌ Файл не найден: {config_path}")
            sys.exit(1)

        config = json.loads(config_path.read_text(encoding='utf-8'))
        generate_sandbox(config, output_path)


if __name__ == '__main__':
    main()
