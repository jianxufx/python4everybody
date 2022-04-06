sender='From stephen.marquard@ uct.ac.za Sat Jan  5 09:14:16 2008'

start=sender.find('@')
end=sender.find('S')

domain=sender[start+1:end]
print(domain)
