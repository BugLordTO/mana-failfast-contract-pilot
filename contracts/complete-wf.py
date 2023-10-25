print("Hello, from the [complete-wf.py] script!")

def ExecuteEndpoint():
    print("call CompleteWorkflow")
    SmCtx.CompleteWorkflow(SmCtx.CrResultDicts["EndpointId"])
