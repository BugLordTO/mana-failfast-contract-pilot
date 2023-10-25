print("Hello, from the [startup] script!")
def ExecuteEndpoint():
    print(SmCtx.Body.GetProperty("Test").GetString())
    body = SmCtx.GetSubmitBody()
    print(body["Test"])
    print(body["Age"])
    
    SmCtx.SetResponse({
        "name": "John",
        "age": 36,
    })