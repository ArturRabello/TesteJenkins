from marshmallow import Schema, fields

class ProdutoSchema(Schema):
    name = fields.Str(required=False, load_default="Minecraft")
    description = fields.Str(required=False, load_default="Game de bloco criativo")
    preco = fields.Float(required=False, load_default=400.00)

class ProdutoViewSchema(Schema):
    name = fields.Str(dump_only=True, load_default="Minecraft")
    description = fields.Str(dump_only=True, load_default="Game de bloco criativo")
    preco = fields.Float(dump_only=True, load_default=400.00)
class ErrorSchema(Schema):
    message = fields.Str(required=False, load_default="Erro")

def apresenta_produto(produto):
    return {
        "name": produto.name,
        "description": produto.description,
        "preco": produto.preco
    }