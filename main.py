import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Lê o arquivo ABS.html que você salvou
        with open('ABS.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        return render_template_string(html_content)
    except Exception as e:
        return f"Erro ao carregar o painel: {e}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
