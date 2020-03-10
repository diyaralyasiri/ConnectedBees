import webhook_functions


token = "ZWVhZTdiMzctZTAyZS00N2Y4LTgwZTktMDVjZWE4MDg0N2E2MWNkMGRmZTYtNjMz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
url = "http://fcc9d4a0.ngrok.io"

functions.delete_wehbook(functions.list_webhook(token), token)
functions.create_webhook_new_message(url, token)
functions.create_webhook_new_room(url, token)
