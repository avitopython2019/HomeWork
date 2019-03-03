import myserver
   
def main():   

    myconfig = {'count_thread': 1}

    @myserver.route('/sum')
    def handler1(request):
        number1 = request[:request.find(' ')]
        number2 = request[request.find(' ')+1:]
        return float(number1)+float(number2)
    @myserver.route('/minus')
    def handler2(request):
        number1 = request[:request.find(' ')]
        number2 = request[request.find(' ')+1:]
        return float(number1)-float(number2)
    @myserver.route('/multiple')
    def handler3(request):
        number1 = request[:request.find(' ')]
        number2 = request[request.find(' ')+1:]
        return float(number1)*float(number2)
    @myserver.route('/divide')
    def handler4(request):
        number1 = request[:request.find(' ')]
        number2 = request[request.find(' ')+1:]
        return float(number1)/float(number2)

    myserver.run_server(handler1,handler2,handler3,handler4,host='http://example.com',port=30001,config=myconfig)
    myserver.request_for_service('/sum 1.1 2')
    myserver.request_for_service('/sum 1.1 2')
    myserver.request_for_service('/minus 1 2.4')
    myserver.request_for_service('/multiple -1 -2')
    myserver.request_for_service('/divide -1 2')

main()