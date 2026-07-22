# LangChain Output Parsers Comparison

| Parser | Ensures JSON | Enforces Schema | Validates Data | Returns |
|---------|:------------:|:---------------:|:--------------:|---------|
| **StrOutputParser** | ❌ | ❌ | ❌ | `str` (Plain String) |
| **JsonOutputParser** | ✅ | ❌ | ❌ | Python `dict` |
| **StructuredOutputParser** | ✅ | ✅ | ❌ | Python `dict` |
| **PydanticOutputParser** | ✅ | ✅ | ✅ | Pydantic `BaseModel` Object |

---

# Quick Summary

## StrOutputParser

- Returns plain text (`str`).
- Best for chatbots, summarization, translation, and other text generation tasks.

---

## JsonOutputParser

- Ensures the output is valid JSON.
- Does **not** enforce field names.
- Does **not** validate data types or values.
- Returns a Python dictionary.

---

## StructuredOutputParser

- Ensures the output is valid JSON.
- Enforces a predefined schema (field names).
- Does **not** validate data types or values.
- Returns a Python dictionary.

---

## PydanticOutputParser

- Ensures the output is valid JSON.
- Enforces a predefined schema.
- Validates data types and values using Pydantic.
- Returns a Pydantic object (`BaseModel`).
- Raises a validation error if the output doesn't match the schema.

---

# Which Parser Should I Use?

| Use Case | Recommended Parser |
|----------|--------------------|
| Normal chatbot | StrOutputParser |
| Need JSON output | JsonOutputParser |
| Need fixed field names | StructuredOutputParser |
| Need data validation and type safety | PydanticOutputParser |
