from app import connectAidApp


connectaid_app=connectAidApp()
if __name__ == '__main__':
    connectaid_app.run(
        host='0.0.0.0',
        debug=True,
        port=5100
    )