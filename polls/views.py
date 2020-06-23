from django.shortcuts import render
from django.core.mail import EmailMessage
# Create your views here.
def home(request):
	emailSent=mandaremail(request)
	print(emailSent)
	args={'modelo':emailSent}
	return render(request,"index.html",args)

def mandaremail(request):
	result=False
	if(request.POST.get('mybtn')):
		print("in")
		nome=str(request.POST.get('nome'))
		sobrenome=str(request.POST.get('sobrenome'))
		emailcliente=str(request.POST.get('email'))
		telefone=str(request.POST.get('telefone'))
		mensagem=str(request.POST.get('menssagem'))
		emailtext=nome+"\n"+sobrenome+"\n"+emailcliente+"\n"+telefone+"\n"+mensagem
		email = EmailMessage('Cliente: ' + emailcliente, emailtext, to=['victor@torquatoadvocacia.adv.br'])
		email.send()
		result=True
	return result