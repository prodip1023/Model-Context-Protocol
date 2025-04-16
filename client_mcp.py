import requests

def test_multiply(a,b):
    response = requests.post("http://127.0.0.1:8089/prodip/mcp/multiply",json={"a":a,"b":b})
    if response.status_code == 200:
        print("multiplication mcp called sucessfully",response.json()['result'])
    else:
        print("Error in calling mcp",response.status_code)


if __name__ == "__main__":
    test_multiply(4,9)