from concurrent import futures
import base64
import time 

from protos import test_pb2
from protos import test_pb2_grpc

import grpc

def encoding(msg):
    return base64.a85encode(msg.encode())

class EService(test_pb2_grpc.EncodeServiceServicer):
    
    def GetEncode(self, request, context):
        return test_pb2.encodetext(enctransactionID = encoding(request.pttransactionID),
                                            encproperties = encoding(request.ptproperties),
                                            encsenderID = request.ptsenderID)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    test_pb2_grpc.add_EncodeServiceServicer_to_server(EService(),server)
    server.add_insecure_port('[::]:22222')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()