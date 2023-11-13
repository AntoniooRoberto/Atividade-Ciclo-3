import tkinter as tk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = peso / (altura ** 2)

        resultado.config(text=f"IMC: {imc:.2f}")
    except ValueError:
        resultado.config(text="Por favor, insira valores válidos.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Criar widgets
label_nome = tk.Label(janela, text="Nome do Paciente:")
entry_nome = tk.Entry(janela)

label_endereco = tk.Label(janela, text="Endereço Completo:")
entry_endereco = tk.Entry(janela)

label_altura = tk.Label(janela, text="Altura (m):")
entry_altura = tk.Entry(janela)

label_peso = tk.Label(janela, text="Peso (kg):")
entry_peso = tk.Entry(janela)

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)

resultado = tk.Label(janela, text="Resultado do IMC aparecerá aqui.")

# Layout dos widgets
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome.grid(row=0, column=1, padx=10, pady=10)
label_endereco.grid(row=1, column=0, padx=10, pady=10)
entry_endereco.grid(row=1, column=1, padx=10, pady=10)
label_altura.grid(row=2, column=0, padx=10, pady=10)
entry_altura.grid(row=2, column=1, padx=10, pady=10)
label_peso.grid(row=3, column=0, padx=10, pady=10)
entry_peso.grid(row=3, column=1, padx=10, pady=10)
botao_calcular.grid(row=4, column=0, columnspan=2, pady=10)
resultado.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar a interface gráfica
janela.mainloop()