# Structured Output in LangChain: When Should You Use What?

LangChain supports multiple ways to generate **structured output** from Large Language Models.

The three most common approaches are:

1. TypedDict
2. Pydantic
3. JSON Schema

Each has different strengths and is suitable for different use cases.

---

# 1. TypedDict

## What is it?

`TypedDict` is a lightweight way to describe the structure of the expected output.

It provides **type hints only**.

Example:

```python
class Person(TypedDict):
    name: str
    age: int
```

Output

```python
{
    "name": "Hardik",
    "age": 22
}
```

---

## Advantages

- Very simple
- Lightweight
- Easy to learn
- No extra validation logic
- Minimal code

---

## Limitations

- No data validation
- No default values
- No custom constraints
- No nested validation
- Only defines the expected structure

---

## Use TypedDict When

✅ You only need type hints.

✅ You trust the LLM to return correct data.

✅ You don't need validation.

✅ You are building small projects.

✅ You want the simplest possible structured output.

---

## Example Use Cases

- Student Information
- User Profile
- Product Details
- Movie Information
- Book Metadata

---

# 2. Pydantic

## What is it?

Pydantic is a data validation library.

It not only defines the structure but also validates and converts data.

Example

```python
class Person(BaseModel):
    name: str
    age: int
```

Output

```python
Person(
    name="Hardik",
    age=22
)
```

---

## Advantages

✔ Data Validation

```python
age > 0
```

---

✔ Default Values

```python
country: str = "India"
```

---

✔ Field Descriptions

```python
name: str = Field(
    description="Full Name"
)
```

---

✔ Automatic Type Conversion

```python
"100"
```

↓

```python
100
```

---

✔ Nested Models

```python
Student

↓

Address

↓

City
```

---

✔ Better IDE Support

Autocomplete

Validation

Documentation

---

## Use Pydantic When

✅ You need validation.

✅ You need default values.

✅ You need field descriptions.

✅ You need nested objects.

✅ You are building production applications.

✅ You are creating APIs.

---

## Example Use Cases

- Resume Parser
- Invoice Extraction
- Medical Report Extraction
- Banking Applications
- CRM Systems
- ERP Systems
- AI Agents

---

# 3. JSON Schema

## What is it?

JSON Schema is an industry-standard format for describing JSON data.

Unlike Pydantic, it is **language-independent**.

Example

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "integer"
    }
  }
}
```

---

## Advantages

- Standard format
- Language independent
- Works with APIs
- Works with JavaScript
- Works with Node.js
- No dependency on Python classes

---

## Limitations

- More verbose
- Harder to write manually
- Less beginner-friendly

---

## Use JSON Schema When

✅ You are integrating with external APIs.

✅ You don't want to use Pydantic.

✅ You need a language-independent schema.

✅ Your frontend/backend communicates using JSON Schema.

---

## Example Use Cases

- REST APIs
- OpenAPI / Swagger
- Microservices
- Frontend Validation
- Third-party Integrations

---

# Comparison Table

| Feature | TypedDict | Pydantic | JSON Schema |
|----------|-----------|-----------|-------------|
| Easy to Learn | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| Type Hints | ✅ | ✅ | ✅ |
| Data Validation | ❌ | ✅ | ✅ |
| Default Values | ❌ | ✅ | ✅ |
| Field Description | ❌ | ✅ | ✅ |
| Automatic Type Conversion | ❌ | ✅ | ❌ |
| Nested Objects | Limited | ✅ | ✅ |
| Python Object | Dict | BaseModel | JSON |
| Language Independent | ❌ | ❌ | ✅ |
| Production Ready | Small Projects | ✅ | ✅ |

---

# Decision Flow

```
Need Structured Output
          │
          ▼
Need only type hints?
          │
     Yes ─────────► TypedDict
          │
         No
          │
          ▼
Need validation, defaults,
descriptions or nested objects?
          │
     Yes ─────────► Pydantic
          │
         No
          │
          ▼
Need a language-independent
schema or API contract?
          │
     Yes ─────────► JSON Schema
```

---

# Quick Cheat Sheet

## Use TypedDict if:

- You only need type hints.
- You trust the LLM output.
- No validation is required.
- Learning LangChain.
- Small applications.

---

## Use Pydantic if:

- You need validation.
- You need default values.
- You need field descriptions.
- You want automatic type conversion.
- You need nested models.
- Building production applications.

---

## Use JSON Schema if:

- You need a standard JSON format.
- You're integrating with APIs.
- You're working across multiple programming languages.
- You don't want Python-specific classes.
- You're defining contracts between services.

---

# Which One Should You Learn First?

```
TypedDict
      ↓
Pydantic
      ↓
JSON Schema
```

This is the recommended learning order because each concept builds naturally on the previous one.

---

# Final Recommendation

| Scenario | Recommended |
|----------|-------------|
| Learning LangChain | ✅ TypedDict |
| Small Projects | ✅ TypedDict |
| AI Applications | ✅ Pydantic |
| RAG Pipelines | ✅ Pydantic |
| AI Agents | ✅ Pydantic |
| FastAPI Projects | ✅ Pydantic |
| Enterprise APIs | ✅ JSON Schema |
| Cross-Language Systems | ✅ JSON Schema |

---

# One-Line Summary

- **TypedDict** → Simple structure with type hints.
- **Pydantic** → Structure + validation + production-ready features.
- **JSON Schema** → Standard, language-independent schema for APIs and distributed systems.