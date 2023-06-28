produto=input("Digite o nome do produto: ")
valorVarejo=float(input("Digite o valor de varejo: "))
desconto=float(input("Digite o valor percentual do desconto: "))
perc= desconto/100
precoAtacado= valorVarejo - (perc * valorVarejo)
print(f"O {produto} custa {valorVarejo:_.2f}")
print(f"Com desconto de {desconto}% fica no valor de {precoAtacado:_.2f}")
