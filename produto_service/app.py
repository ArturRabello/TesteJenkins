from flask import Flask, jsonify
from flask_smorest import Api, Blueprint
from sqlalchemy.exc import IntegrityError, OperationalError
from database import Session


from models import Produto
from schemas import ProdutoSchema, ProdutoViewSchema, ErrorSchema, apresenta_produto

app = Flask(__name__)
app.config["API_TITLE"] = "Produto Service"
app.config["API_VERSION"] = "1.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api = Api(app)

produto_blp = Blueprint("Produto", "produto", url_prefix="/produtos", description="Operações com produtos")


@produto_blp.route("/cadastrar", methods=["POST"])
@produto_blp.arguments(ProdutoSchema)        # valida automaticamente a entrada
@produto_blp.response(200, ProdutoViewSchema)
@produto_blp.response(401, ErrorSchema)
@produto_blp.response(400, ErrorSchema)
# serializa a saída
def cadastrar_produto(produto_data):
    session = Session()
    try:
        produto = Produto(**produto_data)
        print(produto.name, produto.description, produto.preco)
        session.add(produto)
        session.commit()
        session.refresh(produto)
        result= apresenta_produto(produto)
        return jsonify(result), 201
    except OperationalError as e:
        # Erro de conexão ou problemas com o banco
        return {"message": f"Erro de conexão com o banco: {str(e)}"}, 500
    except IntegrityError as e:
        return {"message": str(e)}, 401
    except Exception as e:
        return {"message": str(e)}, 400
    finally:
        session.close()

api.register_blueprint(produto_blp)

if __name__ == "__main__":
    app.run(debug=True)