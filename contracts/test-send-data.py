print("Hello, from the [startup] script!")

def ExecuteEndpoint():
    SetResponse_PythonModel()
    # SetResponse_JsonString()
    # SetResponse_JsonModel()

    # UseBody_JsonNode()
    # UseBody_JsonString()

############################### SetResponse_PythonModel

def SetResponse_PythonModel():
    oil = OilModel("benzene", 95)
    gear1 = GearModel("Helical", 48)
    gear2 = GearModel("Spiral", 36)
    gears = []
    gears.append(gear1)
    gears.append(gear2)
    engine = VehicleEngineModel(oil, 1500, gears)
    vehicle = VehicleModel("vh001", 4, engine)

    SmCtx.SetResponse(vehicle)

class OilModel:
    def __init__(self, oilType, octain):
        self.oilType = oilType
        self.octain = octain

class GearModel:
    def __init__(self, gearType, cog):
        self.gearType = gearType
        self.cog = cog

class VehicleEngineModel:
    def __init__(self, engineType, capacityInCC, gears):
        self.engineType = engineType
        self.capacityInCC = capacityInCC
        self.gears = gears

class VehicleModel:
    def __init__(self, bodyNo, wheel, engine):
        self.bodyNo = bodyNo
        self.wheel = wheel
        self.engine = engine

############################### SetResponse_JsonString

def SetResponse_JsonString():
    SmCtx.SetJsonResponse('''{
        "stringField":"test string",
        "intField": 36,
        "floatField": 15.5,
        "dateTimeField": "2023-06-22T00:00:09.000Z",
        "nestedObjectField": {
            "nestedStringField":"test string",
            "nestedIntField": 0,
            "nestedFloatField": 0.5,
            "nestedDateTimeField": "2023-06-22T00:00:00.000Z"
        },
        "stringArrayField":[
            "item 1",
            "item 2",
            "item 3"
        ],
        "intArrayField":[
            1,
            2,
            3
        ],
        "objectArrayField":[
            {
                "nestedStringField":"object item 1",
                "nestedIntField": 1,
                "nestedFloatField": 1.5,
                "nestedDateTimeField": "2023-06-22T00:00:01.001Z"
            },
            {
                "nestedStringField":"object item 2",
                "nestedIntField": 2,
                "nestedFloatField": 2.5,
                "nestedDateTimeField": "2023-06-22T00:00:02.002Z"
            },
            {
                "nestedStringField":"object item 3",
                "nestedIntField": 3,
                "nestedFloatField": 3.5,
                "nestedDateTimeField": "2023-06-22T00:00:03.003Z"
            },
            {
                "nestedStringField":"object item 4",
                "nestedIntField": 4,
                "nestedFloatField": 4.5,
                "nestedDateTimeField": "2023-06-22T00:00:04.004Z"
            }
        ]
    }''') # ✅

############################### SetResponse_JsonModel

def SetResponse_JsonModel():
    SmCtx.SetJsonResponse({
        "stringField":"test string",
        "intField": 36,
        "floatField": 15.5,
        "dateTimeField": "2023-06-22T00:00:09.000Z",
        "nestedObjectField": {
            "nestedStringField":"test string",
            "nestedIntField": 0,
            "nestedFloatField": 0.5,
            "nestedDateTimeField": "2023-06-22T00:00:00.000Z"
        },
        "stringArrayField":[
            "item 1",
            "item 2",
            "item 3"
        ],
        "intArrayField":[
            1,
            2,
            3
        ],
        "objectArrayField":[
            {
                "nestedStringField":"object item 1",
                "nestedIntField": 1,
                "nestedFloatField": 1.5,
                "nestedDateTimeField": "2023-06-22T00:00:01.001Z"
            },
            {
                "nestedStringField":"object item 2",
                "nestedIntField": 2,
                "nestedFloatField": 2.5,
                "nestedDateTimeField": "2023-06-22T00:00:02.002Z"
            },
            {
                "nestedStringField":"object item 3",
                "nestedIntField": 3,
                "nestedFloatField": 3.5,
                "nestedDateTimeField": "2023-06-22T00:00:03.003Z"
            },
            {
                "nestedStringField":"object item 4",
                "nestedIntField": 4,
                "nestedFloatField": 4.5,
                "nestedDateTimeField": "2023-06-22T00:00:04.004Z"
            }
        ]
    }) # ✅

############################### UseBody_JsonNode

def UseBody_JsonNode():
    body = SmCtx.GetSubmitBody()

    print(body["stringField"])
    print(body["intField"])
    print(body["floatField"])
    print(body["dateTimeField"])

    print(body["nestedObjectField"]["nestedStringField"])
    print(body["nestedObjectField"]["nestedIntField"])
    print(body["nestedObjectField"]["nestedFloatField"])
    print(body["nestedObjectField"]["nestedDateTimeField"])

    print(body["stringArrayField"][0])
    print(body["stringArrayField"][1])
    print(body["stringArrayField"][2])

    print(body["intArrayField"][0])
    print(body["intArrayField"][1])
    print(body["intArrayField"][2])

    print(body["objectArrayField"][0]["nestedStringField"])
    print(body["objectArrayField"][1]["nestedIntField"])
    print(body["objectArrayField"][2]["nestedFloatField"])
    print(body["objectArrayField"][3]["nestedDateTimeField"])

############################### UseBody_JsonString

def UseBody_JsonString():
    body = SmCtx.GetSubmitBodyAsJson()
    print(body)
