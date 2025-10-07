# Error Coverage Analysis: Python Core & Pytest Basics Interactive Sandboxes

**Дата анализа:** 2025-10-08
**Проанализировано файлов:** 9 конфигов (6 Python Core + 3 Pytest Basics)

---

## Методология анализа

Проверил все JSON конфиги в:
- `/Users/admin/Desktop/pytest-interactive-lessons/configs/python_core_01/` (6 файлов)
- `/Users/admin/Desktop/pytest-interactive-lessons/configs/pytest_basics/` (3 файла)

Искал паттерны критичных ошибок в полях `code` и `expected_fixes`.

---

## ✅ Покрыто (уже есть в sandboxes)

### Python Core 01

**1. TypeError (неявный) — type mismatch**
- **Файл:** `lesson_01_sandbox_01_fix_type.json`
- **Код:**
  ```python
  age = "25"  # ❌ Должно быть число!
  assert type(age) == int  # AssertionError из-за неправильного типа
  ```
- **Статус:** ✅ Покрыто через проверку типов (`type(age) == int`)
- **Урок:** Lesson 01 — Variables & Types

**2. AssertionError (частично) — базовые проверки**
- **Файл:** `lesson_01_sandbox_01_fix_type.json` + все остальные
- **Код:** Все sandboxes используют `assert` для проверок
- **Статус:** ✅ Покрыто базовое использование assert
- **НО:** ❌ НЕТ примеров assert БЕЗ сообщений (студенты не видят разницу)

**3. IndexError (потенциальный) — доступ к списку**
- **Файл:** `lesson_04_sandbox_01_lists.json`
- **Код:**
  ```python
  first = fruits[???]  # Студент должен написать fruits[0]
  ```
- **Статус:** ⚠️ ЧАСТИЧНО покрыто
- **Что НЕ хватает:** Нет примера выхода за границы списка `fruits[999]`

**4. KeyError (потенциальный) — доступ к словарю**
- **Файл:** `lesson_05_sandbox_01_dicts.json`
- **Код:**
  ```python
  name = user[???]  # Студент должен написать user["name"]
  ```
- **Статус:** ⚠️ ЧАСТИЧНО покрыто
- **Что НЕ хватает:** Нет примера обращения к несуществующему ключу `user["nonexistent"]`

### Pytest Basics

**5. AssertionError (в pytest контексте)**
- **Файл:** `pytest_01_sandbox_01_assert.json`
- **Код:**
  ```python
  assert result == ???  # Студент должен исправить
  ```
- **Статус:** ✅ Покрыто базовое использование assert в тестах

---

## ❌ НЕ покрыто (критичные ошибки отсутствуют)

### Python Core 01

**1. TypeError (явный) — str + int**
- **Описание:** `"Age: " + 25` → TypeError: can only concatenate str
- **Рекомендуемый урок:** Lesson 01 (Variables & Types)
- **Приоритет:** 🔥 ВЫСОКИЙ (самая частая ошибка новичков)
- **Пример sandbox:**
  ```python
  age = 25
  message = "Age: " + age  # ❌ TypeError!
  # Исправь: message = "Age: " + str(age)
  ```

**2. ZeroDivisionError**
- **Описание:** `10 / 0` → ZeroDivisionError
- **Рекомендуемый урок:** Lesson 03 (Functions) или Lesson 02 (Conditions)
- **Приоритет:** 🔥 ВЫСОКИЙ (частая ошибка в математических операциях)
- **Пример sandbox:**
  ```python
  def divide(a, b):
      return a / b

  result = divide(10, 0)  # ❌ ZeroDivisionError!
  # Исправь: проверь b != 0 перед делением
  ```

**3. IndexError (явный) — выход за границы**
- **Описание:** `fruits[999]` → IndexError: list index out of range
- **Рекомендуемый урок:** Lesson 04 (Lists)
- **Приоритет:** 🔥 ВЫСОКИЙ (частая ошибка при работе со списками)
- **Пример sandbox:**
  ```python
  fruits = ["apple", "banana"]
  last = fruits[5]  # ❌ IndexError!
  # Исправь: используй fruits[-1] или проверь len(fruits)
  ```

**4. KeyError (явный) — несуществующий ключ**
- **Описание:** `user["address"]` → KeyError: 'address'
- **Рекомендуемый урок:** Lesson 05 (Dicts)
- **Приоритет:** 🔥 ВЫСОКИЙ (частая ошибка при работе со словарями)
- **Пример sandbox:**
  ```python
  user = {"name": "Alice", "age": 25}
  city = user["city"]  # ❌ KeyError!
  # Исправь: используй user.get("city", "Unknown")
  ```

**5. NameError — неопределенная переменная**
- **Описание:** `print(undefined_var)` → NameError: name 'undefined_var' is not defined
- **Рекомендуемый урок:** Lesson 01 (Variables & Types)
- **Приоритет:** 🔥 ВЫСОКИЙ (очень частая ошибка новичков)
- **Пример sandbox:**
  ```python
  name = "Alice"
  print(nam)  # ❌ NameError! (опечатка)
  # Исправь: print(name)
  ```

**6. AttributeError — несуществующий метод/атрибут**
- **Описание:** `"hello".append()` → AttributeError
- **Рекомендуемый урок:** Lesson 04 (Lists) или отдельный урок по ООП
- **Приоритет:** 🟡 СРЕДНИЙ (ООП темы — в Advanced модулях)
- **Пример sandbox:**
  ```python
  text = "hello"
  text.append("!")  # ❌ AttributeError! (у строк нет метода append)
  # Исправь: text = text + "!"
  ```

**7. ValueError — неправильное значение**
- **Описание:** `int("abc")` → ValueError: invalid literal for int()
- **Рекомендуемый урок:** Lesson 01 (Variables & Types)
- **Приоритет:** 🔥 ВЫСОКИЙ (частая ошибка при конвертации)
- **Пример sandbox:**
  ```python
  age_str = "abc"
  age = int(age_str)  # ❌ ValueError!
  # Исправь: проверь что строка содержит только цифры
  ```

### Pytest Basics

**8. AssertionError БЕЗ сообщения**
- **Описание:** `assert x == 5` → AssertionError (без объяснения почему)
- **Рекомендуемый урок:** Pytest Lesson 01 или Lesson 05 (Assertions & Reports)
- **Приоритет:** 🔥 ВЫСОКИЙ (best practice для pytest)
- **Пример sandbox:**
  ```python
  def test_login():
      status = 401
      assert status == 200  # ❌ Плохо! Нет сообщения!
      # Исправь: assert status == 200, f"Expected 200, got {status}"
  ```

**9. Fixture scope issues**
- **Описание:** Неправильное понимание scope="function" vs "session"
- **Рекомендуемый урок:** Pytest Lesson 02 (Fixtures)
- **Приоритет:** 🟡 СРЕДНИЙ (Advanced тема)
- **Пример sandbox:**
  ```python
  @pytest.fixture(scope="session")  # ❌ Создаётся только раз!
  def user():
      return {"name": "Alice"}

  def test_modify_user(user):
      user["name"] = "Bob"  # Меняет для ВСЕХ тестов!
  ```

**10. Parametrize с неправильными типами**
- **Описание:** `@pytest.mark.parametrize("x", [1, "2", 3])` — разные типы
- **Рекомендуемый урок:** Pytest Lesson 03 (Parametrize)
- **Приоритет:** 🟡 СРЕДНИЙ
- **Пример sandbox:**
  ```python
  @pytest.mark.parametrize("number", [2, "3", 4])
  def test_square(number):
      assert number ** 2 == number * number  # ❌ TypeError на "3"!
  ```

---

## 💡 Рекомендации

### Приоритет 1 (критичные пробелы — создать СРОЧНО):

1. **TypeError (str + int)** → `python_core_01/lesson_01_sandbox_03_type_error.json`
   - **Почему:** Самая частая ошибка новичков (100% встречается в первую неделю)
   - **Сценарий:** "Age: " + 25 → "Age: " + str(25)

2. **NameError (undefined variable)** → `python_core_01/lesson_01_sandbox_04_name_error.json`
   - **Почему:** Вторая по частоте ошибка (опечатки в именах)
   - **Сценарий:** print(nam) → print(name)

3. **ZeroDivisionError** → `python_core_01/lesson_03_sandbox_02_zero_division.json`
   - **Почему:** Частая ошибка в математических задачах
   - **Сценарий:** return a / b → добавить проверку if b != 0

4. **IndexError (явный)** → `python_core_01/lesson_04_sandbox_02_index_error.json`
   - **Почему:** Частая ошибка при работе со списками
   - **Сценарий:** fruits[999] → fruits[-1] или len(fruits) проверка

5. **KeyError (явный)** → `python_core_01/lesson_05_sandbox_02_key_error.json`
   - **Почему:** Частая ошибка при работе со словарями
   - **Сценарий:** user["city"] → user.get("city", "Unknown")

6. **AssertionError БЕЗ сообщения** → `pytest_basics/pytest_01_sandbox_02_assert_message.json`
   - **Почему:** Best practice для pytest (обязательно для профессионалов)
   - **Сценарий:** assert x == 5 → assert x == 5, f"Expected 5, got {x}"

### Приоритет 2 (важные, но не критичные):

7. **ValueError (int conversion)** → `python_core_01/lesson_01_sandbox_05_value_error.json`
   - **Когда:** После освоения TypeError
   - **Сценарий:** int("abc") → проверка перед конвертацией

8. **AttributeError (wrong method)** → `python_core_01/lesson_04_sandbox_03_attribute_error.json`
   - **Когда:** После освоения базовых методов списков/строк
   - **Сценарий:** "hello".append() → "hello" + "!"

### Приоритет 3 (Advanced темы — для будущих модулей):

9. **Fixture scope issues** → `pytest_basics/pytest_02_sandbox_02_fixture_scope.json`
   - **Когда:** В модуле Pytest Advanced
   - **Требует:** Понимания областей видимости

10. **Parametrize type mismatch** → `pytest_basics/pytest_03_sandbox_02_param_types.json`
    - **Когда:** В модуле Pytest Advanced
    - **Требует:** Углублённого понимания parametrize

---

## 📊 Статистика покрытия

| Категория | Всего ошибок | Покрыто | НЕ покрыто | % покрытия |
|-----------|--------------|---------|------------|------------|
| **Python Core Errors** | 7 | 2 (частично) | 5 | ~29% |
| **Pytest Errors** | 3 | 1 (базово) | 2 | ~33% |
| **ИТОГО** | 10 | 3 | 7 | **30%** |

**Вывод:** 70% критичных ошибок НЕ покрыто интерактивными sandboxes!

---

## 🎯 План действий (Roadmap)

### Неделя 1: Критичные пробелы (Priority 1)
- [ ] Создать 6 новых sandboxes для Priority 1 ошибок
- [ ] Интегрировать их в существующие уроки
- [ ] Протестировать на реальных студентах

### Неделя 2: Важные дополнения (Priority 2)
- [ ] Создать 2 новых sandboxes для Priority 2 ошибок
- [ ] Добавить вариативность (разные сценарии одной ошибки)

### Неделя 3: Advanced темы (Priority 3)
- [ ] Отложить до модуля "Pytest Advanced"
- [ ] Создать отдельный урок "Common Pytest Pitfalls"

---

## 📝 Примечания

**Что уже работает хорошо:**
- ✅ Базовые проверки типов (type checking)
- ✅ Простые assertions в pytest
- ✅ Основные операции со списками/словарями

**Что требует улучшения:**
- ❌ Нет явных примеров runtime ошибок (TypeError, IndexError, KeyError)
- ❌ Нет обучения "как избежать ошибку" (defensive programming)
- ❌ Нет Best Practices для assertions (сообщения в assert)

**Философия sandboxes:**
Текущие sandboxes фокусируются на ПРАВИЛЬНОМ коде ("исправь и заработает").
Нужно добавить sandboxes с ОШИБКАМИ ("сломай, посмотри ошибку, исправь").

---

**Автор анализа:** Claude Agent
**Версия:** 1.0
**Следующий шаг:** Создание Priority 1 sandboxes (см. раздел "Приоритет 1")
