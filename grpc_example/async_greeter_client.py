import asyncio
import logging

import grpc

from generated.hellostreamingworld_pb2 import HelloRequest
from generated.hellostreamingworld_pb2_grpc import MultiGreeterStub


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = MultiGreeterStub(channel)

        # Read from an async generator
        async for response in stub.sayHello(HelloRequest(name="you")):
            print("Greeter client received from async generator: " + response.message)

        # Direct read from the stub
        hello_stream = stub.sayHello(HelloRequest(name="you"))
        while True:
            response = await hello_stream.read()
            if response == grpc.aio.EOF:
                break
            print("Greeter client received from direct read: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
