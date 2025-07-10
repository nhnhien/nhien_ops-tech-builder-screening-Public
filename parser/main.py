# parser/main.py

from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

COLUMN_ALIASES = {
    'po number': 'PO Number',
    'po no': 'PO Number',
    'po': 'PO Number',
    'vendor': 'Vendor',
    'vendor name': 'Vendor',
    'amount': 'Amount',
    'total': 'Amount',
    'total amount': 'Amount'
}

def standardize_column(name):
    return COLUMN_ALIASES.get(name.strip().lower(), None)

@app.route("/parse", methods=["POST"])
def parse_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.filename.endswith((".xlsx", ".xls")):
            df = pd.read_excel(file)
        else:
            return jsonify({"error": "Unsupported file type"}), 400

        # Standardize column names
        mapped_columns = {}
        for col in df.columns:
            std = standardize_column(col)
            if std:
                mapped_columns[col] = std

        df = df.rename(columns=mapped_columns)

        # Check if all required columns are present
        required = ['PO Number', 'Vendor', 'Amount']
        for col in required:
            if col not in df.columns:
                return jsonify({"error": f"Missing column: {col}"}), 400

        # Remove NaN and keep only required columns
        clean_df = df[required].dropna(how="any")

        # Convert to JSON list
        result = clean_df.to_dict(orient="records")

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
