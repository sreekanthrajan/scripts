import csv

writer = csv.writer(open('/home/srrajan/Desktop/partner migration/python/final.csv', 'wb'))
headline=['Partner code','POS','GB','$txn','Profit','Markup','Fee','Tax']
writer.writerow(headline)

reader = csv.DictReader(open('/home/srrajan/Desktop/partner migration/python/All partners.csv', 'rb'))
for row in reader:
        GB=''
        txn=''
        Profit=''
        Tax=''
        Markup=''
        Fee=''        
        partnercode = row['PARTNER_CODE']
        pos=str(partnercode).split("_")[0]
        pricingmodel = row['PRICING_\nMODEL_NAME']
        if 'Booking' in str(pricingmodel):
            GB='Yes'
        elif 'Transaction' in str(pricingmodel):
            txn='Yes'
        elif 'Profit' in str(pricingmodel):
            Profit='Yes'
        elif 'Formula' in str(pricingmodel):
            formula = row['FORMULA']
            if 'totalComponentTax' in str(formula) or 'hotelComponentTax' in str(formula):
                Tax='Yes'
            if 'baseMarkupAmount' in str(formula) or 'hotelPropertyMarkup' in str(formula) or 'distributionPartnerMarkup' in str(formula) or 'hotelMarkupAllRooms' in str(formula):
                Markup='Yes'
            if 'distributorFee' in str(formula) or 'distPartnerFee' in str(formula) or 'optiFee' in str(formula) or 'customerServiceFee' in str(formula) or 'hotelServiceFee' in str(formula) or 'hotelOptifee'  in str(formula) or 'distributorFeeAllRooms'  in str(formula): 
                Fee='Yes'
            exceptionformula = ['EXCEPTION_\nFORMULA1']
            if 'totalComponentTax' in str(exceptionformula) or 'hotelComponentTax' in str(exceptionformula):
                Tax='Yes'
            if 'baseMarkupAmount' in str(exceptionformula) or 'hotelPropertyMarkup' in str(exceptionformula) or 'distributionPartnerMarkup' in str(exceptionformula) or 'hotelMarkupAllRooms' in str(exceptionformula):
                Markup='Yes'
            if 'distributorFee' in str(exceptionformula) or 'distPartnerFee' in str(exceptionformula) or 'optiFee' in str(exceptionformula) or 'customerServiceFee' in str(exceptionformula) or 'hotelServiceFee' in str(exceptionformula) or 'hotelOptifee' in str(exceptionformula) or 'distributorFeeAllRooms'  in str(exceptionformula): 
                Fee='Yes'
        data=[partnercode,pos,GB,txn,Profit,Markup,Fee,Tax]
        print data
        writer.writerow(data)
       
        
        
        
        

            
            