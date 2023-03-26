currencyDict = {
    "1.  US dollar (USD)" : 0.0094,
    "2.  Algerian dinner (DZD)" : 1.2828,
    "3.  Argentine peso (ARS)" : 1.7897,
    "4.  Australian dollar (AUD)" : 0.0136,
    "5.  Bahrain dinner (BHD)" : 0.0035,
    "6.  Belarus rubel (BYN)" : 0.0237,
    "7.  Brazilian real (BRL)" : 0.049,
    "8.  Brunei ringgit (BND)" : 0.0125,
    "9.  Burmese kyat (MMK)" : 19.7353,
    "10. Combodian riel (KHR)" : 38.5,
    "11. Canadian dollar (CAD)" : 0.0125,
    "12. Chilean peso (CLP)" : 7.4972,
    "13. Chinese yuan (CNY)" : 0.064,
    "14. Colombian peso (COP)" : 45.1635,
    "15. Costa Rican Colon (CRC)" : 5.3772,
    "16. Danish krone (DKK)" : 0.0655,
    "17. Egyptian pound (EGP)" : 0.2853,
    "18. Euro (EUR)" : 0.0088,
    "19. Hong Kong dollar (HKD)" : 0.0737,
    "20. Hungarian forint (HUF)" : 3.4061,
    "21. Icelandic krona (ISK)" : 1.3399,
    "22. Indian rupee (INR)" : 0.7752,
    "23. Indonesian rupiah (IDR)" : 142.3333,
    "24. Iranian rial (IRR)" : 391.4167,
    "25. Iraqi dinar (IQD)" : 13.7139,
    "26. Japanese yen (JPY)" : 1.2346,
    "27. Kuwati dinar (KWD)" : 0.0029,
    "28. Malaysian ringgit (MYR)" : 0.0407,
    "29. Mexican peso (MXN)" : 0.1753,
    "30. Moroccan dirham (MAD)" : 0.0965,
    "31. Nepalis ropee (NPR)" : 1.2401,
    "32. New Taiwan dollar (TWD)" : 0.2837,
    "33. New Zealand dollar (NZD)" : 0.0149,
    "34. Omani rial (OMR)" : 0.0036,
    "35. Pakistani rupee (PKR)" : 2.5341,
    "36. Philippines peso (PHP)" : 0.5117,
    "37. Polish zloty (PLN)" : 0.042,
    "38. Qatari riyal (QAR)" : 0.0343,
    "39. Romanian leu (RON)" : 0.0431,
    "40. Russian ruble (RUB)" : 0.6868,
    "41. Saudi riyal (SAR)" : 0.0353,
    "42. Singapore dollar (SGD)" : 0.0127,
    "43. South Africa rand (ZAR)" : 0.1684,
    "44. Sri Lankan rupee (LKR)" : 3.4285,
    "45. Swiss france (CHF)" : 0.0087,
    "46. Syrian pound (SYP)" : 23.603,
    "47. Thai baht (THB)" : 0.3164,
    "48. Turkey lira (TRY)" : 0.1768,
    "49. UAE dirham (AED)" : 0.0345,
    "50. Vietnamese dong (VNG)" : 223.6667
}

print("____________________________________________\nI am learning more! \nNow i just convert 'BDT' to 50 currency!\nHere the list of currency you can convert!\n")

try:
    amount = int(input("Enter your amount of BDT: "))
    print()
except Exception as e:
	print("\nEnter valid amount!\n")
	exit()

[print(item) for item in currencyDict.keys()]

currency = input("\n_____________________________\nEnter the 'currency number' which you want to convert: ")




if currency == "1":
    total = amount*0.0094
    print(f"\n{amount} BDT is equal to {total:.3f} US dollar (USD)")
   
elif currency == "2":
    total = amount*1.2828
    print(f"\n{amount} BDT is equal to {total:.3f} Algerian dinner (DZD)")
    
elif currency == "3":
    total = amount*1.7897
    print(f"\n{amount} BDT is equal to {total:.3f} Argentine peso (ARS)")
    
elif currency == "4":
    total = amount*0.0136
    print(f"\n{amount} BDT is equal to {total:.3f} Australian dollar (AUD)")
   
elif currency == "5":
    total = amount*0.0035
    print(f"\n{amount} BDT is equal to {total:.3f} Bahrain dinner (BHD)")
    
elif currency == "6":
    total = amount*0.0237
    print(f"\n{amount} BDT is equal to {total:.3f} Belarus rubel (BYN)")
    
elif currency == "7":
    total = amount*0.049
    print(f"\n{amount} BDT is equal to {total:.3f} Brazilian real (BRL)")
    
elif currency == "8":
    total = amount*0.0125
    print(f"\n{amount} BDT is equal to {total:.3f} Brunei ringgit (BND)")
   
elif currency == "9":
    total = amount*19.7353
    print(f"\n{amount} BDT is equal to {total:.3f} Burmese kyat (MMK)")
    
elif currency == "10":
    total = amount*38.5
    print(f"\n{amount} BDT is equal to {total:.3f} Combodian riel (KHR)")
    
elif currency == "11":
    total = amount*0.0125
    print(f"\n{amount} BDT is equal to {total:.3f} Canadian dollar (CAD)")

elif currency == "12":
    total = amount*7.4972
    print(f"\n{amount} BDT is equal to {total:.3f} Chilean peso (CLP)")
    
elif currency == "13":
    total = amount*0.064
    print(f"\n{amount} BDT is equal to {total:.3f} Chinese yuan (CNY)")
    
elif currency == "14":
    total = amount*45.1635
    print(f"\n{amount} BDT is equal to {total:.3f} Colombian peso (COP)")
   
elif currency == "15":
    total = amount*5.3772
    print(f"\n{amount} BDT is equal to {total:.3f} Costa Rican Colon (CRC)")
    
elif currency == "16":
    total = amount*0.0655
    print(f"\n{amount} BDT is equal to {total:.3f} Danish krone (DKK)")
    
elif currency == "17":
    total = amount*0.2853
    print(f"\n{amount} BDT is equal to {total:.3f} Egyptian pound (EGP)")
    
elif currency == "18":
    total = amount*0.0088
    print(f"\n{amount} BDT is equal to {total:.3f} Euro (EUR)")
   
elif currency == "19":
    total = amount*0.0737
    print(f"\n{amount} BDT is equal to {total:.3f} Hong Kong dollar (HKD)")
    
elif currency == "20":
    total = amount*3.4061
    print(f"\n{amount} BDT is equal to {total:.3f} Hungarian forint (HUF)")
    
elif currency == "21":
    total = amount*1.3399
    print(f"\n{amount} BDT is equal to {total:.3f} Icelandic krona (ISK)")
    
elif currency == "22":
    total = amount*0.7752
    print(f"\n{amount} BDT is equal to {total:.3f} Indian rupee (INR)")
    
elif currency == "23":
    total = amount*142.3333
    print(f"\n{amount} BDT is equal to {total:.3f} Indonesian rupiah (IDR)")
    
elif currency == "24":
    total = amount*391.4167
    print(f"\n{amount} BDT is equal to {total:.3f} Iranian rial (IRR)")
   
elif currency == "25":
    total = amount*13.7139
    print(f"\n{amount} BDT is equal to {total:.3f} Iraqi dinar (IQD)")
    
elif currency == "26":
    total = amount*1.2346
    print(f"\n{amount} BDT is equal to {total:.3f} Japanese yen (JPY)")
    
elif currency == "27":
    total = amount*0.0029
    print(f"\n{amount} BDT is equal to {total:.3f} Kuwati dinar (KWD)")
    
elif currency == "28":
    total = amount*0.0407
    print(f"\n{amount} BDT is equal to {total:.3f} Malaysian ringgit (MYR)")
   
elif currency == "29":
    total = amount*0.1753
    print(f"\n{amount} BDT is equal to {total:.3f} Mexican peso (MXN)")
    
elif currency == "30":
    total = amount*0.0965
    print(f"\n{amount} BDT is equal to {total:.3f} Moroccan dirham (MAD)")
    
elif currency == "31":
    total = amount*1.2401
    print(f"\n{amount} BDT is equal to {total:.3f} Nepalis ropee (NPR)")
    
elif currency == "32":
    total = amount*0.2837
    print(f"\n{amount} BDT is equal to {total:.3f} New Taiwan dollar (TWD)")
    
elif currency == "33":
    total = amount*0.0149
    print(f"\n{amount} BDT is equal to {total:.3f} New Zealand dollar (NZD)")
    
elif currency == "34":
    total = amount*0.0036
    print(f"\n{amount} BDT is equal to {total:.3f} Omani rial (OMR)")
   
elif currency == "35":
    total = amount*2.5341
    print(f"\n{amount} BDT is equal to {total:.3f} Pakistani rupee (PKR)")
    
elif currency == "36":
    total = amount*0.5117
    print(f"\n{amount} BDT is equal to {total:.3f} Philippines peso (PHP)")
    
elif currency == "37":
    total = amount*0.042
    print(f"\n{amount} BDT is equal to {total:.3f} Polish zloty (PLN)")
    
elif currency == "38":
    total = amount*0.0343
    print(f"\n{amount} BDT is equal to {total:.3f} Qatari riyal (QAR)")
   
elif currency == "39":
    total = amount*0.0431
    print(f"\n{amount} BDT is equal to {total:.3f} Romanian leu (RON)")
    
elif currency == "40":
    total = amount*0.6868
    print(f"\n{amount} BDT is equal to {total:.3f} Russian ruble (RUB)")
    
elif currency == "41":
    total = amount*0.0353
    print(f"\n{amount} BDT is equal to {total:.3f} to Saudi riyal (SAR)")
    
elif currency == "42":
    total = amount*0.0127
    print(f"\n{amount} BDT is equal to {total:.3f} Singapore dollar (SGD)")
    
elif currency == "43":
    total = amount*0.1684
    print(f"\n{amount} BDT is equal to {total:.3f} South Africa rand (ZAR)")
    
elif currency == "44":
    total = amount*3.4285
    print(f"\n{amount} BDT is equal to {total:.3f} Sri Lankan rupee (LKR)")
   
elif currency == "45":
    total = amount*0.0087
    print(f"\n{amount} BDT is equal to {total:.3f} Swiss france (CHF)")
    
elif currency == "46":
    total = amount*23.603
    print(f"\n{amount} BDT is equal to {total:.3f} Syrian pound (SYP)")
    
elif currency == "47":
    total = amount*0.3164
    print(f"\n{amount} BDT is equal to {total:.3f} Thai baht (THB)")
    
elif currency == "48":
    total = amount*0.1768
    print(f"\n{amount} BDT is equal to {total:.3f} Turkey lira (TRY)")
   
elif currency == "49":
    total = amount*0.0345
    print(f"\n{amount} BDT is equal to {total:.3f} UAE dirham (AED)")
    
elif currency == "50":
    total = amount*223.6667
    print(f"\n{amount} BDT is equal to {total:.3f} Vietnamese dong (VNG)")
    
else:
    print("Please input valid currency number!")