 Aplicação simples que conta o número de visitas de um site e mostra o nome do host que está acessando, junto com uma instância do Grafana monitorando o consumo de CPU e memória.


Estrutura do Projeto:
```
contador-visitas/
│
├── app/
│   ├── Dockerfile
│   └── app.py
│
├── docker-compose.yml
│
└── prometheus/
    └── prometheus.yml
```