import json
from settings import app
from settings import general_ns
from settings import CryptOhAdz
from settings import EazyPeazy
from flask_restplus import Resource

@general_ns.route ('/click_ad/<int:user_id>/<int:ad_id>')
class ClickAdClass (Resource):
    def post (self, user_id, ad_id):
        try:
            ### SUCCESSFUL AD CODE HERE
            CryptOhAdz.pay_customer (user_id=EazyPeazy.CryptOhAdzId, ad_id=ad_id)
            server_transactions=CryptOhAdz.get_customer_transactions (user_id=EazyPeazy.CryptOhAdzId)
            last_server_transaction=CryptOhAdz.get_last_customer_transaction (user_id=EazyPeazy.CryptOhAdzId)
            EazyPeazy.pay_customer (user_id=user_id, ad_id=ad_id, transaction_amount=last_server_transaction['amount'])
            user_transactions = EazyPeazy.get_all_customer_transactions ()

            print ('Successfully paid out ad revenue')

            return app.response_class (
                status=200,
                mimetype='application/json',
                response=json.dumps({
                    'server_transactions': server_transactions,
                    'user_transactions': user_transactions
                })
            )
            ### SUCCESSFUL AD CODE HERE

        except Exception as e:
            ### UNSUCCESSFUL AD CODE HERE
            print ('Something went wrong')

            return app.response_class (
                status=400,
                mimetype='application/json',
                response=json.dumps({
                })
            )
            ### UNSUCCESSFUL AD CODE HERE
