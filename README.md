# Ops Tech Builder – My Implementation Journey

Hi there! This is the repository I built for the **Ops Tech Builder Challenge**. I approached this challenge like a real-world project: modular structure, clean data flow, and extensibility as a priority.

## Links

-  [Detailed Report (Google Drive PDF)](https://drive.google.com/file/d/1kvZ4JQGgObZNtFkklB96CSUhPssoGMRK/view?usp=drive_link)
---

## Project Structure

```
├── api/                     # Flask API for text summarization
│   └── main.py
│
├── parser/                  # Flask API for Excel/CSV file parsing
│   ├── main.py
│   └── sample_invoice_data.xlsx
│
├── prompts/                 # Prompt comparison markdown
│   └── prompt_comparison.md
│
├── sql/                     # SQL query to retrieve top vendors
│   └── top_5_vendors.sql
│
├── .env                     # Environment variables (excluded from Git)
├── .gitignore               # Git ignore rules
└── requirements.txt         # Python dependencies
```

---

## 1. Text Summarization API (`/summarize`)

### Setup & Run

```bash
cd api
pip install -r ../requirements.txt
python main.py
```

API runs at: `http://localhost:5000`

### 💬 How to Use

Send a `POST` request to `/summarize` with a JSON body like:

```json
{
  "text": "Nhien will attend the AI Summit in Singapore.",
  "model": "openai"  // or "claude"
}
```

This API currently returns mocked responses (no actual call to OpenAI or Claude).

---

## 2. Excel/CSV File Parser API (`/parse`)

### Setup & Run

```bash
cd parser
pip install -r ../requirements.txt
python main.py
```

API runs at: `http://localhost:5001`

### How to Upload

- Method: `POST`
- Endpoint: `/parse`
- Body type: `form-data`
  - Key: `file` (type: File)
  - Value: upload `sample_invoice_data.xlsx` from the `parser/` folder

The response is a JSON with normalized fields: `PO Number`, `Vendor`, and `Amount`.

---

## 3. Prompt Comparison: GPT vs Claude

Inside the `prompts/` folder, you’ll find:

```
prompt_comparison.md
```

This markdown includes:
- The prompt used to extract structured data from text
- Sample outputs from both GPT and Claude
- Comparison on accuracy, date format normalization, and understanding

Very useful for evaluating prompt behavior and model consistency.

---

## 4. SQL Query – Top 5 Vendors

In the `sql/` folder, the file `top_5_vendors.sql` contains:

```sql
SELECT vendor, SUM(amount) AS total_paid
FROM invoices
WHERE status = 'paid'
  AND created_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY vendor
ORDER BY total_paid DESC
LIMIT 5;
```

Purpose: Retrieve the top 5 vendors with the highest total paid amounts in the last 30 days.

You can run this query in PostgreSQL using mock data.

---

## Requirements

- Python 3.8+
- Flask
- Pandas
- PostgreSQL (optional for SQL testing)
- Postman or curl for API testing

---


