from flask import Flask, request, render_template
import os
import sys

# Ensure project root is on sys.path for imports when running directly
package_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(package_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import function
try:
    from concatenate_nth.concat import concatenate_nth
except Exception:
    from concat import concatenate_nth

app = Flask(__name__, template_folder=package_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        words_raw = request.form.get('words', '')
        # words are provided as comma-separated values
        words = [w.strip() for w in words_raw.split(',') if w.strip()]
        try:
            result = concatenate_nth(words)
        except Exception as e:
            error = str(e)
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100)
