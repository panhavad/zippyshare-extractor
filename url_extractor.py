from engines.js import JSEngine

def extract_download_links(original_urls):
    engine = JSEngine()
    original_urls = original_urls.split("\n")
    zippybase = "https://www61.zippyshare.com"
    durls = []

    for url in original_urls:
        durl_part = engine.get_download_link(url)[0]
        durl = zippybase + durl_part
        durls.append(durl)
    
    return "\n".join(durls)
