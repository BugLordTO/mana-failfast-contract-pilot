print("Hello, from the [get-data] script!")

# # DB get-data ใช้ "EndpointType" : "smart-contract" ได้แล้ว
# {
#     "Path" : "verify-otp",
#     "Url" : "https://failfast.blob.core.windows.net/easy/test-startup/get-data.py",
#     "EndpointType" : "smart-contract",
#     "CallType" : "get-data"
# }, 

# # submit หน้าเลือก bank แล้ว visit หน้า confirm ตาม bank ที่เลือก
# def ExecuteEndpoint():
#     body = SmCtx.GetSubmitBody()
#     if SmCtx.SrcFlow and SmCtx.SrcFlow.lower() == "bank-select":
#         if body["bank"] == "ppay":
#             SmCtx.SetResult({
#                 "Command":"Visit",
#                 "EndpointUrl":"/api/subscriptions/sub-startup/visit/default/confirm-page?endpointId=bank-gsb",
#             })
#         elif body["bank"] == "bank-ktb":
#             SmCtx.SetResult({
#                 "Command":"Visit",
#                 "EndpointUrl":"/api/subscriptions/sub-startup/visit/default/confirm-page?endpointId=bank-ktb",
#             })
#         elif body["bank"] == "bank-gsb":
#             SmCtx.SetResult({
#                 "Command":"Visit",
#                 "EndpointUrl":"/api/subscriptions/sub-startup/visit/default/confirm-page?endpointId=bank-gsb",
#             })

# get data หน้า confirm (get-data.py)
def ExecuteEndpoint():
    if SmCtx.EndpointId == "ppay":
        SmCtx.SetResponse({
            "logo": "https://blob.com/ppay.png",
            "bank": "PPay",
            "name": "Mr.anon bangsan",
        })
    elif SmCtx.EndpointId == "bank-ktb":
        SmCtx.SetResponse({
            "logo": "https://blob.com/ktb.png",
            "bank": "KTB",
            "name": "Mr.anon bangsan",
        })
    elif SmCtx.EndpointId == "bank-gsb":
        SmCtx.SetResponse({
            "logo": "https://blob.com/gsb.png",
            "bank": "GSB",
            "name": "Mr.anon bangsan",
        })