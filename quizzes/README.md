# Pytest Lessons Quizzes

## Overview

This directory contains 5 Google Forms-compatible quizzes for the Pytest Basics module (Lessons 01-05).

Each quiz follows **Bloom's Taxonomy** progression:
- **Remember** (Level 0) — recall key concepts
- **Understand** (Level 1) — explain concepts
- **Apply** (Level 2) — use syntax correctly
- **Analyze** (Level 3) — identify valid examples
- **Evaluate** (Level 4) — explain WHY and provide reasoning

## Quiz Structure

Each quiz contains:
- **5 questions** (balanced across Bloom's levels)
- **Question types:**
  - Multiple Choice (1 correct answer)
  - Checkbox (multiple correct answers)
  - Paragraph (free text with evaluation criteria)
- **Passing score:** 80%
- **Time limit:** 5 minutes
- **Feedback:** Detailed explanations for correct/incorrect answers

## Quiz Files

### Lesson 01: Pytest Intro (ЗАЧЕМ, ЧТО, КАК, assert)
**File:** `lesson_01_quiz.json`

**Topics:**
- Why automated tests (ЗАЧЕМ)
- What is Pytest (ЧТО)
- How to use assert (КАК)
- Naming conventions (test_*.py)
- Pytest vs print() debugging

**Questions:**
1. Remember: Why do we need autotests?
2. Understand: What is Pytest?
3. Apply: Correct assert syntax
4. Analyze: Valid test names
5. Evaluate: Pytest vs print() — explain savings

---

### Lesson 02: Запуск и конфигурация
**File:** `lesson_02_quiz.json`

**Topics:**
- Pytest flags (-v, -s, -k)
- pytest.ini configuration
- Test filtering
- Debug output

**Questions:**
1. Remember: Why flags and pytest.ini?
2. Understand: What does -v do?
3. Apply: Filter tests with -k
4. Analyze: Valid pytest.ini content
5. Evaluate: -v vs -s — when to use

---

### Lesson 03: Fixtures (Setup и Teardown)
**File:** `lesson_03_quiz.json`

**Topics:**
- Why fixtures (убрать дублирование)
- yield vs return
- Guaranteed cleanup
- scope (function, module, session)
- conftest.py

**Questions:**
1. Remember: Why fixtures?
2. Understand: return vs yield
3. Apply: Fixture with cleanup syntax
4. Analyze: scope='module' behavior
5. Evaluate: scope='module' time savings

---

### Lesson 04: Parametrize (Тесты с параметрами)
**File:** `lesson_04_quiz.json`

**Topics:**
- @pytest.mark.parametrize
- Data-Driven Testing
- One test, many inputs
- Parametrize vs for loop
- Scaling tests

**Questions:**
1. Remember: Why parametrize?
2. Understand: parametrize vs for loop
3. Apply: Correct parametrize syntax
4. Analyze: What happens with 5 test cases
5. Evaluate: Time savings on 50 cases

---

### Lesson 05: Assertions + Маркировка тестов
**File:** `lesson_05_quiz.json`

**Topics:**
- pytest.raises (check exceptions)
- pytest.approx (float comparison)
- pytest.warns (warnings)
- Custom markers (smoke, regression, negative)
- Running specific test groups

**Questions:**
1. Remember: Why assertions and markers?
2. Understand: What does pytest.raises do?
3. Apply: pytest.raises with match
4. Analyze: Run smoke + positive tests
5. Evaluate: Markers in CI/CD savings

---

## Usage Instructions

### Option 1: Manual Google Forms Creation

1. Open Google Forms
2. Create new form
3. Set as Quiz (Settings → Make this a quiz)
4. Copy questions from JSON:
   - Question text
   - Answer options
   - Correct answers
   - Feedback messages
5. Set passing score to 80%

### Option 2: Automated Import (Google Forms API)

**Prerequisites:**
```bash
pip install google-api-python-client google-auth
```

**Script example:**
```python
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

def create_google_form(quiz_json_path):
    with open(quiz_json_path) as f:
        quiz = json.load(f)

    service = build('forms', 'v1', credentials=get_credentials())

    # Create form
    form = service.forms().create(body={
        "info": {
            "title": quiz["title"],
            "description": quiz["description"]
        }
    }).execute()

    # Add questions...
    # (see Google Forms API documentation)

    return form["responderUri"]

# Create all quizzes
for i in range(1, 6):
    url = create_google_form(f"lesson_0{i}_quiz.json")
    print(f"Quiz {i}: {url}")
```

---

## Bloom's Taxonomy Mapping

| Level | Cognitive Skill | Question Type | Example |
|-------|----------------|---------------|---------|
| **Remember** | Recall facts | Multiple Choice | "Why do we need autotests?" |
| **Understand** | Explain concepts | Multiple Choice | "What is the difference between X and Y?" |
| **Apply** | Use knowledge | Multiple Choice | "What syntax is correct for...?" |
| **Analyze** | Identify patterns | Checkbox | "Which of these are valid...?" |
| **Evaluate** | Make judgments | Paragraph | "Explain why X saves time..." |

---

## Passing Criteria

**To pass each quiz:**
- Minimum score: **4 out of 5 points** (80%)
- All questions weighted equally except Paragraph (2 points)
- Paragraph questions evaluated against criteria:
  - 4/4 criteria met = 2 points
  - 3/4 criteria met = 1.5 points
  - 2/4 criteria met = 1 point
  - < 2 criteria met = 0 points

---

## Question Distribution

Each quiz follows this structure:

```
Q1: Remember (1 point) — Multiple Choice
Q2: Understand (1 point) — Multiple Choice
Q3: Apply (1 point) — Multiple Choice
Q4: Analyze (1 point) — Checkbox
Q5: Evaluate (2 points) — Paragraph

Total: 6 points
Passing: 4.8 points (80%)
```

---

## Metadata

- **Generated:** 2025-10-08
- **Generator:** QuizGeneratorAgent v1.0
- **Based on:** Educational Framework V2.0 (Hybrid)
- **Source lessons:** `/Users/admin/claude_projects/pytest_lessons/`

---

## Next Steps

1. Import quizzes into Google Forms
2. Share quiz links with students
3. Collect responses
4. Analyze results:
   - Which questions have low pass rate?
   - Which Bloom's levels are challenging?
   - Adjust lessons based on feedback

---

## License

These quizzes are part of the Pytest Basics course materials.

**Author:** Claude Agent
**Course:** QA Automation — Pytest Module
**Framework:** Educational Framework V2.0 (Hybrid)
