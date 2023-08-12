###################################################
### create autogenerated code from .proto files ###
###################################################

PROTO_SRC=./proto
PROTO_DST=./generated

PROTOC=poetry run python -m grpc_tools.protoc

PROTOFLAGS =--proto_path=$(PROTO_SRC)
PROTOFLAGS+=--python_out=$(PROTO_DST)
PROTOFLAGS+=--fatal_warnings
PROTOFLAGS+=--plugin=protoc-gen-mypy=$(PWD)/.venv/bin/protoc-gen-mypy
PROTOFLAGS+=--mypy_out=$(PROTO_DST)
PROTOFLAGS+=--mypy_grpc_out=$(PROTO_DST)
PROTOFLAGS+=--grpc_python_out=$(PROTO_DST)

# specify source files
PROTO_FILES =$(PROTO_SRC)/hellostreamingworld.proto
PROTO_FILES+=$(PROTO_SRC)/helloworld.proto

.PHONY:proto
proto:
	$(PROTOC) $(PROTOFLAGS) $(PROTO_FILES)

############################
### normal build targets ###
############################

.PHONY:clean
clean:
	rm -rf $(PROTO_DST)/*