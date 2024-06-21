def GET_TFL(A1,A2,A3,A4,B1,B2,B3,B4):
  def iff(condition1, condition2): #<->
      return condition1 == condition2
    
  def chain(condition1,condition2): #->
      if ((condition1==True) and (condition2==False)):
        return False
      else:
        return True
  def reject(condition1):
    if (condition1==True):
      return False
    else:
      return True
  count_A=sum([A1,A2,A3,A4])
  count_B=sum([B1,B2,B3,B4])
  if ((count_A==0) and (count_B==1)):

    AB = chain(((reject(A1) or B1) and (reject(A2) and reject(A3) and reject(A4))),(reject(B2) and reject(B3) and reject(B4)))
    if (((iff(AB,A1)==False) and (iff(AB,B1)==True)) and (AB==True)):
      return "RED","GREEN","NORMAL","1"
  
  elif ((count_A==1) and (count_B==0)):
    AB = chain(((reject(A1) or B1) and (reject(A2) and reject(A3) and reject(A4))),(reject(B2) and reject(B3) and reject(B4)))
    if (((iff(AB,A1)==True) and (iff(AB,B1)==False)) and (AB==True)):
      return "GREEN","RED","NORMAL","2"
  
  elif ((count_A==0) and (count_B==2)):
    AB = iff(((reject(A1)or B1) and (reject(A2) or B2) and (reject(A3) and reject(A4))),(reject(B3) and reject(B4)))
    if (((iff(AB,(A1 and A2))==False) and (iff(AB,(B1 and B2))==True)) and (AB==True)):
      return "RED","GREEN","NORMAL","3"
  
  elif ((count_A==2) and (count_B==0)):
    AB = iff(((A1 or reject(B1)) and (A2 or reject(B2)) and (reject(A3) and reject(A4))),(reject(B3) and reject(B4)))
    if (((iff(AB,(A1 and A2))==True) and (iff(AB,(B1 and B2))==False)) and (AB==True)):
      return "GREEN","RED","NORMAL","4"
  
  elif ((count_A==0) and (count_B==3)):
    AB = ((reject(A1) or B1) and (reject(A2) or B2) and (reject(A3) and B3) and (iff(reject(A4),reject(B4))))
    if (chain(AB,(A1 and A2 and A3))==False) and (chain(AB,(B1 and B2 and B3))==True) and (AB==True):
      return "RED","GREEN","ALERT","5"

  elif ((count_A==3) and (count_B==0)):
    AB = ((A1 or reject(B1)) and (A2 or reject(B2)) and (A3 and reject(B3)) and (iff(reject(A4),reject(B4))))
    if (chain(AB,(A1 and A2 and A3))==True) and (chain(AB,(B1 and B2 and B3))==False) and (AB==True):
      return "GREEN","RED","ALERT","6"

  elif ((count_A==0) and (count_B==4)):
    AB = ((reject(A1) or B1) and (reject(A2) or B2) and (reject(A3) or B3) and (reject(A4) or B4))
    if ((chain(AB,(A1 and A2 and A3 and A4))==False) and (chain(AB,(B1 and B2 and B3 and B4))==True)) and (AB==True):
      return "RED","GREEN","ALERT","7"

  elif ((count_A==4) and (count_B==0)):
    AB = ((A1 or reject(B1)) and (A2 or reject(B2)) and (A3 or reject(B3)) and (A4 or reject(B4)))
    if ((chain(AB,(A1 and A2 and A3 and A4))==True) and (chain(AB,(B1 and B2 and B3 and B4))==False)) and (AB==True):
      return "GREEN","RED","ALERT","8"

  elif ((count_A == 1) and (count_B==2)):
    AB = iff(((A1 or B1) and (reject(A2) or B2) and (reject(A3) and reject(A4))),(reject(A4) and reject(B4)))
    if ((chain(AB,(A1 and A2))==False) and (chain(AB,(B1 and B2))==True)) and (AB==True):
      return "RED","GREEN","NORMAL","9"
  
  elif ((count_A == 2) and (count_B==1)):
    AB = iff(((A1 or B1) and (A2 or reject(B2)) and (reject(A3) and reject(A4))),(reject(B3) and reject(B4)))
    if ((chain(AB,(A1 and A2))==True) and (chain(AB,(B1 and B2))==False)) and (AB==True):
      return "GREEN","RED","NORMAL","10"

  elif ((count_A==1) and (count_B==3)):
    AB = ((A1 or B1) and (reject(A2) or B2) and (reject(A3) and B3) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==False) and (chain(AB,(B1 and B2 and B3))==True)) and (AB==True):
      return "RED","GREEN","ALERT","11"
  
  elif ((count_A==3) and (count_B==1)):
    AB = ((A1 or B1) and (A2 or reject(B2)) and (A3 and reject(B3)) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==True) and (chain(AB,B1)==False)) and (AB==True):
      return "GREEN","RED","ALERT","12"

  elif ((count_A==1) and (count_B==4)):
    AB = ((A1 or B1) and (reject(A2) or B2) and (reject(A3) and B3) and ((reject(A4) or B4)))
    if (chain(AB,(A1 and A2 and A3 and A4)) == False) and (chain(AB,(B1 and B2 and B3 and B4)) == True)  and (AB==True):
      return "RED","GREEN","ALERT","13"

  elif ((count_A==4) and (count_B==1)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and reject(B3)) and ((A4 or reject(B4))))
    if (chain(AB,(A1 and A2 and A3 and A4)) == True) and (chain(AB,(B1 and B2 and B3 and B4)) == False)  and (AB==True):
      return "GREEN","RED","ALERT","14"

  elif ((count_A==2) and (count_B==3)):
    AB = ((A1 or B1) and (A2 or B2) and (reject(A3) and B3) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==False) and (chain(AB,(B1 and B2 and B3))==True))  and (AB==True):
      return "RED","GREEN","ALERT","15"

  elif ((count_A==3) and (count_B==2)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and reject(B3)) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==True) and (chain(AB,(B1 and B2 and B3))==False))  and (AB==True):
      return "GREEN","RED","ALERT","16"

  elif ((count_A==2) and (count_B==4)):
    AB = ((A1 or B1) and (A2 or B2) and (reject(A3) or (B3)) and ((reject(A4) or B4)))
    if (chain(AB,(A1 and A2 and A3 and A4))==False) and (chain(AB,(B1 and B2 and B3 and B4))==True) and (AB==True):
      return "RED","GREEN","ALERT","17"

  elif ((count_A==4) and (count_B==2)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and reject(B3)) and ((A4 or reject(B4))))
    if (chain(AB,(A1 and A2 and A3 and A4))==True) and (chain(AB,(B1 and B2 and B3 and B4))==False) and (AB==True):
      return "GREEN","RED","ALERT","18"

  elif ((count_A==3) and (count_B==4)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and B3) and ((reject(A4) or B4)))
    if (chain(AB,(A1 and A2 and A3 and A4))==False) and (chain(AB,(B1 and B2 and B3 and B4))==True) and (AB==True):
      return "RED","GREEN","ALERT","19"
  
  elif ((count_A==4) and (count_B==3)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and B3) and ((A4 or reject(B4))))
    if (chain(AB,(A1 and A2 and A3 and A4))==True) and (chain(AB,(B1 and B2 and B3 and B4))==False) and (AB==True):
      return "GREEN","RED","ALERT","20"

  elif ((count_A==1) and (count_B==1)):
    AB = iff(((A1 or B1) and (reject(A2) and reject(A3) and reject(A4))),(reject(B2) and reject(B3) and reject(B4)))
    if ((chain(AB,A1)==True) and (chain(AB,reject(B1))==False)) and (AB==True):
      return "GREEN","RED","NORMAL","21"

  elif ((count_A==2) and (count_B==2)):
    AB = iff(((A1 or B1) and (A2 or B2) and (reject(A3) and reject(A4))),(reject(B3) and reject(B4)))
    if ((chain(AB,(A1 and A2))==True) and (chain(AB,reject(B1 and B2))==False)) and (AB==True):
      return "GREEN","RED","NORMAL","22"

  elif ((count_A==3) and (count_B==3)):
    AB = ((A1 or B1) and (A2 or B2) and  (A3 or B3) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==True) and (chain(AB,reject(B1 and B2 and B3))==False)) and (AB==True):
      return "GREEN","RED","NORMAL","23"

  elif ((count_A == 4) and (count_B == 4)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 or B3) and (A4 or B4))
    if (chain(AB,(A1 and A2 and A3 and A4))==True) and (chain(AB,reject(B1 and B2 and B3 and B4))== False) and (AB==True):
      return "GREEN","RED","NORMAL","24"

  return "BLACK","BLACK","NONE","25"