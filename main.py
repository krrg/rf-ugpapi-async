from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/")
async def test_req(request):
    return json({
        "hello": "world"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=13400)
