print("Hello, from the [n2m] script!")
function ExecuteEndpoint()
    print("call SetContentLocation")
    SmCtx:SetContentLocation(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["ZipUrl"])
    
    print("call SetPageHeader")
    SmCtx:SetPageHeader(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["HeaderMode"],
        SmCtx.CrResultDicts["HeaderBaseUrl"],
        SmCtx.CrResultDicts["HeaderTitle"])
    
    print("call N2M")
    SmCtx:N2M(
        SmCtx.CrResultDicts["McId"],
        SmCtx.CrResultDicts["Flow"],
        SmCtx.CrResultDicts["EndpointId"],
        SmCtx.CrResultDicts["SubscriptionId"],
        
        SmCtx.CrResultDicts["SrcMcId"],
        SmCtx.CrResultDicts["SrcFlow"],
        SmCtx.CrResultDicts["SrcEndpointId"],
        SmCtx.CrResultDicts["SrcSubscriptionId"])
end

function ActionButton_Clicked()
    SmCtx:OnSubmit()
end
