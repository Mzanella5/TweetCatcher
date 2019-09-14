# Trabalho Trabalhoso de Organização de Arquivos

Por Maicon Zanella e Lucas W Molin

## Hipótese

Qual artista músical é mais comentado no Twitter?

## Modelo dos arquivos de dados

O arquivo terá registros de tamanho fixo para representar os tweets. O registro será composto dos seguintes campos:

1. id, uint (4 bytes)
2. artista, UTF-8 string com 50 caracteres (200 bytes)
3. lista de hashtags, UTF-8 string com 200 caracteres (800 bytes)
4. data, datetime (8 bytes)

Tamanho total do registro: 1012 bytes
