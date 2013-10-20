#!/usr/local/bin/python

mask           = ["this" , "is" , "an" , "ex" , "parrot"]
secret_message = "tthisiis anfexoparrot thisgisnaniexmparrotathiseisrandex parrotethismisiantex parrotfthisois antexoparrotlthis isaan extparrotnthiseispansex parrotethisvisaanhex parrottthissisuanmex parrotrthisoishantexuparrotathis iseanhextparrot this-is ansexkparrotcthisoisran exeparrotmthisaisgan exsparrotithishistan exwparrotothiswis"


def decypher(secret_message):
  for word in mask:
    secret_message = secret_message.replace(word , "")
  return secret_message[::-1]


def main():
  print decypher(secret_message)

if __name__ == '__main__':
  main()
