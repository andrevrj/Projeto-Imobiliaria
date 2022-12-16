# Projeto-Imobiliaria

📌Projeto de uma imobiliaria contendo:

⚙️Cadastro de imóveis, contendo o código, tipo, endereço e valor.

⚙️Listagem dos imóveis por tipo: apartamento, kitnet, casa.

⚙️Cadastro de clientes com o nome, email e telefone.


Para utilizar o projeto siga os passos abaixo:

💻 Clone o repositório em seu computador para poder acessar os projetos:

- git clone https://github.com/andrevrj/Projeto-Imobiliaria.git

📌Instalar o pip:

	https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

📌Após o pip instalado, instale o django com os seguintes comandos:

	pip install django
	pip install djangorestframework
	
📌Crie o projeto Single Aplication

📌Rodar o comando com o caracter "."

  django-admin startproject tutorial .  
  cd tutorial
  django-admin startapp quickstart
  cd ..

📌Criar um super user pra authenticação: (username: admin, passWord: password123):

  python manage.py createsuperuser --email admin@example.com --username admin

📌Referencia pra atualizar as models:
Criar as tabelas de acordo com as models no banco de dados e atualizar:

	python manage.py makemigrations tutorial
	python manage.py migrate

📌Subir o server:

	python manage.py runserver

📌Referencia para a criação do projeto e estrutura:
	https://www.django-rest-framework.org/tutorial/quickstart/

📌instalar o postman:
	
	GET
	*http://127.0.0.1:8000/clientes
	*http://127.0.0.1:8000/imoveis
	*http://127.0.0.1:8000/imoveis?tipo=apartamento
	
	POST
	*http://127.0.0.1:8000/clientes
		{
			"nome":"André",
			"email":"andre@hotmail.com",
			"telefone":"12345677"
    
		}
	
	*http://127.0.0.1:8000/imoveis
		{
			"id": "aada065f-5919-4707-b1a8-a1e88739e0a2",
			"codigo": "6379",
			"tipo": "casa",
			"endereco": "Rua Alvorada n270",
			"valor": "R$ 1000"
		}

🎓 André Vieira Rocha Junior
