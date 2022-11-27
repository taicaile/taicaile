"""main entry"""
import logging
import glob
import markdown
import pandas as pd

FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

logger = logging.getLogger()


def markdown2html(mdfile):
    """convert markdown file to html string"""
    with open(mdfile, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        return markdown.markdown(text, extensions=["markdown.extensions.tables"])


def html2df(html):
    """extract table from html string"""
    return pd.read_html(html, parse_dates=True)


def main():
    """main function"""
    files = glob.glob("docs/*/todo.md")
    for file in files:
        html = markdown2html(file)
        logger.info(html)
        dfs = html2df(html)
        df = dfs[-1]
        logger.info(df)

if __name__ == "__main__":

    main()
