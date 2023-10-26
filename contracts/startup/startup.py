print("Hello, from the [startup] script!")
def ExecuteEndpoint():
    print(SmCtx.SrcFlow.lower())
    if SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "request-otp":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/sub-startup/visit/default/verify-otp",
            "SubmitUrl":"/api/subscriptions/sub-startup/contracts/default/verify-otp",
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "post-create-bankaccount":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/sub-startup/visit/default/verify-otp",
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "verify-otp":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/sub-startup/visit/default/account-display",
            "SubmitUrl":"/api/subscriptions/sub-startup/contracts/default/account-display",
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "account-display":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/sub-startup/visit/default/pin",
            "SubmitUrl":"/api/subscriptions/sub-startup/contracts/default/pin",
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "pin":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/sub-startup/visit/default/login-result",
            
            "LoginResult":"success",
        })
