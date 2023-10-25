import datetime

print("Hello, from the script!")

def ExecuteEndpoint():
    if SmCtx.ServerContexts["Command"] == "N2P":
        MobileCtx.NavigateToPage(SmCtx.ServerContexts["SubscriptionId"],SmCtx.ServerContexts["McId"],SmCtx.ServerContexts["Flow"],SmCtx.ServerContexts["EndpointId"])
    elif SmCtx.ServerContexts["Command"] == "Error":
        MobileCtx.Error(SmCtx.ServerContexts["EndpointId"])
    elif SmCtx.ServerContexts["Command"] == "Visit":
        MobileCtx.Visit(SmCtx.ServerContexts["Flow"],SmCtx.ServerContexts["EndpointUrl"],SmCtx.ServerContexts["McId"])
    else:
        MobileCtx.CallCommand(SmCtx.ServerContexts["Command"])