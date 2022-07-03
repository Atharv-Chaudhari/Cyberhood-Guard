import random
import string

lm=list(i for i in string.ascii_uppercase)
slm=lm.copy()
random.shuffle(slm)
sm=list(i for i in string.ascii_lowercase)
ssm=sm.copy()
random.shuffle(ssm)
otpe=dict(zip(lm,slm))
otpd=dict(zip(sm,ssm))
otpie={v: k for k, v in otpe.items()}
otpids={v: k for k, v in otpd.items()}

def otp_encrypt(text="Hello"):
    ans=""
    for i in text:
        if(i.isalpha() and i.isupper()):
            ans=ans+otpe[i]
        elif(i.isalpha() and i.islower()):
            ans=ans+otpd[i]
        else:
            ans=ans+i
    return ans

def otp_decrypt(cipher):
    ans=""
    for i in cipher:
        if(i.isalpha() and i.isupper()):
            ans=ans+otpie[i]
        elif(i.isalpha() and i.islower()):
            ans=ans+otpids[i]
        else:
            ans=ans+i
    return ans
