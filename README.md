# acm.usu.edu

The source of acm.usu.edu.

## Running

Clone the repository
```bash
git clone git@github.com:pharrison31415/acm.usu.edu.git
cd acm.usu.edu
```

Activate a virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the development server
```bash
flask --app app run
```

## Development

Submit your pull requests and we'll take a look! You can also reach us at admin@acm.usu.edu.

Please keep in mind the following guidelines:
- Use `templates/empty-activity.html` as a template for new activity entries.
- Strip your images of metadata with `magick mogrify -strip FILENAME`.