def domain_name(url):
    if url.find('www.') != -1:
        m = url[(url.find('www.')+4):]
        n = m[:m.find('.')]
    elif url.find('//') != -1:
        m = url[(url.find('//')+2):]
        n = m[:m.find('.')]
    else:
        n = m[:m.find('.')]
<<<<<<< HEAD:lesson1/ex1.py
    return n
=======
    return n

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
>>>>>>> c3fcb1086f0985d0388626d6346ba7e25fd880dd:lesson1/Ex1.py
