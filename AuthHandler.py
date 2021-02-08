import json
import ast
import logging
import traceback

class Auth(object):
    def authenticate_username_pass(self,request_data):
        try:
            logging.info("Starting Function authenticating_user")
            logging.debug("Request payload - " + str(request_data))
            if "username" not in request_data or "password" not in request_data:
                raise Exception("'username' and 'password' must be present in payload")
            username = request_data["username"]
            password = request_data["password"]
            table_name = "auth_details_tables"
            auth_query = "select * from auth_details_tables where user = '' and pass = ''"
            query = auth_query.replace("$$table", table_name).replace("$$user", username).replace("$$pass", password)
            # execute query by creating database connection using mqsql or posgree to fethch user details
            return_value = {}
            if not username or not password:
                return_value = {"status": "failed", "error": "Either user name or password is blank"}
                return return_value
            authentication_status = False
            user_name = ""
            if authentication_status:
                return_value = {
                    "ERROR_KEY": "",
                    "RESULT_KEY": {
                        "message": "User authentication failed",
                        "status": "FAILURE",
                        "user": {
                            "username": request_data["username"],
                            "name": ""
                        }
                    },
                    "STATUS_KEY": "SUCCESS"
                }
                return return_value
            logging.debug(return_value)
            logging.info("Completing Function authenticate_user ...")
            return return_value
        except:
            error_msg = str(traceback.format_exc())
            return {"status": "failed", "result": "", "error": error_msg}
