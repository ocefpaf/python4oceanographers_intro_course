# Website do curso: Introdução à linguagem de programação Python

Site feito com [Hyde](http://hyde.github.io).

## Construindo o site

Instale o hyde
```bash
[~]$ pip install hyde
```

Gere o HTML
```bash
[~]$ make gen
```

Para servir localmente uma prévia,
```bash
[~]$ make serve
```

e navegue com o browser para [http://localhost:8080](http://localhost:8080)

Para publicar o site na web
```
[~]$ hyde publish -c production.yaml -p github
```
