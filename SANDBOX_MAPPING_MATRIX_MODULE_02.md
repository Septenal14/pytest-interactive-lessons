# 🎯 Матрица распределения Interactive Sandboxes — Модуль 2

## Модуль 2: Pytest Basics (5 уроков)

---

### Раздел 3: Pytest Basics

**Особенность:** Sandboxes работают для **pytest синтаксиса**, но НЕ для реальных API запросов.

**Что работает:**
- ✅ Pytest assertions (`assert`, `pytest.raises`)
- ✅ Fixtures (scope, setup/teardown)
- ✅ Parametrize (@pytest.mark.parametrize)
- ✅ Markers (@pytest.mark.smoke)
- ✅ Простые функции (без внешних библиотек)

**Что НЕ работает:**
- ❌ Реальные HTTP запросы (requests/httpx)
- ❌ Mock responses (нужен полноценный Python)
- ❌ Работа с БД

**Решение:** Используем **mock данные** и фокусируемся на **pytest синтаксисе**.

---

## 🗺️ Матрица: Pytest Basics (5 уроков)

### Lesson 01: Pytest Introduction

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем нужен pytest? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ First Assert | Quick Win | Исправь `assert 2 + 2 == ???` (1 строка) | `pytest_01_sandbox_01_assert.html` |
| **Level 2: КАК** | ✅ Assert Messages | Concept | Добавь сообщения в assert (2 строки) | `pytest_01_sandbox_02_messages.html` |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Test Flow | Diagram | Arrange → Act → Assert | `pytest_basics_01_diagram_1.mmd` |
| **Level 4: ПРАКТИКА** | ✅ Multiple Asserts | Practice | Напиши 3 assertion (5 строк) | `pytest_01_sandbox_03_practice.html` |
| **Spaced Repetition** | — | — | Повтор Python Core | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

### Lesson 02: Fixtures (Setup/Teardown)

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем нужны fixtures? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Simple Fixture | Quick Win | Допиши `@pytest.fixture` (1 строка) | `pytest_02_sandbox_01_fixture.html` |
| **Level 2: КАК** | ✅ Fixture Scope | Concept | Исправь scope (function/module/session) | `pytest_02_sandbox_02_scope.html` |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Fixture Lifecycle | Diagram | Setup → Test → Teardown | `pytest_basics_02_diagram_2.mmd` |
| **Level 4: ПРАКТИКА** | ✅ Yield Fixture | Practice | Напиши fixture с yield (7 строк) | `pytest_02_sandbox_03_yield.html` |
| **Spaced Repetition** | — | — | Повтор Lesson 01 | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

### Lesson 03: Parametrize (Data-Driven Tests)

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем parametrize? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Parametrize Syntax | Quick Win | Исправь декоратор (1 строка) | `pytest_03_sandbox_01_parametrize.html` |
| **Level 2: КАК** | ✅ Multiple Params | Concept | Добавь 2-й параметр (3 строки) | `pytest_03_sandbox_02_multi_params.html` |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Parametrize Flow | Diagram | 1 тест → 3 прогона | `pytest_basics_03_diagram_1.mmd` |
| **Level 4: ПРАКТИКА** | ✅ Parametrize Test | Practice | Напиши parametrize тест (8 строк) | `pytest_03_sandbox_03_practice.html` |
| **Spaced Repetition** | — | — | Повтор Lesson 02 | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

### Lesson 04: Markers (Grouping Tests)

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем markers? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Smoke Marker | Quick Win | Добавь `@pytest.mark.smoke` (1 строка) | `pytest_04_sandbox_01_marker.html` |
| **Level 2: КАК** | ✅ Custom Markers | Concept | Создай custom marker в pytest.ini (3 строки) | `pytest_04_sandbox_02_custom.html` |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Marker Groups | Diagram | smoke/regression/critical | `pytest_basics_04_diagram_1.mmd` |
| **Level 4: ПРАКТИКА** | ✅ Skip/Xfail | Practice | Используй skip и xfail (5 строк) | `pytest_04_sandbox_03_skip.html` |
| **Spaced Repetition** | — | — | Повтор Lesson 03 | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

### Lesson 05: Assertions & Reports

| Раздел урока | Sandbox | Тип | Цель | Файл |
|-------------|---------|-----|------|------|
| **Level 0: ЗАЧЕМ** | — | — | Зачем продвинутые assertions? | — |
| **Level 1: ЧТО (Quick Win)** | ✅ Pytest Raises | Quick Win | Исправь `pytest.raises(???)` (1 строка) | `pytest_05_sandbox_01_raises.html` |
| **Level 2: КАК** | ✅ Approx | Concept | Используй pytest.approx для float (2 строки) | `pytest_05_sandbox_02_approx.html` |
| **Level 3: ПРИМЕРЫ** | 📊 Mermaid: Assertion Types | Diagram | assert vs raises vs approx | `pytest_basics_05_diagram_1.mmd` |
| **Level 4: ПРАКТИКА** | ✅ Custom Assertions | Practice | Напиши helper для assertions (8 строк) | `pytest_05_sandbox_03_practice.html` |
| **Spaced Repetition** | — | — | Повтор Lesson 04 | — |

**Итого:** 3 sandboxes + 1 диаграмма

---

## 📊 Статистика Pytest Basics

| Метрика | Значение |
|---------|----------|
| **Всего уроков** | 5 |
| **Sandboxes TODO** | 15 |
| **Диаграммы TODO** | 5 |
| **Среднее sandboxes/урок** | 3 |

---

## 🚫 Что НЕ делаем в sandboxes для API части

**API тесты требуют:**
- Реальные HTTP библиотеки (requests, httpx)
- Mock/stub инфраструктуру (responses, httpretty)
- Реальные endpoints или Docker контейнеры

**Альтернатива для API части:**
- ✅ **Диаграммы Mermaid** (Request → Response flow)
- ✅ **Текстовые примеры** с копируемым кодом
- ✅ **Домашнее предложение** (репозиторий с готовым API)
- ✅ **Видео демонстрации** (Loom screencast)

---

## 💡 Примеры Mock данных для Pytest sandboxes

### Пример 1: Mock Response (для обучения assertions)
```python
# Sandbox: Проверь mock response
mock_response = {
    "status_code": 200,
    "json": {"user_id": 123, "name": "Alice"}
}

# Допиши assertions
assert mock_response["status_code"] == ???
assert mock_response["json"]["user_id"] == ???
```

### Пример 2: Fixture для mock API client
```python
# Sandbox: Исправь fixture
@pytest.fixture
def api_client():
    class MockClient:
        def get(self, url):
            return {"status": "ok"}
    return ???  # Верни экземпляр MockClient

def test_api(api_client):
    response = api_client.get("/users")
    assert response["status"] == "ok"
```

---

## 🎓 Workflow для Модуля 2

### Pytest Basics (Lessons 1-5)
1. **Используем sandboxes** как для Python Core
2. **Фокус на pytest синтаксисе**, не на API
3. **Mock данные** для демонстрации assertions

### API Testing (будущее расширение)
1. **Диаграммы** для визуализации HTTP flow
2. **Копируемые примеры** кода
3. **GitLab репозиторий** с готовым API для практики
4. **Видео демонстрации** реальных запросов

---

## 📁 Структура проекта (обновлённая)

```
pytest-interactive-lessons/
├── configs/
│   ├── python_core_01/               ✅ 6 конфигов готовы
│   └── pytest_basics/                🔄 TODO: 15 конфигов
├── sandboxes/
│   ├── python_core_01/               ✅ 6 HTML готовы
│   └── pytest_basics/                🔄 TODO: 15 HTML
├── sandbox-generator.py              ✅ Готов
└── SANDBOX_MAPPING_MATRIX_MODULE_02.md ✅ Этот документ
```

---

## ✅ Чеклист для Pytest Basics

- [ ] Создать 15 JSON конфигов (по 3 на урок)
- [ ] Сгенерировать 15 HTML sandboxes
- [ ] Создать 5 Mermaid диаграмм
- [ ] Протестировать все sandboxes
- [ ] Залить на GitHub Pages
- [ ] Интегрировать в Skill Space
- [ ] Собрать feedback от студентов

---

## 🚀 Следующие шаги

1. **Создать configs для Pytest Basics** (15 JSON файлов)
2. **Batch генерация** через `sandbox-generator.py --batch`
3. **Интеграция с Python Core матрицей** (единый документ)
4. **Обучить менторов** создавать pytest sandboxes

---

**Последнее обновление:** 2025-10-08
**Статус:** 🟡 Планирование (0/15 sandboxes для Pytest Basics)
