import justpy as jp


class Doc:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Div(a=div, text="Get defination of words", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=moon")
        jp.Hr(a=div)
        jp.Div(a=div, text=""" ..... """)
        return wp
