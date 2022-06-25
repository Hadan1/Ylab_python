def domain_name(url):
    if url.find('www.') != -1:
        m = url[(url.find('www.')+4):]
        n = m[:m.find('.')]
    elif url.find('//') != -1:
        m = url[(url.find('//')+2):]
        n = m[:m.find('.')]
    else:
        n = m[:m.find('.')]
    return n

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"