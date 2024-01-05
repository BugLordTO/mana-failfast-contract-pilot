print("Hello, from the [n2m-consent.py] script!")

def ExecuteEndpoint():
    print("call SetContentLocation")
    SmCtx.SetContentLocation(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["ZipUrl"])
    
    print("call SetPageHeader")
    SmCtx.SetPageHeader(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["HeaderMode"],
        SmCtx.CrResultDicts["HeaderBaseUrl"],
        SmCtx.CrResultDicts["HeaderTitle"])
    
    print("call N2MConsent")
    SmCtx.N2MConsent(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["Flow"],
        SmCtx.CrResultDicts["EndpointId"],
        SmCtx.CrResultDicts["SubscriptionId"],
        
        SmCtx.CrResultDicts["SrcMcId"],
        SmCtx.CrResultDicts["SrcFlow"],
        SmCtx.CrResultDicts["SrcEndpointId"],
        SmCtx.CrResultDicts["SrcSubscriptionId"])

def ActionButton_Clicked():
    SmCtx.OnSubmit()

# def RejectButton_Clicked():
def CancelButton_Clicked():
    SmCtx.OnSubmit()

def ExecuteConsent():
    if SmCtx.CrResultDicts["Acceptance"] == "accept":
        SmCtx.SubmitToServer(SmCtx.CrResultDicts["HostBaseUrl"] + 
            "/api/subscriptions/" + SmCtx.CrResultDicts["DestSubscriptionId"] + 
            "/predefined-consent-accept/" + SmCtx.CrResultDicts["DestApiId"] + 
            "/" + SmCtx.CrResultDicts["DestPath"])
    elif SmCtx.CrResultDicts["Acceptance"] == "reject":
        SmCtx.SubmitToServer(SmCtx.CrResultDicts["HostBaseUrl"] + 
            "/api/subscriptions/" + SmCtx.CrResultDicts["DestSubscriptionId"] + 
            "/predefined-consent-reject/" + SmCtx.CrResultDicts["DestApiId"] + 
            "/" + SmCtx.CrResultDicts["DestPath"])
    else:
        print("call SetContentLocation for Dialog")
        SmCtx.SetContentLocation(
            SmCtx.CrResultDicts["DlgMcId"],
            SmCtx.CrResultDicts["DlgZipUrl"])

        print("call SetPageHeader for Dialog")
        SmCtx.SetPageHeader(
            SmCtx.CrResultDicts["DlgMcId"],
            SmCtx.CrResultDicts["DlgHeaderMode"],
            SmCtx.CrResultDicts["DlgHeaderBaseUrl"],
            SmCtx.CrResultDicts["DlgHeaderTitle"])

        print("call SetData")
        SmCtx.SetData({
            "Title":SmCtx.CrResultDicts["Title"] if SmCtx.CrResultDicts.ContainsKey("Title") is True else "",
            "Logo":SmCtx.CrResultDicts["Logo"] if SmCtx.CrResultDicts.ContainsKey("Logo") is True else "",
            "Message":SmCtx.CrResultDicts["Message"] if SmCtx.CrResultDicts.ContainsKey("Message") is True else "",
            "AppText":SmCtx.CrResultDicts["AppText"] if SmCtx.CrResultDicts.ContainsKey("AppText") is True else "",
        })

        print("call ShowOptionDlg")
        SmCtx.ShowOptionDlg(
            SmCtx.CrResultDicts["DlgMcId"],
            SmCtx.CrResultDicts["DlgFlow"],
            SmCtx.CrResultDicts["DlgEndpointId"],
            SmCtx.CrResultDicts["DlgSubscriptionId"],
            
            SmCtx.CrResultDicts["McId"],
            SmCtx.CrResultDicts["Flow"],
            SmCtx.CrResultDicts["EndpointId"],
            SmCtx.CrResultDicts["SubscriptionId"],

            SmCtx.CrResultDicts["Button1Text"] if SmCtx.CrResultDicts.ContainsKey("Button1Text") is True else "Close",
            SmCtx.CrResultDicts["Button2Text"] if SmCtx.CrResultDicts.ContainsKey("Button2Text") is True else "",
            SmCtx.CrResultDicts["Size"] if SmCtx.CrResultDicts.ContainsKey("Size") is True else "")