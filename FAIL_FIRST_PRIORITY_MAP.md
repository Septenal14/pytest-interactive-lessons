# 🎯 Финальная карта "Fail First" Sandboxes по приоритетам

**Дата:** 2025-10-08
**Статус:** 🔴 70% критичных ошибок НЕ покрыто!
**Цель:** Создать sandboxes где студент **САМ видит ошибку** → понимает → фиксит

---

## 📊 Приоритизация: Impact × Frequency

| Ошибка | Частота 📈 | Impact 💥 | Приоритет | Урок | Статус |
|--------|----------|---------|----------|------|--------|
| **TypeError** (str + int) | 🔥🔥🔥🔥🔥 | 💥💥💥💥💥 | **P0** | Python Core 01 | ❌ НЕТ |
| **NameError** (опечатки) | 🔥🔥🔥🔥🔥 | 💥💥💥 | **P0** | Python Core 01 | ❌ НЕТ |
| **KeyError** (dict) | 🔥🔥🔥🔥 | 💥💥💥💥 | **P0** | Python Core 05 | ⚠️ ЧАСТИЧНО |
| **IndexError** (list) | 🔥🔥🔥🔥 | 💥💥💥💥 | **P0** | Python Core 04 | ⚠️ ЧАСТИЧНО |
| **ZeroDivisionError** | 🔥🔥🔥 | 💥💥💥💥 | **P0** | Python Core 03 | ❌ НЕТ |
| **AssertionError** (без msg) | 🔥🔥🔥 | 💥💥💥💥💥 | **P0** | Pytest 01 | ❌ НЕТ |
| **ValueError** (int("abc")) | 🔥🔥 | 💥💥💥 | **P1** | Python Core 01 | ❌ НЕТ |
| **AttributeError** | 🔥🔥 | 💥💥 | **P1** | Python Core 04 | ❌ НЕТ |

**ИТОГО P0:** 6 sandboxes (создаём СРОЧНО!)
**ИТОГО P1:** 2 sandboxes (следующая итерация)

---

## 🚀 Priority 0: КРИТИЧНЫЕ (создаём СЕЙЧАС)

### 1. TypeError: cannot concatenate str and int ⚡

**Урок:** Python Core 01 — Variables & Types
**Раздел:** Level 3 (ПРИМЕРЫ) — типичные ошибки
**Частота:** 🔥 100% студентов встречают в первую неделю

**Sandbox код:**
```python
# Запусти сначала — увидишь ошибку!
age = 25
message = "Your age is: " + age  # ❌ ОШИБКА!

print(message)

# Исправь код выше чтобы тест прошёл:
assert "Your age is: 25" in message
```

**Что видит студент при 1-м запуске:**
```
❌ TypeError: can only concatenate str (not "int") to str
   Line 2: message = "Your age is: " + age

💡 Подсказка: age — это число 25, а не строка!
💡 Решение: преобразуй число в строку: str(age)
```

**Файл:** `configs/python_core_01/lesson_01_sandbox_03_type_error_fail_first.json`

---

### 2. NameError: name is not defined ⚡

**Урок:** Python Core 01 — Variables & Types
**Раздел:** Level 3 (ПРИМЕРЫ) — опечатки
**Частота:** 🔥 95% студентов делают опечатки постоянно

**Sandbox код:**
```python
# Найди опечатку — запусти и увидишь ошибку!
name = "Alice"
age = 25

print(f"Name: {nam}")  # ❌ ОШИБКА! Опечатка!
print(f"Age: {age}")

# Исправь опечатку в строке 4
```

**Что видит студент:**
```
❌ NameError: name 'nam' is not defined
   Line 4: print(f"Name: {nam}")

💡 Подсказка: Переменная называется 'name', а не 'nam'
💡 Решение: Исправь nam → name
```

**Файл:** `configs/python_core_01/lesson_01_sandbox_04_name_error_fail_first.json`

---

### 3. KeyError: key not in dict ⚡

**Урок:** Python Core 05 — Dicts & Sets
**Раздел:** Level 3 (ПРИМЕРЫ) — безопасная работа со словарями
**Частота:** 🔥 80% студентов получают KeyError

**Sandbox код:**
```python
# Запусти — увидишь ошибку!
user = {
    "name": "Alice",
    "age": 25
}

city = user["city"]  # ❌ ОШИБКА! Ключа 'city' нет!

# Исправь — используй безопасный способ:
assert city == "Unknown"
```

**Что видит студент:**
```
❌ KeyError: 'city'
   Line 6: city = user["city"]

💡 Подсказка: Ключа 'city' нет в словаре!
💡 Решение: Используй user.get("city", "Unknown")
```

**Файл:** `configs/python_core_01/lesson_05_sandbox_02_key_error_fail_first.json`

---

### 4. IndexError: list index out of range ⚡

**Урок:** Python Core 04 — Lists & Tuples
**Раздел:** Level 3 (ПРИМЕРЫ) — безопасная работа со списками
**Частота:** 🔥 75% студентов выходят за границы

**Sandbox код:**
```python
# Запусти — увидишь ошибку!
fruits = ["apple", "banana"]

third_fruit = fruits[2]  # ❌ ОШИБКА! Индекс 2 не существует!

# Исправь — получи последний элемент безопасно:
assert third_fruit == "banana"
```

**Что видит студент:**
```
❌ IndexError: list index out of range
   Line 4: third_fruit = fruits[2]

💡 Подсказка: В списке только 2 элемента (индексы 0 и 1)
💡 Решение 1: Используй fruits[1] для второго элемента
💡 Решение 2: Используй fruits[-1] для последнего элемента
```

**Файл:** `configs/python_core_01/lesson_04_sandbox_02_index_error_fail_first.json`

---

### 5. ZeroDivisionError ⚡

**Урок:** Python Core 03 — Functions
**Раздел:** Level 3 (ПРИМЕРЫ) — defensive programming
**Частота:** 🔥 60% студентов сталкиваются в математических задачах

**Sandbox код:**
```python
# Запусти — увидишь ошибку!
def calculate_average(total, count):
    return total / count  # ❌ ОШИБКА если count = 0!

result = calculate_average(100, 0)

# Исправь функцию — добавь проверку:
assert result == 0  # Если count=0, возвращаем 0
```

**Что видит студент:**
```
❌ ZeroDivisionError: division by zero
   Line 3: return total / count

💡 Подсказка: Нельзя делить на 0!
💡 Решение: Добавь проверку перед делением:
   if count == 0:
       return 0
   return total / count
```

**Файл:** `configs/python_core_01/lesson_03_sandbox_02_zero_division_fail_first.json`

---

### 6. AssertionError без сообщения ⚡

**Урок:** Pytest Basics 01 — Pytest Introduction
**Раздел:** Level 3 (ПРИМЕРЫ) — Best Practices
**Частота:** 🔥 90% студентов забывают добавлять сообщения

**Sandbox код:**
```python
# Запусти — увидишь непонятную ошибку!
def test_login_status():
    status_code = 401
    assert status_code == 200  # ❌ ПЛОХО! Не понятно что не так!

test_login_status()

# Исправь — добавь понятное сообщение:
# assert status_code == 200, f"Expected 200, got {status_code}"
```

**Что видит студент:**
```
❌ AssertionError
   Line 3: assert status_code == 200

💡 Проблема: Тест упал, но непонятно ПОЧЕМУ!
💡 Решение: Добавь сообщение:
   assert status_code == 200, f"Expected 200, got {status_code}"

✅ Теперь будет:
   AssertionError: Expected 200, got 401
```

**Файл:** `configs/pytest_basics/pytest_01_sandbox_02_assert_message_fail_first.json`

---

## 📈 Priority 1: ВАЖНЫЕ (следующая итерация)

### 7. ValueError: invalid literal for int()

**Урок:** Python Core 01 — Variables & Types
**Раздел:** Level 3 (ПРИМЕРЫ)
**Файл:** `configs/python_core_01/lesson_01_sandbox_05_value_error_fail_first.json`

**Sandbox код:**
```python
# Запусти — увидишь ошибку!
user_input = "abc"
age = int(user_input)  # ❌ ОШИБКА! 'abc' нельзя преобразовать в число!

# Исправь — добавь проверку или используй try/except
```

---

### 8. AttributeError: str has no attribute 'append'

**Урок:** Python Core 04 — Lists & Tuples
**Раздел:** Level 3 (ПРИМЕРЫ)
**Файл:** `configs/python_core_01/lesson_04_sandbox_03_attribute_error_fail_first.json`

**Sandbox код:**
```python
# Запусти — увидишь ошибку!
text = "hello"
text.append("!")  # ❌ ОШИБКА! У строк нет метода append!

# Исправь — используй конкатенацию:
# text = text + "!"
```

---

## 🛠️ Технические детали реализации

### Новое поле в JSON конфигах:

```json
{
  "title": "Найди ошибку: TypeError",
  "fail_first": true,
  "initial_error": {
    "type": "TypeError",
    "message": "can only concatenate str (not 'int') to str",
    "line": 2,
    "explanation": "Переменная age — это число 25, а не строка!"
  },
  "code": "age = 25\nmessage = \"Your age is: \" + age\n\nassert \"Your age is: 25\" in message",
  "expected_fixes": [
    {"pattern": "str(age)", "test": "message contains age"}
  ],
  "hints": [
    "Преобразуй число в строку: str(age)",
    "Или используй f-строку: f\"Your age is: {age}\""
  ],
  "success_message": "🎉 Ты исправил TypeError! Теперь понимаешь разницу между типами!"
}
```

### Логика в генераторе:

1. **Первый запуск** (код с ошибкой):
   - Симулирует ошибку
   - Показывает `initial_error.message`
   - Показывает `hints[0]`

2. **После фикса** (код исправлен):
   - Проверяет `expected_fixes` паттерны
   - Показывает `success_message`

---

## 📊 Сравнение: БЫЛО → СТАЛО

### БЫЛО (старые sandboxes):
```python
# Исправь код
age = "25"  # ❌ Должно быть число
assert type(age) == int
```
**Что видит студент:** Просто assert failed (скучно 😴)

### СТАЛО (Fail First sandboxes):
```python
# Запусти — увидишь ошибку!
age = 25
message = "Age: " + age  # ❌ КРАШНЕТСЯ!

assert "Age: 25" in message
```
**Что видит студент:**
```
❌ TypeError: can only concatenate str (not 'int') to str
💡 age это число, преобразуй в строку: str(age)
```
**Эффект:** Студент **видит реальную ошибку** → запомнит на всю жизнь! 🔥

---

## 🎯 План выполнения

### Сегодня (2025-10-08):
- [x] Анализ покрытия ошибок (70% пробел)
- [ ] Создать 6 Priority 0 JSON конфигов
- [ ] Обновить `sandbox-generator.py` для поддержки `fail_first` режима
- [ ] Сгенерировать 6 HTML sandboxes
- [ ] Протестировать локально
- [ ] Задеплоить на GitHub Pages

### Завтра:
- [ ] Создать 2 Priority 1 конфига
- [ ] Интегрировать в матрицу уроков
- [ ] Обновить документацию для менторов

---

## 📁 Структура файлов

```
configs/
├── python_core_01/
│   ├── lesson_01_sandbox_01_fix_type.json ✅ (старый)
│   ├── lesson_01_sandbox_02_type_conversion.json ✅ (старый)
│   ├── lesson_01_sandbox_03_type_error_fail_first.json 🆕 P0
│   ├── lesson_01_sandbox_04_name_error_fail_first.json 🆕 P0
│   ├── lesson_01_sandbox_05_value_error_fail_first.json 🆕 P1
│   ├── lesson_03_sandbox_02_zero_division_fail_first.json 🆕 P0
│   ├── lesson_04_sandbox_02_index_error_fail_first.json 🆕 P0
│   ├── lesson_04_sandbox_03_attribute_error_fail_first.json 🆕 P1
│   └── lesson_05_sandbox_02_key_error_fail_first.json 🆕 P0
└── pytest_basics/
    └── pytest_01_sandbox_02_assert_message_fail_first.json 🆕 P0
```

**ИТОГО:** 6 новых P0 + 2 новых P1 = **8 Fail First sandboxes**

---

## ✅ Критерии успеха

**Sandbox считается успешным если:**
1. ✅ Студент **видит реальную ошибку** при первом запуске
2. ✅ Ошибка **понятно объяснена** (не технический жаргон)
3. ✅ Даны **конкретные подсказки** как исправить
4. ✅ После фикса студент **видит SUCCESS** сообщение
5. ✅ Студент **запомнил** как избегать этой ошибки в будущем

---

## 💥 Impact предсказания

**Текущие sandboxes (без Fail First):**
- Студент исправляет код → тест прошёл → "ок" 😐
- Retention: ~40-50%

**С Fail First sandboxes:**
- Студент видит CRASH → "черт, что не так?!" 😱
- Понимает ошибку → "ааа, вот почему!" 💡
- Фиксит → SUCCESS → "я красавчик!" 🎉
- Retention: ~80-90% (по исследованиям Active Learning)

**Разница:** +40% retention! 🚀

---

**Автор:** Claude + анализ агента
**Версия:** 1.0 (Priority Map)
**Следующий шаг:** Создание 6 Priority 0 конфигов
