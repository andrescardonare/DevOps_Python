from flask import Flask, request, render_template
import os
import sys
import json

# Ensure project root is on sys.path so absolute imports work when running
# this file directly (python price_calculator/server.py)
package_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(package_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import calculate_total robustly
try:
    from price_calculator.calc import calculate_total
except Exception:
    try:
        from calc import calculate_total
    except Exception:
        from price_calculator import calculate_total

app = Flask(__name__, template_folder=package_dir)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    costs_example = '{"a": 1.0, "b": 2.0}'

    if request.method == 'POST':
        # Read form fields
        costs_raw = request.form.get('costs', '')
        items_raw = request.form.get('items', '')
        tax_raw = request.form.get('tax', '0')

        # Parse costs (expect JSON) and items (comma-separated)
        try:
            costs = json.loads(costs_raw) if costs_raw.strip() else {}
        except Exception:
            costs = {}
            error = 'Invalid costs format. Please provide JSON like: ' + costs_example

        items = [it.strip() for it in items_raw.split(',') if it.strip()]
        try:
            tax = float(tax_raw)
        except Exception:
            tax = 0.0
            error = (error + '\nInvalid tax value.') if error else 'Invalid tax value.'

        if not error:
            total = calculate_total(costs, items, tax)
            result = f"{total:.2f}"

    return render_template('index.html', result=result, error=error, costs_example=costs_example)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
