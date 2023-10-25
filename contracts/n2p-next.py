print("Hello, from the [n2p-next.py] script!")

def ExecuteEndpoint():
    print("call SetPageHeader")
    SmCtx.SetPageHeader(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["HeaderMode"],
        SmCtx.CrResultDicts["HeaderBaseUrl"],
        SmCtx.CrResultDicts["HeaderTitle"])
    
    print("call N2P")
    SmCtx.N2P(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["Flow"],
        SmCtx.CrResultDicts["EndpointId"],
        SmCtx.CrResultDicts["SubscriptionId"],
        
        SmCtx.CrResultDicts["SrcMcId"],
        SmCtx.CrResultDicts["SrcFlow"],
        SmCtx.CrResultDicts["SrcEndpointId"],
        SmCtx.CrResultDicts["SrcSubscriptionId"],

        SmCtx.CrResultDicts["Button1Text"] if SmCtx.CrResultDicts.ContainsKey("Button1Text") is True else "Ok",
        SmCtx.CrResultDicts["Button2Text"] if SmCtx.CrResultDicts.ContainsKey("Button2Text") is True else "Cancel")

def ActionButton_Clicked():
    print("call Visit")
    SmCtx.Visit(SmCtx.CrResultDicts["NextEndpointUrl"])
    # SmCtx.N2P(
    #     SmCtx.CrResultDicts["NextMcId"],
    #     SmCtx.CrResultDicts["NextFlow"],
    #     SmCtx.CrResultDicts["NextEndpointId"],
    #     SmCtx.CrResultDicts["NextSubscriptionId"],

    #     SmCtx.CrResultDicts["McId"],
    #     SmCtx.CrResultDicts["Flow"],
    #     SmCtx.CrResultDicts["EndpointId"],
    #     SmCtx.CrResultDicts["SubscriptionId"],

    #     "Submit")
