print("Hello, from the [complete-wf-next.py] script!")

# - complete worlflow
# - visit next url

def ExecuteEndpoint():
    print("call CompleteWorkflow")
    SmCtx.CompleteWorkflow(SmCtx.CrResultDicts["EndpointId"])
    
    print("call Visit")
    SmCtx.Visit(SmCtx.CrResultDicts["HostBaseUrl"] + SmCtx.CrResultDicts["NextEndpointUrl"])

