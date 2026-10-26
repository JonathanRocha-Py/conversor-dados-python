#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversor e Validador de Dados
Jonathan Rocha — Outubro/2026
Exercício de lógica de programação
"""

def converter_moeda(valor, de="BRL", para="USD"):
    """Converte valor entre moedas simples"""
    taxas = {"BRL": 1, "USD": 5.20, "EUR": 5.70}
    if de not in taxas or para not in taxas:
        return None
    valor_em_brl = valor / taxas[para] if de != "BRL" else valor
    resultado = valor_em_brl * taxas[para] if para != "BRL" else valor_em_brl
    return round(resultado, 2)

def validar_dados(dados):
    """Verifica se os dados estão completos"""
    if not dados:
        return False, "Sem dados informados"
    for chave, valor in dados.items():
        if not valor:
            return False, f"Campo {chave} está vazio"
    return True, "Dados válidos"

def main():
    print("=" * 40)
    print("   CONVERSOR E VALIDADOR DE DADOS")
    print("=" * 40)
    
    valor = 100
    resultado = converter_moeda(valor, "BRL", "USD")
    print(f"\n💰 Conversão: R$ {valor} → US$ {resultado}")
    
    cadastro = {"nome": "Jonathan", "setor": "TI", "codigo": ""}
    valido, mensagem = validar_dados(cadastro)
    status = "✅ Válido" if valido else "❌ Inválido"
    print(f"\n📋 Validação: {status} — {mensagem}")
    
    print("\n✅ Programa executado com sucesso!")

if __name__ == "__main__":
    main()
