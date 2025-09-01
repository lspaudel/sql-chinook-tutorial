# Combining conditions with OR


The `OR` operator allows rows that meet at least one of the
specified conditions. This query returns customers who are in
either Brazil or France.


```sql

SELECT * FROM customers WHERE Country = 'Brazil' OR Country = 'France';

```

**Sample result (first few rows):**

| CustomerId | FirstName | LastName | Company | Address | City | State | Country | PostalCode | Phone | Fax | Email | SupportRepId |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Luís | Gonçalves | Embraer - Empresa Brasileira de Aeronáutica S.A. | Av. Brigadeiro Faria Lima, 2170 | São José dos Campos | SP | Brazil | 12227-000 | +55 (12) 3923-5555 | +55 (12) 3923-5566 | luisg@embraer.com.br | 3 |
| 10 | Eduardo | Martins | Woodstock Discos | Rua Dr. Falcão Filho, 155 | São Paulo | SP | Brazil | 01007-010 | +55 (11) 3033-5446 | +55 (11) 3033-4564 | eduardo@woodstock.com.br | 4 |
| 11 | Alexandre | Rocha | Banco do Brasil S.A. | Av. Paulista, 2022 | São Paulo | SP | Brazil | 01310-200 | +55 (11) 3055-3278 | +55 (11) 3055-8131 | alero@uol.com.br | 5 |
| 12 | Roberto | Almeida | Riotur | Praça Pio X, 119 | Rio de Janeiro | RJ | Brazil | 20040-020 | +55 (21) 2271-7000 | +55 (21) 2271-7070 | roberto.almeida@riotur.gov.br | 3 |
| 13 | Fernanda | Ramos | None | Qe 7 Bloco G | Brasília | DF | Brazil | 71020-677 | +55 (61) 3363-5547 | +55 (61) 3363-7855 | fernadaramos4@uol.com.br | 4 |