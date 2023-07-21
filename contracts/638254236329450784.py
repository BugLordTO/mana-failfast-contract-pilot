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

        if endpointCase == "VisitM1":
            request = SmCtx.Body

            wallets = SmCtx.GetCurrentUserWallet(request.WalletId)

            #//TODO: คำนวณตัง
            sess = SmCtx.GetAdhocSession(entityid)

            sess_Amount_Currency = sess.Amount.Currency
            sess_Amount_AmountUnit = SmCtx.Body.Amount * 1000
            sess_Remark = request.Remark
            sess_SrcAccountNo = wallets._id
            sess_SrcSubName = wallets.WalletName

            #//TODO : คำนวนค่าธรรมเนียม
            #//    totalAmount = amount + fee + sourceFee + sourceFee
            biz = SmCtx.GetSubscribeBizAccount(sess.DestId)

            if wallets.Balance.Currency == biz.Wallet.Balance.Currency:
                sess_Fee_Currency = sess_Amount_Currency
                sess_Fee_AmountUnit = sess.Fee.AmountUnit
                sess_TotalFee_Currency = sess_Amount_Currency
                sess_TotalFee_AmountUnit = sess_Fee_AmountUnit
                sess_TotalAmount_Currency = sess_Amount_Currency
                sess_TotalAmount_AmountUnit = sess_Amount_AmountUnit + sess_Fee_AmountUnit

                SmCtx.UpdateM1SessionSameCurrency(entityid,
                    sess_Amount_Currency,
                    sess_Amount_AmountUnit,
                    sess_Remark,
                    sess_SrcAccountNo,
                    sess_SrcSubName,

                    sess_Fee_Currency,
                    sess_Fee_AmountUnit,
                    sess_TotalFee_Currency,
                    sess_TotalFee_AmountUnit,
                    sess_TotalAmount_Currency,
                    sess_TotalAmount_AmountUnit)

                ResultCtx.Command = "N2P"
                ResultCtx.SubscriptionId = SmCtx.SubscriptionId
                ResultCtx.McId = SmCtx.McId
                ResultCtx.Flow = "cartConfirmPage"
                ResultCtx.EndpointId = "{entityid}-GetM2Data".format(entityid = entityid)
            else:
                #//get rate
                sess_RateRequest_Amount = sess_Amount_AmountUnit
                sess_RateRequest_Direction = "SrcFromDest"
                sess_RateRequest_SrcCurrency = wallets.Balance.Currency
                sess_RateRequest_DestCurrency = biz.Wallet.Balance.Currency

                rate = SmCtx.GetMexRate(
                    sess_Amount_AmountUnit,
                    sess_RateRequest_Direction,
                    sess_RateRequest_SrcCurrency,
                    sess_RateRequest_DestCurrency)

                sess_Rate_RateId = rate.RateId
                sess_Rate_Rate = rate.Rate
                sess_Rate_SrcFee_Currency = rate.SrcFee.Currency
                sess_Rate_SrcFee_AmountUnit = rate.SrcFee.AmountUnit
                sess_Rate_DestFee_Currency = rate.DestFee.Currency
                sess_Rate_DestFee_AmountUnit = rate.DestFee.AmountUnit
                sess_Rate_PreCalculateAmount_Currency = rate.PreCalculateAmount.Currency
                sess_Rate_PreCalculateAmount_AmountUnit = rate.PreCalculateAmount.AmountUnit
                sess_Rate_CalculatedAmount_Currency = rate.CalculatedAmount.Currency
                sess_Rate_CalculatedAmount_AmountUnit = rate.CalculatedAmount.AmountUnit
                sess_Rate_RateExpiration = rate.RateExpiration

                #//define amount and fee between Same currency and Diff currency
                preSum_Currency = sess_RateRequest_DestCurrency
                preSum_AmountUnit = sess_Amount_AmountUnit
                shopFee_Currency = sess.Fee.Currency; #// shop service fee
                shopFee_AmountUnit = sess.Fee.AmountUnit; #// shop service fee
                discount_Currency = sess_RateRequest_DestCurrency
                discount_AmountUnit = 0
                mexFee = SmCtx.GetTotalFee(
                    sess_RateRequest_DestCurrency,
                    sess_Amount_AmountUnit,
                    sess_RateRequest_Direction,
                    sess_RateRequest_SrcCurrency,
                    sess_RateRequest_DestCurrency)
                totalFeePlusShopFee_Currency = mexFee.Currency
                totalFeePlusShopFee_AmountUnit = mexFee.AmountUnit + shopFee_AmountUnit
                totalAmount_Currency = sess_RateRequest_DestCurrency
                totalAmount_AmountUnit = sess_Rate_PreCalculateAmount_AmountUnit + discount_AmountUnit + shopFee_AmountUnit
                exchangeAmount_Currency = sess_Rate_CalculatedAmount_Currency
                exchangeAmount_AmountUnit = sess_Rate_CalculatedAmount_AmountUnit

                sess_Fee_Currency = shopFee_Currency
                sess_Fee_AmountUnit = shopFee_AmountUnit
                sess_Discount_Currency = discount_Currency
                sess_Discount_AmountUnit = discount_AmountUnit
                sess_TotalAmount_Currency = totalAmount_Currency
                sess_TotalAmount_AmountUnit = totalAmount_AmountUnit
                sess_TotalFee_Currency = totalFeePlusShopFee_Currency
                sess_TotalFee_AmountUnit = totalFeePlusShopFee_AmountUnit
                rateSrcCurrency = SmCtx.ConvertToSrcCurrency(
                    sess_Amount_AmountUnit,
                    sess_RateRequest_Direction,
                    sess_RateRequest_SrcCurrency,
                    sess_RateRequest_DestCurrency,
                    sess_RateRequest_SrcCurrency,
                    sess_Fee_Currency,
                    sess_Fee_AmountUnit)
                sess_ExchangeAmount_Currency = exchangeAmount_Currency
                sess_ExchangeAmount_AmountUnit = exchangeAmount_AmountUnit + rateSrcCurrency.AmountUnit
                sess_RateDisplay = str(sess_Rate_Rate) + " " + sess_RateRequest_SrcCurrency + "/" + sess_RateRequest_DestCurrency
                sess_SourceFee_Currency = sess_Rate_SrcFee_Currency
                sess_SourceFee_AmountUnit = sess_Rate_SrcFee_AmountUnit
                sess_DestinationFee_Currency = sess_Rate_DestFee_Currency
                sess_DestinationFee_AmountUnit = sess_Rate_DestFee_AmountUnit

                SmCtx.UpdateM1SessionDifferentCurrency(entityid,
                    sess_Amount_Currency,
                    sess_Amount_AmountUnit,
                    sess_Remark,
                    sess_SrcAccountNo,
                    sess_SrcSubName,
                    
                    sess_RateRequest_Amount,
                    sess_RateRequest_Direction,
                    sess_RateRequest_SrcCurrency,
                    sess_RateRequest_DestCurrency,

                    sess_Rate_RateId,
                    sess_Rate_Rate,
                    sess_Rate_SrcFee_Currency,
                    sess_Rate_SrcFee_AmountUnit,
                    sess_Rate_DestFee_Currency,
                    sess_Rate_DestFee_AmountUnit,
                    sess_Rate_PreCalculateAmount_Currency,
                    sess_Rate_PreCalculateAmount_AmountUnit,
                    sess_Rate_CalculatedAmount_Currency,
                    sess_Rate_CalculatedAmount_AmountUnit,
                    sess_Rate_RateExpiration,

                    sess_Fee_Currency,
                    sess_Fee_AmountUnit,
                    sess_Discount_Currency,
                    sess_Discount_AmountUnit,
                    sess_TotalAmount_Currency,
                    sess_TotalAmount_AmountUnit,
                    sess_TotalFee_Currency,
                    sess_TotalFee_AmountUnit,
                    sess_ExchangeAmount_Currency,

                    sess_ExchangeAmount_AmountUnit,
                    sess_RateDisplay,
                    sess_SourceFee_Currency,
                    sess_SourceFee_AmountUnit,
                    sess_DestinationFee_Currency,
                    sess_DestinationFee_AmountUnit)

                ResultCtx.Command = "N2P"
                ResultCtx.SubscriptionId = SmCtx.SubscriptionId
                ResultCtx.McId = SmCtx.McId
                ResultCtx.Flow = "exchangePage"
                ResultCtx.EndpointId = "{entityid}-GetMexData".format(entityid = entityid)

        elif endpointCase == "GetMexData":
            ResultCtx.Command = "N2P"
            ResultCtx.SubscriptionId = SmCtx.SubscriptionId
            ResultCtx.McId = SmCtx.McId
            ResultCtx.Flow = "cartConfirmPage"
            ResultCtx.EndpointId = "{entityid}-GetM2Data".format(entityid = entityid)

        elif endpointCase == "GetM2Data":
            SmCtx.ExecuteSession(entityid)

            ResultCtx.Command = "N2P"
            ResultCtx.SubscriptionId = SmCtx.SubscriptionId
            ResultCtx.McId = SmCtx.McId
            ResultCtx.Flow = "pin"
            ResultCtx.EndpointId = "{entityid}-ConfirmPin".format(entityid = entityid)
