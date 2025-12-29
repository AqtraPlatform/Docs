# Área de texto

![](../../assets/images/app-development/text-area.png)

## Informações gerais
A área de texto é um componente básico da interface do usuário projetado para inserir e exibir texto em várias linhas. É ideal para digitar grandes quantidades de texto, como comentários ou descrições, e fornece espaço suficiente para uma digitação fácil.

## Parâmetros
**Propriedades do Componente:**

| Grupo de configurações | Campo de Configuração | Opções de Valor         | Propósito |
|-----------------------|-----------------------|--------------------------|-----------|
| (Configurações globais) | Nome                  | -                        | Nome do Componente da UI no sistema |
| Comum                 | Desativado            | true, false              | Desativar um elemento |
|                       | Tamanho automático     | true, false              | Controle automático de dimensão |
|                       | Obrigatório           | true, false              | Campo obrigatório a ser preenchido |
|                       | Rótulo                | -                        | Descrição do campo de entrada |
|                       | Vinculação            | Multiseleção de Catálogo | Vinculação de dados |
| Eventos               | Ao valor alterado     | -                        | Evento de alteração de valor |
| Índice da guia       | -                     | Inteiro                  | Ordem de troca de campo |

**Propriedades CSS:**

| Grupo de configurações | Campo de Configuração | Opções de Valor         | Propósito |
|-----------------------|-----------------------|--------------------------|-----------|
| Layout                | Largura               | -                        | Largura do componente |
|                       | Altura                | -                        | Altura do componente |
|                       | Crescer               | true, false              | Estiramento do componente |
|                       | Margem                | -                        | Preenchimento externo |
|                       | Preenchimento         | -                        | Preenchimento interno |
| Aparência             | Raio do Canto         | -                        | Raio do canto |
|                       | Espessura da Borda    | -                        | Espessura da borda |
| Pincel                | Fundo                 | -                        | Cor de fundo |
|                       | Pincel da Borda       | -                        | Cor da borda |

## Casos
- **Entrada de Múltiplas Linhas**: Ideal para formulários que requerem grandes quantidades de texto.
- **Comentários e Descrições**: Usado para escrever comentários, descrições ou qualquer outro script onde a entrada de múltiplas linhas é necessária.

## Exceções
- **Formatação Limitada**: Como a maioria dos campos de entrada de texto, a área de texto restringe o uso de formatação complexa, como hyperlinks ou imagens incorporadas.