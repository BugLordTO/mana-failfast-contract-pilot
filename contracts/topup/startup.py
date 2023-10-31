print("Hello, from the [startup] script!")
def ExecuteEndpoint():
    print(SmCtx.SrcFlow.lower())
    if SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "topuplist":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/topup/visit/default/topuplist?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "topupqr-create":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/topup/visit/default/topupqr-confirm?EndpointId=" + SmCtx.SrcEndpointId,
        }) 
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "topup-create":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/topup/visit/default/topup-confirm?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "topupppay-create":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/topup/visit/default/topupppay-confirm?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "topupqr-confirm":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/topup/visit/default/topup-detail-response?EndpointId=" + SmCtx.SrcEndpointId,
            "SendOsNoti":"/api/subscriptions/topup/visit/default/topup-detail?EndpointId=" + SmCtx.SrcEndpointId,
            "OsNotiTitle":"กำลังส่งคำขอเติมเงินไปยัง",
            "OsNotiMessage":"พร้อมเพย์ 12345678 กรุณายืนยันที่ mobile banking ของคุณ",
            "SendInAppNoti":"/api/subscriptions/topup/visit/default/topup-detail?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "topup-confirm":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/topup/visit/default/topup-detail?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "topupppay-confirm":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/topup/visit/default/display-result-dlg-topup?EndpointId=" + SmCtx.SrcEndpointId,
            "Message":"พร้อมเพย์ 12345678 กรุณายืนยันที่ mobile banking ของคุณ",
            "Title":"กำลังส่งคำขอเติมเงินไปยัง",
            "Logo":"https://failfast.blob.core.windows.net/easy/bank-account/assets/topup.svg",
            "AppText":"Visit",
            "Button1Text":"ปิด",
            "Size":"m",
            "NextEndpointUrl":"/api/subscriptions/topup/visit/default/topup-bank-select?EndpointId=~newid",
            "SendOsNoti":"/api/subscriptions/topup/visit/default/display-result-dlg-topup?EndpointId=" + SmCtx.SrcEndpointId,
            "OsNotiTitle":"กำลังส่งคำขอเติมเงินไปยัง",
            "OsNotiMessage":"พร้อมเพย์ 12345678 กรุณายืนยันที่ mobile banking ของคุณ",
            "SendInAppNoti":"/api/subscriptions/topup/visit/default/display-result-dlg-topup?EndpointId=" + SmCtx.SrcEndpointId,
        })
    elif SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "topup-detail":
        SmCtx.SetResult({
            "Command":"Visit",
            "EndpointUrl":"/api/subscriptions/topup/visit/default/post-topup-qr-complete?EndpointId=" + SmCtx.SrcEndpointId,
        })