-- local json = require 'Services\\LuaExecution\\json'
print("Hello, from the [startup] script!")
function ExecuteEndpoint()
    print(SmCtx.SrcFlow)
    if (string.lower(SmCtx.SrcFlow) == "try-lua" and string.lower(SmCtx.CallType) == "visit") then
        SmCtx:SetResult({
            Command = "Visit",
            EndpointUrl = "/api/subscriptions/topup/visit/default/topuplist?EndpointId=" .. SmCtx.SrcEndpointId
        })
    elseif (string.lower(SmCtx.SrcFlow) == "try-lua" and string.lower(SmCtx.CallType) == "get-data") then
        feeds = SmCtx:List("BizAccount")
        -- feeds = SmCtx:Get("BizAccount","00001")
        response = {
            name = 'im LUA',
            age = 22,
            status = 'die',
            feeds = feeds,
            testarray = {{
                aaa = "123",
                bbb = 456
            }, {
                aaa = "123",
                bbb = 456
            }}
        }
        SmCtx:SetResponse(feeds)
    elseif (string.lower(SmCtx.SrcFlow) == "try-lua" and string.lower(SmCtx.CallType) == "submit-data") then
        SmCtx:SetResult({
            Command = "Visit",
            EndpointUrl = "/api/subscriptions/topup/visit/default/topuplist?EndpointId=" .. SmCtx.SrcEndpointId
        })
    end
end
