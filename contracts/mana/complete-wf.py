print("Hello, from the [complete-wf.py] script!")

# - complete worlflow

def ExecuteEndpoint():
    print("call CompleteWorkflow")
    SmCtx.CompleteWorkflow(SmCtx.CrResultDicts["EndpointId"])
