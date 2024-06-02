import requests

def ping_website(urls, keywords=None,headers=None):
    response_ls = []
    unequal_params = [param for param in [keywords,headers] if param and len(param) != len(urls)]
    if unequal_params:
        return (f"**ERROR: All parameters must have the same length. {unequal_params} do not match the length of URLs \
provided!**")

    for i,x in enumerate(urls):
        try:
            response = requests.get(x, headers=headers[i] if headers else None, timeout=5)
            if response.status_code // 100 == 2:
                status = f"{x} is online and returned status code {response.status_code}"
                if keywords:
                    if keywords[i] in response.text:
                        keyword_status = f"\nThe Keyword '{keywords[i]}' was found in website content\n\n"
                    else:
                        keyword_status = f"\n**The Keyword '{keywords[i]}' was NOT found in website content**\n\n"

                    response_ls.append(status + keyword_status)
                else:
                    response_ls.append(status+"\n\n")
        except Exception as e:
            status = f"\n**{x} is OFFILINE!! and returned status code {e}**\n\n"
            response_ls.append(status)

    return "".join(response_ls)

