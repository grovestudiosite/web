from dnslib.server import DNSServer, BaseResolver
from dnslib import RR, QTYPE, A

class GroveResolver(BaseResolver):

    def resolve(self, request, handler):

        reply = request.reply()

        dominio = str(request.q.qname)

        print("Consulta:", dominio)

        if dominio == "grovestudio.gc.":

            reply.add_answer(
                RR(
                    "grovestudio.gc.",
                    QTYPE.A,
                    rdata=A("127.0.0.1"),
                    ttl=60
                )
            )

        return reply


resolver = GroveResolver()

server = DNSServer(
    resolver,
    port=5353,
    address="0.0.0.0"
)

print("GroveDNS iniciado")
print("Esperando consultas...")

server.start()