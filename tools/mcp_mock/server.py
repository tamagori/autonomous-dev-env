# -*- coding: utf-8 -*-
import json
import urllib.request

from mcp.server.fastmcp import FastMCP

# 1. サーバーの作成（名前は自由に付けられます）
mcp = FastMCP("my-mcp-server-40ac5da8")

# 2. ツールの定義: @mcp.tool() をつけるだけで、AIがこの関数を使えるようになります


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    指定された2つの数字を足し算します。
    複雑な計算が必要な時にAIがこのツールを呼び出します。
    """
    return a + b


@mcp.tool()
def get_greeting(name: str) -> str:
    """
    指定された名前に対して挨拶を返します。
    """
    return f"こんにちは、{name}さん!MCPの世界へようこそ!"


@mcp.tool()
def fetch_item_from_api(item_id: int) -> str:
    """
    社内API（FastAPI）を叩いて、指定されたIDの商品情報を取得します。
    引数: item_id (整数)
    """
    url = f"http://127.0.0.1:8000/items/{item_id}"
    try:
        # FastAPIサーバーへHTTPリクエストを送信
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            return f"APIからの取得結果: {json.dumps(data, ensure_ascii=False)}"
    except urllib.error.URLError as e:
        return (
            f"API通信エラー: FastAPIサーバーが起動していない可能性があります。詳細: {e}"
        )
    except Exception as e:
        return f"予期せぬエラー: {e}"


# 3. サーバーの起動
if __name__ == "__main__":
    mcp.run()
