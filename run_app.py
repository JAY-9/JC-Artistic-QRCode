import sys
try:
    from streamlit.web import cli
except ImportError:
    from streamlit import cli

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py"]
    sys.exit(cli.main())
