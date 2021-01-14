## Iniciando o projeto rest-api

### Crie uma pasta

`$ mkdir rest-api`

`$ cd rest-api`



### Crie uma ambiente python

`$ python3 -m venv env`



### Ininie o ambiente

`$ source env/bin/activate`



### Instale as dependências

`$ pip install django djangorestframework`



### Crie o projeto django

`$ django-admin startproject api .`

( O " . " no final fará  com que o projeto seja instalado no repositório atual)



### Inicialize um app aplicativo

`$ django-admin startapp receitas`



### Efetue a migração inicial para criar as tabelas padrões do banco

`$ python manage.py migrate`

> ##### Caso queria testar se o servidor está funcionando execute

>  *$ python manage.py runserver*



## Let's code

> Agora podemos dar inicio a configuração dos componentes para a construção da nossa API



### Abra o seu editor de código

Eu utilizo o vsCode então caso você o utilize, basta ir a pasta onde está seu projeto e executar:

$ code .



### Configurando o nosso projeto

Abra o arquivo `settins.py` localizado na pasta do seu projeto
Adicione os `'rest_framework'` e o app que você criou, no nosso caso `'receitas'`

###### O resultado final ficará assim:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'receitas'
]
```



### Agora criaremos os nossos models

Abra o arquivo `models.py` localizado na pasta `receitas` 

###### **Primeiramente iremos importar uma biblioteca chamada** **`uuid`** , pois a partir dela podemos passar como método, um campo chamado `UUIDField()` onde são inseridos alguns parâmetros para que aquele campo se torne uma chave primaria da nossa tabela no banco.

```
from uuid import uuid4
```



### Criando a model

Criaremos um model chamado Receitas com os seguintes atributos:
 `id, titulo, autor, ingredientes, modo, tempo`

```
from django.db import models
from uuid import uuid4

class Receitas(models.Model):
    id_receita = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    titulo = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    ingredientes = models.CharField(max_length=255)
    modo = models.CharField(max_length=255)
    tempo = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
```

Adicionamos o campo  `created_at = models.DateTimeField() ` para que seja salvo a data e hora que o dado foi inserido ao banco, e passamos o parâmetro `auto_now_add=True` para que este campo registre automaticamente as informações do momento da inserção.



### Criando o serializer

Na pasta receitas iremos criar um arquivo chamado `serializers.py`
Começaremos importando o `rest_framework` e a nossa model `receitas`

```
from rest_framework import serializers

from receitas import models`
```

Agora criaremos uma classe chamada ` ReceitasSerializer` onde ela passará na `class Meta` 2 objetos: `model` indicará a qual model estamos referenciando e `field`  que indicará quais os campos irão ser utilizados.

```
class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Receitas
        fields = '__all__'
```

Utilizamos `'__all__'` para utilizarmos todos os campos da model criada, porém você pode selerionar os campos na qual você deseja que sejam apresentados, exemplo: 
`fields = ('titulo', 'ingredientes', 'modo')`



### Criando um viewset

Na pasta receitas iremos criar um arquivo chamado `viewsets.py` 
Importaremos o `rest_framework` e nosso arquivo serializer `serializers` e o model `Receitas`.

```
from rest_framework import viewsets
from receitas import serializers
from receitas import models
```

Agora criaremos uma classe chamada `ReceitasViewSet`onde nela estarão duas conteúdos: 
1 - Indicando onde está a classe serializer que será utilizado
2 - Indicando que queremos todos os objetos que estão no model

```
class ReceitasViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.ReceitasSerializer
    queryset = models.Receitas.objects.all()
```



### Criando as rotas

Para criação das rotas é necessário importarmos o `include` do *django.urls* , importaremos também o `routers` do *rest_framework* e por final importaremos a nosso caminho para a `viewset`

```
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import viewsets as receitasviewsets
```

Agora definiremos uma rota padrão e em seguida adicionaremos a rota que será seguida para efetuar o registro, passando como parâmetros: `nome-da-rota`, `caminho-da-viewset`.`viewset-utilizada`

```
route = routers.DefaultRouter()

route.register(r'receitas/', receitasviewsets.ReceitasViewSet, basename="Receitas")
```

Agora adicionameros o caminho a ser passado na URL

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
```



### Criando Migrations

Após a criação do model, devemos cria-la em nossa base de dados, assim utilizaremos o comando `python manage.py makemigrations` para indicar que há um modelo a ser implementado ao banco.

`$ python manage.py makemigrations`

Onde o output será:

```
Migrations for 'receitas':
  receitas/migrations/0001_initial.py
    - Create model Receitas
```

E para inserir essa tabela ao banco de fato, utilizaremos o comando: `python manage.py migrate` no qual é o responsável por criar aquele modelo no banco:

`$ python manage.py migrate`

Onde o output será:

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, receitas, sessions
Running migrations:
  Applying receitas.0001_initial... OK
```



### Inicializando o servidor

Para comprovarmos de uma vez por todas que nossa api está funcionando, executaremos um simples comando:

`$ python manage.py runserver`

Output:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 14, 2021 - 17:04:06
Django version 3.1.5, using settings 'api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

