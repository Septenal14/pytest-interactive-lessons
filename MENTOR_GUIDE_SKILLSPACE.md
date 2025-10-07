# 📚 Гайд для менторов: Как вставлять интерактивные элементы в Skill Space

## 🎯 Цель этого гайда

Показать менторам **пошагово**, как добавить готовые интерактивные элементы (диаграммы, песочницы, квизы) в уроки на платформе Skill Space.

---

## 📦 Что уже готово для использования

### 1. **Pytest Lessons (5 уроков)**

| Урок | URL | Что внутри |
|------|-----|-----------|
| Lesson 01: Введение | `https://septenal14.github.io/pytest-interactive-lessons/` | Mermaid диаграмма + квиз |
| Lesson 01: FULL | `https://septenal14.github.io/pytest-interactive-lessons/lesson-01-full-interactive.html` | **Python песочница + диаграмма + квиз + теория** |
| Lesson 02: Fixtures | `https://septenal14.github.io/pytest-interactive-lessons/lesson-02-fixtures.html` | Lifecycle диаграмма + квиз |
| Lesson 03: Parametrize | `https://septenal14.github.io/pytest-interactive-lessons/lesson-03-parametrize.html` | Data flow диаграмма + квиз |
| Lesson 04: Markers | `https://septenal14.github.io/pytest-interactive-lessons/lesson-04-markers.html` | Фильтрация тестов + квиз |
| Lesson 05: Assertions | `https://septenal14.github.io/pytest-interactive-lessons/lesson-05-assertions.html` | Assertion flow + квиз |

### 2. **Python Core**

| Урок | URL | Что внутри |
|------|-----|-----------|
| Python Types Overview | `https://septenal14.github.io/pytest-interactive-lessons/python-core-overview.html` | Карта всех типов данных + квиз |

### 3. **Mermaid Live URLs (прямые ссылки на диаграммы)**

Если нужна только диаграмма без HTML:

- Pytest Workflow: `https://mermaid.live/view#pako:eNpVkMF...` (см. MASTER_GUIDE_SKILLSPACE.md)

---

## 🚀 Пошаговая инструкция: Как вставить в Skill Space

### Вариант 1: Вставить ПОЛНЫЙ интерактивный урок (РЕКОМЕНДУЕТСЯ)

**Когда использовать:** Когда нужен полноценный урок с теорией + диаграммой + песочницей + квизом.

**Пример:** Lesson 01 FULL (с Python песочницей)

#### Шаги:

1. **Открой урок в Skill Space**
   - Перейди в раздел "Pytest Basics"
   - Найди "Lesson 01: Введение в Pytest"

2. **Добавь текстовый блок (опционально)**
   ```markdown
   ## 🧪 Интерактивный урок: Введение в Pytest

   Ниже — **живой урок** с Python песочницей. Ты сможешь:
   - Редактировать код прямо в браузере
   - Запускать pytest
   - Видеть результаты тестов в реальном времени

   **Загрузка займёт ~10 секунд** (первый запуск).
   ```

3. **Добавь блок "Custom Code"**
   - Нажми "+ Добавить блок"
   - Выбери "Custom Code"
   - Вставь:

   ```html
   <iframe src="https://septenal14.github.io/pytest-interactive-lessons/lesson-01-full-interactive.html" width="100%" height="1200px" frameborder="0" style="border: 1px solid #ddd; border-radius: 8px;"></iframe>
   ```

4. **Сохрани и протестируй**
   - Нажми "Сохранить"
   - Открой урок как студент
   - Проверь что iframe загрузился

✅ **Готово!** Студенты видят полноценный интерактивный урок.

---

### Вариант 2: Вставить только диаграмму

**Когда использовать:** Когда нужна только визуальная схема без песочницы.

**Пример:** Pytest Workflow диаграмма

#### Шаги:

1. **Добавь текст перед диаграммой**
   ```markdown
   ## 🔄 Как работает Pytest?

   Посмотри на схему — так pytest находит и запускает тесты:
   ```

2. **Добавь блок "Custom Code"**
   ```html
   <iframe src="https://septenal14.github.io/pytest-interactive-lessons/lesson-02-fixtures.html" width="100%" height="600px" frameborder="0" style="border: 1px solid #ddd; border-radius: 8px;"></iframe>
   ```

3. **Добавь текст после диаграммы**
   ```markdown
   💡 **Видишь?** Pytest автоматически находит все файлы `test_*.py` и запускает функции `test_*`.
   ```

✅ **Готово!** Студенты видят только диаграмму.

---

### Вариант 3: Вставить только Mermaid диаграмму (без HTML)

**Когда использовать:** Когда Skill Space поддерживает Mermaid напрямую (проверь в админке).

**НО:** Skill Space может НЕ поддерживать Mermaid синтаксис напрямую. В этом случае используй **Mermaid Live URL**:

```html
<iframe src="https://mermaid.live/view#pako:eNpVkMFqwzAMhl9F..." width="100%" height="500px" frameborder="0"></iframe>
```

**Где взять URL:**
- Открой `MASTER_GUIDE_SKILLSPACE.md`
- Скопируй нужный Mermaid Live URL

---

## 🎨 Настройка высоты iframe

**Проблема:** Iframe обрезает контент снизу.

**Решение:** Увеличь `height`:

| Контент | Рекомендуемая высота |
|---------|---------------------|
| Только диаграмма | `500px` - `600px` |
| Диаграмма + квиз | `700px` - `800px` |
| Полный урок (теория + песочница + квиз) | `1200px` - `1500px` |
| Python песочница (Lesson 01 FULL) | `1500px` - `2000px` |

**Пример:**
```html
<iframe src="..." width="100%" height="1500px" frameborder="0"></iframe>
```

---

## 🔥 Рекомендованный workflow

### Для Pytest Lessons (базовые уроки):

1. **Теория** — напиши в Skill Space markdown редакторе (ЗАЧЕМ, ЧТО, КАК)
2. **Диаграмма** — вставь iframe с готовой HTML страницей
3. **Практика** — ссылка на домашнее предложение (GitLab repo)

**Пример структуры урока:**

```
Урок: Pytest Fixtures

1. Блок: Markdown
   ## 📌 Level 0: ЗАЧЕМ нужны fixtures?
   (текст теории)

2. Блок: Custom Code (iframe)
   <iframe src="https://septenal14.github.io/.../lesson-02-fixtures.html" ...>

3. Блок: Markdown
   ## 🎯 Домашнее предложение
   Закрепи материал: [GitLab Repo](...)
```

### Для Python Core (обзорные уроки):

1. **Вставь ПОЛНЫЙ урок через iframe** (всё в одном: теория + диаграмма + квиз)
2. Ничего дополнительно не нужно

---

## 🐛 Troubleshooting (Частые проблемы)

### 1. **Iframe не загружается / показывает ошибку**

**Причины:**
- ❌ Skill Space блокирует внешние iframe (проверь настройки безопасности)
- ❌ GitHub Pages еще не обновился (подожди 1-2 минуты)
- ❌ Неправильный URL

**Решение:**
1. Открой URL напрямую в браузере: `https://septenal14.github.io/...`
2. Если работает — проблема в Skill Space (обратись к админу)
3. Если НЕ работает — сообщи мне (возможно баг в коде)

### 2. **Диаграмма показывает "Syntax error in text"**

**Причина:** Ошибка в Mermaid синтаксисе.

**Решение:**
- Используй ГОТОВЫЕ URL из `MASTER_GUIDE_SKILLSPACE.md`
- Если создаешь свою диаграмму — проверь синтаксис на [mermaid.live](https://mermaid.live/)

### 3. **Python песочница не загружается**

**Причина:** Pyodide (Python в браузере) требует ~10 секунд для первой загрузки.

**Решение:**
- Добавь предупреждение студентам: "Загрузка займёт 10 секунд"
- Проверь что iframe `height` достаточно большой (`1500px+`)

### 4. **Квиз не работает (кнопка не реагирует)**

**Причина:** JavaScript заблокирован в iframe.

**Решение:**
- Проверь настройки Skill Space (разрешены ли iframe с JavaScript)
- Альтернатива: используй Google Forms квизы

---

## 📊 Метрики успеха (для аналитики)

Как понять что интерактивные элементы работают:

| Метрика | Как измерить | Целевое значение |
|---------|--------------|-----------------|
| Время на уроке | Skill Space аналитика | +30% (студенты дольше взаимодействуют) |
| Completion Rate | % студентов завершивших урок | +20% (интерактив мотивирует) |
| Feedback | Опросы студентов | "Очень полезно" > 80% |
| Quiz Pass Rate | % правильных ответов | > 70% (значит материал понятен) |

---

## 🎯 Quick Reference (Шпаргалка)

**Хочу вставить:**

- ✅ **Полный урок с песочницей** → `lesson-01-full-interactive.html` (`height="1500px"`)
- ✅ **Только диаграмму** → `lesson-02-fixtures.html` (`height="600px"`)
- ✅ **Только Mermaid** → Mermaid Live URL (`height="500px"`)
- ✅ **Квиз** → Уже встроен в HTML страницы (ничего дополнительно не нужно)

**Формат вставки:**
```html
<iframe src="URL" width="100%" height="XYZpx" frameborder="0" style="border: 1px solid #ddd; border-radius: 8px;"></iframe>
```

---

## 📞 Поддержка

Если что-то не работает:

1. Проверь этот гайд (90% вопросов решаются здесь)
2. Открой `MASTER_GUIDE_SKILLSPACE.md` (там все URL + примеры)
3. Проверь URL напрямую в браузере
4. Если проблема осталась — напиши мне

---

**Последнее обновление:** 2025-10-08
**Автор:** Claude Code Interactive Lessons
**Версия:** 1.0
