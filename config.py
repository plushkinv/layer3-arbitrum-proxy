
#то что ниже обязательно заполнить своими данными
login = 'my_login'
password = 'my_password'
address = '207.164.21.34'
port = '3128'
changeIPlink = ""


#то что ниже желательно настроить под себя

#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 3600 #минимальная 
timeoutMax = 36000 #максимальная


#то что ниже можно менять только если понимаешь что делаешь
RPC = "https://arb1.arbitrum.io/rpc"
proxies = { 'all': f'http://{login}:{password}@{address}:{port}',}
request_kwargs = {"proxies":proxies, "timeout": 120}