from renderer import render
from decorators import address
from helpers import send_response, write_to_db



@address('about')
def about_handler(request, conn, match=True, data={}):
    template = "about.html"
    abc = render(template)
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(abc)
    # write_to_db(match,data)
    send_response(resp, conn, match)



# @address('shop')
# def shop_handler(request, conn, match=True):
#     template = "shop.html"
#     render(template, conn, match)

@address('contacts')
def contact_handler(request, conn, match=True,data={}):
    template = "contacts.html"
    content = render(template)
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(content)
    write_to_db(match,data)
    # translit(data,)
    send_response(resp, conn, match)


@address('translate')
def translate_handler(request, conn, match=True,data={}):
    template = "translate.html"
    cont = render(template)
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(cont)
    # write_to_db(match, data)
    send_response(resp, conn, match)
