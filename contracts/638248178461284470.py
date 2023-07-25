import datetime

print("Hello, from the script!")

def ExecuteEndpoint():
    if SmCtx.EndpointType == "visit":
        ResultCtx.Command = "N2P"
    elif SmCtx.EndpointType == "get-data":
        ResultCtx.Command = "N2P"
    elif SmCtx.EndpointType == "submit-data":
        endpointSplit = SmCtx.EndpointId.split("-")
        entityid = endpointSplit[0]
        endpointCase = ""

        if len(endpointSplit) > 1:
            endpointCase = endpointSplit[1]
        else:
            endpointCase = SmCtx.EndpointId

        if endpointCase == "ConfirmPin":
            upper_flow_mcid = "638248194446880158"
            upper_flow_SubscriptionId= "638247291986347382"
            sess = SmCtx.GetAdhocSession(entityid)
            if sess is None:
                ResultCtx.Command = "Error"
                ResultCtx.EndpointId = "Session Id not found"

            else:
                SmCtx.SendNotification(SmCtx.UserId,
                    SmCtx.HostBaseUrl + "/api/visit/" + upper_flow_SubscriptionId + "?flow=billPage&endpointid=" + entityid + "-VisitBillSuccess")

                receiver = SmCtx.GetUser(sess.SrcId)
                SmCtx.SendNotification(receiver._id,
                    SmCtx.HostBaseUrl + "/api/visit/" + upper_flow_SubscriptionId + "?flow=dlgSuccess&endpointid=" + entityid + "-VisitQRSuccess")
            ResultCtx.Command = "Non"

        elif endpointCase == "VisitBillSuccess":
            ResultCtx.Command = "GoHome"

        elif endpointCase == "VisitQRSuccess":
            ResultCtx.Command = "GoHome"
