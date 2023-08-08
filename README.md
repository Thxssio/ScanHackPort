<h1 align="center">ScanHackPort</h1>




***ScanPortNAT***

- [x] Ubuntu
- [ ] Windows

#


`0 até 1023` - São as consideradas “portas conhecidas”. Portas nesse intervalo são fornecidas apenas para serviços estabelecidos e grandes empresas ou centros de pesquisa de confiança.

`1024 até 49151` - São as chamadas “portas registradas”. Esse nome significa que as portas nesse intervalo podem ser registradas para protocolos específicos por grandes corporações.

`49152 até 65535` - É o intervalo que engloba as portas dinâmicas e as portas privadas. Portas nesse intervalo podem ser usadas por praticamente qualquer um e, portanto, são as com maior probabilidade de haver vulnerabilidade.

#

Instale os requerimentos

```
pip install -r requirements.txt
```

#
Executavel

```
python scanport.py
```
