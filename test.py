from jinja2 import Environment, FileSystemLoader
import os
import webbrowser
from pathlib import Path

def main():
    # Configure Jinja2 environment
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=True
    )

    # Load template (existing file is templates/test.html)
    template = env.get_template("test.html")

    # Data passed to the template
    context = {
        "title": "Jinja2 Example",
        "message": "Hello from Jinja2"
    }

    # Render HTML
    rendered_html = template.render(context)

    # Write rendered HTML to a file and open in default browser
    output_path = Path(__file__).parent / "rendered.html"
    output_path.write_text(rendered_html, encoding="utf-8")

    uri = output_path.resolve().as_uri()
    print(f"Wrote rendered HTML to {output_path}. Opening in browser...")
    webbrowser.open_new_tab(uri)


if __name__ == "__main__":
    main()
