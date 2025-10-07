# 🎯 Матрица распределения Interactive Sandboxes

## Цель документа
Этот документ описывает **куда, когда и зачем** вставлять интерактивные sandboxes в материалы курса.

---

## 📋 Принципы размещения

### 1. Quick Win Sandboxes (Level 0-1)
**Где:** Начало урока (первые 5-10 минут)
**Зачем:** Мгновенный результат → мотивация
**Сложность:** 1 строка кода для изменения
**Пример:**
```
# Исправь одну строку
age = "25"  # ❌ Сделай это числом!
assert type(age) == int
```

### 2. Concept Sandboxes (Level 2)
**Где:** После объяснения синтаксиса (КАК раздел)
**Зачем:** Закрепить понимание концепции
**Сложность:** 2-3 строки кода
**Пример:**
```
def greet(name):
    return ???  # Верни приветствие

assert greet("Alice") == "Hello, Alice!"
```

### 3. Practice Sandboxes (Level 4)
**Где:** Конец урока (практика)
**Зачем:** Проверка усвоения материала
**Сложность:** 5-10 строк кода (Faded Example: 50% готово)
**Пример:**
```
# Напиши функцию полностью
def calculate_total(prices):
    # Твой код здесь
    pass

assert calculate_total([10, 20, 30]) == 60
```

---

## 🗺️ Матрица: Python Core 1 (5 уроков)

### Lesson 01: Variables & Types

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Мотивация (текст) | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Fix Type | Quick Win | Исправь "25" → 25 (1 строка) | `lesson_01_sandbox_01_fix_type.html` |
| **Level 2: КАК** | ✅ Type Conversion | Concept | Преобразуй типы (2 строки) | `lesson_01_sandbox_02_type_conversion.html` |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Type Errors | Diagram | Типичные ошибки (визуально) | `python_core_01_diagram_4.mmd` |
| **Level 4: ПРАКТИКА** | ✅ Complex Types | Practice | Работа с int/float/str (5 строк) | `lesson_01_sandbox_03_practice.html` *(TODO)* |
| **Spaced Repetition** | — | — | Повтор Lesson 00 | — |

**Итого:** 2 sandboxes + 1 диаграмма

---

### Lesson 02: Conditions & Loops

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем нужны условия? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Fix If | Quick Win | Допиши `if age >= ???` (1 строка) | `lesson_02_sandbox_01_if_else.html` |
| **Level 2: КАК** | ✅ If/Elif/Else | Concept | Множественные условия (3 строки) | `lesson_02_sandbox_02_elif.html` *(TODO)* |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Control Flow | Diagram | Схема if/elif/else | `python_core_02_diagram_1.mmd` *(TODO)* |
| **Level 4: ПРАКТИКА** | ✅ For Loop | Practice | Напиши цикл for (5 строк) | `lesson_02_sandbox_03_for_loop.html` *(TODO)* |
| **Spaced Repetition** | — | — | Повтор Lesson 01 | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

### Lesson 03: Functions

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем нужны функции? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Return Value | Quick Win | Допиши `return a * b` (1 строка) | `lesson_03_sandbox_01_function.html` |
| **Level 2: КАК** | ✅ Function with Args | Concept | Параметры и возврат (3 строки) | `lesson_03_sandbox_02_args.html` *(TODO)* |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Function Flow | Diagram | Call → Execute → Return | `python_core_03_diagram_1.mmd` *(TODO)* |
| **Level 4: ПРАКТИКА** | ✅ Complex Function | Practice | Функция с условиями (7 строк) | `lesson_03_sandbox_03_practice.html` *(TODO)* |
| **Spaced Repetition** | — | — | Повтор Lesson 02 | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

### Lesson 04: Lists & Tuples

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем нужны списки? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Append & Index | Quick Win | `fruits.append()` + `fruits[0]` (2 строки) | `lesson_04_sandbox_01_lists.html` |
| **Level 2: КАК** | ✅ Slicing | Concept | Срезы списков (3 строки) | `lesson_04_sandbox_02_slicing.html` *(TODO)* |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: List Operations | Diagram | append/remove/slice визуально | `python_core_04_diagram_2.mmd` *(TODO)* |
| **Level 4: ПРАКТИКА** | ✅ List Comprehension | Practice | Фильтрация списка (5 строк) | `lesson_04_sandbox_03_practice.html` *(TODO)* |
| **Spaced Repetition** | — | — | Повтор Lesson 03 | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

### Lesson 05: Dicts & Sets

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем нужны словари? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Dict Keys | Quick Win | `user["city"] = "Moscow"` (2 строки) | `lesson_05_sandbox_01_dicts.html` |
| **Level 2: КАК** | ✅ Dict Methods | Concept | `.get()`, `.keys()`, `.values()` (3 строки) | `lesson_05_sandbox_02_methods.html` *(TODO)* |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Dict vs List | Diagram | Когда использовать dict, когда list | `python_core_05_diagram_1.mmd` *(TODO)* |
| **Level 4: ПРАКТИКА** | ✅ Nested Dicts | Practice | Работа с вложенными словарями (7 строк) | `lesson_05_sandbox_03_practice.html` *(TODO)* |
| **Spaced Repetition** | — | — | Повтор Lesson 04 | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

## 📊 Статистика Python Core 1

| Метрика | Значение |
|---------|----------|
| **Всего уроков** | 5 |
| **Sandboxes созданы** | 6 |
| **Sandboxes TODO** | 9 |
| **Всего sandboxes** | 15 |
| **Диаграммы TODO** | 5 |
| **Среднее sandboxes/урок** | 3 |

---

## 🎯 Правила для составления ТЗ ментору

### Шаблон ТЗ для Sandbox

```markdown
## Sandbox: [Название]

**Урок:** Lesson XX: [Тема]
**Раздел:** Level X (ЗАЧЕМ/ЧТО/КАК/ПРИМЕРЫ/ПРАКТИКА)
**Тип:** Quick Win / Concept / Practice
**Цель:** [Что студент должен научиться делать]

**Код (90% готов):**
```python
# [Комментарий что нужно сделать]
code here
```

**Expected Fixes:**
- Паттерн 1: `код` (тест: `assert выражение`)
- Паттерн 2: `код` (тест: `assert выражение`)

**Hints:**
- Подсказка 1
- Подсказка 2

**Success Message:** "[Мотивационное сообщение]"

**Файл:** `lesson_XX_sandbox_YY_название.html`
```

### Пример ТЗ (реальный)

```markdown
## Sandbox: Fix Type

**Урок:** Lesson 01: Variables & Types
**Раздел:** Level 1 (ЧТО)
**Тип:** Quick Win
**Цель:** Научиться различать строки и числа

**Код (90% готов):**
```python
name = "Alice"
age = "25"  # ❌ Должно быть число!
salary = "50000"  # ❌ Должно быть число!

assert type(name) == str
assert type(age) == int
assert type(salary) == int
```

**Expected Fixes:**
- `age = 25` (тест: `type(age) == int`)
- `salary = 50000` (тест: `type(salary) == int`)

**Hints:**
- Убери кавычки вокруг 25
- Убери кавычки вокруг 50000

**Success Message:** "🎉 Отлично! Теперь возраст и зарплата — это числа!"

**Файл:** `lesson_01_sandbox_01_fix_type.html`
```

---

## 🚀 Workflow для ментора

1. **Читает матрицу** → видит куда нужен sandbox
2. **Получает ТЗ** по шаблону выше
3. **Создаёт JSON конфиг** (по примеру готовых)
4. **Запускает генератор:**
   ```bash
   python sandbox-generator.py config.json output.html
   ```
5. **Тестирует** локально (открыть HTML в браузере)
6. **Коммитит** в репозиторий
7. **GitHub Pages деплоит** автоматически
8. **Вставляет iframe** в Skill Space:
   ```html
   <iframe
     src="https://septenal14.github.io/pytest-interactive-lessons/sandboxes/python_core_01/lesson_XX_sandbox_YY.html"
     width="100%"
     height="600px"
     frameborder="0">
   </iframe>
   ```

---

## 📁 Структура проекта

```
pytest-interactive-lessons/
├── configs/                          # JSON конфиги
│   ├── python_core_01/
│   │   ├── lesson_01_sandbox_01_fix_type.json ✅
│   │   ├── lesson_01_sandbox_02_type_conversion.json ✅
│   │   ├── lesson_02_sandbox_01_if_else.json ✅
│   │   ├── lesson_03_sandbox_01_function.json ✅
│   │   ├── lesson_04_sandbox_01_lists.json ✅
│   │   └── lesson_05_sandbox_01_dicts.json ✅
│   ├── pytest_basics/                # TODO
│   └── playwright/                   # TODO
├── sandboxes/                        # Сгенерированные HTML
│   └── python_core_01/
│       ├── lesson_01_sandbox_01_fix_type.html ✅
│       ├── lesson_01_sandbox_02_type_conversion.html ✅
│       ├── lesson_02_sandbox_01_if_else.json ✅
│       ├── lesson_03_sandbox_01_function.html ✅
│       ├── lesson_04_sandbox_01_lists.html ✅
│       └── lesson_05_sandbox_01_dicts.html ✅
├── sandbox-generator.py              # Генератор ✅
├── sandbox-split-screen.html         # Template (эталон) ✅
└── SANDBOX_MAPPING_MATRIX.md         # Этот документ ✅
```

---

## ✅ Чеклист интеграции Sandbox в урок

- [ ] Определён раздел урока (Level 0-4)
- [ ] Выбран тип (Quick Win / Concept / Practice)
- [ ] Создан JSON конфиг
- [ ] Сгенерирован HTML через `sandbox-generator.py`
- [ ] Протестирован локально
- [ ] Залит на GitHub Pages
- [ ] Добавлен iframe в Skill Space материал
- [ ] Проверена работоспособность в LMS
- [ ] Обновлена матрица (этот файл)

---

## 🎓 Следующие шаги

1. **Создать оставшиеся 9 sandboxes** для Python Core 1
2. **Создать конфиги для Pytest Basics** (5 уроков × 3 sandboxes = 15)
3. **Интегрировать Mermaid диаграммы** (ТОП-25 из предыдущего анализа)
4. **Обучить менторов** использовать sandbox-generator.py
5. **Собрать feedback** от студентов после первой итерации

---

**Последнее обновление:** 2025-10-08
**Статус:** 🟢 В работе (6/15 sandboxes готовы для Python Core 1)
