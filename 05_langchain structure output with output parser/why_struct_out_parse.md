# StructuredOutputParser

## What is StructuredOutputParser?

`StructuredOutputParser` is an output parser in LangChain that helps extract **structured JSON data** from LLM responses based on a **predefined schema**.

Unlike `JsonOutputParser`, it explicitly defines **which fields** the LLM must return and what each field represents.

---

# Why Do We Need It?

`JsonOutputParser` only ensures that the output is **valid JSON**.

Example:

```json
{
  "username": "Hardik",
  "years": 22
}
```

This is valid JSON, but the field names are not what our application expects.

Suppose our application requires:

```json
{
  "name": "Hardik",
  "age": 22
}
```

Simply returning JSON is **not enough**.

We also need to enforce a **schema** (field names and descriptions).

That's where **StructuredOutputParser** comes in.

---

# How Does It Work?

1. Define the fields using `ResponseSchema`.
2. Create a `StructuredOutputParser`.
3. Generate format instructions.
4. Add those instructions to the prompt.
5. The LLM returns JSON that follows the required schema.

---

# Example Schema

```text
name : Person's full name

age : Person's age

city : City where the person lives
```

The parser instructs the LLM to always return these exact fields.

---

# JsonOutputParser vs StructuredOutputParser

| JsonOutputParser | StructuredOutputParser |
|------------------|------------------------|
| Ensures valid JSON | Ensures valid JSON + predefined schema |
| No fixed field names | Fixed field names |
| Flexible output | Strict structure |
| Best for generic JSON | Best for information extraction |

---

# When Should You Use It?

Use `StructuredOutputParser` when:

- You know exactly which fields you want.
- Your application expects a fixed JSON structure.
- You are extracting information from text, PDFs, resumes, invoices, etc.
- You need consistent field names across all responses.

---

# One-Line Summary

> **`JsonOutputParser` ensures the output is valid JSON, while `StructuredOutputParser` ensures the output is valid JSON that also follows a predefined schema.**

---

# Limitations of StructuredOutputParser

Although `StructuredOutputParser` enforces a predefined schema (field names and structure), it **does not perform data validation**.

For example, if your schema expects:

```json
{
    "age": 25
}
```

and the LLM returns:

```json
{
    "age": "twenty five"
}
```

`StructuredOutputParser` will still parse the output successfully because it only checks the **structure**, not the **data types or values**.

If you need validation such as:

- Ensuring `age` is an integer.
- Checking that `email` is a valid email address.
- Restricting `sentiment` to `"positive"`, `"neutral"`, or `"negative"`.
- Applying default values or custom validation rules.

then you should use **Pydantic** instead of `StructuredOutputParser`.