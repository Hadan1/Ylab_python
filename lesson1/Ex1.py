def domain_name(url):
    if url.find('www.') != -1:
        m = url[(url.find('www.')+4):]
        n = m[:m.find('.')]
    elif url.find('//') != -1:
        m = url[(url.find('//')+2):]
        n = m[:m.find('.')]
    else:
        m = url
        n = m[:m.find('.')]
    return n