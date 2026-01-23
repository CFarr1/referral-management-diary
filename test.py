from jinja2 import Environment, FileSystemLoader

def main():
    # Configure Jinja2 environment
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=True
    )

    # Load template
    template = env.get_template("index.html")

    # Data passed to the template
    context = {
        "title": "Jinja2 Example",
        "message": "Hello from Jinja2"
    }

    # Render HTML
    rendered_html = template.render(context)

    # Output result (console or file)
    print(rendered_html)

if __name__ == "__main__":
    main()
