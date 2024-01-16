print("Hello, from the [complete-dlg-content-next2.py] script!")

# - open complete dialog
# - mcontent
# - 2 button 
#   1 complete workflow
#   2 visit next url

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

    print("call ShowResultDlg")
    SmCtx.ShowResultDlg(
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
    print("call CompleteWorkflow")
    SmCtx.CompleteWorkflow(SmCtx.CrResultDicts["EndpointId"])

def CancelButton_Clicked():
    print("call Visit")
    SmCtx.Visit(SmCtx.CrResultDicts["HostBaseUrl"] + SmCtx.CrResultDicts["NextEndpointUrl"])

    print("call CompleteWorkflow")
    SmCtx.CompleteWorkflow(SmCtx.CrResultDicts["EndpointId"])
