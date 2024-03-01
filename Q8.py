def is_valid_url(url):
    """""
    take a string
    :return: Whether it is a URL or not
    """
    if url.startswith("http://") or url.startswith("https://") or url.startswith("ftp://"):
        return True
    else:
        return False
# Examples:
url1 = "https://www.example.com"
url2 = "ftp://ftp.example.com"
url3 = "lalalala_3"
print("Is", url1, "a valid URL?", is_valid_url(url1))
print("Is", url2, "a valid URL?", is_valid_url(url2))
print("Is", url3, "a valid URL?", is_valid_url(url3))