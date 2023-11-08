print("Hello, from the [startup] script!")
def ExecuteEndpoint():
    print(SmCtx.SrcFlow.lower())
    if SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "account-ppay-create":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/bank-account/visit/default/account-ppay-confirm?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "account-bank-create":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/bank-account/visit/default/account-bank-confirm?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "account-bank-confirm":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/bank-account/visit/default/display-result-dlg?EndpointId=" + SmCtx.SrcEndpointId,
            "Message":"คุณต้องการเติมเงินต่อหรือไม่",
            "Title":"ผูกบัญชีสำเร็จ",
            "Logo":"https://failfast.blob.core.windows.net/easy/bank-account/assets/checksuccess-blue.svg",
            "AppText":"xxxxxxx",
            "Button1Text":"ทำเลย",
            "Button2Text":"ยังก่อน",
            "NextEndpointUrl":"/api/subscriptions/topup/visit/default/topuplist?EndpointId=~newid",
        })        
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "account-ppay-confirm":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/bank-account/visit/default/display-result-dlg?EndpointId=" + SmCtx.SrcEndpointId,
            "Message":"คุณต้องการเติมเงินต่อหรือไม่",
            "Title":"ผูกบัญชีสำเร็จ",
            "Logo":"https://failfast.blob.core.windows.net/easy/bank-account/assets/checksuccess-blue.svg",
            "AppText":"xxxxxxx",
            "Button1Text":"ทำเลย",
            "Button2Text":"ยังก่อน",
            "NextEndpointUrl":"/api/subscriptions/topup/visit/default/topuplist?EndpointId=~newid",
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "account-editname":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/bank-account/visit/default/account-editname-complete?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "account-info":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/bank-account/visit/default/account-main?EndpointId=" + SmCtx.SrcEndpointId,
        })