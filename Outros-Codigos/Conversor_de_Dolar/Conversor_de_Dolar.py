# Conversor de Dolar
# Bravoow Tecnologia

# Abaixo encontra-se o script de um Conversor de Dolar, bastante simples.

# A letra "d" indica o valor do dolar.
# O numero "10" indica o valor (de 0 a 10) que sera convertido de Dolar para Reais.

# ------------------------------------------------------------------------------- #

# ---------------- #
# Inicio do Script #
# ---------------- #


d = 3.73

for p in range(10): print 'US$ %5.2f = R$ %5.2f' % (p, p * d)
print '-' * 20


# ---------------- #
# Fim do Script    #
# ---------------- #