""" 爬取网页的通用代码框架 """
import requests


def get_html_text(url):
    try:
        headers = {'user-agent': 'my-app/0.0.1 '}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(f"There was a error: {e}")


def save_text2file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)


if __name__ == "__main__":
    url = "https://item.jd.com/100008348542.html"
    r_text = get_html_text(url)

    filename = ".\\iphone_msg.txt"
    save_text2file(filename, r_text)
