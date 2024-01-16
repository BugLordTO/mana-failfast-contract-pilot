print("Hello, from the [dlg-msg-confirm.py] script!")

# - open confirm dialog
# - msg mcontent
# - 2 button 
#   1 submit to server
#   2 close dialog

def ExecuteEndpoint():
    print("call SetContentLocation for Dialog")
    SmCtx.SetContentLocation(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["ZipUrl"])

    print("call SetPageHeader for Dialog")
    SmCtx.SetPageHeader(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["HeaderMode"],
        SmCtx.CrResultDicts["HeaderBaseUrl"],
        SmCtx.CrResultDicts["HeaderTitle"])

    print("call SetData")
    SmCtx.SetData({
        "Title":SmCtx.CrResultDicts["Title"] if SmCtx.CrResultDicts.ContainsKey("Title") is True else "",
        "Logo":SmCtx.CrResultDicts["Logo"] if SmCtx.CrResultDicts.ContainsKey("Logo") is True else "",
        "Message":SmCtx.CrResultDicts["Message"] if SmCtx.CrResultDicts.ContainsKey("Message") is True else "",
        "AppText":SmCtx.CrResultDicts["AppText"] if SmCtx.CrResultDicts.ContainsKey("AppText") is True else "",
    })

    print("call ShowConfirmDlg")
    SmCtx.ShowConfirmDlg(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["Flow"],
        SmCtx.CrResultDicts["EndpointId"],
        SmCtx.CrResultDicts["SubscriptionId"],
        
        SmCtx.CrResultDicts["SrcMcId"],
        SmCtx.CrResultDicts["SrcFlow"],
        SmCtx.CrResultDicts["SrcEndpointId"],
        SmCtx.CrResultDicts["SrcSubscriptionId"],

        SmCtx.CrResultDicts["Button1Text"] if SmCtx.CrResultDicts.ContainsKey("Button1Text") is True else "Ok",
        SmCtx.CrResultDicts["Button2Text"] if SmCtx.CrResultDicts.ContainsKey("Button2Text") is True else "Cancel",
        SmCtx.CrResultDicts["Size"] if SmCtx.CrResultDicts.ContainsKey("Size") is True else "")

def ActionButton_Clicked():
    print("call SubmitToServer")
    SmCtx.SubmitToServer(SmCtx.CrResultDicts["HostBaseUrl"] + SmCtx.CrResultDicts["SubmitUrl"])

def CancelButton_Clicked():
    print("call CloseDialog")
    SmCtx.CloseDialog(SmCtx.CrResultDicts["EndpointId"])
