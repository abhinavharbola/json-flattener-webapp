# 🪶 Flat D. JSON - JSON Flattener Web App

**Flat D. JSON** is a lightweight, interactive web app built with Streamlit that lets you flatten complex nested JSON files into a clean, key–value structure.

You can upload a `.json` file or paste raw JSON text — the app instantly flattens it and lets you download the flattened JSON or CSV with one click.

---

## Features

- Upload or paste JSON — works with files or raw JSON text  
- Handles deeply nested JSON with objects and arrays  
- Customizable key separator (default `"."`)  
- Instant download as flattened `.json`  
- Export to CSV (new!) — get flattened data in tabular form  
- Simple Streamlit UI with recursive flattening logic  
- Unit tested with `pytest`  

---

## Tech Stack

| Tool       | Purpose                          |
|-------------|----------------------------------|
| **Python 3.x** | Core language                  |
| **Streamlit**  | Web app framework              |
| **Pandas**     | CSV generation                 |
| **Pytest**     | Unit testing                   |
| **JSON (built-in)** | Parsing & serialization   |

---

## Project Structure

```
flatd-json/
├── app.py              # Main Streamlit app (UI)
├── flattener.py        # Core flattening logic
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/flatd-json.git
cd flatd-json
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
# OR
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## Example Usage

### Input JSON
```json
{
  "user": {
    "name": "Alice",
    "address": {
      "city": "Wonderland",
      "postal": 12345
    },
    "tags": ["admin", "dev"]
  }
}
```

### Output (Flattened JSON)
```json
{
  "user.name": "Alice",
  "user.address.city": "Wonderland",
  "user.address.postal": 12345,
  "user.tags.0": "admin",
  "user.tags.1": "dev"
}
```

### Output (Flattened CSV)
| user.name | user.address.city | user.address.postal | user.tags.0 | user.tags.1 |
|------------|------------------|---------------------|--------------|--------------|
| Alice      | Wonderland       | 12345               | admin        | dev          |

---

## Potential Enhancements

- Search bar for flattened keys  
- Tree view toggle to compare flat vs nested JSON  
- Excel (XLSX) export via `openpyxl`  
- Handle various file encodings (UTF-8, UTF-16)  

---

## Contribute & Support

If you find this project helpful, please consider **starring ⭐ the repo** or submitting a **pull request** with your improvements!

---


**Author:** [Abhinav Harbola](https://github.com/abhinavharbola)
